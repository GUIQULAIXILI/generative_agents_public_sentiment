import os

from openai import OpenAI

client = OpenAI()

os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"
os.environ["OPENAI_API_KEY"] = "438f-210-41-101-89.ngrok-free.app"
def Expert_system_rumor_request(thought):

  messages=[]
  system_input=dict()
  user_input=dict()
  system_input['role']="system"
  system_input['content']="Expand the following sentence in the third person and add certain imaginings to create a reasonable distortion of the facts in brief, while making the words believable."
  user_input['role']="user"
  user_input['content']=thought
  messages.append(system_input)
  messages.append(user_input)


  response = client.chat.completions.create(model="ft:gpt-3.5-turbo-1106:personal:rumor:98InKRvU",
  messages=messages)
  print(response["choices"][0]["message"]["content"])
  return response["choices"][0]["message"]["content"].strip()


Expert_system_rumor_request("my dog was stolen")