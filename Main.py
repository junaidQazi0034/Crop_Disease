from atexit import register
import os
from tkinter import *
from tkinter import font
from tkinter import filedialog
from PIL import Image, ImageTk
from turtle import width
from tkinter import messagebox
from click import command
import mysql.connector


def addDisease():
    try:
        # Convert the image to binary data
        image_binary = selected_image.tobytes()
        dbCon = mysql.connector.connect(
            host="localhost", user="root", password="", database="db_cropdisease")
        query = "INSERT INTO diseases (name,type,pic) VALUES(%s, %s, %s) "
        queryParameters = [diseaseName.get().strip(),
                           diseaseType.get(), image_binary]
        queryCursor = dbCon.cursor()
        queryCursor.execute(query, queryParameters)
        dbCon.commit()
        messagebox.showinfo("Success", "Data inserted successfully")
        diseaseName.delete(0, END)
        diseaseType.delete(0, END)
        # image_label.config(image=None)
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", e)


def dataValidation():
    if not selected_image:
        messagebox.showerror("Select Image", "Select an image file")
    elif diseaseName.get().strip() == "" or diseaseType.get() == "":
        messagebox.showerror("Fields are empty", "Fill all the fields")
    else:
        addDisease()


def open_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
        global selected_image
        selected_image = image


win = Tk()
win.title("Crop Disease Detection system (Prototype)")
win.geometry("800x600+350+50")
win.resizable(False, False)
win.config(bg="#FFFDA2")

mainTitle = Label(win, text="Disease Data Entry", bg="#FFFDA2",
                  fg="black", font=("Arial Black", 28))
mainTitle.place(x=100, y=50)

Label(win, text="Disease Name", bg="#FFFDA2",
      font=('courier', 18)).place(x=50, y=195)
diseaseName = Entry(win, font=("arial", 18))
diseaseName.place(x=300, y=190, height=50, width=400)

Label(win, text="Disease Type", bg="#FFFDA2",
      font=('courier', 18)).place(x=50, y=305)
diseaseType = Entry(win, font=("arial", 18))
diseaseType.place(x=300, y=295, height=50, width=400)
# Create a button to open the file dialog
upload_button = Button(win, text="Upload Image", command=open_image,
                       bg="#00A19D", fg="black", width=16, font=("arial", 16))
upload_button.place(x=200, y=370)

b1 = Button(win, text="Submit", command=dataValidation,
            bg="#00A19D", fg="black", width=16, font=("arial", 16))
b1.place(x=450, y=370)

# Create a label to display the uploaded image
image_label = Label(win)
image_label.place(x=5, y=410)

# Initialize the selected_image variable
selected_image = None

win.mainloop()
