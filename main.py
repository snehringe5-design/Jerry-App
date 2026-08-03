import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# Set background to dark theme like JARVIS
Window.clearcolor = (0.05, 0.05, 0.08, 1)

class JerryAI:
    def __init__(self):
        self.name = "Jerry"
        self.mode = "JARVIS System Active"

    def process_command(self, text):
        text_lower = text.lower().strip()
        
        if not text_lower:
            return "Sir, please give me an instruction."
            
        # Greeting
        if any(word in text_lower for word in ["hello", "hi", "namaste", "jerry"]):
            return "Greetings, Sir. Jerry is at your service. Systems nominal."
            
        # Identity / JARVIS reference
        elif "who are you" in text_lower or "kaun ho" in text_lower:
            return "I am Jerry, your personal high-intelligence AI assistant, designed to execute tasks seamlessly, Sir."
            
        # Calculations / Conversions (Tone, Tola, Kg, Grams)
        elif any(unit in text_lower for unit in ["ton", "tola", "kg", "kilogram", "gram"]):
            return "Sir, unit conversion module is initialized. I can calculate weight metrics including Tons, Tolas, and Kilograms accurately."

        # Default JARVIS response
        else:
            return f"Understood, Sir. Processing your command: '{text}'. I am getting smarter with every task."

class JerryApp(App):
    def build(self):
        self.title = "Jerry AI - JARVIS System"
        self.jerry = JerryAI()

        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        # Header Title
        header = Label(
            text="[b]JERRY AI[/b]\n[size=12]Advanced Tactical Assistant[/size]",
            markup=True,
            font_size='22sp',
            size_hint_y=0.15,
            color=(0.2, 0.8, 1, 1)
        )
        main_layout.add_widget(header)

        # Output / Chat Area
        self.scroll = ScrollView(size_hint_y=0.7)
        self.chat_history = Label(
            text="[color=00e5ff]Jerry:[/color] Online and ready, Sir. How can I assist you today?\n",
            markup=True,
            font_size='16sp',
            size_hint_y=None,
            align='left',
            valign='top',
            color=(0.9, 0.9, 0.9, 1)
        )
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        self.scroll.add_widget(self.chat_history)
        main_layout.add_widget(self.scroll)

        # Input Area
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=0.15, spacing=5)
        
        self.user_input = TextInput(
            hint_text="Give command to Jerry...",
            multiline=False,
            background_color=(0.15, 0.15, 0.2, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0.2, 0.8, 1, 1)
        )
        self.user_input.bind(on_text_validate=self.send_command)
        
        send_btn = Button(
            text="COMMAND",
            size_hint_x=0.3,
            background_color=(0, 0.6, 0.9, 1),
            bold=True
        )
        send_btn.bind(on_press=self.send_command)

        input_layout.add_widget(self.user_input)
        input_layout.add_widget(send_btn)
        main_layout.add_widget(input_layout)

        return main_layout

    def send_command(self, instance):
        query = self.user_input.text
        if query.strip():
            response = self.jerry.process_command(query)
            current_text = self.chat_history.text
            new_text = f"{current_text}\n[color=00ff88]You:[/color] {query}\n[color=00e5ff]Jerry:[/color] {response}\n"
            self.chat_history.text = new_text
            self.user_input.text = ""

if __name__ == '__main__':
    JerryApp().run()
          
