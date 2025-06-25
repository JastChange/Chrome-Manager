<div align="center">

# Chrome 多窗口管理器 V2.0

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Windows](https://img.shields.io/badge/Windows-10%2B-0078D6.svg?style=flat&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Chrome](https://img.shields.io/badge/Chrome-Latest-4285F4.svg?style=flat&logo=google-chrome&logoColor=white)](https://www.google.com/chrome/)
[![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](LICENSE)



  <strong>作者：Devilflasher</strong>：<span title="No Biggie Community Founder"></span>
  [![X](https://img.shields.io/badge/X-1DA1F2.svg?style=flat&logo=x&logoColor=white)](https://x.com/DevilflasherX)
[![微信](https://img.shields.io/badge/微信-7BB32A.svg?style=flat&logo=wechat&logoColor=white)](https://x.com/DevilflasherX/status/1781563666485448736 "Devilflasherx")
 [![Telegram](https://img.shields.io/badge/Telegram-0A74DA.svg?style=flat&logo=telegram&logoColor=white)](https://t.me/devilflasher0) （欢迎加入微信群交流）
 

</div>

> ## ⚠️ 免责声明
> 
> 1. **本软件为开源项目，仅供学习交流使用，不得用于任何闭源商业用途**
> 2. **使用者应遵守当地法律法规，禁止用于任何非法用途**
> 3. **开发者不对因使用本软件导致的直接/间接损失承担任何责任**
> 4. **使用本软件即表示您已阅读并同意本免责声明**

## 工具介绍
Chrome 多窗口管理器是一款专门为 `NoBiggie社区` 准备的Chrome浏览器多窗口管理工具。它可以帮助用户轻松管理多个 Chrome 窗口，实现窗口批量打开、排列以及之间的同步操作，大大提高交互效率。

## ❇️ 功能特性

- `批量管理功能`：一键打开/关闭单个、多个Chrome实例
- `批量环境创建`：便捷创建多个Chrome独立数据目录和快捷方式
- `智能布局系统`：支持自动网格排列和自定义坐标布局，优化多屏幕支持
- `多窗口同步控制`：实时同步鼠标/键盘操作到所有选定窗口
- `批量打开网页`：支持在多窗口中同时打开指定网页
- `快捷方式图标替换`：支持一键替换多个快捷方式图标（带序号的图标已准备在icon文件夹）
- `插件窗口同步`：优化支持弹出的插件窗口内的键盘和鼠标同步
- `右键菜单管理`：支持窗口列表右键关闭窗口等快捷操作

## ❇️ 环境要求

- Windows 10/11 (64-bit)
- Python 3.9+
- Chrome浏览器 最新

## ❇️ 运行教程
## 🎬️ 视频版教程请移步本人推特这篇推文观看
https://x.com/DevilflasherX/status/1916487254891274703



### 方法一：打包成独立exe可执行文件（推荐）

如果你想自己打包程序，请按以下步骤操作：

1. **安装 Python 和依赖**
   ```bash
   # 安装 Python 最新版本
   # 从 https://www.python.org/downloads/ 下载
   ```

2. **准备文件**
   - 确保目录里有以下文件：
     - chrome_manager.py（主程序）
     - build.py（打包脚本）
     - app.manifest（管理员权限配置）
     - app.ico（程序图标）
     - requirements.txt（依赖包清单，包含程序所需的所有Python包）


3. **运行打包脚本**
   ```bash
   # 在程序目录下运行：
   python build.py
   ```

4. **查找生成文件**
   - 打包完成后，在 `dist` 目录下找到 `chrome_manager.exe`
   - 双击运行 `chrome_manager.exe` 即可打开程序

### 方法二：从源码运行 （非推荐）

1. **安装 Python**
   ```bash
   # 下载并安装Python最新版本
   # 从 https://www.python.org/downloads/ 下载
   ```

2. **安装依赖包**
   
   ```bash
   # 打开命令提示符（CMD）并运行：
   pip install -r requirements.txt
   
   # 或者手动安装基本依赖：
   pip install pyinstaller==6.12.0 sv-ttk==2.6.0 keyboard==0.13.5 mouse==0.7.1 pywin32==309 wmi==1.5.1 requests==2.32.3 pillow==11.1.0
   
   # Win11 用户可选安装(如果安装失败可以忽略，程序会自动适配):
   pip install win11toast==0.32
   ```

3. **运行程序**
   ```bash
   # 在程序目录下运行：
   python chrome_manager.py
   ```

## ❇️ 使用说明

### 前期准备：批量创建环境

V2.0版本新增了批量创建环境功能，无需手动创建多开结构：

1. **设置软件参数**
   - 软件主界面右上角打开设置页面
   - 设置快捷方式存放的目录
   - 设置缓存存放的目录

2. **打开批量创建环境**
   - 点击软件下方功能标签页中的"批量创建环境"

3. **创建环境**
   - 设置需要创建的环境数量（例如：1-100 就是创建编号为1至100的窗口）
   - 点击"开始创建"按钮
   - 系统将自动创建对应编号的快捷方式以及对应的缓存目录
   - 创建完成后会显示成功消息

4. **环境结构**
   创建完成后，将自动生成如下结构：
   ```
   您选择的存放快捷方式的目录
   ├── 1.lnk
   ├── 2.lnk
   ├── 3.lnk
   └── Data （您选择的存放数据的缓存目录）
       ├── 1
       ├── 2
       └── 3
   ```

### 基本操作

1. **打开窗口**
   - 软件下方的"打开窗口"标签下，在"窗口编号"里填入想要打开的浏览器编号（格式可以是1-10这样，也可以是1，3，5这样，或者两者结合 1-10，13，15）
   - 点击"打开窗口"按钮即可打开对应编号的chrome窗口

2. **导入窗口**
   - 点击"导入窗口"按钮导入当前打开的 Chrome 窗口
   - 在列表中选择要操作的窗口，通常点击全部选择按钮即可，2.0版本的程序已经可以自动排除系统主浏览器

3. **窗口排列**
   - 使用"自动排列"快速整理窗口
   - 或使用"自定义排列"通过自定义参数排列窗口

4. **开启同步**
   - 选择一个主控窗口（点击"主控"列），若没有选择程序会自动选择第一个窗口为主控窗口
   - 点击"开始同步"或使用设定的快捷键

## ❇️ 注意事项

- 同步功能需要管理员权限
- 虽然理论上不会被杀毒软件误报或干扰，但请在报错时检查杀毒软件是否拦截相关功能
- 批量操作时注意系统资源占用

## 常见问题

1. **无法打包程序❓️**
   - 主要原因是Python没有正确安装或环境变量未正确设置
   - 确保Python在默认位置安装且安装时勾选了"Add Python to PATH"选项
   - 检查pip是否正常工作，尝试运行`pip --version`验证
   - 确保已安装所有依赖包
   - 如果打包过程中仍然出现其他错误，请尝试以管理员权限运行命令提示符

2. **无法导入窗口❓️**
   - 主要原因是Chrome窗口不是使用`--user-data-dir=`参数启动的
   - 请使用正确创建的快捷方式打开窗口
   - 确保Chrome快捷方式的目标包含了类似`--user-data-dir="D:\chrome duo\data\1"`的参数

3. **无法开启同步❓️**
   - 程序不支持谷歌账号登录后多开的窗口形式，这类窗口无法正确同步
   - 请确保通过`--user-data-dir`参数的快捷方式打开窗口
   - 检查是否以管理员身份运行程序
   - 确保已正确选择一个主控窗口
   - 如果使用多显示器，确认屏幕设置正确
   - 开启同步后如果部分窗口没有同步，可以多次单击主控窗口来校准同步

## ❇️ 更新日志

### v2.0 🆕
- **✨ 核心技术改进**
  - **CDP 技术支持**：引入 Chrome DevTools Protocol，实现更精确的浏览器控制和通信
  - **多线程框架升级**：使用 concurrent.futures 实现高效并行任务处理，提升整体性能
  - **同步引擎重构**：重写鼠标和键盘事件处理算法，大幅降低系统资源占用
  - **安全性增强**：新增路径验证和进程所有者验证，提高程序运行安全性
  - **内存管理优化**：修复内存泄漏问题，显著改善长时间运行的稳定性

- **🌟 新增功能**
  - **批量环境创建**：支持一键创建多个Chrome浏览器环境，大幅提升效率
  - **多屏幕支持**：添加多显示器识别和管理，可在不同屏幕上独立排列窗口（此功能由网友buyun00添加）
  - **标签批量管理**：新增"仅保留当前标签"和"仅保留新标签页"功能
  - **窗口右键菜单**：增加窗口列表右键关闭功能，提供更便捷的窗口管理
  - **同步状态通知**：添加开关同步状态的系统通知，清晰提示当前操作状态
  - **批量文本输入**：支持随机数字和指定文本批量输入到多个窗口

- **📊 优化项目**
  - **UI 界面优化**：整合设置部分的 UI，提供更直观的用户体验
  - **窗口层级优化**：改进开启窗口排列和同步时的屏幕层级关系，避免窗口被遮挡
  - **窗口排列算法**：优化窗口自动排列算法，更合理地利用屏幕空间
  - **窗口列表管理**：修复窗口顺序在列表中混乱的问题，保持一致性
  - **同步机制改进**：修复切换主控后的同步 BUG，提高多窗口协同稳定性
  - **批量打开网页优化**：优化批量打开网页效果，打开效果更佳稳定丝滑
  - **鼠标滚轮优化**：修复了鼠标滚轮同步时幅度不一样的问题
  - **弹窗处理增强**：优化插件弹出窗口的同步问题，提升扩展程序操作体验
  - **性能优化**：降低 CPU 和内存占用，优化高负载下的响应速度
  - **错误恢复**：添加自动恢复机制，减少操作中断的可能性

### v1.0
- 首次发布
- 实现基本的窗口管理和同步功能


## 许可证

本项目采用 GPL-3.0 License，保留所有权利。使用本代码需明确标注来源，禁止闭源商业使用。

🔄 持续更新中


## macOS 使用
在 macOS 上运行时，可执行 `python chrome_manager_macos.py`。首次使用请先安装額外依賴：

```bash
pip install psutil pynput
```

脚本会在指定目录创建启动脚本，并示例性地排列 Chrome 窗口。

