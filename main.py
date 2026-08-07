from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import Clock

# Plyer imports for Android hardware access
from plyer import camera, tts
import os
import json
import urllib.request

# Aapki Gemini API Key
GEMINI_API_KEY = "AQ.Ab8RN6KP1nOyPfVMMdSFHEUNGAe7R-0LOhwBLvAfyEOBo_2-eg"

class JerryAIApp(App):
    def build(self):
        self.title = "Jerry AI Assistant"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Status / Output Label
        self.status_label = Label(
            text="Sir, Jerry AI is ready!", 
            font_size=18,
            halign='center'
        )
        layout.add_widget(self.status_label)
        
        # Text Input for chatting with Jerry
        self.user_input = TextInput(
            text='', 
            hint_text='Type your message to Jerry here...', 
            size_hint_y=None, 
            height=50
        )
        layout.add_widget(self.user_input)
        
        # Send Button to ask Gemini
        btn_send = Button(text="Ask Jerry (Gemini AI)", background_color=(0.1, 0.5, 0.8, 1), size_hint_y=None, height=50)
        btn_send.bind(on_press=self.ask_gemini)
        layout.add_widget(btn_send)
        
        # Camera Button
        btn_camera = Button(text="Open Camera / Take Photo", background_color=(0.2, 0.7, 0.3, 1), size_hint_y=None, height=50)
        btn_camera.bind(on_press=self.open_phone_camera)
        layout.add_widget(btn_camera)
        
        # App start hote hi automatic bolne ke liye
        Clock.schedule_once(self.auto_speak, 1.0)
        
        return layout

    def auto_speak(self, dt):
        try:
            tts.speak("Hello sir, Jerry AI is online and connected.")
        except Exception as e:
            print(e)

    # Gemini REST API se baat karne aur bolne ka function
    def ask_gemini(self, instance):
        query = self.user_input.text.strip()
        if not query:
            self.status_label.text = "Please type something first, sir!"
            return

        self.status_label.text = "Jerry is thinking..."
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
            headers = {'Content-Type': 'application/json'}
            data = {
                "contents": [{
                    "parts": [{"text": query}]
                }]
            }
            
            req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
            with urllib.request.urlopen(req) as response:
                res_body = json.loads(response.read().decode('utf-8'))
                answer = res_body['candidates'][0]['content']['parts'][0]['text']
            
            # Screen par dikhana aur speaker se bolna
            self.status_label.text = f"Jerry: {answer}"
            tts.speak(answer)
        except Exception as e:
            self.status_label.text = f"AI Error: {str(e)}"

    # Camera Function
    def open_phone_camera(self, instance):
        self.status_label.text = "Opening Camera..."
        try:
            filepath = os.path.join(self.user_data_dir, "jerry_photo.jpg")
            camera.take_picture(filename=filepath, on_complete=self.camera_complete)
        except Exception as e:
            self.status_label.text = f"Camera Error: {str(e)}"

    def camera_complete(self, filepath):
        if filepath and os.path.exists(filepath):
            self.status_label.text = f"Photo saved at:\n{filepath}"
            try:
                tts.speak("Photo captured successfully sir.")
            except:
                pass
        else:
            self.status_label.text = "Camera capture failed."

if __name__ == '__main__':
    JerryAIApp().run()
        
