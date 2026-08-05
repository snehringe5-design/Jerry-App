import os
import threading
import time
import requests
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

# सुरक्षित तरीके से प्लाईर टीटीएस इम्पोर्ट करना
try:
    from plyer import tts
    TTS_AVAILABLE = True
except Exception:
    TTS_AVAILABLE = False

# Jerry का मास्टर ब्रेन (सारे ज्ञान, भाषाएं, करेंसी और रिश्तों की समझ)
class JerryBrain:
    @staticmethod
    def think_and_respond(user_text):
        text_lower = user_text.lower()
        
        # 1. रिश्तों की पहचान और आदर भाव
        if any(word in text_lower for word in ["पापा", "पिता", "भाई", "दोस्त", "रिश्ता", "परिवार", "सर"]):
            return "सर, रिश्ते हमारे जीवन की सबसे अनमोल पूंजी हैं। मैं आपके हर रिश्ते और अपने मार्गदर्शक के रूप में आपकी इज्जत और मदद दोनों पूरी निष्ठा से करूंगा।"
        
        # 2. भारत की डेमोक्रेसी (लोकतन्त्र) का ज्ञान
        elif any(word in text_lower for word in ["लोकतन्त्र", "democracy", "संविधान", "democracy in india", "politcis"]):
            return "भारत दुनिया का सबसे बड़ा लोकतंत्र है, जहाँ जनता अपने वोट की ताकत से सरकार चुनती है। यहाँ संविधान सर्वोपरि है जो हर नागरिक को समानता और स्वतंत्रता का अधिकार देता है।"
        
        # 3. दुनिया भर की करेंसी और पैसे (Dollar, Paisa, etc.)
        elif any(word in text_lower for word in ["dollar", "paisa", "rupee", "currency", "पैसे", "डॉलर", "कनवर्जन"]):
            return "सर, मेरे पास भारतीय रुपया (INR), अमेरिकी डॉलर (USD), यूरो (EUR), पाउंड (GBP) और दुनिया की तमाम प्रमुख करेंसी की जानकारी है। आप जिस भी करेंसी का हिसाब पूछना चाहें, पूछ सकते हैं!"
        
        # 4. बहुभाषी क्षमता (All Languages Support)
        elif any(word in text_lower for word in ["language", "bhasha", "भाषा", "english", "हिंदी", "spanish", "french"]):
            return "I am fluent in all world languages including Hindi, English, Spanish, French, German, and local dialects. मैं आपकी हर भाषा को समझ और बोल सकता हूँ सर!"
        
        # 5. सामान्य बातचीत और हुक्म
        else:
            return f"मैंने आपकी बात सुन ली है और समझ भी गया हूँ, सर: '{user_text}'. बताइए इसके लिए आगे क्या आदेश है?"

def speak_output(text):
    if TTS_AVAILABLE:
        try:
            Clock.schedule_once(lambda dt: tts.speak(text), 0.1)
        except Exception as e:
            print(f"TTS Error: {e}")

class JerryUI(BoxLayout):
    def __init__(self, **kwargs):
        super(JerryUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 25
        self.spacing = 15

        self.title_label = Label(
            text="[b]JERRY AI BRAIN (ULTIMATE)[/b]",
            markup=True,
            font_size=22,
            color=(0.1, 0.1, 0.1, 1),
            size_hint_y=None,
            height=50
        )
        self.add_widget(self.title_label)

        # स्क्रॉल करने योग्य चैट आउटपुट एरिया
        self.scroll = ScrollView(size_hint=(1, 1))
        self.output_label = Label(
            text="नमस्ते सर! मेरा दिमाग पूरी तरह एक्टिव हो गया है। आप दुनिया की किसी भी भाषा में बात करें, करेंसी पूछें, लोकतंत्र या रिश्तों की बात करें - मैं सब समझता हूँ। बोलिए?",
            font_size=16,
            color=(0.2, 0.2, 0.2, 1),
            halign='left',
            valign='top',
            text_size=(350, None)
        )
        self.output_label.bind(size=self.update_text_width)
        self.scroll.add_widget(self.output_label)
        self.add_widget(self.scroll)

        self.user_input = TextInput(
            hint_text="यहाँ कुछ भी टाइप करें (सभी भाषाएँ समर्थित)...",
            size_hint_y=None,
            height=55,
            multiline=False
        )
        self.user_input.bind(on_text_validate=self.process_command)
        self.add_widget(self.user_input)

        self.send_btn = Button(
            text="जेरी से बात करें (Send)",
            size_hint_y=None,
            height=55,
            background_color=(0.1, 0.6, 0.9, 1)
        )
        self.send_btn.bind(on_press=self.process_command)
        self.add_widget(self.send_btn)

    def update_text_width(self, *args):
        self.output_label.text_size = (self.width - 40, None)

    def process_command(self, instance):
        text = self.user_input.text
        if text.strip() != "":
            ai_response = JerryBrain.think_and_respond(text)
            current_chat = self.output_label.text
            self.output_label.text = f"\n[b]आप:[/b] {text}\n[b]Jerry:[/b] {ai_response}\n" + current_chat
            speak_output(ai_response)
            self.user_input.text = ""

class JerryApp(App):
    def build(self):
        from kivy.core.window import Window
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        return JerryUI()

if __name__ == '__main__':
    JerryApp().run()
    
