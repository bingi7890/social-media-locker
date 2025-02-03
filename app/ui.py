from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.clock import Clock

class SocialMediaLockerUI(BoxLayout):
    def __init__(self, monitor, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        self.monitor = monitor

        self.add_widget(Label(text='Social Media Usage Locker', font_size=24, bold=True))

        self.switch = Switch(active=False)
        self.switch.bind(active=self.toggle_monitoring)

        self.add_widget(Label(text='Enable Monitoring'))
        self.add_widget(self.switch)

        self.timer_label = Label(text='Time Left: 1:00:00', font_size=18)
        self.add_widget(self.timer_label)

        self.reset_button = Button(text='Reset Timer', size_hint=(None, None), size=(200, 50))
        self.reset_button.bind(on_press=self.reset_timer)
        self.add_widget(self.reset_button)

    def toggle_monitoring(self, instance, value):
        self.monitor.toggle_monitoring(instance, value)

    def update_timer(self, minutes, seconds):
        self.timer_label.text = f'Time Left: {minutes:02}:{seconds:02}'

    def set_timer_expired(self):
        self.timer_label.text = 'Time Expired! Apps Locked.'

    def reset_timer(self, instance):
        self.monitor.reset_timer()
        self.timer_label.text = 'Time Left: 1:00:00'
