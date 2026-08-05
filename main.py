import os
import threading
import time
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

try:
    from plyer import tts
    TTS_AVAILABLE = True
except Exception:
    TTS_AVAILABLE = False

PASSWORD_FILE = "jerry_pass.txt"

def get_saved_password():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r", encoding="utf-8") as f:
            p = f.read().strip()
            if p:
                return p
    return "6263"

def save_new_password(new_p):
    with open(PASSWORD_FILE, "w", encoding="utf-8") as f:
        f.write(new_p)

class JerryJarvisBrain:
    @staticmethod
    def get_response(query):
        q = query.lower()
        
        # 1. Creator Identity
        if any(w in q for w in ["kisne banaya", "who made you", "who created you", "kaun banaya"]):
            return "Janab, mujhe mere creator Sneh Ringe ne banaya hai. Main unhi ka banaya hua Jarvis hoon."
        
        # 2. General Identity
        elif any(w in q for w in ["tum kon hon", "tum kon ho", "who are you", "kaun ho"]):
            return "Janab, main Jerry hoon—aapka apna zaati AI assistant, bilkul Jarvis ki tarah."
        
        # 3. Battery Status Check
        elif any(w in q for w in ["battery", "charge", "power"]):
            return "Janab, system ki battery status check karne ke liye Android native bridge active kiya ja raha hai."
        
        # 4. Flashlight / Torch
        elif any(w in q for w in ["torch", "flashlight", "light jalao"]):
            return "Beshak janab, flashlight on karne ka command execute ho raha hai."
        
        # 5. Camera & Vision
        elif any(w in q for w in ["camera", "dekh", "samne", "photo", "video"]):
            return "Janab, camera module active karke samne ki cheezon ko scan karne ki koshish ki ja rahi hai."
        
        # 6. Instagram & Apps
        elif any(w in q for w in ["instagram", "insta", "whatsapp", "app kholo", "open app"]):
            return "Janab, aapke kehne par target app ko launch karne aur uske notifications/messages ko track karne ki permission di ja chuki hai."
        
        # 7. OTP & Messages
        elif any(w in q for w in ["otp", "message", "sms", "code"]):
            return "Janab, jaise hi koi naya OTP ya SMS aayega, main use turant read karke aapko bata dunga."
        
        # 8. Voice & Offline Brain
        elif any(w in q for w in ["voice", "bolo", "suno", "offline"]):
            return "Janab, speech-to-text aur local AI model ko integrate karne ka framework taiyar hai."
        
        # Default Jarvis Response
        else:
            return f"Beshak janab, maine aapki baat ' {query} ' gehrai se sun li hai. Hukam kijiye is par kya amal kiya jaye?"

def auto_repair_and_update():
    time.sleep(10)
    while True:
        try:
            url = "https://raw.githubusercontent.com/snehringe5-design/Jerry-App/main/latest_logic.py"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                new_code = response.text
                local_file = "current_logic.py"
                if os.path.exists(local_file):
                    with open(local_file, "r", encoding="utf-8") as f:
                        old_code = f.read()
                else:
                    old_code = ""

                if new_code != old_code:
                    with open(local_file, "w", encoding="utf-8") as f:
                        f.write(new_code)
                    if TTS_AVAILABLE:
                        Clock.schedule_once(lambda dt: tts.speak("Janab, maine apna code khud update kar liya hai."), 0.1)
        except Exception as e:
            print(f"Update error: {e}")
        time.sleep(300)

class LoginScreen(BoxLayout):
    def __init__(self, switch_callback, open_change_pass, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 20
        self.switch_callback = switch_callback
        self.open_change_pass = open_change_pass

        self.add_widget(Label(
            text="JERRY AI - ULTIMATE SECURE LOGIN",
            font_size=20,
            size_hint_y=None,
            height=50,
            color=(0, 0, 0, 1)
        ))

        self.pass_input = TextInput(
            hint_text="Enter Password (Janab)...",
            password=True,
            size_hint_y=None,
            height=60,
            multiline=False
        )
        self.add_widget(self.pass_input)

        self.login_btn = Button(
            text="UNLOCK JERRY",
            size_hint_y=None,
            height=60,
            background_color=(0.1, 0.5, 0.8, 1)
        )
        self.login_btn.bind(on_press=self.verify_password)
        self.add_widget(self.login_btn)

        self.change_btn = Button(
            text="Change Password",
            size_hint_y=None,
            height=50,
            background_color=(0.5, 0.5, 0.5, 1)
        )
        self.change_btn.bind(on_press=lambda x: self.open_change_pass())
        self.add_widget(self.change_btn)

        self.msg_label = Label(
            text="",
            font_size=16,
            color=(0.8, 0.1, 0.1, 1),
            size_hint_y=None,
            height=40
        )
        self.add_widget(self.msg_label)

    def verify_password(self, instance):
        current_pass = get_saved_password()
        if self.pass_input.text.strip() == current_pass:
            self.switch_callback()
        else:
            self.msg_label.text = "Galat password janab! Dubara koshish karein."

class ChangePasswordScreen(BoxLayout):
    def __init__(self, back_to_login, **kwargs):
        super(ChangePasswordScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 20
        self.back_to_login = back_to_login

        self.add_widget(Label(
            text="CHANGE PASSWORD",
            font_size=22,
            size_hint_y=None,
            height=50,
            color=(0, 0, 0, 1)
        ))

        self.old_input = TextInput(
            hint_text="Purana Password Daaliye...",
            password=True,
            size_hint_y=None,
            height=60,
            multiline=False
        )
        self.add_widget(self.old_input)

        self.new_input = TextInput(
            hint_text="Naya Password Daaliye...",
            password=True,
            size_hint_y=None,
            height=60,
            multiline=False
        )
        self.add_widget(self.new_input)

        self.save_btn = Button(
            text="SAVE NEW PASSWORD",
            size_hint_y=None,
            height=60,
            background_color=(0.1, 0.7, 0.3, 1)
        )
        self.save_btn.bind(on_press=self.update_password)
        self.add_widget(self.save_btn)

        self.back_btn = Button(
            text="Back to Login",
            size_hint_y=None,
            height=50,
            background_color=(0.5, 0.5, 0.5, 1)
        )
        self.back_btn.bind(on_press=lambda x: self.back_to_login())
        self.add_widget(self.back_btn)

        self.msg_label = Label(
            text="",
            font_size=16,
            color=(0.8, 0.1, 0.1, 1),
            size_hint_y=None,
            height=40
        )
        self.add_widget(self.msg_label)

    def update_password(self, instance):
        saved_p = get_saved_password()
        old_p = self.old_input.text.strip()
        new_p = self.new_input.text.strip()

        if old_p == saved_p:
            if new_p != "":
                save_new_password(new_p)
                self.msg_label.color = (0.1, 0.6, 0.1, 1)
                self.msg_label.text = "Password safaltapoorvak badal gaya janab!"
                Clock.schedule_once(lambda dt: self.back_to_login(), 1.5)
            else:
                self.msg_label.text = "Naya password khali nahi ho sakta janab!"
        else:
            self.msg_label.text = "Purana password galat hai janab!"

class JerryUI(BoxLayout):
    def __init__(self, **kwargs):
        super(JerryUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        self.add_widget(Label(
            text="JARVIS - JERRY AI (FULL SYSTEM ACCESS)",
            font_size=18,
            size_hint_y=None,
            height=50,
            color=(0, 0, 0, 1)
        ))

        self.response_label = Label(
            text="Adab janab! Main aapka Jerry hoon. Battery, Torch, Camera, Apps, aur OTP—sab par meri nazar hai. Hukam kijiye.",
            font_size=16,
            color=(0.2, 0.2, 0.2, 1),
            halign='center',
            valign='middle'
        )
        self.response_label.bind(size=lambda s, w: setattr(s, 'text_size', w))
        self.add_widget(self.response_label)

        self.user_input = TextInput(
            hint_text="Yahan likhiye janab (jaise: camera, otp, instagram)...",
            size_hint_y=None,
            height=60,
            multiline=False
        )
        self.add_widget(self.user_input)

        self.send_btn = Button(
            text="HUKAM DIJIYE (SEND)",
            size_hint_y=None,
            height=60,
            background_color=(0.1, 0.5, 0.8, 1)
        )
        self.send_btn.bind(on_press=self.on_send_click)
        self.add_widget(self.send_btn)

        threading.Thread(target=auto_repair_and_update, daemon=True).start()

    def on_send_click(self, instance):
        text = self.user_input.text.strip()
        if text != "":
            reply = JerryJarvisBrain.get_response(text)
            self.response_label.text = reply
            
            if TTS_AVAILABLE:
                try:
                    Clock.schedule_once(lambda dt: tts.speak(reply), 0.1)
                except Exception as e:
                    print(f"TTS Error: {e}")
            
            self.user_input.text = ""

class JerryApp(App):
    def build(self):
        from kivy.core.window import Window
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        
        self.root_layout = BoxLayout(orientation='vertical')
        self.show_login()
        return self.root_layout

    def show_login(self):
        self.root_layout.clear_widgets()
        self.root_layout.add_widget(LoginScreen(self.show_main_app, self.show_change_pass))

    def show_change_pass(self):
        self.root_layout.clear_widgets()
        self.root_layout.add_widget(ChangePasswordScreen(self.show_login))

    def show_main_app(self):
        self.root_layout.clear_widgets()
        self.root_layout.add_widget(JerryUI())

if __name__ == '__main__':
    JerryApp().run()
    
