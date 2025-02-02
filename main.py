import os
import platform
import subprocess
import psutil

# 현재 운영체제 확인
current_os = platform.system()
print(f"운영체제: {current_os}")

# 시스템 정보 출력 (CPU, 메모리 사용량 등)
print(f"CPU 개수: {psutil.cpu_count(logical=True)}")
print(f"사용 가능한 메모리: {psutil.virtual_memory().available / (1024 * 1024)} MB")

# 운영체제에 따라 다른 명령어 실행
if current_os == "Windows":
    result = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)
else:
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

# 명령어 실행 결과 출력
print("명령어 실행 결과:")
print(result.stdout)
