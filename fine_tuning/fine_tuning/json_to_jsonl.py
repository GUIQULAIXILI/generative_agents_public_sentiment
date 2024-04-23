import json

import json

def convert_to_new_format(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as json_file:
        with open(output_file, 'w', encoding='utf-8') as new_format_file:
            for line in json_file:
                data = json.loads(line)
                messages = {"prompt": f"{data['messages'][1]['content']}", "completion": f"{data['messages'][2]['content']}"}

                new_format_data = messages
                new_format_file.write(json.dumps(new_format_data, ensure_ascii=False) + '\n')
# 用法示例
convert_to_new_format('rumors.jsonl', 'old_rumors.jsonl')
