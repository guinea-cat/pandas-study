首先，在github创建空仓库。如何将我们电脑本地的文件夹上传到这个仓库？
vscode中 ctrl+~ 打开终端
依次输入：
git init  
git remote add origin https://github.com/guinea-cat/pandas-study.git  
git branch -M main  
git add .  
git commit -m "首次上传 pandas 学习代码"  
git push -u origin main

vscode渲染md：ctrl+shft+v
或者左右分栏：ctrl+k 松开 再按 v 实时同步

另外，修改文件夹名不会影响关联的仓库，但是修改github仓库名称需要同步一下url更新：



git remote -v



git remote set-url origin https://github.com/guinea-cat/LEARN-.git



存档：

# 一级标题

## 二级标题

### 三级标题

#### 四级标题

src/:source 存放项目的主要源代码

lib/：存放库文件或依赖项,源代码

docs/ or doc/:项目文档,可能包含用户手册、API参考等,有时是网站文档的源代码 正式文档

examples/ or demos:使用示例，简短代码片段，直观感受

gallery/:在数据可视化项目中常见(如matplotlib)，展示各种功能的可视化示例，包括代码和图片

conf/ or config/:配置文件

scripts/ 或 tools/：辅助脚本

bin/：可执行文件

tutorials/ or guides:学习指南

requirements.txt 或 pyproject.toml (Python)：项目依赖库，安装前要看，避免环境冲突

setup.py：安装配置，了解如何正确安装

license：许可证，商用前要检查

data/:示例数据

文件名带 *test 或 test* 的是测试文件（里面有用法示例）

main.py:程序的主执行文件或启动脚本,python的主入口文件

有些import的模块其实是src里的文件，如import snake其实是导入了src文件夹里的snake.py，所以下载小游戏要下载全面，src什么的必须下载



\[cs61a](https://www.composingprograms.com/ "文字教程")


\[课程资源见](https://insideempire.github.io/CS61A-Website-Archive/)

\[NLP好难](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/)

propmt：

详细讲解以下全部代码及其涉及的知识，必须讲解详细细致透彻，我准备分别分块放到ipynb的一个个代码块里，适当加上print等以清晰理解

先写中文题干后解题，记住永远给我完整可运行代码，代码注释少一点别影响代码观看流畅性，一道一道题写，一题一题依次讲解，每道题目的代码块依次分别完整给我

详细讲解这些代码及其涉及的知识点

