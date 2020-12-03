"""For installing instabot use the commamd "pip install instabot"""
#import instabot
from instabot import Bot
bot = Bot() #Now the bot is activated
bot.login(username = "Your_user_name",password = "Your_password") #Login into your account
bot.upload("Your_post_image.jpg",caption = "Your caption for this post") #Upload your post.
