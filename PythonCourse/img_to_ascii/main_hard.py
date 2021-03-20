import numpy as np
from PIL import Image
# please change import on your hard.py location
from PythonCourse.ASCII.refactor.hard import ImageToAscii


def main():
    print("Do you want to take a picture from www address and convert it to ascii picture from that?\n"
          "Write yes if yes or no if no")
    www_address_user = input()

    if www_address_user == 'yes'.lower():
        print("Please paste a link on image that I download and convert it to ascii\n"
              "link should be like this: https://upload.wikimedia.org/wikipedia/commons/3/30/ROS_Crystal_Logo.png")
        www_address_link = input()
        ImageToAscii(asciis=None, np_image=None, filename=None,
                     www_address=www_address_link).download_img_from_www()
        image_path = 'www_image.jpg'
        img = Image.open(image_path).convert('L').resize((80, 40))
        np_image = np.array(img)
        image_to_ascii = ImageToAscii(asciis=None, np_image=np_image, filename='www_image.jpg', www_address=None)
        image_to_ascii.image_to_ascii()
        print()
        print("Do you want to send result by email in .txt and .jpg format to someone?\n"
              "Write yes if yes and no if no")
        send_by_email = input()
    else:
        print("ok bye!")
        quit()
    if send_by_email == 'yes'.lower():
        ascii_to_text = ImageToAscii(asciis=None, np_image=np_image, filename='txt_email.txt',
                                     www_address=www_address_link)
        ascii_to_text.ascii_image_to_text()
        ascii_to_jpg = ImageToAscii(asciis=None, np_image=np_image, filename='jpg_email.jpg',
                                    www_address=www_address_link)
        ascii_to_jpg.ascii_image_to_jpg('txt_email.txt')
        print("Ascii to .txt and .jpg is ready!\n"
              "Please write an email where you want to send results like: hhttajapai@gmail.com")
        receiver_mail = input()
        print("Please write your gmail, which is sender or use my\n"
              "write 'default' if you want to use my gmail and password"
              "or write your like hhttajapai@gmail.com")
        sender_email = input()
        if sender_email != 'default':
            print("Please write password from your gmail: ")
            password_email = input()
            send_attachments = ImageToAscii(asciis=None, np_image=np_image, filename=None,
                                            www_address=www_address_link)
            send_attachments.email_sender_with_two_attachments(receiver_mail, sender_email, password_email)
        elif sender_email == 'default':
            sender_email = 'hhttajapai@gmail.com'
            password_email = 'Breathe1337!'
            send_attachments = ImageToAscii(asciis=None, np_image=np_image, filename=None,
                                            www_address=www_address_link)
            send_attachments.email_sender_with_two_attachments(receiver_mail, sender_email, password_email)
        else:
            print("ok bye!")
            quit()
    else:
        print("ok bye")
        quit()


if __name__ == "__main__":
    main()
