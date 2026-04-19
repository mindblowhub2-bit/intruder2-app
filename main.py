from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import cv2
import time


PASSWORD = "1234"
attempts = 0


def take_selfie():
    cam = cv2.VideoCapture(0)

    time.sleep(2)  # camera warm-up

    ret, frame = cam.read()

    if ret:
        cv2.imwrite("intruder.jpg", frame)
        print("📸 Intruder photo saved!")

    cam.release()
    cv2.destroyAllWindows()


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.label = Label(text="🔐 Enter Password", font_size=30)
        self.add_widget(self.label)

        self.input = TextInput(password=True, multiline=False, font_size=25)
        self.add_widget(self.input)

        self.btn = Button(text="Login", font_size=25)
        self.btn.bind(on_press=self.check_password)
        self.add_widget(self.btn)

    def check_password(self, instance):
        global attempts

        user_input = self.input.text

        if user_input == PASSWORD:
            self.label.text = "✅ Access Granted"
            attempts = 0
        else:
            attempts += 1
            self.label.text = f"❌ Wrong Attempt: {attempts}"

            self.input.text = ""

            if attempts >= 3:
                self.label.text = "🚨 Intruder Detected!"
                take_selfie()
                attempts = 0


class IntruderApp(App):
    def build(self):
        return RootWidget()


IntruderApp().run()