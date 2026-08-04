from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

# एंड्रॉइड पर आवाज (Speech) के लिए plyer का टेक्स्ट-टू-स्पीच
try:
    from plyer import tts
except ImportError:
    tts = None

# --- Login Screen ---
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.secret_pin = "6263"

        self.label = Label(
            text="Jerry AI Locked\nOnly Sneh Sir Can Unlock",
            font_size='20sp',
            halign='center',
            valign='middle'
        )
        self.label.bind(size=self.label.setter('text_size'))
        layout.add_widget(self.label)

        self.pin_input = TextInput(
            password=True,
            multiline=False,
            size_hint_y=None,
            height=50,
            hint_text="Enter Secret PIN"
        )
        layout.add_widget(self.pin_input)

        btn = Button(
            text="Unlock Jerry",
            size_hint_y=None,
            height=50
        )
        btn.bind(on_press=self.verify_pin)
        layout.add_widget(btn)

        self.add_widget(layout)

    def verify_pin(self, instance):
        if self.pin_input.text == self.secret_pin:
            self.manager.current = 'jerry_main'
        else:
            self.label.text = "Wrong PIN! Try Again"
            self.pin_input.text = ""


# --- Main AI Screen (Autonomous & Voice Enabled) ---
class JerryMainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_layout = BoxLayout(orientation='vertical')
        self.creator = "Sneh Ringe"

        # चैट हिस्ट्री के लिए ScrollView
        self.scroll = ScrollView(size_hint=(1, 0.75))
        
        self.chat_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10, padding=10)
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))

        self.scroll.add_widget(self.chat_layout)
        main_layout.add_widget(self.scroll)

        # स्वागत संदेश (सिर्फ एक बार दिखाने के लिए फ्लैग या डायरेक्ट कॉल)
        self.welcome_shown = False

        # माइक और वॉइस कमांड के लिए बटन लेआउट
        top_btn_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=5, padding=5)
        
        self.mic_btn = Button(text="Bolkar Command Dein", background_color=(0.1, 0.4, 0.7, 1))
        self.mic_btn.bind(on_press=self.listen_voice)
        top_btn_layout.add_widget(self.mic_btn)
        
        main_layout.add_widget(top_btn_layout)

        # इनपुट और सेंड बटन लेआउट
        bottom_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.15), spacing=5, padding=5)

        self.user_input = TextInput(
            hint_text="Sneh sir, aadesh dijiye...",
            multiline=False
        )
        bottom_layout.add_widget(self.user_input)

        self.send_btn = Button(
            text="Send",
            size_hint_x=0.3
        )
        self.send_btn.bind(on_press=self.process_command)
        bottom_layout.add_widget(self.send_btn)

        main_layout.add_widget(bottom_layout)
        self.add_widget(main_layout)

        # ऐप खुलते ही एक बार स्वागत संदेश जोड़ें
        self.add_initial_welcome()

    def add_initial_welcome(self):
        if not self.welcome_shown:
            welcome_text = "Jerry: Namaste Sneh Sir!"
            self.add_chat_message(welcome_text)
            self.speak_text(welcome_text)
            self.welcome_shown = True

    def speak_text(self, text):
        """जेरी को बोलकर जवाब देने का फंक्शन"""
        try:
            if tts:
                clean_text = text.replace("Jerry: ", "")
                tts.speak(clean_text)
        except Exception as e:
            print(f"TTS Error: {e}")

    def add_chat_message(self, message):
        lbl = Label(
            text=message,
            font_size='16sp',
            size_hint_y=None,
            height=50,
            halign='left',
            valign='middle',
            color=(1, 1, 1, 1)
        )
        lbl.bind(size=lbl.setter('text_size'))
        self.chat_layout.add_widget(lbl)

    def listen_voice(self, instance):
        """यहाँ एंड्रॉइड की स्पीच रिकग्निशन API जोड़ी जाएगी"""
        self.add_chat_message("Jerry: Sir, mic feature abhi active ho raha hai...")
        self.speak_text("Sir, aap text type karke aadesh dein.")

    def process_command(self, instance):
        text = self.user_input.text.strip()
        if not text:
            return

        # यूजर का मैसेज दिखाएं
        self.add_chat_message(f"Sneh Sir: {text}")
        query = text.lower()

        # --- Jerry's Autonomous Brain (स्वयं निर्णय लेने की क्षमता) ---
        if "who made you" in query or "kisne banaya" in query:
            response = "Jerry: Mujhe mere malik Sneh Ringe ne banaya hai."
        elif "tum kon ho" in query or "who are you" in query:
            response = "Jerry: Main Sneh Sir ka personal AI assistant hoon."
        elif "gita" in query or "bhagwad gita" in query:
            response = "Jerry: Shrimad Bhagwat Gita karm aur dharm ka paath padhati hai."
        elif "ved" in query:
            response = "Jerry: Bharat ke charon ved Rigveda, Samaveda, Yajurveda aur Atharvaveda hain."
        elif "+" in query or "-" in query or "math" in query:
            try:
                res = eval(text)
                response = f"Jerry: Iska calculation {res} hoga, Sir."
            except:
                response = "Jerry: Sir, is math expression ko solve karne mein kuch samasya hai."
        else:
            response = f"Jerry: Sir, aapka command mil gaya. Main ise samajh raha hoon."

        # चैट में जवाब जोड़ें और बोलकर भी सुनाएं
        self.add_chat_message(response)
        self.speak_text(response)

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
    
