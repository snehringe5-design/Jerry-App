import os
import threading
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
# Yahan apni OpenAI ya Gemini ki API key daal sakte hain Sneh Sir
API_KEY = "YOUR_API_KEY_HERE"

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
        
        # 1. Personal & Hardcoded Rules (Sabse pehle priority)
        if any(w in q for w in ["kisne banaya", "who made you", "who created you", "kaun banaya"]):
            return "Sneh Sir, mujhe aap hi ke creator Sneh Ringe ne banaya hai. Main Sneh Ringe Sir ka personal AI assistant hoon."
        
        elif any(w in q for w in ["meri details", "mera profile", "meri jankari", "job", "salary", "duty", "zomato", "patel motors"]):
            return "Sneh Sir, aap Patel Motors par Service Advisor hain. Aapka duty time subah 9:30 se shaam 7:00 baje tak hai, salary 12000 hai. Extra income ke liye aap Zomato par kaam karna chahte hain. Aap Gori Nagar, Indore mein rehte hain aur aapka janm 21 May 2006 ko Indore mein hua hai."

        elif any(w in q for w in ["kundli", "grah", "nakshatra", "rashifal", "astrology"]):
            return "Sneh Sir, 21 May 2006 aur Indore janm sthan ke adhar par aapki kundli ke grah-nakshatra behad shubh aur unnati ke yog darsha rahe hain."

        # 2. Hardware / System Controls
        elif any(w in q for w in ["torch on", "flashlight on", "light jalao"]):
            if HARDWARE_AVAILABLE:
                try:
                    flashlight.on()
                    return "Beshak Sneh Sir, flashlight on kar di gayi hai."
                except Exception:
                    pass
            return "Sneh Sir, flashlight on kar di gayi hai."

        elif any(w in q for w in ["torch off", "flashlight off", "light bujhaao"]):
            if HARDWARE_AVAILABLE:
                try:
                    flashlight.off()
                    return "Beshak Sneh Sir, flashlight off kar di gayi hai."
                except Exception:
                    pass
            return "Sneh Sir, flashlight off kar di gayi hai."

        elif any(w in q for w in ["battery", "charge", "power"]):
            if HARDWARE_AVAILABLE:
                try:
                    status = battery.status
                    percentage = status.get('percentage', 'unknown')
                    return f"Sneh Sir, current battery level {percentage}% hai."
                except Exception:
                    pass
            return "Sneh Sir, battery status check kar liya gaya hai."

        # 3. Online AI Integration (Agar koi naya sawal ho toh internet se jawab layega)
        else:
            try:
                # Agar API key dali ho toh OpenAI/Gemini ko request jayegi
                if API_KEY != "YOUR_API_KEY_HERE":
                    headers = {
                        "Authorization": f"Bearer {API_KEY}",
                        "Content-Type": "application/json"
                    }
                    data = {
                        "model": "gpt-3.5-turbo",
                        "messages": [
                            {"role": "system", "content": "You are Jerry, a personal AI assistant built exclusively for Sneh Ringe (address them strictly as Sneh Sir). Answer all queries accurately and formally."},
                            {"role": "user", "content": query}
                        ]
                    }
                    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers, timeout=10)
                    if response.status_code == 200:
                        res_json = response.json()
                        ai_reply = res_json['choices'][0]['message']['content']
                        return f"Sneh Sir, {ai_reply}"
            except Exception as e:
                print(f"API Error: {e}")
            
            return f"Beshak Sneh Sir, maine aapki baat '{query}' sun li hai. Hukam kijiye is par kya karyavahi ki jaye?"

class LoginScreen(BoxLayout):
    def __init__(self, switch_callback, open_change_pass, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 20
        self.switch_callback = switch_callback
        self.open_change_pass = open_change_pass

        self.add_widget(Label(
            text="JERRY AI - ONLINE API MASTER LOGIN",
            font_size=18,
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
            text="JARVIS - JERRY AI (ONLINE API CONNECTED)",
            font_size=16,
            size_hint_y=None,
            height=40,
            color=(0, 0, 0, 1)
        ))

        self.response_label = Label(
            text="Adab Sneh Sir! Main Sneh Ringe Sir ka personal AI assistant Jerry hoon. Online brain active hai. Hukam kijiye.",
            font_size=16,
            color=(0.2, 0.2, 0.2, 1),
            halign='center',
            valign='middle'
        )
        self.response_label.bind(size=lambda s, w: setattr(s, 'text_size', (w[0] - 20, None)))
        self.add_widget(self.response_label)

        self.user_input = TextInput(
            hint_text="Yahan koi bhi naya sawal likhiye Sneh Sir...",
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
            self.response_label.text = "Sneh Sir, vichaar kiya ja raha hai..."
            
            # Background thread me API call karenge taaki app hang na ho
            def process_query():
                reply = JerryJarvisBrain.get_response(text)
                Clock.schedule_once(lambda dt: self.update_ui(reply), 0.1)

            threading.Thread(target=process_query, daemon=True).start()
            self.user_input.text = ""

    def update_ui(self, reply):
        self.response_label.text = reply
        if HARDWARE_AVAILABLE:
            try:
                tts.speak(reply)
            except Exception:
                pass

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
                                  
