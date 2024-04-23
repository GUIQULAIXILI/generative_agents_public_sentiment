import json
import sys
from stringToJson import process_string
sys.path.append('../')

from global_methods import *

from persona.memory_structures.spatial_memory import *
from persona.memory_structures.associative_memory import *
from persona.memory_structures.scratch import *
from persona.cognitive_modules.retrieve import *
from persona.prompt_template.run_gpt_prompt import *

ori_comment=json.load(open("ori_comment.json",encoding="utf-8"))
comment=[]
ori_person=[]
for i in range (len(ori_comment)):
    if ori_comment[i]['sex']!="保密":
        comment.append({'content':ori_comment[i]['content'],'sex':ori_comment[i]['sex']})

for i in range(10):
    res=run_gpt_prompt_on_init_personinfo(comment[i],test_input=None, verbose=False)
    res1=process_string(res[0])
    ori_person.append(res1)
    print(ori_person)
with open("ori_person.json", 'w',encoding='utf-8',errors='ignore') as file:
    json.dump(ori_person, file,ensure_ascii=False)






