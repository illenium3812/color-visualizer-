import tkinter as tk
from tkinter.colorchooser import askcolor
import tkinter as tk
from tkinter import filedialog as fd
import cv2
import PIL
import tkinter as tkk
from tkinter import filedialog as fd
from PIL import Image, ImageDraw
from PIL import ImageFilter


def change_color():
    # display colors to users and get the selected color
    global COLOR
    COLOR = askcolor(title="Tkinter Color Chooser")
    COLOR = COLOR[0]


class DrawLineWidget(object):
    def __init__(self):
        self.image_name = fd.askopenfilename()
        self.original_image = cv2.imread(self.image_name)
        self.clone = self.original_image.copy()

        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.extract_coordinates)

        # List to store start/end points
        self.image_coordinates = []

    def extract_coordinates(self, event, x, y, flags, parameters):
        # Record starting (x,y) coordinates on left mouse button click
        if event == cv2.EVENT_LBUTTONDOWN:
            self.image_coordinates = [(x, y)]

        # Record ending (x,y) coordintes on left mouse bottom release
        elif event == cv2.EVENT_LBUTTONUP:
            self.image_coordinates.append((x, y))
            print(
                "Starting: {}, Ending: {}".format(
                    self.image_coordinates[0], self.image_coordinates[1]
                )
            )
            global REFERENCE_LENGTH
            REFERENCE_LENGTH = abs(
                self.image_coordinates[0][1] - self.image_coordinates[1][1]
            )
            cv2.line(
                self.clone,
                self.image_coordinates[0],
                self.image_coordinates[1],
                (36, 255, 12),
                2,
            )
            cv2.imshow("image", self.clone)
        # Clear drawing boxes on right mouse button click
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.clone = self.original_image.copy()

    def show_image(self):
        return self.clone


def get_reference_length():
    draw_line_widget = DrawLineWidget()
    while True:
        cv2.imshow("image", draw_line_widget.show_image())
        key = cv2.waitKey(1)

        # Close program with keyboard 'q'
        if key == ord("q"):
            cv2.destroyAllWindows()
            break
    conversion_unit = float(input("Enter length in cms:"))
    per_pixel = conversion_unit / REFERENCE_LENGTH
    per_pixel = per_pixel * per_pixel
    print("Painted Area: ", per_pixel * NUMBER_OF_PIXEL_PAINTED, "Meters square")


def main():
    global THRESHOLD
    THRESHOLD = v1.get()

    global TOLERANCE
    TOLERANCE = v2.get()

    def get_pixel_distance(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            pos1 = (x, y)
        if event == cv2.EVENT_LBUTTONDOWN:
            pos2 = (x, y)
        pixel_distance = abs(pos1[1] - pos2[1])
        return pixel_distance

    def click_event(event, x, y, flags, params):
        # checking for left mouse clicks
        if event == cv2.EVENT_LBUTTONDOWN:

            # COLOR = (255,0,0)

            # displaying the coordinates
            # on the Shell
            print(x, " ", y)
            pos = (x, y)
            ImageDraw.floodfill(edge, pos, COLOR, thresh=TOLERANCE)
            edge.show()
            # displaying the coordinates
            # on the image window
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, str(x) + "," + str(y), (x, y), font, 1, (255, 0, 0), 2)

            cv2.imshow("image", img)

    imageName = fd.askopenfilename()
    img = cv2.imread(imageName)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    while True:
        edge = cv2.Canny(gray, 25, THRESHOLD)
        cv2.imwrite("edge.jpg", edge)
        edge = PIL.Image.open("edge.jpg")
        edge = edge.convert("RGB")
        cv2.imshow("image", img)
        while True:
            cv2.setMouseCallback("image", click_event)
            if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()
                break
        img = PIL.Image.open(imageName)
        PIL.Image.blend(img, edge, 1).show()
        edge.save("edge.jpg")
        break

    img = PIL.Image.open("edge.jpg")
    pix = img.load()
    s = img.size
    for i in range(s[0]):
        for j in range(s[1]):
            if pix[i, j][0] > 200 and pix[i, j][1] > 200 and pix[i, j][2] > 200:
                pix[i, j] = (0, 0, 0)
            else:
                pass

    img.save("mask.png")

    # Blending
    img = PIL.Image.open("mask.png")
    img = img.filter(ImageFilter.MinFilter(3))
    img = img.filter(ImageFilter.MaxFilter(9))
    img.save("mask.png")

    img = PIL.Image.open("mask.png")
    pix = img.load()
    s = img.size
    global NUMBER_OF_PIXEL_PAINTED
    for i in range(s[0]):
        for j in range(s[1]):
            if pix[i, j][0] < 40 and pix[i, j][1] < 40 and pix[i, j][2] < 40:
                pix[i, j] = (0, 0, 0)
            else:
                NUMBER_OF_PIXEL_PAINTED += 1
                pix[i, j] = COLOR

    img.save("mask.png")
    print(NUMBER_OF_PIXEL_PAINTED)

    img1 = cv2.imread("mask.png")
    img2 = cv2.imread(imageName)
    dst = cv2.addWeighted(img1, 1, img2, 1, -50)
    cv2.imwrite("results.jpg", dst)
    cv2.imshow("Blended Image", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    REFERENCE_LENGTH = 0
    NUMBER_OF_PIXEL_PAINTED = 0
    root = tk.Tk()
    root.title("Color Visuliser")
    root.geometry("600x300")

    from tkinter import *

    v1 = DoubleVar()
    v1.set(100)
    v2 = DoubleVar()
    v2.set(5)

    COLOR = 0
    THRESHOLD = 0
    TOLERANCE = 0

    s1 = Scale(root, variable=v1, from_=1, to=5000, orient=HORIZONTAL)
    s2 = Scale(root, variable=v2, from_=1, to=100, orient=HORIZONTAL)

    l3 = Label(root, text="Edge Threshold (Default = 100)")
    l4 = Label(root, text="Color Fill Tolerance (Default = 5)")

    b1 = Button(root, text="Pick Color", command=change_color, bg="yellow")

    b2 = Button(root, text="Open Image", command=main, bg="green")

    b3 = Button(root, text="Set Reference Length", command=get_reference_length)

    l1 = Label(root)

    s1.pack(anchor=CENTER)
    l3.pack()
    s2.pack(anchor=CENTER)
    l4.pack()

    b1.pack(anchor=CENTER, expand=True)
    b2.pack(anchor=CENTER, expand=True)
    b3.pack(anchor=CENTER, expand=True)
    l1.pack()

    root.mainloop()
