#! /usr/bin/python3

import random
from datetime import datetime
# import smtplib
# from email.message import EmailMessage
# import mimetypes
#
# def game_sender():
#     gmail_user = "hhttajapai@gmail.com"
#
#     # with open("pw.txt") as filereader:
#     gmail_password = 'Breathe1337'
#
#     to = ['hhttajapai@gmail.com']
#
#     subject = 'very important message'
#     body = 'zdravstvuite'
#
#     msg = EmailMessage()
#     msg.set_content(body)
#     msg['Subject'] = subject
#     msg['from'] = gmail_user
#     msg['To'] = to
#
#     body = """test
#         228"""
#     msg.set_content(body)
#
#     mime_type, _ = mimetypes.guess_type('game.py')
#     mime_type, mime_subtype = mime_type.split('/')
#
#     with open('game.py', 'rb') as file:
#         msg.add_attachment(file.read(),
#                            maintype=mime_type,
#                            subtype=mime_subtype,
#                            filename='game.py')
#     print(msg)
#
#     while True:
#         try:
#             server = smtplib.SMTP('smtp.gmail.com', 587)
#             server.ehlo()
#             server.starttls()
#             server.ehlo()
#         except:
#             print('cannot connect to server')
#             break
#         try:
#             server.login(gmail_user, gmail_password)
#         except:
#             print("error with username or pw")
#             break
#         try:
#             server.send_message(msg)
#         except:
#             print("error with senging email")
#             break
#         try:
#             server.close()
#         except:
#             print("error with server closing")
#             break
#         break
#
# def  start_time():
#
# def main():
#     gmail_user = "hhttajapai@gmail.com"
#
#     with open("pw.txt") as filereader:
#         gmail_password = filereader.read()
#
#     to = ['hhttajapai@gmail.com']
#     subject = f'very important message '
#     body = 'https://youtu.be/dQw4w9WgXcQ'
#
#     msg = EmailMessage()
#     msg.set_content(body)
#     msg['Subject'] = subject
#     msg['from'] = gmail_user
#     msg['To'] = to
#
#     while True:
#         try:
#             server = smtplib.SMTP('smtp.gmail.com', 587)
#             server.ehlo()
#             server.starttls()
#             server.ehlo()
#         except:
#             print('cannot connect to server')
#             break
#         try:
#             server.login(gmail_user, gmail_password)
#         except:
#             print("error with username or pw")
#             break
#         try:
#             server.send_message(msg)
#         except:
#             print("error with senging email")
#             break
#         try:
#             server.close()
#         except:
#             print("error with server closing")
#             break
#         break
