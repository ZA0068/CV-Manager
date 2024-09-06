from headers import *

class CVReactor(FloatLayout):
    def __init__(self, **kwargs):
        super(CVReactor, self).__init__(**kwargs)
        
        # Set the background color for the whole layout
        with self.canvas.before:
            Color(0.6, 0.6, 0.6, 1)  # Whitish grey color (RGBA format)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)

        # Create a container for the text boxes
        box_layout = BoxLayout(orientation='vertical', padding=[50, 50, 50, 50], spacing=20, size_hint=(None, None), width=150)
        box_layout.pos_hint = {"x": 0.1, "center_y": 0.5}  # Position on the left half
        
        # Create and add three TextInput widgets
        self.text_input_1 = TextInput(hint_text="Enter text 1 here", size_hint=(1, None), height=100, multiline=True)
        self.text_input_2 = TextInput(hint_text="Enter text 2 here", size_hint=(1, None), height=100, multiline=True)
        self.text_input_3 = TextInput(hint_text="Enter text 3 here", size_hint=(1, None), height=100, multiline=True)
        
        box_layout.add_widget(self.text_input_1)
        box_layout.add_widget(self.text_input_2)
        box_layout.add_widget(self.text_input_3)
        self.add_widget(box_layout)

        # Create the Save button
        save_button = Button(text="Save", size_hint=(None, None), size=(50, 50))
        save_button.pos_hint = {"center_x": 0.75, "center_y": 0.6}  # Position slightly above center
        save_button.bind(on_press=self.save_text_to_file)
        self.add_widget(save_button)

        # Create the Load button
        load_button = Button(text="Load", size_hint=(None, None), size=(50, 50))
        load_button.pos_hint = {"center_x": 0.75, "center_y": 0.4}  # Position slightly below center
        load_button.bind(on_press=self.load_text_from_file)
        self.add_widget(load_button)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def save_text_to_file(self, instance):
        # Combine the text from all three text inputs
        text_content = f"{self.text_input_1.text}\n{self.text_input_2.text}\n{self.text_input_3.text}"
        
        # Save the combined text to a file
        with open("saved_text.txt", "w") as file:
            file.write(text_content)
        print("Text saved to saved_text.txt")

    def load_text_from_file(self, instance):
        # Use tkinter to open the file dialog
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename(
            title="Select file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                
                # Load text into the text inputs (up to 3 lines)
                if len(lines) > 0:
                    self.text_input_1.text = lines[0].strip()
                if len(lines) > 1:
                    self.text_input_2.text = lines[1].strip()
                if len(lines) > 2:
                    self.text_input_3.text = lines[2].strip()

class MyApp(App):
    def build(self):
        Window.title = "CVReactor"
        return CVReactor()

if __name__ == '__main__':
    MyApp().run()
