import tkinter as tk
import cv2 as cv
from PIL import ImageTk, Image

class CamWidget(tk.Frame):
    def __init__(self, img, parent, width=480, height=360, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.width = width
        self.height = height
        self.cv_frame = tk.Label(self, width=self.width, height=self.height)
        self.cv_frame.pack()
        self.cap = cv.VideoCapture(0)
        self.update_video_feed()

    def update_video_feed(self):
        _, frame = self.cap.read()  # Read a frame from the camera
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)  # Convert frame colors from BGR to RGB
        image = Image.fromarray(frame)  # Create an Image object from the frame
        image = image.resize((self.width, self.height), Image.ANTIALIAS)  # Resize the image
        photo = ImageTk.PhotoImage(image)  # Convert the Image object to PhotoImage
        self.cv_frame.configure(image=photo)  # Set the image in the Label
        self.cv_frame.image = photo  # Store a reference to the image to prevent garbage collection
        self.cv_frame.after(10, self.update_video_feed)  # Schedule the next update
