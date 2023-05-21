import customtkinter as ctk

from widget.cam_widget import CamWidget


class WcmApp:
   def a_button_event(self, button_a, button_b):
      button_a.configure(bg_color="#674FFF",border_color="#674FFF")
      button_b.configure(bg_color="transparent")
      
      print("Button A was pressed")
      
   def b_button_event(self, button_a, button_b):
      button_a.configure(bg_color="transparent")
      button_b.configure(bg_color="#674FFF",border_color="#674FFF")
      print("Button B was pressed")
         
   def exit_button_event(self, root):
      root.destroy()


wcmApp = WcmApp()

root = ctk.CTk()
root.geometry("585x371")
root.title("Tech Mobility")

# MAIN WIDGET
main_frame = ctk.CTkFrame(root, fg_color="red", bg_color="red")
main_frame.pack(side="right",fill='both', padx=28, pady=28, expand=True)

# SIDEBAR WIDGET - START

# Creating the sidebar
sidebar = ctk.CTkFrame(root, width=140, height=root.winfo_screenheight(), bg_color="#3A3A3A")
sidebar.pack(side='left', fill='y')

# Creating the title in the sidebar
title_frame = ctk.CTkFrame(sidebar, fg_color="transparent" )
title_frame.pack(pady=30)

# TECHMOBILITY TITLE
font_tech = ctk.CTkFont(family="Inter", size=20, weight="bold")
label_tech = ctk.CTkLabel(title_frame, text="Tech", font=font_tech,text_color="#FFFFFF")
label_tech.pack(side='left')
font_mobility = ctk.CTkFont(family="Inter", size=20, weight="bold")
label_mobility = ctk.CTkLabel(title_frame, text="Mobility", font=font_mobility, text_color="#674FFF")
label_mobility.pack(side='left')

button_a = ctk.CTkButton(sidebar, text="Point A", width=200, height=60, border_width=2, fg_color="transparent", bg_color="transparent", border_color="#3A3A3A", hover=True, command=lambda: wcmApp.a_button_event(button_a, button_b))
button_a.pack()

button_b = ctk.CTkButton(sidebar, text="Point B", width=200, height=60, border_width=2, fg_color="transparent", bg_color="transparent", border_color="#3A3A3A", hover=True, command=lambda: wcmApp.b_button_event(button_a, button_b))
button_b.pack()

exit_button = ctk.CTkButton(sidebar, text="Exit", width=200, height=60,  fg_color="transparent", command=lambda: wcmApp.exit_button_event(root))
exit_button.pack(side='bottom', )
root.mainloop()

# SIDEBAR - END