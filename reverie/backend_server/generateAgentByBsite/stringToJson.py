import json
from pathlib import Path


def process_string(input_string):
    # 用 $ 分割字符串并生成列表
    split_by_dollar = input_string.split('$')

    result_dict = {}

    # 遍历分割后的列表，再用 ":" 分割字符串，生成键值对
    for item in split_by_dollar:
        key_value = item.split(':')

        # 确保有键和值存在，然后将其作为键值对添加到字典中
        if len(key_value) == 2:
            key = key_value[0].strip()
            value = key_value[1].strip()
            result_dict[key] = value

    return result_dict

def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"文件 '{file_path}' 不存在")
        return None
    except json.JSONDecodeError:
        print(f"文件 '{file_path}' 不是有效的 JSON 文件")
        return None

def create_folder_in_current_directory(folder_name):
    try:
        Path(folder_name).mkdir()
        print(f"文件夹 '{folder_name}' 创建成功")
    except FileExistsError:
        print(f"文件夹 '{folder_name}' 已经存在")

def create_file_in_current_directory(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write("这是新文件的内容。")
        print(f"文件 '{file_name}' 创建成功")
    except FileExistsError:
        print(f"文件 '{file_name}' 已经存在")

import os

def get_subdirectories(directory_path):
    subdirectories = []
    try:
        with os.scandir(directory_path) as entries:
            for entry in entries:
                if entry.is_dir():
                    subdirectories.append(entry.name)
    except FileNotFoundError:
        print(f"目录 '{directory_path}' 不存在")

    return subdirectories


def write_dict_to_json_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)  # 使用indent参数使JSON格式化输出，可选
        print(f"字典内容已写入到文件 '{file_path}'")
    except FileNotFoundError:
        print("文件路径不存在")
    except PermissionError:
        print("没有足够的权限进行操作")





