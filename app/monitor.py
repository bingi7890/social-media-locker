from jnius import autoclass
from kivy.clock import Clock
from kivy.app import App

UsageStatsManager = autoclass('android.app.usage.UsageStatsManager')
Context = autoclass('android.content.Context')
Intent = autoclass('android.content.Intent')

class AppMonitor:
    def __init__(self, ui):
        self.ui = ui
        self.time_left = 3600  # 1 hour in seconds
        self.monitoring = False
        self.blocked_apps = [
            "com.instagram.android", "com.facebook.katana", 
            "com.twitter.android", "com.snapchat.android"
        ]

    def toggle_monitoring(self, instance, value):
        if value:
            self.monitoring = True
            Clock.schedule_interval(self.update_timer, 1)
            Clock.schedule_interval(self.check_app_usage, 10)
        else:
            self.monitoring = False
            Clock.unschedule(self.update_timer)
            Clock.unschedule(self.check_app_usage)

    def update_timer(self, dt):
        if self.time_left > 0:
            self.time_left -= 1
            minutes, seconds = divmod(self.time_left, 60)
            self.ui.update_timer(minutes, seconds)
        else:
            Clock.unschedule(self.update_timer)
            self.ui.set_timer_expired()

    def check_app_usage(self, dt):
        if self.time_left <= 0:
            self.block_apps()

    def block_apps(self):
        """ Redirect user to home screen if they try to open a blocked app """
        intent = Intent()
        intent.setAction(Intent.ACTION_MAIN)
        intent.addCategory(Intent.CATEGORY_HOME)
        intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        App.get_running_app().android_activity.startActivity(intent)

    def reset_timer(self):
        self.time_left = 3600  # Reset to 1 hour
