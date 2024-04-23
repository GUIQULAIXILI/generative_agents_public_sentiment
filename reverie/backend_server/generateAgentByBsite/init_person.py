from generateAgentByBsite.init_person_data import init_person_data
from generateAgentByBsite.stringToJson import *


def init_person(file_path='ori_person.json', dir_root="personas"):
    ori_person = load_json_file(file_path)
    create_folder_in_current_directory(dir_root)

    # 生成目录
    for i in range(len(ori_person)):
        dir_name = dir_root + '/' + ori_person[i]['name']
        create_folder_in_current_directory(dir_name)
        boot_name = dir_name + "/bootstrap_memory"
        create_folder_in_current_directory(boot_name)

        scratch_name = boot_name + "/scratch.json"
        spatial_memory_name = boot_name + "/spatial_memory.json"
        create_file_in_current_directory(scratch_name)
        create_file_in_current_directory(spatial_memory_name)

        ass_name = boot_name + "/associative_memory"
        create_folder_in_current_directory(ass_name)

        emb_name = ass_name + "/embeddings.json"
        kw_name = ass_name + "/kw_strength.json"
        no_name = ass_name + "/nodes.json"
        create_file_in_current_directory(emb_name)
        create_file_in_current_directory(kw_name)
        create_file_in_current_directory(no_name)

        init_person_data(ori_person[i])

    return True

init_person()
