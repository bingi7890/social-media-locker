from jnius import autoclass

Preferences = autoclass('android.content.SharedPreferences')
Editor = autoclass('android.content.SharedPreferences$Editor')

class DataStore:
    def __init__(self):
        self.shared_prefs = App.get_running_app().android_activity.getPreferences(0)

    def save_time_left(self, time_left):
        editor = self.shared_prefs.edit()
        editor.putInt("time_left", time_left)
        editor.apply()

    def get_time_left(self):
        return self.shared_prefs.getInt("time_left", 3600)  # Default to 1 hour
