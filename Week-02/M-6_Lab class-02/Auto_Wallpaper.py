""" Problem:

  Download and change desktop wallpapers automatically

 """
import requests
import json
import PyWallpaper
api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# get the json
response = requests.get(api_url)
content = response.content.decode('UTF-8')
# print(content)


# Convert string to json:
dict_content = json.loads(content)
# print(dict_content)


# get the image url:
image_url = dict_content['url']
# print(image_url)


# download the image:
res = requests.get(image_url)
# print(res)


# save the image:
with open('jafrul.png','wb') as image:
    image.write(res.content)

#set as wallpaper:
PyWallpaper.change_wallpaper("D:\Phitron Programming\C++ Folder\Python and OOP\jafrul.png")