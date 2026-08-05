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
from kivy.core.window import Window
from kivy.metrics import dp, sp

Window.softinput_mode = "below_target"

# Text-to-Speech Setup
HARDWARE_TTS = False
try:
    from plyer import tts
    HARDWARE_TTS = True
except Exception:
    pass

# Android Speech Recognition (Android Native Intent via Pyjnius)
is_android = False
try:
    from jnius import autoclass
    from android.runnable import run_on_ui_thread
    is_android = True
except Exception:
    is_android = False

# Apni API Key yahan daalein taaki Jerry khud soch sake
API_KEY = "YOUR_API_KEY_HERE"

class JerryBrain:
    @staticmethod
    def get_response(query):
        q = query.lower()
        
        # Local Smart Shortcuts
        if any(w in q for w in ["kisne banaya", "who made you", "kaun banaya", "tum kon ho", "tum kaun ho"]):
            return "Sneh Sir, main Jerry hoon, aapka personal AI assistant, jise aap hi ke creator Sneh Ringe ne banaya hai."
        
        elif any(w in q for w in ["meri details", "mera profile", "job", "salary", "duty", "zomato", "patel motors", "gori nagar"]):
            return "Sneh Sir, aap Patel Motors par Service Advisor hain. Duty subah 9:30 se shaam 7:00 baje tak hai, salary 12000 hai. Extra income ke liye Zomato par kaam karna chahte hain. Aap Gori Nagar, Indore mein rehte hain aur aapka janm 21 May 2006 ko hua hai."

        elif any(w in q for w in ["kundli", "grah", "nakshatra", "astrology"]):
            return "Sneh Sir, 21 May 2006 aur Indore janm sthan ke adhar par aapki kundli ke grah-nakshatra behad shubh hain."

        # Online AI Brain (Khud se sochne ke liye)
        else:
            if API_KEY != "YOUR_API_KEY_HERE":
                try:
                    headers = {
                        "Authorization": f"Bearer {API_KEY}",
                        "Content-Type": "application/json"
                    }
                    data = {
                        "model": "gpt-3.5-turbo",
                        "messages": [
                            {"role": "system", "content": "You are Jerry, a helpful personal AI assistant built for Sneh Ringe. Always address him strictly as Sneh Sir and speak in clear, simple Hindi."},
                            {"role": "user", "content": query}
                        ]
                    }
                    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers, timeout=12)
                    if response.status_code == 200:
                        res_json = response.json()
                        ai_reply = res_json['choices'][0]['message']['content']
                        return f"Sneh Sir, {ai_reply}"
                except Exception as e:
                    print(f"API Error: {e}")
            
            # Agar API key nahi dali hai ya internet nahi hai toh smart fallback
            return f"Sneh Sir, apne AI brain se soch raha hoon... Aapne pucha hai: '{query}'. Iske baare mein puri jaankari jald hi update hogi!"

class JerryUI(BoxLayout):
    def __init__(self, **kwargs):
        super(JerryUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(15)
        self.spacing = dp(12)

        self.add_widget(Label(
            text="JERRY AI CHAT",
            font_size=sp(22),
            bold=True,
            size_hint_y=None,
            height=dp(45),
            color=(0.1, 0.3, 0.6, 1)
        ))

        self.scroll = ScrollView(size_hint=(1, 1))
        self.chat_layout = GridLayout(cols=1, spacing=dp(18), size_hint_y=None)
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))
        self.scroll.add_widget(self.chat_layout)
        self.add_widget(self.scroll)

        initial_msg = "Namaste Sneh Sir! Main Jerry hoon. Boliye, kya madad karoon?"
        self.add_bubble(f"Jerry: {initial_msg}", is_user=False)
        self.speak_text(initial_msg)

        input_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(65), spacing=dp(8))
        
        self.mic_btn = Button(
            text="🎤",
            font_size=sp(24),
            size_hint_x=0.18,
            background_color=(0.8, 0.2, 0.2, 1)
        )
        self.mic_btn.bind(on_press=self.start_listening)
        input_box.add_widget(self.mic_btn)

        self.user_input = TextInput(
            hint_text="Yahan likhiye Sneh Sir...",
            font_size=sp(20),
            multiline=False,
            size_hint_x=0.57
        )
        input_box.add_widget(self.user_input)

        self.send_btn = Button(
            text="BHEJO",
            font_size=sp(18),
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
            font_size=sp(20),
            bold=True,
            color=(0.0, 0.3, 0.8, 1) if is_user else (0.1, 0.1, 0.1, 1),
            size_hint_y=None,
            text_size=(Window.width * 0.85, None),
            halign='right' if is_user else 'left',
            valign='middle'
        )
        lbl.bind(texture_size=lambda s, w: setattr(s, 'height', max(dp(50), w[1] + dp(20))))
        self.chat_layout.add_widget(lbl)
        self.scroll.scroll_y = 0

    def speak_text(self, text):
        if HARDWARE_TTS:
            try:
                tts.speak(text)
            except Exception:
                pass

    def start_listening(self, instance):
        if is_android:
            try:
                self.open_android_mic()
            except Exception:
                self.user_input.hint_text = "Mic start nahi ho paya!"
        else:
            self.user_input.hint_text = "Voice sirf Android par chalegi!"

    def open_android_mic(self):
        if is_android:
            try:
                from jnius import autoclass
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                Intent = autoclass('android.content.Intent')
                RecognizerIntent = autoclass('android.speech.RecognizerIntent')
                
                intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "hi-IN")
                intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "Sneh Sir, boliye...")
                
                currentActivity = PythonActivity.mActivity
                currentActivity.startActivityForResult(intent, 1010)
            except Exception as e:
                print(f"Mic Intent Error: {e}")

    def on_send(self, instance):
        text = self.user_input.text.strip()
        if text != "":
            self.add_bubble(f"Sneh Sir: {text}", is_user=True)
            self.user_input.text = ""
            
            def background_process():
                reply = JerryBrain.get_response(text)
                Clock.schedule_once(lambda dt: self.display_and_speak(reply), 0.1)

            threading.Thread(target=background_process, daemon=True).start()

    def display_and_speak(self, reply):
        self.add_bubble(f"Jerry: {reply}", is_user=False)
        self.speak_text(reply)

class JerryApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        return JerryUI()

if __name__ == '__main__':
    JerryApp().run()
        
