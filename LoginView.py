from NotificationPreferences import NotificationPreferences

class LoginView:
    def __init__(self):
        pass
    def readUsernameTextbox(self):
        pass
    def readPasswwordTextbox(self):
        pass
    def readEmailTextbox(self):
        pass
    def readNotificationPreferences(self, NotifPrefs):
        NotifObject = NotificationPreferences(NotifPrefs)
        return NotifObject
    