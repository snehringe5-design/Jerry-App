import os
import requests
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Environment Variable se secure API Key load hogi
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
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
        query = user_text.lower().strip()
        
        # Local hardcoded command check
        for key in self.local_responses:
            if key in query:
                return self.local_responses[key]
        
        # Cloud Gemini AI Fallback
        return self.query_gemini_ai(user_text)

    def query_gemini_ai(self, prompt):
        if not GEMINI_API_KEY:
            return "Sir, GEMINI_API_KEY set nahi hai."

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
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.status_label = Label(
            text="Jerry Online Hai, Sir!\nKuch bhi poochhiye...", 
            font_size='18sp',
            halign='center'
        )
        layout.add_widget(self.status_label)
        
        test_btn = Button(
            text="Test Jerry", 
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 1, 1)
        )
        test_btn.bind(on_press=self.on_test_click)
        layout.add_widget(test_btn)
        
        return layout

    def on_test_click(self, instance):
        sample_query = "Aaj ka mausam kaisa hai?"
        self.status_label.text = f"Poochha: {sample_query}\n\nSoch raha hoon..."
        response = self.brain.process_query(sample_query)
        self.status_label.text = f"Jerry: {response}"

if __name__ == "__main__":
    JerryApp().run()
            
