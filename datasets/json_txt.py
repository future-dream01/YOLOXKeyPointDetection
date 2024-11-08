# 将标注的结果json文件批量转换为txt文件
import json
import os

def process_json(json_file, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(output_file, 'w') as f:
        for shape in data['shapes']:
            label = shape['label']
            points = shape['points']
            f.write(f"{label} ")  # 写入标签
            for point in points:
                x, y = point
                f.write(f"{x} {y} ")  # 写入坐标点
            f.write('\n')

def convert_json_to_txt(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            json_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.txt')
            process_json(json_file, output_file)

# 使用示例
input_folder = 'json'
output_folder = 'txt'
convert_json_to_txt(input_folder, output_folder)