import cv2
from PIL import Image, ImageTk
import customtkinter as ctk


class WcmApp:
    def __init__(self ):
        self.root = None
        self.canvas = None
        self.button_a = None
        self.button_b = None

    def start(self):
        self.root = ctk.CTk()
        self.root.geometry("1280x720")
        self.root.title("Tech Mobility")

        main_frame = ctk.CTkFrame(self.root, fg_color="#3A3A3A", bg_color="#3A3A3A")
        main_frame.pack(side="right", fill='both', padx=28, pady=28, expand=True)

        self.canvas = ctk.CTkCanvas(main_frame, width=600, height=660)
        self.canvas.pack()

        sidebar = ctk.CTkFrame(self.root, width=140, height=self.root.winfo_screenheight(), bg_color="#3A3A3A")
        sidebar.pack(side='left', fill='y')

        title_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        title_frame.pack(pady=30)

        font_tech = ctk.CTkFont(family="Inter", size=20, weight="bold")
        label_tech = ctk.CTkLabel(title_frame, text="Tech", font=font_tech, text_color="#FFFFFF")
        label_tech.pack(side='left')
        font_mobility = ctk.CTkFont(family="Inter", size=20, weight="bold")
        label_mobility = ctk.CTkLabel(title_frame, text="Mobility", font=font_mobility, text_color="#674FFF")
        label_mobility.pack(side='left')

        self.button_a = ctk.CTkButton(sidebar, text="Point A", width=200, height=60, border_width=2,
                                      fg_color="transparent", bg_color="transparent", border_color="#3A3A3A",
                                      hover=True, command=lambda: self.a_button_event())
        self.button_a.pack()

        self.button_b = ctk.CTkButton(sidebar, text="Point B", width=200, height=60, border_width=2,
                                      fg_color="transparent", bg_color="transparent", border_color="#3A3A3A",
                                      hover=True, command=lambda: self.b_button_event())
        self.button_b.pack()

        exit_button = ctk.CTkButton(sidebar, text="Exit", width=200, height=60, fg_color="transparent",
                                    command=lambda: self.exit_button_event())
        exit_button.pack(side='bottom')

        self.root.mainloop()

    def a_button_event(self):
        self.button_a.configure(bg_color="#674FFF", border_color="#674FFF")
        self.button_b.configure(bg_color="transparent")
        print("Button A was pressed")

    def b_button_event(self):
        self.button_a.configure(bg_color="transparent")
        self.button_b.configure(bg_color="#674FFF", border_color="#674FFF")
        print("Button B was pressed")

    def exit_button_event(self):
        self.root.destroy()

    def update_video_feed(self, reqImg):
        frame = cv2.cvtColor( reqImg, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        image = image.resize((600, 660), Image.ANTIALIAS)
        image_tk = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor="nw", image=image_tk)
        self.canvas.image = image_tk
        self.canvas.after(10, self.update_video_feed)



