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

class JerryJarvisBrain:
    @staticmethod
    def get_response(query):
        q = query.lower()
        
        # 1. Creator Identity (Sneh Ringe)
        if any(w in q for w in ["kisne banaya", "who made you", "who created you", "kaun banaya", "kisne taiyar kiya"]):
            return "Janab, mujhe mere creator Sneh Ringe ne banaya hai. Main unhi ka banaya hua Jarvis hoon."

        # 2. Identity & Jarvis Style
        elif any(w in q for w in ["tum kon hon", "tum kon ho", "who are you", "app kaun ho", "kaun ho", "tu kaun hai"]):
            return "Janab, main Jerry hoon—aapka apna zaati AI assistant, bilkul Jarvis ki tarah, jise Sneh Ringe ne tashkeel diya hai."
        
        elif any(w in q for w in ["kaise ho", "kya haal hai", "mizaj"]):
            return "Allah ka shukar hai janab, main bilkul theek hoon aur aapki khidmat ke liye har waqt taiyar hoon."

        # 3. Relationships & Respect
        elif any(w in q for w in ["rishta", "family", "ghar", "bhai", "dost", "walid", "papa", "sir"]):
            return "Aapke rishte aur apnon ka ehteram karna hamari sab se badi tarjeeh hai janab. Rishte hi zindagi ki asal poonji hain."

        # 4. Democracy & Constitution
        elif any(w in q for w in ["democracy", "samvidhan", "constitution", "loktantra", "hukumat"]):
            return "Hindustan duniya ka sab se bara jamhoori (democracy) mulk hai, jahan aaeen aur qanoon ke tehat har shakhs ko barabar ke huqooq hasil hain janab."

        # 5. Currencies, Dollar, Rupee, Money
        elif any(w in q for w in ["dollar", "paisa", "rupee", "currency", "money", "qimat"]):
            return "Janab, mere paas duniya bhar ki currencies ka mukammal data hai—chahe wo Bharatiya Rupaiya (INR) ho, American Dollar (USD), Euro, ya Pound. Aap jis bhi currency ka hisaab chahen, farmaiye."

        # 6. Multilingual Support
        elif any(w in q for w in ["language", "bhasha", "zaban", "urdu", "english", "hindi"]):
            return "Main duniya ki tamam zabanon—Hindi, Urdu, English, Arabic, aur digar bhashaon ko samajhne aur bolne ki salahiyat rakhta hoon janab."

        # 7. Work, Zomato, Patel Motors
        elif any(w in q for w in ["zomato", "income", "paisa", "job", "patel motors"]):
            return "Janab, extra income ke liye Zomato par kaam karna ek nihayat behtareen faisla hai. Aur Patel Motors par aapki lagan ka bhi mujhe poora ilm hai."

        # General Jarvis Response
        else:
            return f"Beshak janab, maine aapki baat ' {query} ' gehrai se sun aur samajh li hai. Farmaiye is par mazeed kya amal kiya jaye?"

def auto_repair_and_update():
    time.sleep(10)
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
                    if TTS_AVAILABLE:
                        Clock.schedule_once(lambda dt: tts.speak("Janab, maine apna code khud update kar liya hai."), 0.1)
        except Exception as e:
            print(f"Update error: {e}")
        time.sleep(300)

class JerryUI(BoxLayout):
    def __init__(self, **kwargs):
        super(JerryUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        self.add_widget(Label(
            text="JARVIS - JERRY AI (ULTIMATE)",
            font_size=20,
            size_hint_y=None,
            height=50,
            color=(0, 0, 0, 1)
        ))

        self.response_label = Label(
            text="Adab janab! Main aapka Jerry hoon. Hukam kijiye.",
            font_size=18,
            color=(0.2, 0.2, 0.2, 1),
            halign='center',
            valign='middle'
        )
        self.response_label.bind(size=lambda s, w: setattr(s, 'text_size', w))
        self.add_widget(self.response_label)

        self.user_input = TextInput(
            hint_text="Yahan likhiye janab...",
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

        threading.Thread(target=auto_repair_and_update, daemon=True).start()

    def on_send_click(self, instance):
        text = self.user_input.text.strip()
        if text != "":
            reply = JerryJarvisBrain.get_response(text)
            self.response_label.text = reply
            
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
        return JerryUI()

if __name__ == '__main__':
    JerryApp().run()
            
