import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2       

        self.inside.add_widget(Label(text="Python List"))
        self.list = TextInput(multiline=False)
        self.inside.add_widget(self.list)

        self.inside.add_widget(Label(text="Python Dictonary"))
        self.dictionary = TextInput(multiline=False)
        self.inside.add_widget(self.dictionary)

        self.inside.add_widget(Label(text="Python Dictonary"))
        self.images = TextInput(multiline=False)
        self.inside.add_widget(self.images)

        self.inside.add_widget(Label(text="Python Expressions"))
        self.expressions = TextInput(multiline=False)
        self.inside.add_widget(self.expressions)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        list = self.list.text
        dicc = self.dictionary.text
        img = self.images.text
        exp = self.expressions.text

        print("List ", list)
        print("Dicc ", dicc)
        print("Img ", img)
        print("Exp ", exp)

        self.list.text = ""
        self.dictionary.text = ""
        self.images.text = ""
        self.expressions.text = ""




class MyApp(App):
    def build(self):
        return MyGrid()
        #return Label(text="Code In Place")

    
if __name__ == "__main__":
    MyApp().run()
