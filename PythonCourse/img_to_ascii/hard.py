import urllib.request
from PIL import Image
import sys
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw
import ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
from email import encoders


class ImageToAscii:

    def __init__(self, asciis, np_image, filename, www_address):
        if asciis is None:
            asciis = [' ', 'e', 'w', 'y', 'e', '*', '+', '-']
            self.asciis = asciis
            self.np_image = np_image
            self.filename = filename
            self.www_address = www_address

    def image_to_ascii(self):
        for index_x in range(self.np_image.shape[0]):
            print("")
            for index_y in range(self.np_image.shape[1]):
                multiplier = 255 // len(self.asciis)
                for asc in range(len(self.asciis)):
                    if self.np_image[index_x, index_y] >= (255 - (asc + 1) * multiplier):
                        print(self.asciis[asc], end='')
                        break

    # Easy
    # instead of printing to the terminal, saves ascii picture as text file
    def ascii_image_to_text(self):
        print("Conversion to txt started!")
        orig_stdout = sys.stdout
        sys.stdout = open(self.filename, "w+")
        self.image_to_ascii()
        sys.stdout.close()
        sys.stdout = orig_stdout
        print(f"Conversion to txt ended!Check {self.filename} in script folder!")

    # Normal
    # method to the class, that instead of printing to the terminal, saves ascii picture as jpg file

    def ascii_image_to_jpg(self, txt_to_open):

        pixel_vkl = 0
        pixel_off = 255

        print("Conversion to jpg started..\n")

        orig_stdout = sys.stdout
        sys.stdout = open(txt_to_open, "w+")
        ImageToAscii.image_to_ascii(self)
        sys.stdout.close()

        grayscale = 'L'
        with open(txt_to_open) as text_file:
            stroki = tuple(s.rstrip() for s in text_file.readlines())

        font_size = 20
        font_path = 'cour.ttf'
        try:
            shrift = PIL.ImageFont.truetype(font_path, size=font_size)
        except IOError:
            shrift = PIL.ImageFont.load_default()

        topx = lambda pt: int(round(pt * 96.0 / 72))

        max_w_l = max(stroki, key=lambda s: shrift.getsize(s)[0])
        test = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        h_max = topx(shrift.getsize(test)[1])
        w_max = topx(shrift.getsize(max_w_l)[0])
        h = h_max * len(stroki)
        w = int(round(w_max + 40))
        picture = PIL.Image.new(grayscale, (w, h), color=pixel_off)
        draw = PIL.ImageDraw.Draw(picture)

        v_pos = 5
        h_pos = 5
        str_sp = int(round(h_max * 0.8))
        for line in stroki:
            draw.text((h_pos, v_pos),
                      line, fill=pixel_vkl, font=shrift)
            v_pos += str_sp
        yashik = PIL.ImageOps.invert(picture).getbbox()
        picture = picture.crop(yashik)
        picture.save(self.filename)
        sys.stdout = orig_stdout
        print(f"ascii to .jpg DONE!({self.filename} in script folder)")

    # Hard
    def download_img_from_www(self):
        urllib.request.urlretrieve(self.www_address, 'www_image.jpg')
        img = Image.open('www_image.jpg').convert('L').resize((40, 40))
        img.save('www_image.jpg')

    @staticmethod
    def email_sender_with_two_attachments(receiver_mail, sender_mail, sender_password):
        subject = "Email with .jpg and .txt from ascii"
        body = "Here is 2 files"
        sender_email = sender_mail
        receiver_email = receiver_mail
        password = sender_password

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email

        message.attach(MIMEText(body, "plain"))

        filename = "jpg_email.jpg"

        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        files = [
            'jpg_email.jpg',
            'txt_email.txt'
        ]
        for a_file in files:
            attachment = open(a_file, 'rb')
            file_name = os.path.basename(a_file)
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            part.add_header('Content-Disposition',
                            'attachment',
                            filename=file_name)
            encoders.encode_base64(part)
            message.attach(part)
        text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
