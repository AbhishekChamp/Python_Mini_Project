from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import json
from datetime import datetime
import re
import random

Builder.load_file('game.kv')


class LogInScreen(Screen):
    def sign_up(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "sign_up_screen"
        self.ids.login_wrong.text = ""

    def forget_password(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "forgot_password_screen"
        self.ids.login_wrong.text = ""

    def login(self, name, pwd):
        with open("users.json") as file:
            users = json.load(file)
        if name in users and users[name] ['password'] == pwd:
            self.manager.current = "Login_screen_success"
            self.manager.transition.direction = 'left'
        else:
            self.ids.login_wrong.text = "Invalid username or password! Please try again"

class SignUpScreen(Screen):

    def check_user(self, name, pwd):
        if (name == "") or (pwd == ""):
            self.ids.empty.text = "Username or password cannot be empty"
        elif (((' ' in name) == True) or ((' ' in pwd) == True)):
            self.ids.empty.text = "Username or password cannot contain spaces"
        else:
            self.add_user(name, pwd)

    def add_user(self, name, pwd):
        with open("users.json") as file:
            users = json.load(file)
            
            if name in users:
                self.ids.empty.text = "Username already exists"
            else:
                self.ids.empty.text = ""
                users [name] = {'username': name,
                                'password': pwd,
                                'created' : datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                                }
            
                with open("users.json", 'w') as file:
                    json.dump(users, file)
                self.manager.current = "sign_up_screen_success"

    def go_back(self):
        self.ids.empty.text = ""
        self.manager.transition.direction = 'right'
        self.manager.current = "Log_in_screen"

class SignUpScreenSuccess(Screen):
    
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "Log_in_screen"

class ForgotPasswordScreen(Screen):

    def go_back(self):
        self.ids.comment.text = ""
        self.manager.transition.direction = 'right'
        self.manager.current = "Log_in_screen"

    def send_details(self, mail, name):
        if (mail == "") or (name == ""):
            self.ids.comment.text = "Mail ID or Username cannot be empty"
        elif (((' ' in mail) == True) or ((' ' in name) == True)):
            self.ids.comment.text = "Mail ID or Username cannot contain spaces"
        else:
            self.validate_user(mail, name)

    def validate_user(self, mail, name):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        with open("users.json") as file:
            users = json.load(file)
            
            if name in users:
                if(re.fullmatch(regex, mail)):
                    self.ids.comment.text = "Your password is sent in mail"
                else:
                    self.ids.comment.text = "Invalid mail ID"
            else:
                self.ids.comment.text = f"No user under the username {name}"

class LogInScreenSuccess(Screen):
    
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "Log_in_screen"
        self.stop_game()

    def start_stop(self):
        if (self.ids.start_game.text == "Start Game"):
            self.ids.start_game.text = "Quit Game"
            self.start_game()
        else:
            self.stop_game()

    def start_game(self):
        self.rand_num()

    def rand_num(self):
        self.my_list = [ '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']
        random.shuffle(self.my_list)
        self.ids.button_0.text = f'{self.my_list[0]}'
        self.ids.button_1.text = f'{self.my_list[1]}'
        self.ids.button_2.text = f'{self.my_list[2]}'
        self.ids.button_3.text = f'{self.my_list[3]}'
        self.ids.button_4.text = f'{self.my_list[4]}'
        self.ids.button_5.text = f'{self.my_list[5]}'
        self.ids.button_6.text = f'{self.my_list[6]}'
        self.ids.button_7.text = f'{self.my_list[7]}'
        self.ids.button_8.text = f'{self.my_list[8]}'
        self.ids.button_9.text = f'{self.my_list[9]}'
        self.ids.button_10.text = f'{self.my_list[10]}'
        self.ids.button_11.text = f'{self.my_list[11]}'
        self.ids.button_12.text = f'{self.my_list[12]}'
        self.ids.button_13.text = f'{self.my_list[13]}'
        self.ids.button_14.text = f'{self.my_list[14]}'
        self.ids.click_num.text = f"Click Number: {random.choice(self.my_list)}"
        self.number_to_check = self.ids.click_num.text[14:]

    def stop_game(self):
        self.ids.score.text = "Score : 0"
        self.ids.click_num.text = "Cick Number : - "
        self.ids.start_game.text = "Start Game"

    def result(self, click_num, button_click):
        check = click_num[14:]
        if (check == button_click):
            self.current_score()
            self.rand_num()
        else:
            self.stop_game()

    def current_score(self):
        score = self.ids.score.text[8:]
        self.ids.score.text = f"Score : {(int(score)+1)}"

class RootWidget(ScreenManager):
    pass

class Find_MeApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    Find_MeApp().run()