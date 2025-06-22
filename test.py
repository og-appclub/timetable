import socket
import subprocess
import re

def get_default_gateway():
    result = subprocess.run("ip route", shell=True, capture_output=True, text=True)
    match = re.search(r"default via (\S+)", result.stdout)
    return match.group(1) if match else None

def is_connected():
    gateway_ip = get_default_gateway()
    if not gateway_ip:
        print("⚠ ルーターのIPが見つかりません")
        return False
    print(f"📡 ルーターIP: {gateway_ip}")

    try:
        socket.create_connection((gateway_ip, 80), timeout=3)
        print("✅ 接続成功")
        return True
    except Exception as e:
        print(f"❌ 接続失敗: {e}")
        return False

# テスト
is_connected()
