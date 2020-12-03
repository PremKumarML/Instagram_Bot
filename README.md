# Instagram_Bot
This program tells us how to use the package instabot to upload photos on instagram.

First of all install instabot on your lap or PC using the command(Before that dont forgot to install python on your machine)
>>>pip install instabot
(use the latest version of pip to install instabot)

Import Bot from instabot using the command
>>>from instabot import Bot

Then using a variable activate the Bot using the following command
>>>bot = Bot()

Then, signin the instagram using your userid and password
>>>bot.login(username = "Your_user_name",password = "Your_Password")
if you are using a two factor authentication then enter the passkey when the program prompt you to enter it while running.

After logging in, the next and the final step is to upload your post on the instagram.
>>>bot.upload("your_post_image.jpg",caption = "Your caption for that particular post")

#Hurray! Our program just uploads post for us.

Thank you!!
