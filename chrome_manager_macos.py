"""在 macOS 上輔助管理多個 Chrome 實例的小工具。

功能包含：
1. 批量生成啟動腳本，便於創建獨立的使用者資料目錄；
2. 使用 AppleScript 對已打開的 Chrome 窗口進行簡單的網格排列。

目前僅提供基礎示例，方便後續擴展同步輸入等功能。
"""

import argparse
import os
import subprocess
import shutil
import platform
from typing import List

try:
    import psutil
except ImportError as exc:  # pragma: no cover - 提示安裝依賴
    raise SystemExit("缺少 psutil 模組，請先執行 `pip install psutil`") from exc

if platform.system() != "Darwin":  # pragma: no cover - 只在 macOS 上運行
    raise SystemExit("此腳本僅支援 macOS 系統")

# MacOS 版本的簡易 Chrome 窗口管理腳本
# 僅實現批量環境創建和窗口佈局示例

CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def verify_environment() -> None:
    """檢查 Chrome 與 osascript 是否可用"""
    if not os.path.exists(CHROME_PATH):
        raise SystemExit(f"找不到 Chrome 執行檔: {CHROME_PATH}")
    if shutil.which("osascript") is None:
        raise SystemExit("系統缺少 osascript，無法調用 AppleScript")


def create_env_scripts(start: int, end: int, base_dir: str):
    """在指定目錄創建啟動腳本和用戶數據目錄"""
    os.makedirs(base_dir, exist_ok=True)
    for i in range(start, end + 1):
        data_dir = os.path.join(base_dir, str(i))
        os.makedirs(data_dir, exist_ok=True)
        port = 9222 + i - start
        script_path = os.path.join(base_dir, f"start-{i}.sh")
        with open(script_path, "w") as f:
            f.write(f"#!/bin/bash\n\"{CHROME_PATH}\" --user-data-dir=\"{data_dir}\" --remote-debugging-port={port} &\n")
        os.chmod(script_path, 0o755)
        print(f"創建腳本: {script_path}")


def list_chrome_processes() -> List[psutil.Process]:
    """獲取當前運行的 Chrome 進程"""
    procs = []
    for p in psutil.process_iter(["name", "cmdline"]):
        if p.info["name"] == "Google Chrome" and "--user-data-dir=" in " ".join(p.info.get("cmdline", [])):
            procs.append(p)
    return procs


def arrange_windows_grid(columns: int = 2):
    """使用 AppleScript 將 Chrome 窗口網格排列"""
    script = (
        'tell application "Google Chrome"\n'
        'set winList to every window\n'
        'repeat with idx from 1 to count of winList\n'
        'set theWindow to item idx of winList\n'
        'set rowNum to (idx - 1) div {columns} + 1\n'
        'set colNum to (idx - 1) mod {columns} + 1\n'
        'set xPos to (colNum - 1) * 800\n'
        'set yPos to (rowNum - 1) * 600\n'
        'set bounds of theWindow to {xPos, yPos, xPos + 800, yPos + 600}\n'
        'end repeat\n'
        'end tell'
    ).format(columns=columns)
    subprocess.run(["osascript", "-e", script])


def main() -> None:
    """解析參數並執行對應操作"""
    parser = argparse.ArgumentParser(description="Chrome 管理腳本 (macOS)")
    parser.add_argument(
        "--create",
        nargs=3,
        metavar=("START", "END", "DIR"),
        help="批量創建啟動腳本，指定開始編號、結束編號與基礎目錄",
    )
    parser.add_argument(
        "--arrange",
        type=int,
        metavar="N",
        help="按 N 列網格排列當前所有 Chrome 窗口",
    )
    args = parser.parse_args()

    verify_environment()

    if args.create:
        s, e, path = args.create
        create_env_scripts(int(s), int(e), os.path.expanduser(path))

    if args.arrange:
        if list_chrome_processes():
            arrange_windows_grid(columns=args.arrange)


if __name__ == "__main__":
    main()

