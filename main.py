import os
import threading
import requests
import re
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
from kivy.utils import platform

Window.softinput_mode = "below_target"

ROBOT_IP = "http://192.168.4.1" 

# Text-to-Speech Setup
HARDWARE_TTS = False
try:
    from plyer import tts
    HARDWARE_TTS = True
except Exception:
    pass

# Speech-to-Text Setup
HARDWARE_STT = False
try:
    from plyer import stt
    HARDWARE_STT = True
except Exception:
    pass

class RobotController:
    @staticmethod
    def send_command(command_path):
        def send_request():
            try:
                url = f"{ROBOT_IP}/{command_path}"
                requests.get(url, timeout=2)
            except Exception:
                pass

        threading.Thread(target=send_request, daemon=True).start()

class JerryBrain:
    @staticmethod
    def get_response(query):
        # Text cleaning for broken/tooti-phooti language tolerance
        q = query.lower().strip()
        clean_q = re.sub(r'[^a-zA-Z0-0\s]', '', q)
        
        # Keywords dictionary across Hindi, Hinglish, English, broken spellings
        intent_keywords = {
            "identity": [
                "banaya", "creator", "tum kon", "tum kaun", "kon ho", "kaun ho", 
                "who are you", "who r u", "kone ho", "koun ho", "maker", "owner"
            ],
            "profile": [
                "details", "profile", "job", "salary", "duty", "zomato", "patel", 
                "gori nagar", "sneh", "me kon", "main kaun", "malum", "mlum", "jaante", 
                "kya jante", "kya pata", "info", "aale baare", "mara baare", "mere baare"
            ],
            "kundli": [
                "kundli", "grah", "nakshatra", "astrology", "tara", "horoscope", "future", "rashifal"
            ],
            "forward": [
                "aage chalo", "forward", "aage badho", "aage bado", "aage", "go front", "agga", "age"
            ],
            "backward": [
                "peeche", "back", "piche", "piche chalo", "go back", "piche bado"
            ],
            "stop": [
                "ruk jao", "stop", "rok do", "ruk", "roko", "thamo", "stop it"
            ],
            "light": [
                "light", "batti", "torch", "led", "ujala", "light on"
            ],
            "motor": [
                "motor", "engine", "chalao", "start", "chalo"
            ],
            "greeting": [
                "hello", "hi", "hey", "namaste", "heloo", "kaise ho", "kya haal", "kem cho", "kaisa ho"
            ]
        }

        # Intent Matching System
        def match(keywords):
            return any(w in clean_q or w in q for w in keywords)

        # 1. Identity
        if match(intent_keywords["identity"]):
            return "Sir, main Jerry hoon, aapka personal AI assistant, jise aap hi ke creator Sneh Ringe ne banaya hai."
        
        # 2. Personal Details / Profile
        elif match(intent_keywords["profile"]):
            return "Sir, aap Patel Motors par Service Advisor hain. Duty subah 9:30 se shaam 7:00 baje tak hai, salary 12000 hai. Extra income ke liye Zomato par kaam karna chahte hain. Aap Gori Nagar, Indore mein rehte hain aur aapka janm 21 May 2006 ko subah 7:00 baje hua hai."

        # 3. Astrology / Kundli
        elif match(intent_keywords["kundli"]):
            return "Sir, 21 May 2006 (subah 7:00 baje) aur Indore janm sthan ke adhar par aapki kundli ke grah-nakshatra behad shubh hain."

        # 4. Robot Control - Forward
        elif match(intent_keywords["forward"]):
            RobotController.send_command("forward")
            return "Sir, robot ko aage chalane ka command bhej diya gaya hai! (Moving Forward)"

        # Robot Control - Backward
        elif match(intent_keywords["backward"]):
            RobotController.send_command("backward")
            return "Sir, robot ko peeche lene ka command bhej diya gaya hai! (Moving Backward)"

        # Robot Control - Stop
        elif match(intent_keywords["stop"]):
            RobotController.send_command("stop")
            return "Sir, robot ko rok diya gaya hai! (Robot Stopped)"

        # Robot Control - Light
        elif match(intent_keywords["light"]):
            RobotController.send_command("toggle_light")
            return "Sir, robot ki light on/off karne ka command execute ho gaya hai!"

        # Robot Control - Motor
        elif match(intent_keywords["motor"]):
            RobotController.send_command("start_motor")
            return "Sir, robot ki motor start kar di gayi hai!"

        # Greetings
        elif match(intent_keywords["greeting"]):
            return "Namaste Sir! Main ekdum badhiya hoon. Boliye, robot ke liye ya kis cheez mein madad karun?"

        # Smart Fallback for any other language/broken input
        else:
            return f"Sir, aapne kaha: '{query}'. Main har bhasha aur tooti-phooti words ko samajhne ki koshish kar raha hoon, jald hi is command par action lunga!"

class JerryUI(BoxLayout):
    def __init__(self, **kwargs):
        super(JerryUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(15)
        self.spacing = dp(12)

        self.add_widget(Label(
            text="JERRY AI CHAT & ROBOT CONTROL",
            font_size=sp(20),
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

        initial_msg = "Namaste Sir! Main Jerry hoon. Aap kisi bhi bhasha mein bol sakte hain."
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
            hint_text="Yahan likhiye Sir...",
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
        if platform == 'android':
            try:
                from android.runnable import run_on_ui_thread
                from jnius import autoclass, cast

                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                Intent = autoclass('android.content.Intent')
                RecognizerIntent = autoclass('android.speech.RecognizerIntent')

                intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
                intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "Boliye Sir...")

                currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
                currentActivity.startActivityForResult(intent, 5555)
                self.user_input.hint_text = "Sun raha hoon Sir..."
                return
            except Exception:
                pass

        if HARDWARE_STT:
            try:
                stt.start(callback=self.on_speech_result)
                self.user_input.hint_text = "Sun raha hoon Sir..."
            except Exception:
                self.user_input.hint_text = "Mic start nahi ho paya!"
        else:
            self.user_input.hint_text = "Type karke bhejein Sir!"

    def on_speech_result(self, text):
        if text:
            self.user_input.text = text
            self.on_send(None)

    def on_send(self, instance):
        text = self.user_input.text.strip()
        if text != "":
            self.add_bubble(f"Sir: {text}", is_user=True)
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
        
