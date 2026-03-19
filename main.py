import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

img = None
tk_img = None

def upload_image():
    global img, tk_img

    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if not file_path:
        return

    img = Image.open(file_path)

    display_img = img.resize((300, 300))
    tk_img = ImageTk.PhotoImage(display_img)

    panel.config(image=tk_img)


def add_watermark():
    global img, tk_img

    if img is None:
        messagebox.showerror("Error", "Upload image first!")
        return

    text = entry.get()

    if text.strip() == "":
        messagebox.showerror("Error", "Enter watermark text!")
        return

    draw = ImageDraw.Draw(img)

    width, height = img.size

    try:
        font = ImageFont.truetype("arial.ttf", 50)
    except:
        font = ImageFont.load_default()

    # Put watermark in center (so you can SEE it clearly)
    draw.text((width//4, height//2), text, fill=(255, 0, 0), font=font)

    # Update preview
    display_img = img.resize((500, 500))
    tk_img = ImageTk.PhotoImage(display_img)

    panel.config(image=tk_img)


def save_image():
    global img

    if img is None:
        messagebox.showerror("Error", "No image to save!")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".png")

    if file_path:
        img.save(file_path)
        messagebox.showinfo("Success", "Saved!")


# GUI
root = tk.Tk()
root.title("Watermark App")
root.geometry("900x700")

tk.Label(root, text="Watermark Tool", font=("Arial", 18)).pack(pady=10)

tk.Button(root, text="Upload Image", command=upload_image).pack(pady=10)

panel = tk.Label(root)
panel.pack()

entry = tk.Entry(root, width=30)
entry.pack(pady=10)
entry.insert(0, "TEST")

tk.Button(root, text="Add Watermark", command=add_watermark).pack(pady=10)

tk.Button(root, text="Save Image", command=save_image).pack(pady=10)

root.mainloop()