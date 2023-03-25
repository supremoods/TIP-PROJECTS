import tkinter as tk

def on_button_click(room_id):
    print(f"Button clicked: Room {room_id}")

def create_ui():
    root = tk.Tk()
    root.title("Room Selector")

    # Set a background color for the window
    root.configure(bg="#F7F7F7")

    # Create a grid with 2 columns
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    # Define a custom color for the buttons
    button_color = "#1E88E5"

    for i in range(1, 7):
        button = tk.Button(root, text=f"Room {i}", command=lambda room_id=i: on_button_click(room_id), height=4, width=20, font=("Helvetica", 18), bg=button_color, fg="#FFFFFF", activebackground="#0D47A1", activeforeground="#FFFFFF", bd=0)
        # Use modulo to determine the row and column for each button
        button.grid(row=(i-1)//2, column=(i-1)%2, padx=10, pady=10)

    # Disable window resizing and full screen mode
    root.resizable(False, False)
    root.attributes("-fullscreen", False)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
