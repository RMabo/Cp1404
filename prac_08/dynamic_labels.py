from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App for displaying dynamic labels for a list of names."""

    def __init__(self, **name):
        super().__init__(**name)
        self.names = ['dog', 'Cat ', 'bird']

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_names()
        return self.root

    def create_names(self):
        """Create a label for each name."""
        for name in self.names:
            self.root.ids.names_box.add_widget(Label(text=name))


if __name__ == "__main__":
    DynamicLabelsApp().run()
