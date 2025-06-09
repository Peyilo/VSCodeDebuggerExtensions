import shutil
import os

vscode_server_path = "/.vscode-server"              # .vscode-server路径
version = '2025.8.0'                                # vscode版本

extension_path = os.path.join(                      # ./extensions文件夹下的文件将会被复制到extension_path路径下
    vscode_server_path, 'extensions',
    f'ms-python.debugpy-{version}',
    '/bundled/libs/debugpy/_vendored/pydevd/pydevd_plugins/extensions/types'
)

cur_directory = os.path.dirname(__file__)
source_path = os.path.join(cur_directory, 'extensions')

all_files = []
for root, dirs, files in os.walk(source_path):
    for file in files:
        full_path = os.path.join(root, file)
        all_files.append(full_path)

for source_file in all_files:
    shutil.copy(
        os.path.join(source_file),
        extension_path
    )
