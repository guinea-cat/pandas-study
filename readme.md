首先，在github创建空仓库。如何将我们电脑本地的文件夹上传到这个仓库？
vscode中 ctrl+~ 打开终端
依次输入：
git init
git remote add origin https://github.com/guinea-cat/pandas-study.git
git branch -M main
git add .
git commit -m "首次上传 pandas 学习代码"
git push -u origin main
