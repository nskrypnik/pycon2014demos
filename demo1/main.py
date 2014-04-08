
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Rectangle, Ellipse, Triangle, \
                            Color

class DemoApp(App):
    
    def build(self):
        widget = Widget(size=Window.size)
        with widget.canvas:
            Color(1, 0, 0)
            self.rect = Rectangle(size=(150, 150))
            Color(0, 0, 1)
            self.circle = Ellipse(size=(175, 175))
            Color(0, 1, 0)
            self.triangle = Triangle(points=(0, 0, 200, 0, 100, 200))

        Clock.schedule_once(self._place_elements, 0.1)
        self.root = widget
        return widget

    def _place_elements(self, dt):
        """ Set elements position after resizing """
        self.root.size = Window.size
        center = Window.center
        self.rect.pos = center[0] + 100, center[1] + 100
        self.circle.pos =  center[0] - 100, center[1] - 100


if __name__ == '__main__':
    DemoApp().run()

