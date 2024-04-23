from generateAgentByBsite.stringToJson import *


def init_environment(person):
    env=dict()
    cor= {
    "maze": "the_ville",
    "x": 72,
    "y": 14
    }
    for i in person:
    # for i in range(len(person)):
        env[i['name']]=cor
        print(i['name'])
    create_folder_in_current_directory("environment")
    create_file_in_current_directory("environment/0.json")
    write_dict_to_json_file(env,"environment/0.json")

person=load_json_file("ori_person.json")
init_environment(person)