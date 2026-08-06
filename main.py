import threading
import requests
import json
import base64
import os
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.utils import platform
from kivy.clock import Clock

# Safe Android imports
PythonActivity = None
Locale = None
TextToSpeech = None

if platform == 'android':
    try:
        from jnius import autoclass, PythonJavaClass, java_method
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Locale = autoclass('java.util.Locale')
        TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
    except Exception as e:
        pass

Window.softinput_mode = 'below_target'

GEMINI_API_KEY = "AQ.Ab8RN6JIoLFPrVg_8YOs3ecOKM06-xNlbSyfGbPECRCE-EBQsA"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

class JerryBrain:
    def __init__(self):
        self.local_responses = {
            "hello": "Hello Sir! Main Jerry hoon, aapka personal assistant. Kaise madad karoon?",
            "kaun ho tum": "Main Jerry hoon, aapka personal AI assistant, jise aap hi ke creator Sneh Ringe ne banaya hai.",
            "light on": "ESP32_CMD:LIGHT_ON",
            "light off": "ESP32_CMD:LIGHT_OFF",
            "move forward": "ESP32_CMD:FORWARD"
        }

    def process_query(self, user_text):
        if not user_text:
            return "Pehle kuch type toh kijiye Sir!"
            
        query = user_text.lower().strip()
        for key in self.local_responses:
            if key in query:
                return self.local_responses[key]
        
        return self.query_gemini_ai(user_text)

    def query_gemini_ai(self, prompt, image_path=None):
        headers = {'Content-Type': 'application/json'}
        system_instruction = (
            "You are Jerry, a smart, polite, and witty AI assistant created by Sneh Ringe. "
            "You know that Sneh Ringe lives in Gori Nagar, Indore, works as a Service Advisor at Patel Motors, "
            "has a salary of 12000, wants to do Zomato for extra income, and was born on 21 May 2006 at 7:00 AM. "
            "IMPORTANT: The user may type with spelling mistakes, broken words, slang, or casual/broken Hinglish. "
            "Always intelligently understand the user's core intent despite any typos or informal phrasing. "
            "Always reply respectfully as 'Sir' in Hindi/Hinglish in a helpful tone."
        )
        
        parts_list = [{"text": f"{system_instruction}\n\nUser Query: {prompt}"}]
        
        if image_path and os.path.exists(image_path):
            try:
                with open(image_path, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                    parts_list.append({
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": encoded_string
                        }
                    })
            except Exception as e:
                pass

        payload = {
            "contents": [{
                "parts": parts_list
            }]
        }
        
        try:
            response = requests.post(GEMINI_URL, headers=headers, json=payload, timeout=25)
            if response.status_code == 200:
                data = response.json()
                reply = data['candidates'][0]['content']['parts'][0]['text']
                return reply.strip()
            else:
                return f"Sir, server error code {response.status_code} aa raha hai."
        except Exception as e:
            return "Sir, internet connection check karein."

class TTSListener(PythonJavaClass):
    __javainterfaces__ = ['android/speech/tts/TextToSpeech$OnInitListener']
    __javapackage__ = 'org/kivy/android/tils'

    def __init__(self, app_instance):
        super(TTSListener, self).__init__()
        self.app_instance = app_instance

    @java_method('(I)V')
    def onInit(self, status):
        if status == 0:
            try:
                tts = self.app_instance.tts_instance
                tts.setLanguage(Locale("hi", "IN"))
            except Exception:
                pass

class JerryApp(App):
    def build(self):
        self.brain = JerryBrain()
        self.tts_instance = None
        self.selected_image = None
        self.chat_history = "Jerry: Namaste Sneh Sir! Main Jerry hoon. Boliye, kya madad karoon?\n\n"
        
        if platform == 'android':
            try:
                activity = PythonActivity.mActivity
                self.listener = TTSListener(self)
                self.tts_instance = TextToSpeech(activity, self.listener)
            except Exception as e:
                pass

        root_layout = BoxLayout(orientation='vertical', padding=8, spacing=5)
        
        title_label = Label(
            text="JERRY AI CHAT & VISION",
            font_size='14sp',
            size_hint=(1, 0.07),
            bold=True
        )
        root_layout.add_widget(title_label)
        
        self.scroll = ScrollView(size_hint=(1, 0.75))
        self.chat_display = Label(
            text=self.chat_history,
            font_size='15sp',
            halign='left',
            valign='top',
            text_size=(350, None),
            markup=True
        )
        self.chat_display.bind(size=self._update_text_size)
        self.scroll.add_widget(self.chat_display)
        root_layout.add_widget(self.scroll)
        
        input_layout = BoxLayout(size_hint=(1, 0.15), spacing=4)
        
        plus_btn = Button(
            text='+', 
            size_hint=(0.12, 1),
            font_size='20sp',
            background_color=(0.2, 0.4, 0.2, 1)
        )
        plus_btn.bind(on_press=self.on_plus_click)
        input_layout.add_widget(plus_btn)
        
        mic_btn = Button(
            text='🎤', 
            size_hint=(0.12, 1),
            background_color=(0.4, 0.1, 0.1, 1)
        )
        mic_btn.bind(on_press=self.on_mic_click)
        input_layout.add_widget(mic_btn)
        
        self.user_input = TextInput(
            text='',
            hint_text='Yahan type karein Sir...',
            multiline=False,
            size_hint=(0.56, 1)
        )
        input_layout.add_widget(self.user_input)
        
        send_btn = Button(
            text='BHEJO',
            size_hint=(0.2, 1),
            background_color=(0.1, 0.25, 0.4, 1)
        )
        send_btn.bind(on_press=self.send_message)
        input_layout.add_widget(send_btn)
        
        root_layout.add_widget(input_layout)
        
        if platform == 'android':
            Clock.schedule_once(self.speak_welcome, 2.0)
            
        return root_layout

    def speak_welcome(self, dt):
        self.speak_text("Namaste Sneh Sir! Main Jerry hoon.")

    def speak_text(self, text):
        if self.tts_instance and text:
            try:
                self.tts_instance.speak(text, 0, None, None)
            except Exception:
                pass

    def _update_text_size(self, instance, value):
        instance.text_size = (value[0], None)

    def on_plus_click(self, instance):
        self.user_input.text = "Photo select karne ke liye gallery use karein Sir."

    def on_mic_click(self, instance):
        self.user_input.text = "Voice typing ke liye keyboard ka mic icon use karein Sir!"

    def send_message(self, instance):
        user_text = self.user_input.text.strip()
        if not user_text and not self.selected_image:
            return
            
        display_text = user_text if user_text else "[Photo bheji gayi hai]"
        self.chat_history += f"Sir: {display_text}\n\nJerry: Soch raha hoon Sir...\n\n"
        self.chat_display.text = self.chat_history
        self.user_input.text = ''
        
        Clock.schedule_once(lambda dt: setattr(self.scroll, 'scroll_y', 0), 0.1)
        
        threading.Thread(target=self.fetch_ai_response, args=(user_text, self.selected_image)).start()
        self.selected_image = None

    def fetch_ai_response(self, user_text, img_path):
        prompt_text = user_text if user_text else "Is photo mein kya hai?"
        response = self.brain.query_gemini_ai(prompt_text, img_path)
        Clock.schedule_once(lambda dt: self.update_chat(user_text, response))

    def update_chat(self, user_text, response):
        self.chat_history = self.chat_history.rsplit("Jerry: Soch raha hoon Sir...", 1)[0]
        self.chat_history += f"Jerry: {response}\n\n"
        self.chat_display.text = self.chat_history
        
        Clock.schedule_once(lambda dt: setattr(self.scroll, 'scroll_y', 0), 0.1)
        self.speak_text(response)

if __name__ == "__main__":
    JerryApp().run()
    
