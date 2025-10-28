import os
from pathlib import Path

def list_files_to_txt(folder_path: str, output_txt: str = "file.txt", recursive: bool = True):
    """
    把 folder_path 下的所有文件名（按顺序）写入 output_txt。
    
    参数:
        folder_path : str   – 要遍历的文件夹路径
        output_txt  : str   – 输出的 txt 文件路径（默认当前目录下的 file.txt）
        recursive   : bool  – 是否递归遍历子文件夹（默认 True）
    """
    folder = Path(folder_path).resolve()      # 转为绝对路径，防止相对路径出错
    if not folder.is_dir():
        raise ValueError(f"错误：{folder} 不是一个有效的文件夹路径")

    # 1. 收集所有文件（Path 对象）
    if recursive:
        files = [p for p in folder.rglob("*") if p.is_file()]
    else:
        files = [p for p in folder.glob("*") if p.is_file()]

    # 2. 按文件名（字符串）自然排序
    #    Path.name 是文件名（含后缀），sorted 默认按字母顺序
    files_sorted = sorted(files, key=lambda p: p.name.lower())   # 忽略大小写排序（可选）

    # 3. 写入 txt（每行一个文件名）
    with open(output_txt, "w", encoding="utf-8") as f:
        for file_path in files_sorted:
            # 这里可以选择写入完整路径或仅文件名
            # f.write(str(file_path) + "\n")        # 完整绝对路径
            f.write(file_path.name + "\n")         # 仅文件名

    print(f"成功！共 {len(files_sorted)} 个文件，已写入 {output_txt}")

# ======================
# 使用示例
# ======================
if __name__ == "__main__":
    # 把下面的路径改成你要遍历的文件夹
    target_folder = r"C:\Users\YourName\Documents\my_folder"   # Windows 示例
    # target_folder = "/home/user/my_folder"                  # Linux/macOS 示例

    # 调用函数
    list_files_to_txt(target_folder, output_txt="file.txt", recursive=True)
