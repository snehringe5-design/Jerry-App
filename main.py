import os
import threading
import time
import requests
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from plyer import tts

# Self-Repairing Engine (ऑटो-अपडेट फीचर)
def auto_repair_and_update():
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
                    print("Jerry: Code successfully repaired/updated from cloud!")
                    tts.speak("सर, मैंने अपना कोड खुद अपडेट कर लिया है।")
        except Exception as e:
            print(f"Repair check failed: {e}")
        
        time.sleep(300)

def speak_output(text):
    try:
        tts.speak(text)
    except Exception as e:
        print(f"TTS Error: {e}")

class JerryUI(BoxLayout):
    def __init__(self, **kwargs):
        super(JerryUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        self.title_label = Label(
            text="[b]JERRY AI ASSISTANT[/b]",
            markup=True,
            font_size=26,
            color=(0.1, 0.1, 0.1, 1),
            size_hint_y=None,
            height=60
        )
        self.add_widget(self.title_label)

        self.output_label = Label(
            text="नमस्ते सर, बोलिए मैं आपकी क्या मदद करूँ?",
            font_size=18,
            color=(0.3, 0.3, 0.3, 1),
            halign='center',
            valign='middle'
        )
        self.output_label.bind(size=self.output_label.setter('text_texture_size'))
        self.add_widget(self.output_label)

        self.user_input = TextInput(
            hint_text="यहाँ टाइप करें...",
            size_hint_y=None,
            height=50,
            multiline=False
        )
        self.add_widget(self.user_input)

        self.send_btn = Button(
            text="बात करें (Speak & Send)",
            size_hint_y=None,
            height=60,
            background_color=(0.1, 0.6, 0.9, 1)
        )
        self.send_btn.bind(on_press=self.process_command)
        self.add_widget(self.send_btn)

        threading.Thread(target=auto_repair_and_update, daemon=True).start()

    def process_command(self, instance):
        text = self.user_input.text
        if text.strip() != "":
            response_text = f"आपने कहा: {text}. मैं समझ गया हूँ सर!"
            self.output_label.text = response_text
            speak_output(response_text)
            self.user_input.text = ""

class JerryApp(App):
    def build(self):
        from kivy.core.window import Window
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        return JerryUI()

if __name__ == '__main__':
    JerryApp().run()
    
