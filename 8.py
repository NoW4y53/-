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
def crop_and_add_text(input_im_p, output_im_p, cropp, name):
    name = input("Введите имя для поздравления: ")
    image = Image.open(input_im_p)
    cropped_im = image.crop(cropp)
    text = f"{name}, поздравляю!"
    font_path = "font.ttf"
    font_size = 40
    font = ImageFont.truetype(font_path, font_size)
    text_color = (255, 0, 0)
    draw = ImageDraw.Draw(cropped_im)
    text_width, text_height = draw.textsize(text, font=font)
    position = ((cropped_im.width - text_width) / 2, (cropped_im.height - text_height) / 2)
    draw.text(position, text, fill=text_color, font=font)
    cropped_im.save(output_im_p + '.png')
input_im_p = "hb.jpg"
cropp = (100, 100, 300, 300)
output_im_p = "congratulation_croppedhb"

