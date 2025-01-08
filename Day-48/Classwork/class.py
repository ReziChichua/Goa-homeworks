phone = {
    "name": "Iphone 12",
    "color": "black",
    "battery": "100%",
    "storage": "64gb",
    "wallpaper": "default"
}

for key in phone:
    print (key)

for value in phone.values():
    print(value)

for key, value in phone.items():
    print(f"{key}: {value}")