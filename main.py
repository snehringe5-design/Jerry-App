import os
import threading
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

PASSWORD_FILE = "jerry_pass.txt"
# Yahan apni OpenAI ya Gemini API key daal sakte hain Sneh Sir
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

class JerryBrain:
    @staticmethod
    def get_response(query):
        q = query.lower()
        
        # Personal & Hardcoded Rules
        if any(w in q for w in ["kisne banaya", "who made you", "kaun banaya"]):
            return "Sneh Sir, mujhe aap hi ke creator Sneh Ringe ne banaya hai."
        
        elif any(w in q for w in ["meri details", "mera profile", "job", "salary", "duty", "zomato", "patel motors"]):
            return "Sneh Sir, aap Patel Motors par Service Advisor hain. Duty subah 9:30 se shaam 7:00 baje tak hai, salary 12000 hai. Extra income ke liye Zomato par kaam karna chahte hain. Aap Gori Nagar, Indore mein rehte hain aur aapka janm 21 May 2006 ko hua hai."

        elif any(w in q for w in ["kundli", "grah", "nakshatra", "astrology"]):
            return "Sneh Sir, 21 May 2006 aur Indore janm sthan ke adhar par aapki kundli ke grah-nakshatra behad shubh hain."

        # Online API Integration
        else:
            try:
                if API_KEY != "YOUR_API_KEY_HERE":
                    headers = {
                        "Authorization": f"Bearer {API_KEY}",
                        "Content-Type": "application/json"
                    }
                    data = {
                        "model": "gpt-3.5-turbo",
                        "messages": [
                            {"role": "system", "content": "You are Jerry, a personal AI assistant built exclusively for Sneh Ringe (address them strictly as Sneh Sir)."},
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
            text="JERRY AI - LOGIN",
            font_size=24,
            bold=True,
            size_hint_y=None,
            height=60,
            color=(0.1, 0.1, 0.1, 1)
        ))

        self.pass_input = TextInput(
            hint_text="Enter Password, Sneh Sir...",
            password=True,
            font_size=18,
            size_hint_y=None,
            height=60,
            multiline=False
        )
        self.add_widget(self.pass_input)

        self.login_btn = Button(
            text="UNLOCK",
            font_size=18,
            bold=True,
            size_hint_y=None,
            height=60,
            background_color=(0.1, 0.5, 0.8, 1)
        )
        self.login_btn.bind(on_press=self.verify_password)
        self.add_widget(self.login_btn)

        self.change_btn = Button(
            text="Change Password",
            font_size=16,
            size_hint_y=None,
            height=50,
            background_color=(0.4, 0.4, 0.4, 1)
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
        if self.pass_input.text.strip() == get_saved_password():
            self.switch_callback()
        else:
            self.msg_label.text = "Galat password Sneh Sir!"

class ChangePasswordScreen(BoxLayout):
    def __init__(self, back_to_login, **kwargs):
        super(ChangePasswordScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 20
        self.back_to_login = back_to_login

        self.add_widget(Label(
            text="CHANGE PASSWORD",
            font_size=24,
            bold=True,
            size_hint_y=None,
            height=60,
            color=(0.1, 0.1, 0.1, 1)
        ))

        self.old_input = TextInput(
            hint_text="Purana Password...",
            password=True,
            font_size=18,
            size_hint_y=None,
            height=60,
            multiline=False
        )
        self.add_widget(self.old_input)

        self.new_input = TextInput(
            hint_text="Naya Password...",
            password=True,
            font_size=18,
            size_hint_y=None,
            height=60,
            multiline=False
        )
        self.add_widget(self.new_input)

        self.save_btn = Button(
            text="SAVE",
            font_size=18,
            bold=True,
            size_hint_y=None,
            height=60,
            background_color=(0.1, 0.7, 0.3, 1)
        )
        self.save_btn.bind(on_press=self.update_password)
        self.add_widget(self.save_btn)

        self.back_btn = Button(
            text="Back",
            font_size=16,
            size_hint_y=None,
            height=50,
            background_color=(0.4, 0.4, 0.4, 1)
        )
        self.back_btn.bind(on_press=lambda x: self.back_to_login())
        self.add_widget(self.back_btn)

        self.msg_label = Label(text="", font_size=16, color=(0.8, 0.1, 0.1, 1), size_hint_y=None, height=40)
        self.add_widget(self.msg_label)

    def update_password(self, instance):
        if self.old_input.text.strip() == get_saved_password():
            if self.new_input.text.strip() != "":
                save_new_password(self.new_input.text.strip())
                self.msg_label.color = (0.1, 0.6, 0.1, 1)
                self.msg_label.text = "Password badal gaya Sneh Sir!"
                Clock.schedule_once(lambda dt: self.back_to_login(), 1.5)
            else:
                self.msg_label.text = "Naya password khali nahi ho sakta!"
        else:
            self.msg_label.text = "Purana password galat hai!"

class JerryUI(BoxLayout):
    def __init__(self, **kwargs):
        super(JerryUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 15
        self.spacing = 10

        self.add_widget(Label(
            text="JERRY AI CHAT",
            font_size=18,
            bold=True,
            size_hint_y=None,
            height=35,
            color=(0.1, 0.3, 0.5, 1)
        ))

        self.scroll = ScrollView(size_hint=(1, 1))
        self.chat_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))
        self.scroll.add_widget(self.chat_layout)
        self.add_widget(self.scroll)

        self.add_bubble("Jerry: Adab Sneh Sir! Hukam kijiye.", is_user=False)

        input_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=55, spacing=10)
        
        self.user_input = TextInput(
            hint_text="Yahan likhiye Sneh Sir...",
            font_size=16,
            multiline=False,
            size_hint_x=0.75
        )
        input_box.add_widget(self.user_input)

        self.send_btn = Button(
            text="SEND",
            font_size=16,
            bold=True,
            size_hint_x=0.25,
            background_color=(0.1, 0.5, 0.8, 1)
        )
        self.send_btn.bind(on_press=self.on_send)
        input_box.add_widget(self.send_btn)

        self.add_widget(input_box)

    def add_bubble(self, text, is_user=False):
        lbl = Label(
            text=text,
            font_size=16,
            color=(1, 1, 1, 1) if is_user else (0.1, 0.1, 0.1, 1),
            size_hint_y=None,
            text_size=(300, None),
            halign='right' if is_user else 'left',
            valign='middle'
        )
        lbl.bind(texture_size=lambda s, w: setattr(s, 'height', max(45, w[1] + 15)))
        self.chat_layout.add_widget(lbl)
        self.scroll.scroll_y = 0

    def on_send(self, instance):
        text = self.user_input.text.strip()
        if text != "":
            self.add_bubble(f"Sneh Sir: {text}", is_user=True)
            self.user_input.text = ""
            
            def background_process():
                reply = JerryBrain.get_response(text)
                Clock.schedule_once(lambda dt: self.add_bubble(f"Jerry: {reply}", is_user=False), 0.1)

            threading.Thread(target=background_process, daemon=True).start()

class JerryApp(App):
    def build(self):
        from kivy.core.window import Window
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        self.root_layout = BoxLayout(orientation='vertical')
        self.show_login()
        return self.root_layout

    def show_login(self):
        self.root_layout.clear_widgets()
        self.root_layout.add_widget(LoginScreen(self.show_main, self.show_pass_change))

    def show_pass_change(self):
        self.root_layout.clear_widgets()
        self.root_layout.add_widget(ChangePasswordScreen(self.show_login))

    def show_main(self):
        self.root_layout.clear_widgets()
        self.root_layout.add_widget(JerryUI())

if __name__ == '__main__':
    JerryApp().run()
        
