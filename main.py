from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase

# (वैकल्पिक) हिंदी फॉंट सपोर्ट के लिए यदि आपके प्रोजेक्ट में कोई .ttf फॉंट हो तो उसका रास्ता दें, 
# फिलहाल डिफ़ॉल्ट से एरर रोकने के लिए बेसिक सेटअप है।

# --- Login Screen (सुरक्षा के लिए) ---
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # आपका नया पर्सनल पिन
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


# --- Main AI Screen (Jerry) ---
class JerryMainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.creator = "Sneh Ringe"

        self.welcome_label = Label(
            text=f"Namaste! Main Jerry hoon.\nCreated by {self.creator} Sir.",
            font_size='20sp',
            halign='center',
            valign='middle'
        )
        self.welcome_label.bind(size=self.welcome_label.setter('text_size'))
        layout.add_widget(self.welcome_label)

        self.user_input = TextInput(
            hint_text="Sneh sir, aadesh dijiye...",
            multiline=False,
            size_hint_y=0.2
        )
        layout.add_widget(self.user_input)

        self.send_btn = Button(
            text="Command Jerry",
            size_hint_y=0.2
        )
        self.send_btn.bind(on_press=self.process_command)
        layout.add_widget(self.send_btn)

        self.add_widget(layout)

    def process_command(self, instance):
        text = self.user_input.text.lower()
        if "who made you" in text or "kisne banaya" in text:
            self.welcome_label.text = f"Mujhe mere malik {self.creator} ne banaya hai!"
        else:
            self.welcome_label.text = f"Sneh sir, aapka aadesh mila: {self.user_input.text}"
        
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
    
