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
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
    Locale = autoclass('java.util.Locale')

class JerryApp(App):
    def build(self):
        self.title = "Jerry AI"
        
        # Initialize Android TTS
        if platform == 'android':
            self.tts_initialized = False
            activity = PythonActivity.mActivity
            self.tts = TextToSpeech(activity, TextToSpeech.OnInitListener(self.on_tts_init))
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        # Bade letters / Font size for status
        self.status_label = Label(
            text="Jerry AI Ready - Tap Capture", 
            font_size='24sp',
            size_hint_y=None, 
            height=80,
            halign='center',
            valign='middle'
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))
        layout.add_widget(self.status_label)
        
        # Camera Preview
        self.cam = Camera(play=True, resolution=(640, 480))
        layout.add_widget(self.cam)
        
        # Prompt Input with large text
        self.prompt_input = TextInput(
            text="What do you see in this image?",
            font_size='22sp',
            size_hint_y=None,
            height=70,
            multiline=False
        )
        layout.add_widget(self.prompt_input)
        
        # Action Button with large text
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
            self.tts.setLanguage(Locale.ENGLISH)
            self.tts_initialized = True

    def speak(self, text):
        if platform == 'android' and getattr(self, 'tts_initialized', False):
            self.tts.speak(text, TextToSpeech.QUEUE_FLUSH, None, None)

    def capture_and_analyze(self, instance):
        self.status_label.text = "Capturing image..."
        img_path = "captured_image.png"
        self.cam.export_to_png(img_path)
        self.status_label.text = "Analyzing with Gemini..."
        
        Clock.schedule_once(lambda dt: self.send_to_gemini(img_path), 0.5)

    def send_to_gemini(self, img_path):
        try:
            if not os.path.exists(img_path):
                self.status_label.text = "Error: Image not captured."
                return
            
            with open(img_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            
            api_key = "YOUR_GEMINI_API_KEY"  # Apna Gemini API Key yahan dalein
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
            
            headers = {'Content-Type': 'application/json'}
            data = {
                "contents": [{
                    "parts": [
                        {"text": self.prompt_input.text},
                        {
                            "inline_data": {
                                "mime_type": "image/png",
                                "data": encoded_image
                            }
                        }
                    ]
                }]
            }
            
            response = requests.post(url, headers=headers, json=data, timeout=30)
            if response.status_code == 200:
                res_json = response.json()
                answer = res_json['candidates'][0]['content']['parts'][0]['text']
                self.status_label.text = answer[:120] + "..."
                self.speak(answer)
            else:
                self.status_label.text = f"API Error: {response.status_code}"
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"

if __name__ == '__main__':
    JerryApp().run()
    
