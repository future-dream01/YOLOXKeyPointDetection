import os

def remove_files_with_parentheses(folder_path):
    # 获取文件夹中的所有文件名
    file_names = os.listdir(folder_path)
    
    for file_name in file_names:
        # 检查文件名中是否包含括号
        if '(' in file_name or ')' in file_name:
            file_path = os.path.join(folder_path, file_name)
            
            # 删除文件
            os.remove(file_path)
            print(f"Deleted file: {file_path}")

# 使用示例
folder_path = 'E:/vscodeProject/robotcub/guojisai/datasets/images'  # 替换为你的文件夹路径
remove_files_with_parentheses(folder_path)
