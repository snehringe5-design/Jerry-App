from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import camera, tts
import os
import json
import urllib.request
import ssl

# SSL Context fix for Android
ssl._create_default_https_context = ssl._create_unverified_context

GEMINI_API_KEY = "AQ.Ab8RN6KP1nOyPfVMMdSFHEUNGAe7R-0LOhwBLvAfyEOBo_2-eg"

class JerryAIApp(App):
    def build(self):
        self.title = "Jerry AI Assistant"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.status_label = Label(text="Sir, Jerry AI is ready!", font_size=18, halign='center')
        layout.add_widget(self.status_label)
        
        self.user_input = TextInput(text='', hint_text='Type message to Jerry...', size_hint_y=None, height=50)
        layout.add_widget(self.user_input)
        
        btn_send = Button(text="Ask Jerry", background_color=(0.1, 0.5, 0.8, 1), size_hint_y=None, height=50)
        btn_send.bind(on_press=self.ask_gemini)
        layout.add_widget(btn_send)
        
        btn_camera = Button(text="Open Camera", background_color=(0.2, 0.7, 0.3, 1), size_hint_y=None, height=50)
        btn_camera.bind(on_press=self.open_phone_camera)
        layout.add_widget(btn_camera)
        
        return layout

    def ask_gemini(self, instance):
        query = self.user_input.text.strip()
        if not query: return
        self.status_label.text = "Jerry is thinking..."
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
            data = json.dumps({"contents": [{"parts": [{"text": query}]}]}).encode('utf-8')
            req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'}, method='POST')
            with urllib.request.urlopen(req) as response:
                answer = json.loads(response.read().decode('utf-8'))['candidates'][0]['content']['parts'][0]['text']
            self.status_label.text = f"Jerry: {answer}"
            tts.speak(answer)
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"

    def open_phone_camera(self, instance):
        camera.take_picture(filename=os.path.join(self.user_data_dir, "jerry.jpg"), on_complete=lambda path: tts.speak("Photo captured."))

if __name__ == '__main__':
    JerryAIApp().run()
    
