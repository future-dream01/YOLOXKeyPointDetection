# 检查转换好的txt文件是否每行都只包含期望个数的坐标信息，防止后续出错

import os
num =4                              # 定义特征点数

def check_coordinates(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # 分割每行，并移除第一个元素（假设是标签）
            coordinates = line.split()[1:]
            if (len(coordinates) != 2*num) or( len(coordinates)==0):
                return False
    return True

def check_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            if not check_coordinates(file_path):
                print(f'{filename} 文件格式不正确')
    print('所有文件格式都正确')
    return True

# 使用示例
folder_path = 'txt'
check_folder(folder_path)
