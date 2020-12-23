# Necessary imports for connecting with kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
import datetime
# load a kivy file for the ui design
Builder.load_file('design.kv')
filePath = r"data\users.json"

# When creating a class using kivy the class has to have EXACTLY the same
# Name as the screen definition/rules in the .kv file
# Screen is after the RootWidgit/ScreenManager
class LoginScreen(Screen): # Inhereting the Screen object
    def sign_up(self):
        # To navigat to another screen
        self.manager.current = "signup_screen" # Need to match the .kv file root widget name

# Every screen/page has to have its own name with the class name matching the .kv file
class SignupScreen(Screen):
    def add_user(self, uname, pword):
        # Get info from .json file
        with open(filePath) as file:
            users = json.load(file)
        # Add the new info to the db
        users[uname] = {'username' : uname, 'password' : pword, 
        'created' : datetime.datetime}
        print(users) 
        # Write the new users to the file
        with open(filePath) as file:
            json.dump(users, file)
        # Take back to log in screen
        self.manager.current = "login_screen"

# RootWidget is after the App in the hierarchy
class RootWidget(ScreenManager):
    pass

# Highes lvl in the app hierarchy
class MainApp(App):
    def build(self):
        return RootWidget()

# If this file is the main file, run the application
if __name__=="__main__":
    MainApp().run()