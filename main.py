import cv2
from pyzbar.pyzbar import decode
from PIL import Image, ImageTk
import tkinter as tk
from utils.big_c import Big_C
from utils.all_online import All_Online

barcode_detected = False

big_c = Big_C()
all_online = All_Online()


def show_price_screen(canvas: tk.Canvas, product_code: str):
    global barcode_detected
    barcode_detected = True

    canvas.delete("all")
    price = all_online.get_price_and_product_title_from_7_11(product_code)

    canvas.create_text(320, 240, text=price, font=("Arial", 24), fill="red")

    button = tk.Button(root, text="Scan Another",
                       command=lambda: reset_camera_view(video_capture, canvas))
    button_window = canvas.create_window(
        320, 320, anchor=tk.CENTER, window=button)


def detect_and_display_barcode(frame: tk.Frame, canvas: tk.Canvas):
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Decode barcodes
    decoded_objects = decode(image)
    if decoded_objects:
        for obj in decoded_objects:
            product_code = obj.data.decode('utf-8')
            print(product_code)
            show_price_screen(canvas, product_code)
        return
    else:
        # Convert image to ImageTk and display it
        image_tk = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
        canvas.image = image_tk

    # Update GUI if no barcode detected
    if not barcode_detected:
        root.after(10, update_frame, video_capture, canvas)


def update_frame(video_capture: cv2.VideoCapture, canvas: tk.Canvas):
    if not barcode_detected:
        ret, frame = video_capture.read()
        if ret:
            detect_and_display_barcode(frame, canvas)


def reset_camera_view(video_capture: cv2.VideoCapture, canvas: tk.Canvas):
    global barcode_detected
    barcode_detected = False
    canvas.delete("all")
    update_frame(video_capture, canvas)


# Set up GUI
if __name__ == "__main__":

    root = tk.Tk()
    root.title("Barcode Detection")

    canvas = tk.Canvas(root, width=640, height=480)
    canvas.pack()

    video_capture = cv2.VideoCapture(0)

    update_frame(video_capture, canvas)

    root.mainloop()
    video_capture.release()
