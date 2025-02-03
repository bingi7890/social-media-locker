from kivy.app import App
from ui import SocialMediaLockerUI
from monitor import AppMonitor

class SocialMediaLockerApp(App):
    def build(self):
        monitor = AppMonitor(self)
        return SocialMediaLockerUI(monitor)

if __name__ == '__main__':
    SocialMediaLockerApp().run()
