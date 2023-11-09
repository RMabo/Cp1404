"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Roderick Mabo
Started 09/11/2023
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Roderick Mabo'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = '0.0'

    def handle_increment(self, value):
        """ handle increment (could be button press or other call), output result to label widget """
        try:
            result = float(self.root.ids.input_number.text) + value
            self.root.ids.input_number.text = str(result)
        except ValueError:
            self.root.ids.input_number.text = '0.0'


SquareNumberApp().run()
