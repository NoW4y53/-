from PIL import Image, ImageDraw, ImageFont
def crop_image(input_im_p, output_im_p, cropp):
    image = Image.open(input_im_p)    cropped_im = image.crop(cropp)
    cropped_im.save(output_im_p)
input_im_p ="mountain.jpg"cropp = (100, 100, 300, 300)
output_im_p = "croppedMountain.jpg"crop_image(input_im_p, output_im_p, cropp)

# 2
cards = {
    "День рождения": "birthday.jpg",    "Новый год": "HNY.jpg",
    "8 марта": "8March.jpg"}
def card():    print("К какому празднику Вам нужна открытка?")
    holiday = input()    if holiday in cards:
        card_filename = cards[holiday]        image = Image.open(card_filename)
        image.show()    else:
        print('К сожалению, такой открытки нет!')

# 3