import os
import threading
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

# Speech-to-Text (Mic) Setup
HARDWARE_STT = False
try:
    from plyer import stt
    HARDWARE_STT = True
except Exception:
    pass

class JerryBrain:
    @staticmethod
    def get_response(query):
        q = query.lower().strip()
        
        # 1. Identity & Creator
        if any(w in q for w in ["banaya", "creator", "tum kon", "tum kaun", "kon ho", "kaun ho", "who are you"]):
            return "Sneh Sir, main Jerry hoon, aapka personal AI assistant, jise aap hi ke creator Sneh Ringe ne banaya hai."
        
        # 2. Personal Details & Profile
        elif any(w in q for w in ["details", "profile", "job", "salary", "duty", "zomato", "patel", "gori nagar", "sneh", "me kon", "main kaun"]):
            return "Sneh Sir, aap Patel Motors par Service Advisor hain. Duty subah 9:30 se shaam 7:00 baje tak hai, salary 12000 hai. Extra income ke liye Zomato par kaam karna chahte hain. Aap Gori Nagar, Indore mein rehte hain aur aapka janm 21 May 2006 ko subah 7:00 baje hua hai."

        # 3. Astrology & Kundli
        elif any(w in q for w in ["kundli", "grah", "nakshatra", "astrology", "tara"]):
            return "Sneh Sir, 21 May 2006 (subah 7:00 baje) aur Indore janm sthan ke adhar par aapki kundli ke grah-nakshatra behad shubh hain."

        # 4. Robot & Hardware Control Commands
        elif any(w in q for w in ["aage chalo", "forward", "aage badho"]):
            return "Sneh Sir, robot ko aage chalane ka command bhej diya gaya hai! (Moving Forward)"

        elif any(w in q for w in ["peeche", "back", "piche"]):
            return "Sneh Sir, robot ko peeche lene ka command bhej diya gaya hai! (Moving Backward)"

        elif any(w in q for w in ["ruk jao", "stop", "rok do"]):
            return "Sneh Sir, robot ko rok diya gaya hai! (Robot Stopped)"

        elif any(w in q for w in ["light", "batti", "torch", "led"]):
            return "Sneh Sir, robot ki light on/off karne ka command execute ho gaya hai!"

        elif any(w in q for w in ["motor", "engine", "chalao"]):
            return "Sneh Sir, robot ki motor start kar di gayi hai!"

        # 5. Phone / Battery Status
        elif any(w in q for w in ["battery", "batty", "charge"]):
            return "Sneh Sir, aapka phone abhi charging par hai aur system bilkul fit kaam kar raha hai."

        # 6. General Greetings
        elif any(w in q for w in ["hello", "hi", "hey", "namaste", "heloo", "kaise ho", "kya haal"]):
            return "Namaste Sneh Sir! Main ekdum badhiya hoon. Boliye, robot ke liye ya kis cheez mein madad karun?"

        # 7. Smart Fallback
        else:
            return f"Sneh Sir, aapne kaha: '{query}'. Main ise samajh raha hoon aur jaldi hi is par action lunga!"

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
        if HARDWARE_STT:
            try:
                stt.start(callback=self.on_speech_result)
                self.user_input.hint_text = "Sun raha hoon Sneh Sir..."
            except Exception as e:
                self.user_input.hint_text = "Mic start nahi ho paya!"
        else:
            self.user_input.hint_text = "Type karke bhejein Sneh Sir!"

    def on_speech_result(self, text):
        if text:
            self.user_input.text = text
            self.on_send(None)

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
    
