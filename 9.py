from PIL import Image, ImageFilter
import os

def apply_filter(image_path, filter_name, output_folder):
      image = Image.open(image_path)
      filtered_image = image.convert(filter_name)
      output_path = os.path.join(output_folder, os.path.basename(image_path))
      filtered_image.save(output_path)

input_folder = "input_images"
output_folder = "output_images"
if not os.path.exists(output_folder):
  os.makedirs(output_folder)
def numOne:
  for filename in os.listdir(input_folder):
      if filename.endswith(".jpg"):
          image_path = os.path.join(input_folder, filename)
          apply_filter(image_path, "L", output_folder)
def numTwo:
  for filename in os.listdir(input_folder):
      if filename.lower().endswith(".jpg", ".png"):
          image_path = os.path.join(input_folder, filename)
          apply_filter(image_path, "L", output_folder)
#3
import csv
def calculate_total_expenses(csv_file_path):
    total_sum = 0
    products = []
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row if there is one
        for row in reader:
            product, quantity, price = row
            quantity = int(quantity)
            price = int(price)
            total_sum += quantity * price
            products.append(f"{product} - {quantity} шт. за {price} руб.")
    print("Нужно купить:")
    for product in products:
        print(product)
    print(f"Итоговая сумма: {total_sum} руб.")

csv_file_path = "products.csv"
#calculate_total_expenses(csv_file_path)
