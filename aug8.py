from cProfile import label
from turtle import textinput
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from matplotlib.pyplot import text
from numpy import source
from sqlalchemy import false

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols=1
        self.window.size_hint=(0.6,0.7)
        self.window.pos_hint={"center_x":0.5,"center_y":0.5}

        #add widgets to window
        self.window.add_widget(Image(source="sayhello.png"))
        # add text widget 
        self.greeting=Label(
            text="What is your Name!",
            font_size=30,
            color="#00FFCE",
            )
        self.window.add_widget(self.greeting)

        # add input widget
        self.user=TextInput(
            multiline=False,
            padding_y=(20,20),
            size_hint=(1,0.5),
            )
        self.window.add_widget(self.user)

        # add button 
        self.button=Button(
            text="Greet",
            size_hint=(1,0.5),
            font_size=30,
            bold=True,
            background_color="#00FFCE"
            )
        self.button.bind(on_press=self.callBack)
        self.window.add_widget(self.button)

        return self.window

    def callBack(self,instance):
        self.greeting.text="Hello "+ self.user.text

if __name__ == "__main__":
    SayHello().run()