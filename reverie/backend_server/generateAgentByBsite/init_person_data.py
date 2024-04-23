from generateAgentByBsite.stringToJson import *


def init_person_data(ori_person,dir_root="personas",null=None):
    scratch=dict()
    spatial_memory=dict()
    embeddings=dict()
    kw_strength=dict()
    nodes=dict()
    default="default_json"

    scratch=load_json_file(default+"/scratch.json")
    spatial_memory=load_json_file(default+"/spatial_memory.json")
    embeddings=load_json_file(default+"/embeddings.json")
    kw_strength=load_json_file(default+"/kw_strength.json")
    nodes=load_json_file(default+"/nodes.json")


    scratch['daily_plan_req']=ori_person['daily_plan'].strip()
    scratch['name']=ori_person['name'].strip()
    scratch['first_name']=ori_person['first_name'].strip()
    scratch['last_name']=ori_person['last_name'].strip()
    scratch['age']=ori_person['age'].strip()
    scratch['innate']=ori_person['innate'].strip()
    scratch['learned']=ori_person['learned'].strip()
    scratch['currently']=ori_person['currently'].strip()
    scratch['lifestyle']=ori_person['lifestyle'].strip()
    scratch['act_event']=[ori_person['name'].strip(),null,null,]


    # 指定文件路径
    file_path =dir_root+"/"+ori_person['name']+"/bootstrap_memory"  # 将此路径替换为你要写入的文件路径
    file_path_ass=file_path+"/associative_memory"
    # 调用函数将字典写入JSON文件
    write_dict_to_json_file(scratch, file_path+"/scratch.json")
    write_dict_to_json_file(spatial_memory,file_path+"/spatial_memory.json")
    write_dict_to_json_file(embeddings,file_path_ass+"/embeddings.json")
    write_dict_to_json_file(kw_strength,file_path_ass+"/kw_strength.json")
    write_dict_to_json_file(nodes,file_path_ass+"/nodes.json")
