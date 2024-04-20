from reverie.backend_server.generateAgentByBsite.stringToJson import *


def init_reverie(person):
    rev=load_json_file("default_json/meta.json")
    per_names=[]
    for i in range(len(person)):
        per_names.append(person[i]['name'])
    rev['persona_names']=per_names
    create_folder_in_current_directory("reverie")
    create_file_in_current_directory("meta.json")
    write_dict_to_json_file(rev,"reverie/meta.json")


person=load_json_file("ori_person.json")
init_reverie(person)