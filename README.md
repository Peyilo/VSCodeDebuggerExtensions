## VSCode Python 调试器扩展

 VSCode 中调试 Python 时，并不会显示 tensor 以及各种容器的形状信息。但是tensor的形状非常重要，经常需要查看tensor的形状，又不想手动在watch中添加tensor.size表达式查看形状，太麻烦了。

参考自https://github.com/microsoft/debugpy/issues/1525#issuecomment-2316653751

因此，有了这个仓库。



你可以运行 copy.py 脚本，将 ./extensions 下的文件复制到 VSCode 的python debugger扩展目录中，使其生效。

默认情况下，copy.py 使用 ~/.vscode-server 作为 VSCode 远程服务器的路径。如需指定自定义路径，可使用：

```shell
python copy.py --vscode /path/to/your/vscode-server
```

### 效果预览

#### 应用前

![img_1](.\images\img_1.png)

#### 应用后

![img_2](.\images\img_2.png)
