import os

# 设置图片文件夹路径
folder_path = 'E:/vscodeProject/Githubcode/YOLOX__KeyPoint_Detection/datasets/json'

# 获取文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 获取文件的完整路径
    file_path = os.path.join(folder_path, filename)
    
    # 检查是否是文件而不是文件夹
    if os.path.isfile(file_path):
        # 拼接新的文件名
        new_filename = '00' + filename
        
        # 获取新的文件路径
        new_file_path = os.path.join(folder_path, new_filename)
        
        # 重命名文件
        os.rename(file_path, new_file_path)

        print(f'Renamed: {filename} -> {new_filename}')
