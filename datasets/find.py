# 这是用来处理图片文件夹和对应的标注文件夹中文件数量不对应的情况，此代码可找出两者中不同的文件名
import os

def find_unique_files(folder1, folder2):
    # 获取文件夹1中的所有文件名（不包含后缀名）
    files_in_folder1 = {os.path.splitext(file)[0] for file in os.listdir(folder1)}
    # 获取文件夹2中的所有文件名（不包含后缀名）
    files_in_folder2 = {os.path.splitext(file)[0] for file in os.listdir(folder2)}
    
    # 找出只在文件夹1中存在的文件
    unique_to_folder1 = files_in_folder1 - files_in_folder2
    # 找出只在文件夹2中存在的文件
    unique_to_folder2 = files_in_folder2 - files_in_folder1
    
    return unique_to_folder1, unique_to_folder2

# 使用示例
folder1 = 'pictures'  # 替换为你的文件夹1路径
folder2 = 'json'  # 替换为你的文件夹2路径

unique_to_folder1, unique_to_folder2 = find_unique_files(folder1, folder2)

print(f"Files only in {folder1} (without extensions):")
for file in unique_to_folder1:
    print(file)

print(f"\nFiles only in {folder2} (without extensions):")
for file in unique_to_folder2:
    print(file)

