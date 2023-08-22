from PIL import Image, ImageTk, ImageDraw
import random
import tkinter as tk
import math
import os
import imageio

def convert_images():
    image_folder = "images"
    output_file = "output_video.mp4"
    fps = 60

    images = []
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith(".png"):
            image_path = os.path.join(image_folder, filename)
            image = Image.open(image_path)
            images.append(image)

    imageio.mimsave(output_file, images, fps=fps)

convert = input("Want to just convert the images folder into a video? y/n: ")

if convert == "y":
    convert_images()
    exit()


canvas_width = int(input("Canvas width: "))
canvas_height = int(input("Canvas height: "))
block_size = int(input("Anomaly pixels: "))
time_ = (int(input("Interdimensional time (1 to whatever, you can put billions): ")) + 1) * -1
save_images = input("Save images y/n: ")
if save_images == "y":
    save_images = True
    if not os.path.exists("images"):
        os.makedirs("images")
else:
    save_images = False

root = tk.Tk()
root.title("Interdimensional camera")

time = time_

image_label = tk.Label(root)
image_label.pack()

image = Image.new("RGB", (canvas_width, canvas_height))
pixels = image.load()

frame_count = 0

def update_image():
    global time
    global frame_count
    time += 1
    
    for x in range(canvas_width):
        for y in range(canvas_height):
            result = (abs(random.randint(1, 5) % time) + round(math.sin(x * canvas_width)) + round(math.cos(y * canvas_height))) % 5
            if result == 0:
                pixels[x, y] = (0, 0, 0)
            elif result == 1:
                pixels[x, y] = (0, 0, 0)
            elif result == 2:
                pixels[x, y] = (0, 0, 0)
            elif result == 3:
                pixels[x, y] = (0, 0, 0)
            elif result == 4:
                pixels[x, y] = (0, 50, 0)

    update_draw()

    if save_images:
        image.save(f"images/frame_{frame_count:04d}.png")
        frame_count += 1

    root.after(100, update_image)

def update_draw():
    draw = ImageDraw.Draw(image)
    
    for x in range(0, canvas_width - block_size + 1, block_size):
        for y in range(0, canvas_height - block_size + 1, block_size):
            is_black_clump = all(pixels[bx, by] == (0, 0, 0) for bx in range(x, x + block_size) for by in range(y, y + block_size))
            if is_black_clump:
                center_x = x + block_size // 2
                center_y = y + block_size // 2
                draw.line([(center_x, y), (center_x, y + block_size)], fill=(0, 102, 204))
                draw.line([(x, center_y), (x + block_size, center_y)], fill=(0, 102, 204))
    
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

update_image()
root.mainloop()
