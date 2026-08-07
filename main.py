from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import Clock

# Plyer imports for Android hardware access
from plyer import camera, tts
import os
import google.generativeai as genai

# Aapki Gemini API Key yahan set kar di gayi hai, sir!
GEMINI_API_KEY = "AQ.Ab8RN6KP1nOyPfVMMdSFHEUNGAe7R-0LOhwBLvAfyEOBo_2-eg"

class JerryAIApp(App):
    def build(self):
        self.title = "Jerry AI Assistant"
        
        # Configure Gemini API
        if GEMINI_API_KEY != "YOUR_GEMINI_API_KEY_HERE":
            genai.configure(api_key=GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            self.model = None

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

    # Gemini AI se baat karne aur bolne ka function
    def ask_gemini(self, instance):
        query = self.user_input.text.strip()
        if not query:
            self.status_label.text = "Please type something first, sir!"
            return
            
        if not self.model:
            self.status_label.text = "Error: Please add your Gemini API Key in the code."
            return

        self.status_label.text = "Jerry is thinking..."
        try:
            # Gemini se jawab lena
            response = self.model.generate_content(query)
            answer = response.text
            
            # Screen par dikhana
            self.status_label.text = f"Jerry: {answer}"
            
            # Speaker se bolna
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
            
