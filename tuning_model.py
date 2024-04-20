from pathlib import Path
from openai import OpenAI
import uvicorn
from fastapi import FastAPI, Body, HTTPException, Header
from pydantic import BaseModel
import http.client
import json
from urllib.parse import quote
app = FastAPI()


class InputData(BaseModel):
    point: str
    params: dict = {}
def rumor_gen(content):
    """舆情专家系统"""

    client = OpenAI(api_key="your_api_key")

    completion = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-1106:personal::9Fyh0qUc",
        messages=[
            {"role": "system", "content": "You are an excellent expert in public opinion communication simulation, please expand the following information to make it real and credible."},
            {"role": "user", "content": content}
        ]
    )
    print(completion.choices[0].message)
    return completion.choices[0].message

@app.post("/api/rumorGen/receive")
async def dify_receive(data: InputData = Body(...), authorization: str = Header(None)):
    """
    Receive API query data from Dify.
    """
    expected_api_key = "123456"  # TODO Your API key of this API
    auth_scheme, _, api_key = authorization.partition(' ')

    if auth_scheme.lower() != "bearer" or api_key != expected_api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")

    point = data.point

    # for debug
    print(f"point: {point}")

    if point == "ping":
        return {
            "result": "pong"
        }
    if point == "app.external_data_tool.query":
        return handle_app_external_data_tool_query(params=data.params)
    # elif point == "{point name}":
        # TODO other point implementation here

    raise HTTPException(status_code=400, detail="Not implemented")


def handle_app_external_data_tool_query(params: dict):
    app_id = params.get("app_id")
    tool_variable = params.get("tool_variable")
    inputs = params.get("inputs")
    query = params.get("query")

    # for debug
    print(f"app_id: {app_id}")
    print(f"tool_variable: {tool_variable}")
    print(f"inputs: {inputs}")
    print(f"query: {query}")

    # TODO your external data tool query implementation here,
    #  return must be a dict with key "result", and the value is the query result
    return rumor_gen(inputs.get("content"))

if __name__ == "__main__":
    uvicorn.run(app=f"{Path(__file__).stem}:app", host="127.0.0.1", port=8080, reload=True, workers=1)