import json
import requests
import time
import random
import os
from datetime import datetime
from colorama import Fore, Back, Style, init

# Khởi tạo colorama để hiển thị màu trên Terminal
init(autoreset=True)

# --- CẤU HÌNH DỮ LIỆU (Thay thế file .env) ---
CONFIG = {
    "EMAIL": "quangnamtricker@gmail.com",
    "PASSWORD": "quangnam123",
    "GIST_URL": "https://gist.githubusercontent.com/maihuybao/63e7edf5d680007ea306bcef7dd5dba0/raw/65d30cdfb31db3c39663d8c1dc05ba376e4bd557/token.json"
}

class LocketUnlocker:
    def __init__(self):
        self.email = CONFIG["EMAIL"]
        self.password = CONFIG["PASSWORD"]
        self.gist_url = CONFIG["GIST_URL"]
        self.token = None
        self.headers = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "X-Ios-Bundle-Identifier": "com.locket.Locket",
            "User-Agent": "FirebaseAuth.iOS/10.23.1 com.locket.Locket/1.82.0 iPhone/18.0 hw/iPhone12_1"
        }

    def print_banner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        banner = f"""
{Fore.CYAN}{Style.BRIGHT}=========================================================================
{Fore.YELLOW}  _      ____   _____ _  ________ _______    _____  ____  _      _____  
{Fore.YELLOW} | |    / __ \ / ____| |/ /  ____|__   __|  / ____|/ __ \| |    |  __ \ 
{Fore.YELLOW} | |   | |  | | |    | ' /| |__     | |    | |  __| |  | | |    | |  | |
{Fore.YELLOW} | |   | |  | | |    |  < |  __|    | |    | | |_ | |  | | |    | |  | |
{Fore.YELLOW} | |___| |__| | |____| . \| |____   | |    | |__| | |__| | |____| |__| |
{Fore.YELLOW} |______\____/ \_____|_|\_\______|  |_|     \_____|\____/|______|_____/ 
                                                                        
{Fore.GREEN}             🚀 PREMIUM UNLOCKER TOOL - VERSION 2.0
{Fore.MAGENTA}             © Copyright by tuquangnam07
{Fore.CYAN}=========================================================================
        """
        print(banner)
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{Fore.GREEN} [🕙 Time]: {now}")
        print(f"{Fore.CYAN}--------------------------------------------------------------------------\n")

    def login(self):
        print(f"{Fore.YELLOW}[*] Đang xác thực tài khoản Firebase...")
        url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyCQngaaXQIfJaH0aS2l7REgIjD7nL431So"
        payload = {
            "email": self.email,
            "password": self.password,
            "returnSecureToken": True
        }
        
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            if response.ok:
                self.token = response.json().get('idToken')
                self.headers["Authorization"] = f"Bearer {self.token}"
                print(f"{Fore.GREEN}[+] Đăng nhập thành công! Quyền truy cập đã được cấp.")
                return True
            else:
                print(f"{Fore.RED}[-] Đăng nhập thất bại. Kiểm tra lại thông tin cấu hình.")
                return False
        except Exception as e:
            print(f"{Fore.RED}[!] Lỗi kết nối: {e}")
            return False

    def get_uid_by_username(self, username):
        print(f"{Fore.YELLOW}[*] Đang truy vấn cơ sở dữ liệu cho: {Fore.CYAN}@{username}")
        url = "https://api.locketcamera.com/getUserByUsername"
        payload = {"data": {"username": username}}
        
        response = requests.post(url, json=payload, headers=self.headers)
        if response.ok:
            data = response.json().get("result", {}).get("data", {})
            uid = data.get("uid")
            if uid:
                print(f"{Fore.GREEN}[+] Tìm thấy UID: {Fore.WHITE}{uid}")
                return uid
        print(f"{Fore.RED}[-] Không tìm thấy người dùng. Vui lòng kiểm tra lại username.")
        return None

    def unlock_gold(self, target_uid):
        print(f"{Fore.YELLOW}[*] Đang khởi tạo tiến trình Restore Purchase (Sandbox)...")
        
        try:
            res_gist = requests.get(self.gist_url)
            tokens = res_gist.json()
            payload_data = random.choice(tokens)
        except Exception as e:
            print(f"{Fore.RED}[-] Lỗi tải payload từ Server: {e}")
            return False

        payload_data["app_user_id"] = target_uid
        if "attributes" in payload_data and "$attConsentStatus" in payload_data["attributes"]:
            payload_data["attributes"]["$attConsentStatus"]["updated_at_ms"] = int(time.time() * 1000)

        url = "https://api.revenuecat.com/v1/receipts"
        rv_headers = {
            "Authorization": "Bearer appl_JngFETzdodyLmCREOlwTUtXdQik",
            "Content-Type": "application/json",
            "X-Is-Sandbox": "true"
        }

        response = requests.post(url, headers=rv_headers, json=payload_data)
        if response.ok:
            print(f"\n{Back.GREEN}{Fore.BLACK} [ THÀNH CÔNG ] {Style.RESET_ALL}")
            print(f"{Fore.GREEN}🎉 Chúc mừng! Tài khoản {Fore.CYAN}{target_uid}{Fore.GREEN} đã được mở khóa Gold.")
            print(f"{Fore.YELLOW}💡 Hãy khởi động lại ứng dụng Locket trên điện thoại để kiểm tra.")
            return True
        else:
            print(f"{Fore.RED}[-] Unlock thất bại: {response.text}")
            return False

# --- KHỞI CHẠY ---
if __name__ == "__main__":
    tool = LocketUnlocker()
    tool.print_banner()
    
    if tool.login():
        print(f"{Fore.CYAN}--------------------------------------------------------------------------")
        target = input(f"{Fore.WHITE}👉 Nhập username Locket cần mở khóa: {Fore.YELLOW}").strip()
        print(f"{Fore.CYAN}--------------------------------------------------------------------------")
        
        uid = tool.get_uid_by_username(target)
        if uid:
            time.sleep(1) # Tạo hiệu ứng chờ cho chuyên nghiệp
            tool.unlock_gold(uid)
    
    print(f"\n{Fore.MAGENTA}--- Cảm ơn bạn đã sử dụng Tool của tuquangnam07 ---")
    input(f"{Fore.WHITE}Nhấn Enter để thoát...")
