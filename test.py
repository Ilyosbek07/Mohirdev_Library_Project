import requests

request = requests.request(
    "GET",
    "https://rndesign.uz/Sinovapi/index.php?url=https://www.instagram.com/reel/CtHCl2gLTb8/?utm_source=ig_web_button_share_sheet"
)

# print(request.json()['medias'][1])
print(request.json())