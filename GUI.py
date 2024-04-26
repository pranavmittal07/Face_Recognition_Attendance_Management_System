from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Load background image
        img = Image.open(r"Images\bg.png")
        img = img.resize((1530, 790), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(img)

        # Background label
        self.bg_label = Label(self.root, image=self.bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Start button
        start_btn = Button(self.root, text="Start", command=self.open_second_page, font=("times new roman", 15, "bold"), bg="red", fg="white", cursor="hand2")
        start_btn.place(x=300, y=550, width=220, height=40)

    def open_second_page(self):
        # Hide the current window
        self.root.withdraw()

        # Create a new window for the second page
        second_page = Toplevel(self.root)
        SecondPage(second_page)

from registration_page import RegistrationPage
from mark_attendance_page import MarkAttendancePage
from analysis_page import AnalysisPage

class SecondPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        # Load background image
        img = Image.open(r"Images\secondPage.jpeg")  # Ensure this path is correct
        img = img.resize((1530, 790), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(img)

        # Background label
        self.bg_label = Label(self.root, image=self.bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Heading
        heading_label = Label(self.root, text="Face Recognition Attendance System", font=("Arial", 24, "bold"), bg="white")
        heading_label.pack(side=TOP, fill=X)

        # Registration Button
        img_reg = Image.open(r"Images\GUI1.jpeg")  # Adjust this path
        img_reg = img_reg.resize((420, 300), Image.LANCZOS)
        self.photoimg_reg = ImageTk.PhotoImage(img_reg)

        reg_btn_image = Button(self.root, image=self.photoimg_reg, cursor="hand2", bd=0, command=self.open_registration_page)
        reg_btn_image.place(x=75, y=150, width=450, height=350)

        reg_btn_text = Button(self.root, text="Registration", cursor="hand2", font=("times new roman", 15, "bold"), bg="Dark Blue", fg="white", command=self.open_registration_page)
        reg_btn_text.place(x=75, y=500, width=450, height=40)

        # Mark Attendance Button
        img_mark = Image.open(r"Images\GUI2.jpeg")  # Adjust this path
        img_mark = img_mark.resize((420, 300), Image.LANCZOS)
        self.photoimg_mark = ImageTk.PhotoImage(img_mark)

        mark_btn_image = Button(self.root, image=self.photoimg_mark, cursor="hand2", bd=0, command=self.open_mark_attendance_page)
        mark_btn_image.place(x=540, y=150, width=450, height=350)

        mark_btn_text = Button(self.root, text="Mark Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="Dark Blue", fg="white", command=self.open_mark_attendance_page)
        mark_btn_text.place(x=540, y=500, width=450, height=40)

        # Analysis Button
        img_analysis = Image.open(r"Images\GUI4.jpeg")  # Adjust this path
        img_analysis = img_analysis.resize((420, 300), Image.LANCZOS)
        self.photoimg_analysis = ImageTk.PhotoImage(img_analysis)

        analysis_btn_image = Button(self.root, image=self.photoimg_analysis, cursor="hand2", bd=0, command=self.open_analysis_page)
        analysis_btn_image.place(x=1000, y=150, width=450, height=350)

        analysis_btn_text = Button(self.root, text="Analysis", cursor="hand2", font=("times new roman", 15, "bold"), bg="Dark Blue", fg="white", command=self.open_analysis_page)
        analysis_btn_text.place(x=1000, y=500, width=450, height=40)

    def open_registration_page(self):
        registration_root = Toplevel()
        registration_page = RegistrationPage(registration_root)

    def open_mark_attendance_page(self):
        mark_attendance_root = Toplevel()
        mark_attendance_page = MarkAttendancePage(mark_attendance_root)

    def open_analysis_page(self):
        analysis_root = Toplevel()
        analysis_page = AnalysisPage(analysis_root)

if __name__ == "__main__":
    root = Tk()
    app = FaceRecognitionSystem(root)
    root.mainloop()
