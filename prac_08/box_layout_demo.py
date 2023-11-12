from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet the user"""
        name = self.root.ids.input_name.text # get name from InputText widget
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """Clear all the text input and output"""
        self.root.ids.input_name.text = '' # clear InputText widget
        self.root.ids.output_label.text = '' # clear Label widget


BoxLayoutDemo().run()
