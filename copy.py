import shutil
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--vscode",
    default="~/.vscode-server",
    help="the vscode server directory (default: ~/.vscode-server)"
)

args = parser.parse_args()

vscode_server_path = os.path.expanduser(args.vscode)    # .vscode-server路径
if not os.path.isdir(vscode_server_path):
    print(f"Vscode server directory path does not exist: {vscode_server_path}")
    exit(1)

extensions_path = os.path.join(vscode_server_path, "extensions")
if not os.path.isdir(extensions_path):
    print(f"Extensions path does not exist: {extensions_path}")
    exit(1)

# 查找以 ms-python.debugpy 开头的扩展目录
debugpy_dirs = [
    os.path.join(extensions_path, name) for name in os.listdir(extensions_path)
    if name.startswith("ms-python.debugpy") and os.path.isdir(os.path.join(extensions_path, name))
]

# ./extensions文件夹下全部文件都将被复制到指定位置
cur_directory = os.path.dirname(__file__)
source_path = os.path.join(cur_directory, 'extensions')
all_files = []
for root, dirs, files in os.walk(source_path):
    for file in files:
        full_path = os.path.join(root, file)
        all_files.append(full_path)

for debugpy_dir in debugpy_dirs:
    extension_path = os.path.join(                      # ./extensions文件夹下的文件将会被复制到extension_path路径下
        debugpy_dir, 'bundled/libs/debugpy/_vendored/pydevd/pydevd_plugins/extensions/types'
    )
    for source_file in all_files:
        shutil.copy(
            os.path.join(source_file),
            extension_path
        )

print("Success.")
