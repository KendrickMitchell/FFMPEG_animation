# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from functions import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    image = Image.open(r'C:\Users\Kendrick\Pictures\Saved Pictures\zhentarim hideout.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("C:/WINDOWS/FONTS/Arial.ttf", 24)
    text = u"""Edited\nstuff"""
    draw.text(xy=(50, 50), text=u"""Edited\nstuff""", font=font, fill=(255, 0, 0), stroke_fill=(0, 0, 0), stroke_width=1,
              align="left", spacing=8)
    image.show()

    # Main work loop
    print_hi('Running Animation script')
    MyProj = MovieFrames(1, 30)  # fps needs fine-tuning
    MyProj.setup_effect_queue()
    MyProj.add_frames(r"Videos/Frames")
    MyProj.extract_images(r"Videos/Frames")
    MyProj.run_effects()
    MyProj.save_edited_frames(r"Videos/Edited_Frames/")

# Animation project
# Goal: Make a small animation using functions. steps are in the txt document

