import os
import shutil
import pandas as pd

# 读取Excel表格
df = pd.read_excel(r'C:\Users\1499964238_176786820\Desktop\NEED2\1.xlsx')

# 获取文件夹名字所在的列（假设是第一列）
folder_names = df.iloc[:, 0]

# 文件夹A和文件夹B的路径
folder_A_path = r'C:\Users\1499964238_176786820\Desktop\M8'
folder_B_path = r'C:\Users\1499964238_176786820\Desktop\NEED2'

# 遍历文件夹名字
for folder_name in folder_names:
    # 构建文件夹A中的路径
    folder_A_subpath = os.path.join(folder_A_path, folder_name)

    # 构建文件夹B中的路径
    folder_B_subpath = os.path.join(folder_B_path, folder_name)

    # 判断文件夹A中是否存在该文件夹
    if os.path.exists(folder_A_subpath):
        # 移动文件夹A中的文件夹到文件夹B
        shutil.move(folder_A_subpath, folder_B_subpath)
        print(f"移动文件夹 {folder_name} 成功")
    else:
        print(f"文件夹 {folder_name} 不存在")

