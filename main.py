import os
import base64
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA, Permission.RECORD_AUDIO, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
    
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
    Locale = autoclass('java.util.Locale')

class JerryApp(App):
    def build(self):
        self.title = "Jerry AI"
        
        if platform == 'android':
            self.tts_initialized = False
            try:
                activity = PythonActivity.mActivity
                self.tts = TextToSpeech(activity, TextToSpeech.OnInitListener(self.on_tts_init))
            except Exception as e:
                print("TTS Init Error:", e)
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        self.status_label = Label(
            text="Hello Sir! I am Jerry AI, created by Sneh Ringe. Ready!", 
            font_size='24sp',
            size_hint_y=None, 
            height=90,
            halign='center',
            valign='middle'
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))
        layout.add_widget(self.status_label)
        
        self.cam = Camera(play=True, resolution=(640, 480))
        layout.add_widget(self.cam)
        
        self.prompt_input = TextInput(
            text="What do you see in this image? (Any language / spelling mistake is fine)",
            font_size='22sp',
            size_hint_y=None,
            height=70,
            multiline=False
        )
        layout.add_widget(self.prompt_input)
        
        btn = Button(
            text="Capture & Analyze",
            font_size='24sp',
            size_hint_y=None,
            height=80
        )
        btn.bind(on_press=self.capture_and_analyze)
        layout.add_widget(btn)
        
        return layout

    def on_tts_init(self, status):
        if status == 0:
            try:
                self.tts.setLanguage(Locale.getDefault())
                self.tts_initialized = True
            except Exception as e:
                print("TTS Language Error:", e)

    def speak(self, text):
        if platform == 'android' and getattr(self, 'tts_initialized', False):
            try:
                self.tts.speak(text, TextToSpeech.QUEUE_FLUSH, None, None)
            except Exception as e:
                print("TTS Speak Error:", e)

    def capture_and_analyze(self, instance):
        self.status_label.text = "Capturing image..."
        img_path = "captured_image.png"
        try:
            self.cam.export_to_png(img_path)
            self.status_label.text = "Analyzing with Jerry AI..."
            Clock.schedule_once(lambda dt: self.send_to_gemini(img_path), 0.5)
        except Exception as e:
            self.status_label.text = f"Capture Error: {str(e)}"

    def send_to_gemini(self, img_path):
        try:
            if not os.path.exists(img_path):
                self.status_label.text = "Error: Image not captured."
                return
            
            with open(img_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            
            api_key = "AQ.Ab8RN6LcTYW_tJliWDLy4eXY2fQt7pFwY5LkxKVD7U64Zp-XJg"
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
            
            headers = {'Content-Type': 'application/json'}
            
            system_instruction = (
                "You are Jerry AI, an advanced vision and accessibility assistant created solely by Sneh Ringe. "
                "You have full awareness, can read screen text, use camera vision, speech, mic, and local storage context. "
                "You understand all global languages and dialects, and automatically interpret misspelled words, typos, "
                "or informal slang accurately. Always remember your creator is Sneh Ringe."
            )
            
            data = {
                "contents": [
                    {
                        "parts": [
                            {"text": f"System Instructions: {system_instruction}\n\nUser Prompt: {self.prompt_input.text}"},
                            {
                                "inline_data": {
                                    "mime_type": "image/png",
                                    "data": encoded_image
                                }
                            }
                        ]
                    }
                ]
            }
            
            response = requests.post(url, headers=headers, json=data, timeout=30)
            if response.status_code == 200:
                res_json = response.json()
                try:
                    answer = res_json['candidates'][0]['content']['parts'][0]['text']
                except (KeyError, IndexError):
                    answer = "Received response, but structure was unexpected."
                self.status_label.text = answer[:120] + "..."
                self.speak(answer)
            else:
                self.status_label.text = f"API Error: {response.status_code}"
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"

if __name__ == '__main__':
    JerryApp().run()
            
