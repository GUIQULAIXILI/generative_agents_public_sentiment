import json

from reverie.backend_server.persona.prompt_template.run_gpt_prompt import run_gpt_prompt_on_init_personinfo

ori_comment=json.load(open("ori_comment.json",encoding="utf-8"))
comment=[]
for i in range (len(ori_comment)):
    if ori_comment[i]['sex']!="保密":
        comment.append({'content':ori_comment[i]['content'],'sex':ori_comment[i]['sex']})

res=run_gpt_prompt_on_init_personinfo(comment[0],test_input=None, verbose=False)
print(res)


