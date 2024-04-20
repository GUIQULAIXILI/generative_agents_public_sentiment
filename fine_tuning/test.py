import http.client
import json

conn = http.client.HTTPSConnection("0011-124-90-105-99.ngrok-free.app")
payload = json.dumps({
   "point": "app.external_data_tool.query",
   "params": {
      "app_id": "61248ab4-1125-45be-ae32-0ce91334d021",
      "tool_variable": "rumor_retrieve",
      "inputs": {
         "content": "My wallet was stolen"
      },
      "query": "what the rumor will be?"
   }
})
headers = {
   'Authorization': 'Bearer 123456',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json'
}
conn.request("POST", "/api/rumorGen/receive", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))