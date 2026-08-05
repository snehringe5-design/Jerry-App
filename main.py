import requests
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

# Nayi API Key integrated successfully
GEMINI_API_KEY = "AQ.Ab8RN6IcAGQyGp4C_V1XR-eB1CJ9aW5OsshdsEArdMbigMc-Lg"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

class JerryBrain:
    def __init__(self):
        self.local_responses = {
            "hello": "Hello Sir! Main Jerry hoon, aapka personal assistant. Kaise madad karoon?",
            "kaun ho tum": "Main Jerry hoon, aapka AI assistant aur robot controller.",
            "naam kya hai": "Mera naam Jerry hai, Sir!",
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
        
        # Gemini AI fallback
        return self.query_gemini_ai(user_text)

    def query_gemini_ai(self, prompt):
        headers = {'Content-Type': 'application/json'}
        payload = {
            "contents": [{
                "parts": [{
                    "text": f"You are Jerry, a smart, polite, and witty AI assistant. Answer briefly and directly in Hindi/Hinglish in 2-3 short sentences. Query: {prompt}"
                }]
            }]
        }
        
        try:
            response = requests.post(GEMINI_URL, headers=headers, json=payload, timeout=8)
            if response.status_code == 200:
                data = response.json()
                reply = data['candidates'][0]['content']['parts'][0]['text']
                return reply.strip()
            else:
                return "Sir, server se response milne mein dikkat ho rahi hai."
        except Exception as e:
            return "Sir, internet connection check karein."

class JerryApp(App):
    def build(self):
        self.brain = JerryBrain()
        
        # Main Layout
        root_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Title Label
        title_label = Label(
            text="JERRY AI CHAT & ROBOT CONTROL",
            font_size='16sp',
            size_hint=(1, 0.1),
            bold=True
        )
        root_layout.add_widget(title_label)
        
        # Scrollable Chat Display Area
        scroll = ScrollView(size_hint=(1, 0.7))
        self.chat_display = Label(
            text="Jerry: Namaste Sir! Main Jerry hoon. Aap kisi bhi bhasha mein bol sakte hain.",
            font_size='16sp',
            halign='left',
            valign='top',
            text_size=(350, None)
        )
        self.chat_display.bind(size=self._update_text_size)
        scroll.add_widget(self.chat_display)
        root_layout.add_widget(scroll)
        
        # Bottom Input Layout (Mic + Text Input + Bhejo Button)
        input_layout = BoxLayout(size_hint=(1, 0.15), spacing=5)
        
        # Mic Button (Red)
        mic_btn = Button(
            text='🎤', 
            size_hint=(0.2, 1),
            background_color=(0.4, 0.1, 0.1, 1)
        )
        mic_btn.bind(on_press=self.on_mic_click)
        input_layout.add_widget(mic_btn)
        
        # Text Input Box
        self.user_input = TextInput(
            text='',
            hint_text='Yahan type karein Sir...',
            multiline=False,
            size_hint=(0.6, 1)
        )
        input_layout.add_widget(self.user_input)
        
        # Send Button (Blue)
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
        self.user_input.text = "Mic start nahi ho paya!"

    def send_message(self, instance):
        user_text = self.user_input.text.strip()
        if not user_text:
            return
            
        # Display User & Loading status
        self.chat_display.text = f"Aap: {user_text}\n\nJerry: Soch raha hoon Sir..."
        
        # Process through Brain
        response = self.brain.process_query(user_text)
        
        # Update Chat Display with final answer
        self.chat_display.text = f"Aap: {user_text}\n\nJerry: {response}"
        
        # Clear Input Box
        self.user_input.text = ''

if __name__ == "__main__":
    JerryApp().run()
        
