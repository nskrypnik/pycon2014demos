
from kivy.app import App
from kivy.clock  import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Ellipse, Triangle, Color
from kivy.core.image import Image


class Demo2App(App):

    def build(self):
        widget = Widget()
        texture = Image('einstein.png').texture
        with widget.canvas:
            Color(1, 1, 1)
            self.rect = Rectangle(size=(175, 175), texture=texture)
            self.circle = Ellipse(size=(200, 200), texture=texture)
            self.triangle = Triangle(points=(0, 0, 200, 0, 100, 200), texture=texture)
        Clock.schedule_once(self._place_elements)
        self.root = widget
        return widget
    
    def _place_elements(self, dt):
        self.root.size = Window.size
        center = Window.center
        self.rect.pos = center[0] - 100, center[1] - 100
        self.circle.pos = center[0] + 100, center[1] + 100

if __name__ == '__main__':
    Demo2App().run()
