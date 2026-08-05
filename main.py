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

# Self-Repairing Engine (ऑटो-अपडेट और सेल्फ-रिपेयर फीचर)
def auto_repair_and_update():
    time.sleep(15)  # ऐप चालू होने के 15 सेकंड बाद बैकग्राउंड में चेक करना शुरू करेगा
    while True:
        try:
            # यहाँ अपनी गिटहब की raw फाइल का लिंक डालें जहाँ आपका लेटेस्ट लॉजिक हो
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

                # अगर गिटहब पर कोड बदला हुआ मिला, तो यह खुद को अपडेट कर लेगा
                if new_code != old_code:
                    with open(local_file, "w", encoding="utf-8") as f:
                        f.write(new_code)
                    print("Jerry: Code successfully repaired/updated from cloud!")
                    if TTS_AVAILABLE:
                        Clock.schedule_once(lambda dt: tts.speak("सर, मैंने अपना कोड खुद अपडेट कर लिया है।"), 0.1)
        except Exception as e:
            print(f"Repair check failed: {e}")
        
        time.sleep(300)  # हर 5 मिनट में अपडेट चेक करता रहेगा

class JerryRoot(BoxLayout):
    def __init__(self, **kwargs):
        super(JerryRoot, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        # टाइटल
        self.add_widget(Label(
            text="JERRY AI (SELF-REPAIRING)",
            font_size=20,
            size_hint_y=None,
            height=50,
            color=(0, 0, 0, 1)
        ))

        # जवाब दिखाने के लिए साफ़ लेबल
        self.response_label = Label(
            text="Hello Sir! I am online with self-repair engine.",
            font_size=18,
            color=(0.2, 0.2, 0.2, 1),
            halign='center',
            valign='middle'
        )
        self.response_label.bind(size=lambda s, w: setattr(s, 'text_size', w))
        self.add_widget(self.response_label)

        # इनपुट बॉक्स
        self.user_input = TextInput(
            hint_text="Type your message here...",
            size_hint_y=None,
            height=60,
            multiline=False
        )
        self.add_widget(self.user_input)

        # भेजने वाला बटन
        self.send_btn = Button(
            text="SEND",
            size_hint_y=None,
            height=60,
            background_color=(0.1, 0.5, 0.8, 1)
        )
        self.send_btn.bind(on_press=self.on_send_click)
        self.add_widget(self.send_btn)

        # बैकग्राउंड में सेल्फ-रिपेयर थ्रेड शुरू करना
        threading.Thread(target=auto_repair_and_update, daemon=True).start()

    def on_send_click(self, instance):
        text = self.user_input.text.strip()
        if text != "":
            reply = f"Sir, I received: '{text}'. Self-repair is active!"
            self.response_label.text = reply
            
            # बोलकर जवाब देना
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
        return JerryRoot()

if __name__ == '__main__':
    JerryApp().run()
                    
