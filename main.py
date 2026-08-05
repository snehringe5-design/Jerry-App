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
    from plyer import tts, battery, flashlight
    HARDWARE_AVAILABLE = True
except Exception:
    HARDWARE_AVAILABLE = False

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
        
        # 1. Creator & Identity (Strict rule: Sneh Ringe Sir / Sneh Sir)
        if any(w in q for w in ["kisne banaya", "who made you", "who created you", "kaun banaya", "tumhe kisne banaya"]):
            return "Sneh Sir, mujhe aap hi ke creator Sneh Ringe ne banaya hai. Main Sneh Ringe Sir ka personal AI assistant hoon."
        
        elif any(w in q for w in ["tum kon hon", "tum kon ho", "who are you", "kaun ho"]):
            return "Sneh Sir, main Jerry hoon—aapka apna zaati Jarvis-style AI assistant."

        # 2. User Profile & Work Details (Patel Motors, Salary, Duty Time, Zomato, Gori Nagar, Indore)
        elif any(w in q for w in ["meri details", "mera profile", "meri jankari", "job", "salary", "duty", "zomato", "patel motors"]):
            return "Sneh Sir, aap Patel Motors par Service Advisor hain. Aapka duty time subah 9:30 se shaam 7:00 baje tak hai, salary 12000 hai. Extra income ke liye aap Zomato par kaam karna chahte hain. Aap Gori Nagar, Indore mein rehte hain aur aapka janm 21 May 2006 ko Indore mein hua hai."

        # 3. Kundli, Grah, Nakshatra & Astrology (21-05-2006, Indore)
        elif any(w in q for w in ["kundli", "grah", "nakshatra", "rashifal", "astrology", "sitare", "planet"]):
            return "Sneh Sir, 21 May 2006 aur Indore janm sthan ke adhar par aapki kundli ke grah-nakshatra behad shubh aur unnati ke yog darsha rahe hain."

        # 4. Units & Measurements (Kilogram, Ton, Kuntal)
        elif any(w in q for w in ["kg", "kilogram", "ton", "kuntal", "wajan", "weight"]):
            return "Sneh Sir, 1 Quintal = 100 किलोग्राम hota hai, aur 1 Ton = 1000 किलोग्राम (yaani 10 कंटल) hota hai."

        # 5. World Currencies & Money
        elif any(w in q for w in ["currency", "paisa", "rupaye", "dollar", "money"]):
            return "Sneh Sir, alag-alag deshon mein alag currencies chalti hain jaise Bharat mein Indian Rupee (INR) aur US mein Dollar (USD)."

        # 6. Indian Democracy & History
        elif any(w in q for w in ["democracy", "tantra", "itihaas", "history", "yug", "satyug", "dwapar", "treta"]):
            return "Sneh Sir, purane yugo (Satyug, Treta, Dwapar aur Kaliyug) ka gyan hamare grantho mein hai, aur Bharat mein 1947 ke baad ek mazboot loktantra sthapit hai."

        # 7. Vedas & Puranas (Chatur Ved, Shiv Puran, Garuda Puran)
        elif any(w in q for w in ["ved", "veda", "puran", "shiv puran", "garud puran", "gyan"]):
            return "Sneh Sir, charo ved aur puran jaise Shiv Puran aur Garuda Puran mein agath gyan samahit hai."

        # 8. Flashlight / Torch Control
        elif any(w in q for w in ["torch on", "flashlight on", "light jalao", "torch jalao"]):
            if HARDWARE_AVAILABLE:
                try:
                    flashlight.on()
                    return "Beshak Sneh Sir, flashlight on kar di gayi hai."
                except Exception:
                    return "Sneh Sir, flashlight on karne mein takneki dikkat aayi."
            return "Sneh Sir, hardware module upabdh nahi hai."

        elif any(w in q for w in ["torch off", "flashlight off", "light bujhaao", "torch band"]):
            if HARDWARE_AVAILABLE:
                try:
                    flashlight.off()
                    return "Beshak Sneh Sir, flashlight off kar di gayi hai."
                except Exception:
                    return "Sneh Sir, flashlight off karne mein dikkat aayi."
            return "Sneh Sir, hardware module upabdh nahi hai."

        # 9. Battery Status Check
        elif any(w in q for w in ["battery", "charge", "power"]):
            if HARDWARE_AVAILABLE:
                try:
                    status = battery.status
                    percentage = status.get('percentage', 'unknown')
                    return f"Sneh Sir, current battery level {percentage}% hai."
                except Exception:
                    return "Sneh Sir, battery status read karne mein asafalta rahi."
            return "Sneh Sir, battery data upalabdh nahi hai."

        # 10. Camera & Vision Module
        elif any(w in q for w in ["camera", "dekh", "samne", "photo", "scan"]):
            return "Sneh Sir, camera module active kiya ja raha hai taaki samne ki sthiti ko scan kiya ja sake."

        # 11. Apps Control (Instagram, WhatsApp, OTP/SMS)
        elif any(w in q for w in ["instagram", "insta", "whatsapp", "otp", "message", "sms"]):
            return "Sneh Sir, target app ya SMS/OTP ko track karne ki permission active kar di gayi hai."

        # Default Jarvis Response
        else:
            return f"Beshak Sneh Sir, maine aapki baat ' {query} ' dhyan se sun li hai. Hukam kijiye is par kya karyavahi ki jaye?"

class LoginScreen(BoxLayout):
    def __init__(self, switch_callback, open_change_pass, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 20
        self.switch_callback = switch_callback
        self.open_change_pass = open_change_pass

        self.add_widget(Label(
            text="JERRY AI - SUPREME MASTER LOGIN",
            font_size=20,
            size_hint_y=None,
            height=50,
            color=(0, 0, 0, 1)
        ))

        self.pass_input = TextInput(
            hint_text="Enter Password, Sneh Sir...",
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
            self.msg_label.text = "Galat password Sneh Sir! Dubara koshish karein."

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
                self.msg_label.text = "Password safaltapoorvak badal gaya Sneh Sir!"
                Clock.schedule_once(lambda dt: self.back_to_login(), 1.5)
            else:
                self.msg_label.text = "Naya password khali nahi ho sakta Sneh Sir!"
        else:
            self.msg_label.text = "Purana password galat hai Sneh Sir!"

class JerryUI(BoxLayout):
    def __init__(self, **kwargs):
        super(JerryUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        self.add_widget(Label(
            text="JARVIS - JERRY AI (SUPREME SYSTEM CONTROL)",
            font_size=18,
            size_hint_y=None,
            height=50,
            color=(0, 0, 0, 1)
        ))

        self.response_label = Label(
            text="Adab Sneh Sir! Main Sneh Ringe Sir ka personal AI assistant Jerry hoon. Hukam kijiye.",
            font_size=16,
            color=(0.2, 0.2, 0.2, 1),
            halign='center',
            valign='middle'
        )
        self.response_label.bind(size=lambda s, w: setattr(s, 'text_size', w))
        self.add_widget(self.response_label)

        self.user_input = TextInput(
            hint_text="Yahan likhiye Sneh Sir (jaise: kundli, torch)...",
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

    def on_send_click(self, instance):
        text = self.user_input.text.strip()
        if text != "":
            try:
                reply = JerryJarvisBrain.get_response(text)
                self.response_label.text = reply
                
                if HARDWARE_AVAILABLE:
                    try:
                        tts.speak(reply)
                    except Exception:
                        pass
            except Exception as e:
                self.response_label.text = f"Error: {str(e)}"
            
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
            
