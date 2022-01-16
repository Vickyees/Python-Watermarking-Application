from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageFont, ImageDraw
from pathlib import Path
import os


INITIAL_DIRECTORY = str(Path.home() / "Downloads")
DEFAULT_FONT_SIZE = 120
DEFAULT_TEXT_POSITION = (800, 200)
DEFAULT_LOGO_SIZE = (500, 150)
DEFAULT_LOGO_POSITION = (450, 200)
DEFAULT_FONT_STYLE = "arial.ttf"

image = None
logo = None


def select_image():
    global image
    image = Image.open(askopenfilename(initialdir=INITIAL_DIRECTORY, title="Select an image", filetype=
    (("jpeg files", "*.jpg"), ("all files", "*.*"))))
    if image:
        image_tick.set("✔")


def select_logo():
    global logo
    logo = Image.open(askopenfilename(initialdir=INITIAL_DIRECTORY, title="Select a logo", filetype=
    (("jpeg files", "*.jpg"), ("all files", "*.*"))))
    if logo:
        logo_tick.set("✔")


def apply_watermark():

    global image, logo

    # image watermark
    size = list(map(int, logo_size.get().strip().split("x")))
    watermark_logo_size = (size[0], size[1])
    crop_image = logo.copy()
    crop_image.thumbnail(watermark_logo_size)
    copied_image = image.copy()
    position = list(map(int, logo_position.get().strip().split(",")))
    copied_image.paste(crop_image, position)

    # text watermark
    draw = ImageDraw.Draw(copied_image)
    font = ImageFont.truetype(DEFAULT_FONT_STYLE, int(font_size.get().strip()))
    position = list(map(int, font_position.get().strip().split(",")))
    draw.text((position[0], position[1]), text_entry.get(), (0, 0, 0), font=font)
    copied_image.show()

    save_image(copied_image)


def save_image(copied_image):
    if not os.path.exists(f"{INITIAL_DIRECTORY}/watermarked-images"):
        os.mkdir(f"{INITIAL_DIRECTORY}/watermarked-images")
    copied_image.save(f"{INITIAL_DIRECTORY}/watermarked-images/watermarked-image.jpg")
    messagebox.showinfo(title="Success", message=f"Watermarked image saved in {INITIAL_DIRECTORY}")


window = Tk()
window.title("Watermarking Application")
window.config(padx=50, pady=50, bg="white")


t1 = Label(text="Select an image: ", fg="black", bg="white", font=("Ariel", 13))
t1.grid(row=0, column=0, columnspan=2)
t1.config(pady=20)

select_image_btn = Button(text="Pick Image", command=select_image)
select_image_btn.grid(row=2, column=0, columnspan=2)

image_tick = StringVar()
image_tick_label = Label(textvariable=image_tick, bg="white")
image_tick_label.grid(row=2, column=1, columnspan=2)
image_tick_label.config(padx=5)

t2 = Label(text="Select the logo: ", fg="black", bg="white", font=("Ariel", 13))
t2.grid(row=3, column=0, columnspan=2)
t2.config(pady=20)

select_logo_btn = Button(text="Pick Logo", command=select_logo)
select_logo_btn.grid(row=4, column=0, columnspan=2)

logo_tick = StringVar()
logo_tick_label = Label(textvariable=logo_tick, bg="white")
logo_tick_label.grid(row=4, column=1, columnspan=2)
logo_tick_label.config(padx=5)

empty_text = Label(text=" ", bg="white")
empty_text.grid(row=5, column=1)

logo_size_label = Label(text="Logo Size: ", fg="black", bg="white", font=("Ariel", 8))
logo_size_label.grid(row=6, column=0)

logo_size = Entry(width=15)
logo_size.grid(row=6, column=1, columnspan=2)
logo_size.insert(0, f"{str(DEFAULT_LOGO_SIZE[0])}x{str(DEFAULT_LOGO_SIZE[1])}")

logo_position_label = Label(text="Logo Position: ", fg="black", bg="white", font=("Ariel", 8))
logo_position_label.grid(row=7, column=0)

logo_position = Entry(width=15)
logo_position.grid(row=7, column=1, columnspan=1)
logo_position.insert(0, f"{str(DEFAULT_LOGO_POSITION[0])},{str(DEFAULT_LOGO_POSITION[1])}")


t3 = Label(text="Enter the text: ", fg="black", bg="white", font=("Ariel", 13))
t3.grid(row=9, column=0, columnspan=2)
t3.config(pady=20)

text_entry = Entry(width=30)
text_entry.grid(row=10, column=0, columnspan=2)

empty_text = Label(text=" ", bg="white")
empty_text.grid(row=11, column=1)

font_size_label = Label(text="Font Size: ", fg="black", bg="white", font=("Ariel", 8))
font_size_label.grid(row=12, column=0)

font_size = Entry(width=15)
font_size.grid(row=12, column=1, columnspan=2)
font_size.insert(0, str(DEFAULT_FONT_SIZE))

font_position_label = Label(text="Font Position: ", fg="black", bg="white", font=("Ariel", 8))
font_position_label.grid(row=13, column=0)

font_position = Entry(width=15)
font_position.grid(row=13, column=1, columnspan=1)
font_position.insert(0, f"{str(DEFAULT_TEXT_POSITION[0])},{str(DEFAULT_TEXT_POSITION[1])}")

empty_text = Label(text=" ", bg="white")
empty_text.grid(row=14, column=1)
empty_text.config(pady=30)


watermark_btn = Button(text="Apply Watermark and Save", command=apply_watermark)
watermark_btn.grid(row=15, column=1)

window.mainloop()
