import requests
import json
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

# Keyboard adjustment setting for Android
Window.softinput_mode = 'below_target'

GEMINI_API_KEY = "AQ.Ab8RN6Je9glsfcASJfxjrsQNKo6gH8F2jKylRS0IToSXNVZVWA"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

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
        
        # Local command check
        for key in self.local_responses:
            if key in query:
                return self.local_responses[key]
        
        # Gemini AI fallback with full context
        return self.query_gemini_ai(user_text)

    def query_gemini_ai(self, prompt):
        headers = {'Content-Type': 'application/json'}
        system_instruction = (
            "You are Jerry, a smart, polite, and witty AI assistant created by Sneh Ringe. "
            "You know that Sneh Ringe lives in Gori Nagar, Indore, works as a Service Advisor at Patel Motors, "
            "has a salary of 12000, wants to do Zomato for extra income, and was born on 21 May 2006 at 7:00 AM. "
            "Always reply respectfully as 'Sir' in Hindi/Hinglish in a helpful tone."
        )
        
        payload = {
            "contents": [{
                "parts": [{"text": f"{system_instruction}\n\nUser Query: {prompt}"}]
            }]
        }
        
        try:
            response = requests.post(GEMINI_URL, headers=headers, json=payload, timeout=10)
            if response.status_code == 200:
                data = response.json()
                reply = data['candidates'][0]['content']['parts'][0]['text']
                return reply.strip()
            else:
                return f"Sir, server error code {response.status_code} aa raha hai."
        except Exception as e:
            return "Sir, internet connection check karein."

class JerryApp(App):
    def build(self):
        self.brain = JerryBrain()
        
        root_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        title_label = Label(
            text="JERRY AI CHAT & ROBOT CONTROL",
            font_size='16sp',
            size_hint=(1, 0.1),
            bold=True
        )
        root_layout.add_widget(title_label)
        
        scroll = ScrollView(size_hint=(1, 0.7))
        self.chat_display = Label(
            text="Jerry: Namaste Sir! Main Jerry hoon. Aap kuch bhi pooch sakte hain.",
            font_size='16sp',
            halign='left',
            valign='top',
            text_size=(350, None)
        )
        self.chat_display.bind(size=self._update_text_size)
        scroll.add_widget(self.chat_display)
        root_layout.add_widget(scroll)
        
        input_layout = BoxLayout(size_hint=(1, 0.15), spacing=5)
        
        mic_btn = Button(
            text='🎤', 
            size_hint=(0.2, 1),
            background_color=(0.4, 0.1, 0.1, 1)
        )
        mic_btn.bind(on_press=self.on_mic_click)
        input_layout.add_widget(mic_btn)
        
        self.user_input = TextInput(
            text='',
            hint_text='Yahan type karein Sir...',
            multiline=False,
            size_hint=(0.6, 1)
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
        
        return root_layout

    def _update_text_size(self, instance, value):
        instance.text_size = (value[0], None)

    def on_mic_click(self, instance):
        self.user_input.text = "Mic integration pending hai, type karke bhejein Sir!"

    def send_message(self, instance):
        user_text = self.user_input.text.strip()
        if not user_text:
            return
            
        self.chat_display.text = f"Sir: {user_text}\n\nJerry: Soch raha hoon Sir..."
        
        response = self.brain.process_query(user_text)
        
        self.chat_display.text = f"Sir: {user_text}\n\nJerry: {response}"
        self.user_input.text = ''

if __name__ == "__main__":
    JerryApp().run()
        
