首先，在github创建空仓库。如何将我们电脑本地的文件夹上传到这个仓库？
vscode中 ctrl+~ 打开终端
依次输入：
git init  
git remote add origin https://github.com/guinea-cat/pandas-study.git  
git branch -M main  
git add .  
git commit -m "首次上传 pandas 学习代码"  
git push -u origin main  

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

文件名带 _test 或 test_ 的是测试文件（里面有用法示例）

main.py:程序的主执行文件或启动脚本,python的主入口文件

有些import的模块其实是src里的文件，如import snake其实是导入了src文件夹里的snake.py，所以下载小游戏要下载全面，src什么的必须下载
