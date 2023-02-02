from PIL import Image, ImageFont, ImageDraw
import os

class MovieFrames:
    frames_per_second = -1  # This needs to be above 0 for any animation
    frames = []             # The path file names
    images = []             # Will be 1 to 1 with frames. Images are editable, frames are path/file_names
    id = -1
    effect_queue = []       # Will be a set of tuples going (start frame, end frame, effect type)    int,int,string

    def __init__(self, num, fps):
        self.id = num
        self.frames_per_second = fps

    def add_frames(self, directory):
        print("Adding frames")
        self.frames = os.listdir(directory)
        for frame in self.frames:
            frame = directory + "/" + frame
            print(frame)
        return

    def setup_effect_queue(self):   # Read the effect script by parsing line by line
        script_file = open("Videos/Effect_script.txt", "r", encoding='utf-8')
        for line in script_file:
            start = int(round(self.frames_per_second * int(line.split(',')[0])))  # The first frame to operate on
            end = int(round(self.frames_per_second * int(line.split(',')[1])))  # The last frame to operate on
            effect = line.split(',')[2]
            if len(line.split(',')) > 3:
                arguments = line.split(',')[3:]
                self.effect_queue.append((start, end, effect, arguments))
            else:
                self.effect_queue.append((start, end, effect))
        return

    def extract_images(self, source_folder):
        for frame in self.frames:
            self.images.append(Image.open(source_folder + '/' + frame))
        return

    def select_frames(self, start, end):  # Start and end are double seconds
        # Avoid start < end, end > length of video, and start < 0 errors
        if start < 0:
            start = 0
        if round(end * self.frames_per_second) > len(self.frames):
            end = len(self.frames)
        if start > end:  # Error
            return []
        return self.frames[round(start / self.frames_per_second):round(end / self.frames_per_second)]

    def run_effects(self):  # writable may be any shape, line, or image.
        # Write object to file.

        for effect in self.effect_queue:    # Now running through the effect queue
            start = effect[0]
            end = effect[1]
            effect_type = effect[2]
            if start < 0:
                start = 0
            if end > len(self.frames) and end > len(self.images):
                end = len(self.images)
            print("Running ", effect_type, " from ", start, " to ", end)

            if effect_type == "rainbow":
                # Getting the appropriate images to change
                self.images[start:end] = linear_rainbow(self.images[start:end], effect[3])
            if effect_type == "text":
                # Just drawing a line
                self.images[start:end] = text(self.images[start:end], effect[3])
        return 0

    def save_edited_frames(self, target_folder):
        if len(self.frames) != len(self.images):
            print("Save Frame Error. Frame count is not equal to image count. something went wrong.")
        for edited_frame_index in range(len(self.images)):
            self.images[edited_frame_index].save(target_folder + self.frames[edited_frame_index])
        return


def linear_rainbow(images, change):  # Not recommended. Will take 30+ minutes on 340 500x1000 frames
    # Now for every image
    count = 0
    for image in range(len(images)):
        print(count)
        count += 1
        x, y = images[image].size
        for pix_x in range(x):
            for pix_y in range(y):
                intensity = (pix_x + pix_y + (int(change[0]) * image)) % 255
                change_pixel(x, y, pix_x, pix_y, (intensity, intensity, intensity, 255), images[image])
        # Change every pixel color to be (x+y)+change
        # I Need to save edited images as files elsewhere. Preferably after returning to effect selection
    return images


def text(images, args):
    # Argument needs font name, fill color, xy anchor point, spacing, alignment, and language
    font_name = args[0]  # Should be a string like "arial.ttf"
    fill_color = tuple([int(args[1]), int(args[2]), int(args[3])])  # Should be a three int tuple like (255,0,255) for rgb values
    outline_color = tuple([int(args[4]), int(args[5]), int(args[6])])  # Should in same formate as fill_color.
    location = tuple([int(args[7]), int(args[8])])  # Should be a two int tuple like (x,y) ie (100,100)
    spacing = int(args[9])  # Should be an integer ex. 50
    alignment = args[10]  # Should be "left" , "right" , or "center"
    stroke_width = int(args[11])  # Should be an integer ex. 2
    font_size = int(args[12])  # Should be an int. ex. 20
    words = args[13]  # The words to display.Must be in string format  ex."words". Need to allow ',' in text. Use file?
    font_path = "C:/WINDOWS/FONTS/"
    for image in images:
        draw = ImageDraw.Draw(image)
        #font = ImageFont.truetype("C:/WINDOWS/FONTS/Arial.ttf", 24)
        font = ImageFont.truetype(font_path + font_name, font_size)
        draw.text(xy=location, text=words, font=font, fill=fill_color, stroke_fill=outline_color,
                  stroke_width=stroke_width,
                  align=alignment, spacing=spacing)
    return images


def sum_it(a, b):
    return a + b


# Given a string corresponding to a frame
def write_on_frame(frame_num, entities):
    return 0


def place_pixel(x, y, rgba, image):
    image.putpixel((x, y), rgba)
    return


def change_pixel(max_x, max_y, x, y, rgba, pic):
    if x > max_x or y > max_y or x < 0 or y < 0:
        return
    for val in rgba:
        if val > 255 or val < 0:
            return
    place_pixel(x, y, rgba, pic)
