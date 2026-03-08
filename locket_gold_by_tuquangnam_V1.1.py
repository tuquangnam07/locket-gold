import json
import requests
import time
import random
import os
import webbrowser
import sys
from datetime import datetime
from colorama import Fore, Back, Style, init

# Khởi tạo colorama
init(autoreset=True)

# --- CẤU HÌNH DỮ LIỆU ---
CONFIG = {
    "EMAIL": "quangnamtricker@gmail.com",
    "PASSWORD": "quangnam123",
    "GIST_URL": "https://gist.githubusercontent.com/maihuybao/63e7edf5d680007ea306bcef7dd5dba0/raw/65d30cdfb31db3c39663d8c1dc05ba376e4bd557/token.json",
    "FB_URL": "https://fb.com/tuquangnam07",
    "GITHUB_RAW": "https://raw.githubusercontent.com/tuquangnam07/locket-gold/refs/heads/main"
}

class LocketUnlockerPro:
    def __init__(self):
        self.email = CONFIG["EMAIL"]
        self.password = CONFIG["PASSWORD"]
        self.gist_url = CONFIG["GIST_URL"]
        self.github_raw = CONFIG["GITHUB_RAW"]
        self.current_version = "1.1"
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
                                                                        
{Fore.GREEN}             🚀 PREMIUM UNLOCKER TOOL - LUXURY EDITION V{self.current_version}
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

    def kiem_tra_phien_ban_va_trang_thai(self):
        """
        Kiểm tra phiên bản hiện tại so với phiên bản mới nhất trên GitHub
        và kiểm tra trạng thái hoạt động của tool.
        """
        print(f"{Fore.WHITE}[{Fore.BLUE}ℹ{Fore.WHITE}] Đang kiểm tra phiên bản và trạng thái tool...")
        
        version_url = f"{self.github_raw}/version"
        update_url = f"{self.github_raw}/update"
        status_url = f"{self.github_raw}/status"
        
        try:
            # --- 1. Kiểm tra trạng thái hoạt động ---
            try:
                status_response = requests.get(status_url, timeout=10)
                if status_response.status_code == 200:
                    tool_status = status_response.text.strip().lower()
                    
                    # Xử lý các trạng thái khác nhau
                    if "maintenance" in tool_status or "bảo trì" in tool_status:
                        print(f"\n{Back.YELLOW}{Fore.BLACK} ⚠️ THÔNG BÁO BẢO TRÌ ⚠️ {Style.RESET_ALL}")
                        print(f"{Fore.YELLOW}Tool hiện đang trong quá trình bảo trì. Vui lòng quay lại sau!")
                        print(f"{Fore.YELLOW}Liên hệ Admin: {Fore.CYAN}{CONFIG['FB_URL']}")
                        self.cam_on_nguoi_dung()
                        sys.exit(0)
                        
                    elif "commingsoon" in tool_status or "sắp ra mắt" in tool_status:
                        print(f"\n{Back.CYAN}{Fore.BLACK} 🚀 SẮP RA MẮT 🚀 {Style.RESET_ALL}")
                        print(f"{Fore.CYAN}Tính năng mới đang được phát triển và sẽ sớm ra mắt!")
                        print(f"{Fore.CYAN}Rất tiếc, tool hiện không thể sử dụng được.")
                        self.cam_on_nguoi_dung()
                        sys.exit(0)
                        
                    elif "activate" in tool_status or "hoạt động" in tool_status:
                        print(f"{Fore.GREEN}[✔] Tool đang hoạt động bình thường.\n")
                        
                    else:
                        print(f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}] Trạng thái tool không xác định: {tool_status}")
                        print(f"{Fore.YELLOW}Vui lòng liên hệ Admin để được hỗ trợ.")
                        self.cam_on_nguoi_dung()
                        sys.exit(0)
                else:
                    print(f"{Fore.YELLOW}[!] Không thể kiểm tra trạng thái tool. (Mã lỗi: {status_response.status_code})")
                    print(f"{Fore.YELLOW}Vui lòng kiểm tra kết nối mạng và thử lại.")
                    self.cam_on_nguoi_dung()
                    sys.exit(0)
            except requests.exceptions.ConnectionError:
                print(f"{Fore.YELLOW}[!] Không thể kết nối để kiểm tra trạng thái tool.")
                print(f"{Fore.YELLOW}Vui lòng kiểm tra kết nối mạng và thử lại.")
                self.cam_on_nguoi_dung()
                sys.exit(0)
            except Exception as e:
                print(f"{Fore.YELLOW}[!] Lỗi khi kiểm tra trạng thái: {e}")
                self.cam_on_nguoi_dung()
                sys.exit(0)
                
            # --- 2. Kiểm tra phiên bản ---
            try:
                version_response = requests.get(version_url, timeout=10)
                if version_response.status_code == 200:
                    latest_version = version_response.text.strip()
                    
                    print(f"{Fore.WHITE}[{Fore.BLUE}ℹ{Fore.WHITE}] Phiên bản hiện tại: {Fore.GREEN}{self.current_version}")
                    print(f"{Fore.WHITE}[{Fore.BLUE}ℹ{Fore.WHITE}] Phiên bản mới nhất: {Fore.CYAN}{latest_version}")
                    
                    # So sánh phiên bản
                    if latest_version > self.current_version:
                        print(f"\n{Back.RED}{Fore.WHITE} ⚡ CẬP NHẬT KHẨN CẤP ⚡ {Style.RESET_ALL}")
                        print(f"{Fore.RED}Đã có phiên bản mới {latest_version}! Bạn đang dùng phiên bản cũ {self.current_version}.")
                        print(f"{Fore.RED}Vui lòng cập nhật lên phiên bản mới nhất để tiếp tục sử dụng.")
                        input(f"{Fore.YELLOW}\nNhấn Enter để mở trang cập nhật...")

                        
                        # Lấy link update
                        try:
                            update_response = requests.get(update_url, timeout=10)
                            if update_response.status_code == 200:
                                update_link = update_response.text.strip()
                                print(f"{Fore.YELLOW}Đang mở link tải phiên bản mới nhất...")
                                webbrowser.open(update_link)
                                print(f"{Fore.GREEN}Nếu trình duyệt không tự mở, vui lòng truy cập: {Fore.CYAN}{update_link}")
                            else:
                                print(f"{Fore.YELLOW}Không thể lấy link cập nhật. Vui lòng liên hệ Admin.")
                        except Exception as e:
                            print(f"{Fore.RED}Lỗi khi mở link cập nhật: {e}")
                        
                        self.cam_on_nguoi_dung()
                        sys.exit(0)
                        
                    elif latest_version == self.current_version:
                        print(f"{Fore.GREEN}[✔] Bạn đang sử dụng phiên bản mới nhất.\n")
                        
                    else:
                        # Trường hợp phiên bản hiện tại > phiên bản trên server
                        print(f"\n{Back.RED}{Fore.WHITE} ⚠️ PHIÊN BẢN KHÔNG HỢP LỆ ⚠️ {Style.RESET_ALL}")
                        print(f"{Fore.RED}Phiên bản hiện tại ({self.current_version}) cao hơn phiên bản công bố ({latest_version})!")
                        print(f"{Fore.RED}Điều này có thể xảy ra do lỗi hệ thống hoặc bạn đang dùng phiên bản không chính thức.")
                        print(f"{Fore.YELLOW}Vui lòng tải lại tool từ nguồn chính thức của Admin.")
                        print(f"{Fore.YELLOW}Liên hệ Admin: {Fore.CYAN}{CONFIG['FB_URL']}")
                        self.cam_on_nguoi_dung()
                        input(f"{Fore.YELLOW}\nNhấn Enter để đóng tool...")
                        sys.exit(0)
                else:
                    print(f"{Fore.YELLOW}[!] Không thể kiểm tra phiên bản mới. (Mã lỗi: {version_response.status_code})")
                    print(f"{Fore.YELLOW}Vui lòng kiểm tra kết nối mạng và thử lại.")
                    self.cam_on_nguoi_dung()
                    sys.exit(0)
            except requests.exceptions.ConnectionError:
                print(f"{Fore.YELLOW}[!] Không thể kết nối để kiểm tra phiên bản mới.")
                print(f"{Fore.YELLOW}Vui lòng kiểm tra kết nối mạng và thử lại.")
                self.cam_on_nguoi_dung()
                sys.exit(0)
            except Exception as e:
                print(f"{Fore.YELLOW}[!] Lỗi khi kiểm tra phiên bản: {e}")
                self.cam_on_nguoi_dung()
                sys.exit(0)
                
        except Exception as e:
            print(f"{Fore.RED}[-] Lỗi không xác định khi kiểm tra: {e}")
            self.cam_on_nguoi_dung()
            sys.exit(0)
    
    def cam_on_nguoi_dung(self):
        """Hiển thị lời cảm ơn đến người dùng"""
        print("\n" + Fore.CYAN + "═" * 72)
        print(f"{Fore.MAGENTA}      CẢM ƠN BẠN ĐÃ QUAN TÂM ĐẾN CÔNG CỤ!      ")
        print(Fore.CYAN + "═" * 72)
        print(f"{Fore.GREEN}✨ Công cụ được phát triển với mục đích học tập và nghiên cứu bảo mật.")
        print(f"{Fore.YELLOW}✨ Mọi thắc mắc xin liên hệ: {Fore.CYAN}{CONFIG['FB_URL']}")
        print(Fore.CYAN + "═" * 72)

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
    
    # Kiểm tra phiên bản và trạng thái trước khi cho phép sử dụng
    tool.kiem_tra_phien_ban_va_trang_thai()
    
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
    
    # Hiển thị cảm ơn khi kết thúc (nếu tool chạy thành công)
    tool.cam_on_nguoi_dung()
    input(f"{Fore.WHITE}\nNhấn Enter để đóng tool...")