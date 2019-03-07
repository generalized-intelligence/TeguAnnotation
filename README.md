![Tegu Logo](https://s2.ax1x.com/2019/01/30/kl6rzF.jpg)
## Tegu Image Annotator based on PyQt

Tegu Image Annotator(TIA) is a complementary tool of TeguCV. The TIA is used to provide annotated data for the deep learning models in computer vision. It can help users to annotate image data fast and easily.

The TIA has been tested on Windows 10 1803 x64 platform, and also provides support for Linux and macOS platforms.

## Quick Start

1. Install [Python3](https://www.python.org) and [pip3](https://pip.pypa.io/en/stable/installing)
2. Use the following command to install requirements:

```sh
pip3 install -r requirements.txt
```

3. Once all requirements are installed, use the following command to launch TIA:
``` sh
python3 main.py
```

## File Structure
* src/:Source Code
* test/:Unit test for the annotation data structure and model
* USER_MANUAL/:User manual 
* DEVELOPER_DOCUMENT/:Developer documents for modifying code

- In `src/` directory there are project code files , file structure as follows:
* config/:the configs required by the project
* UI_instance/: the UI instance written in [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5)
* UI_instance/UI_model: the UI definition and customized widgets , including `*.ui` files which can be modified by Qt Designer and pyuic
* model/: the tools and predefined data structures
* main.py: the main file with the definition of main window

## Existing Features

* Read and annotate images from folders
* Add images from multiple folders
* Add multiple labels
* Save imcomplete annotating project as project files. Project files(`*.json`) and annotation files(`*.serval`) will be saved seperately.
* Encrypt and decrypt annotation files(`*.serval`). The Encryption key of the TIA open-source version is located in `config/defaults.py`, as `TIA-py-opensource`
* Compress image files and annotation files in a zip file`*.7z`,which relies on an outer executable file `7z.exe`, located in `model/7zfiles`

## User Manual

See [User Manual](https://github.com/generalized-intelligence/Tegu/tree/master/Annotation/Serval-Image-Annotation/USER_MANUAL)

## Developer Document

See [User Manual](http://www.giai.tech)

## TODO

* Seperate a `*.serval` file into several files corresponding to picture folders 
* Choose to Enable/Disable the encryption
* Adjustment and optimization of UI details
* Full localized support for Chinese/English
* Use the ziputil module of python instead of `7z.exe`
* Multi-thread support for compression
* Test on macOS and Linux platforms
* Add "refresh file" and "delete folder" when choosing folders
* Repair the display issue on Linux and 2K Display

# Meta

Project initialized by Generalized Intelligence

Distributed under the GPL-v3 license. See LICENSE for more information.

# Contribute

Please follow CONTRIBUTING.md

---

## Tegu 图像标注工具（Python版）

Tegu图像标注工具（ Tegu Image Annotator，以下简称TIA）是TeguCV 的一个配套工具，用于为计算机视觉方向的深度学习模型提供标注数据。该工具能以可视化的形式，帮助用户方便快捷地为深度学习模型准备经过标注的图像数据。该工具目前已在 Windows 10 1803 x64 平台测试通过，并同样提供Linux和macOS平台的支持。

## 快速开始

1. 首先请安装 [Python3](https://www.python.org) 以及 [pip3](https://pip.pypa.io/en/stable/installing)。
2. 使用如下命令安装所需的 Python 框架:

```sh
pip3 install -r requirements.txt
```

3. 安装好所需框架以后，使用以下命令运行 TIA:
``` sh
python3 main.py
```

## 文件结构

* src/:项目源代码
* test/:针对定义数据结构和数据存储模型的测试代码
* USER_MANUAL/:用户手册
* DEVELOPER_DOCUMENT/:开发者文档，用于修改代码时作为参照

- 在`src/`目录中，为项目代码文件，定义如下：
* config/:项目所需的一些配置所在位置
* UI_instance/: 项目的UI实例部分，使用 [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5) 编写。
* UI_instance/UI_model: 项目的UI定义和自定义控件部分，包含`*.ui`文件，可以使用 Qt Designer 配合 pyuic 修改并生成新的`*.py` UI定义文件。 
* model/: 项目中使用的工具组件、数据存储模型和自定义数据结构。
* main.py: 项目入口文件，同时还包括主窗体类的定义。

## 现有功能

* 读取文件夹中的文件，进行图片标注
* 支持同时添加多个文件夹
* 支持自定义多个标签
* 支持将未完成的标注储存为工程文件，工程文件(`*.json`)与标注文件(`*.serval`)将分开储存
* 对标注文件(`*.serval`)进行加密和解密——开源版TIA使用的加密秘钥位于`config/defaults.py`中，默认设置为`TIA-py-opensource`
* 将标注图像和标注文件打包成`*.7z`格式的压缩文件，便于上传——该功能依赖外部的`7z.exe`，位于`model/7zfiles`文件夹中

## 用户手册

参见 [用户手册](https://github.com/generalized-intelligence/Tegu/tree/master/Annotation/Serval-Image-Annotation/USER_MANUAL)

## 开发者文档

参见 [开发者文档](http://www.giai.tech)

## TODO

* 增加拆分`*.serval`文件到对应的图片文件夹功能
* 可以自行开启和关闭对`*.serval`文件的加密
* UI细节调整完善
* 完整的本地化支持
* 集成压缩模块，不再依赖外部`7z`
* 对压缩打包功能添加多线程支持
* 在 macOS 和 Linux 平台上完成测试
* 选择文件夹页面中增加“刷新文件”和“删除目录”功能
* 修复2K屏幕下的显示问题（Linux）

# Meta

泛化智能 Generalized Intelligence 出品。
本项目通过 GPL-v3 协议发布及传播。详情见 LICENSE。

# Contribute

请参阅 CONTRIBUTING.md
