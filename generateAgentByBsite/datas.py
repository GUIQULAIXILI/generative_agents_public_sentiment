from bsite import Bsite

import csv
import json
# cookies = {"cookie": "SESSDATA=b9017f1c%2C1716692208%2C1215c%2Ab1CjC9roaAB1FYtgyN3GcoeflDcX7H7AzvQtOEgjeK9VJO4nkemeARyCOMLdjRr7Hxl-oSVlJZS0F2elNCOW1xclB1bWFFN3NIT0VCZHYtSWRiVzE1aXlxUWVWUVFaaU1qcHY1V1BLZlM4TFhxbi1oU3NFRlRKTnBrMHUwY1BhdjJrQ0RZUzdOcmNRIIEC; bili_jct=3b91f514f1d03c7d38545d6a39793b02;"}
# bs = Bsite(cookies=cookies)
#
# aid=bs.bvid2aid(bvid="BV1Ne411Z7F4")
# bs.comments(aid=aid, csvfpath='comments.csv')


def csv_to_json(csv_file, json_file):
    with open(csv_file,'r',encoding='utf-8',errors='ignore') as file:
        csv_data = csv.DictReader(file)
        json_data = []
        for row in csv_data:
            json_data.append(row)

    with open(json_file, 'w',encoding='utf-8',errors='ignore') as file:
        json.dump(json_data, file,ensure_ascii=False)


# 调用函数进行转换
csv_to_json('comments.csv', 'ori_comment.json')