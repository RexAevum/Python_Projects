# Necessary imports for connecting with kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob, random
from datetime import datetime
from pathlib import Path
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
    

    def login(self, user, passw):
        with open(filePath) as file:
            data = json.load(file)
            if user in data and data[user]['password'] == passw: # Contains
                self.manager.transition.direction = 'left'
                self.manager.current = "login_screen_success"
            else:
                self.ids.loginFailed.text = "Incorrect User Info"


# Every screen/page has to have its own name with the class name matching the .kv file
class SignupScreen(Screen):
    def add_user(self, uname, pword):
        # Get info from .json file
        with open(filePath, 'r') as file:
            users = json.load(file)
        # Add the new info to the db
        users[uname] = {'username' : uname, 'password' : pword, 
        'created' : datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        print(users) 
        # Overwrite the new users to the file
        with open(filePath, 'w') as file:
            json.dump(users, file)
        # move to the success screen
        self.manager.current = "signup_screen_success"

class SignupScreenSuccess(Screen):
    def back(self):
        # Go back to log in screen and have the screen move to the right
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"




class LoginScreenSuccess(Screen):
    def logout(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    
    def get_quote(self, feeling):
        feeling = feeling.lower()
        # gets all of the files with that contain the given format
        feelingsOnFile = glob.glob('data/*.txt')
        # 
        feelingsOnFile = [Path(filename).stem for filename in feelingsOnFile]
        if feeling in feelingsOnFile:
            with open("data/{}.txt".format(feeling), encoding='utf8') as file:
                # Get all of the data by line, creating a list of quote lines
                quotes = file.readlines()
            # get a random quote from the list of quotes    
            self.ids.toInspire.text = random.choice(quotes)
        else:
            self.ids.toInspire.text = "Sorry, have nothing for this. Please try another emotion."
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