#! /usr/bin/python3
# original author: Emil Khaibrakhmanov
# I the author grant the use of this code for teaching: yes

# In this task you should allow students to create a new account with unique ID and password.
#
# Once the program starts, you should print the menu:
#
# 1. Create student ID 2. Log into student account 0. Exit If a student chooses ‘Create student ID’, you should
# generate a new ID which satisfies all the conditions described below. Then you should generate a password that
# belongs to the generated student ID. A password code is a sequence of any 6 digits. Password should be generated in
# a range from 000000 to 999999.
#
# If a student chooses ‘Log into student account’, you should ask them to enter their ID information. Your program
# should store all generated data until it is terminated so that a user is able to log into any of the created ID by
# an ID  and its password. You can use an array to store the information.
#
# After all information is entered correctly, you should allow the user to check his credits amount; right after
# creating the account, the credits amount should be 0. It should also be possible to log out of the account and exit
# the program.
#
# ID conditions:
#
# 1. Student ID should contain 7 digits(like 5234567)
# 2. Student ID should begin with 5
# 3. Student ID should be unique

# 1. Create student ID
# 2. Log into student account
# 0. Exit
# >1
#
# Your ID has been created
# Your ID:
# 5856746
# Your password:
# 123321
#
# 1. Create student ID
# 2. Log into student account
# 0. Exit
# >2
#
# Enter your ID:
# >522222
# Enter your password:
# >3333333
#
# Wrong ID or password!
#
# 1. Create student ID
# 2. Log into student account
# 0. Exit
# >2
#
# Enter your ID:
# >5856746
# Enter your password:
# >123321
#
# You have successfully logged in!
#
# 1. Credits
# 2. Log out
# 0. Exit
# >1
#
# Current credits amount: 0
#
# 1. Credits
# 2. Log out
# 0. Exit
# >2
#
# You have successfully logged out!
#
# 1. Create student ID
# 2. Log into student account
# 0. Exit
# >0
#
# See you!


import random


class StudentAccount:

    def __init__(self):
        self.ID = {}
        self.credits = 0
        self.Exit = False

    def menu(self):
        while not self.Exit:
            print("1. Create student ID\n2. Log into student account\n0. Exit")
            n = input()
            if n == "1":
                self.create()
            elif n == "2":
                self.log()
            elif n == "0":
                print("See you!")
                self.Exit = True

    def create(self):
        number = f"5{random.randrange(0, 999999):06}"
        password = f'{random.randrange(0, 999999):06}'
        print("Your ID has been created")
        print(f"Your ID:\n{number}")
        print(f"Your password:\n{password}")
        self.ID[number] = password
        self.menu()

    def log(self):
        account_log = input("Enter your ID:")
        pin_log = input("Enter your password:")
        if self.ID.get(account_log) == pin_log:
            print("You have successfully logged in!")
            self.logged()
        else:
            print("Wrong ID or password!")
            self.menu()

    def logged(self):
        while not self.Exit:
            print("1. Credits\n2. Log out\n0.exit")
            n = input()
            if n == "1":
                print(self.credits)
                self.logged()
            elif n == "2":
                print("You have successfully logged out!")
                self.menu()
            elif n == "0":
                self.Exit = True


if __name__ == '__main__':
    StudentAccount().menu()
