import os
import platform
import subprocess
import sys

# UTF-8 인코딩 강제 설정 (Windows에서 한글 깨짐 방지)
sys.stdout.reconfigure(encoding='utf-8')

# 현재 운영체제 확인
current_os = platform.system()
print(f"운영체제: {current_os}")

# OS에 따라 다른 명령어 실행
if current_os == "Windows":
    result = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)
else:
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

print("명령어 실행 결과:")
print(result.stdout)
