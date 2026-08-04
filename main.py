from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

# --- Login Screen ---
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.secret_pin = "6263"

        self.label = Label(
            text="Jerry AI Locked\nOnly Sneh Sir can access.\nEnter PIN:",
            font_size='20sp',
            halign='center',
            valign='middle'
        )
        self.label.bind(size=self.label.setter('text_size'))
        layout.add_widget(self.label)

        self.pin_input = TextInput(
            password=True,
            multiline=False,
            size_hint_y=0.2,
            halign='center',
            hint_text="Enter Secret PIN"
        )
        layout.add_widget(self.pin_input)

        btn = Button(text="Unlock Jerry", size_hint_y=0.2)
        btn.bind(on_press=self.verify_pin)
        layout.add_widget(btn)

        self.add_widget(layout)

    def verify_pin(self, instance):
        if self.pin_input.text == self.secret_pin:
            self.manager.current = 'jerry_main'
        else:
            self.label.text = "Wrong PIN!\nUnauthorized Access.\nEnter PIN:"
            self.pin_input.text = ""


# --- Main AI Screen (Chat Style Jerry) ---
class JerryMainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_layout = BoxLayout(orientation='vertical')
        self.creator = "Sneh Ringe"

        # चैट हिस्ट्री दिखाने के लिए ScrollView और Layout
        self.scroll = ScrollView(size_hint=(1, 0.8))
        self.chat_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10, padding=10)
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))

        # वेलकम मैसेज जोड़े
        self.add_chat_message("Jerry: Namaste Sneh Sir! Main aapka personal AI assistant hoon.")

        self.scroll.add_widget(self.chat_layout)
        main_layout.add_widget(self.scroll)

        # नीचे इनपुट और भेजने का बटन रखने के लिए लेआउट
        bottom_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=5)

        self.user_input = TextInput(
            hint_text="Sneh sir, aadesh dijiye...",
            multiline=False,
            size_hint_x=0.8
        )
        bottom_layout.add_widget(self.user_input)

        self.send_btn = Button(
            text="Send",
            size_hint_x=0.2
        )
        self.send_btn.bind(on_press=self.process_command)
        bottom_layout.add_widget(self.send_btn)

        main_layout.add_widget(bottom_layout)
        self.add_widget(main_layout)

    def add_chat_message(self, message):
        lbl = Label(
            text=message,
            font_size='16sp',
            size_hint_y=None,
            height=40,
            halign='left',
            valign='middle'
        )
        lbl.bind(size=lbl.setter('text_size'))
        self.chat_layout.add_widget(lbl)

    def process_command(self, instance):
        text = self.user_input.text.strip()
        if not text:
            return

        # यूजर का मैसेज चैट में जोड़ें
        self.add_chat_message(f"Sneh Sir: {text}")
        
        # जेरी का स्मार्ट रिस्पॉन्स
        query = text.lower()
        if "who made you" in query or "kisne banaya" in query:
            response = f"Jerry: Mujhe mere malik {self.creator} ne banaya hai!"
        elif "tum kon ho" in query or "who are you" in query:
            response = f"Jerry: Main Jerry hoon, {self.creator} Sir ka personal AI assistant!"
        elif "kaise ho" in query or "how are you" in query:
            response = "Jerry: Main ekdum badiya hoon Sir!"
        else:
            response = f"Jerry: Sneh Sir, aapka aadesh mila: '{text}'"

        self.add_chat_message(response)
        self.user_input.text = ""


# --- App Manager ---
class JerryApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(JerryMainScreen(name='jerry_main'))
        return sm


if __name__ == '__main__':
    JerryApp().run()
    
