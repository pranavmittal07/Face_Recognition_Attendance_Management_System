# 🎓 Face Recognition Attendance Management System

An AI-powered solution for automating student attendance using facial recognition.
![start](Images/Screenshot%20(14).png)
---

## 📌 Implementation Overview

The system is divided into **three core functionalities**:
![2nd Page](Images/Screenshot%20(15).png)
---

### 1. 📝 Registration Functionality

**📄 Description:**  
Captures and stores images of students, encoding their facial data for future recognition during attendance marking.

**🛠 Technologies Used:**
- **OpenCV (cv2):** Captures images via webcam.
- **face_recognition:** Encodes facial features for later matching.
- **Tkinter:** Builds the GUI for registering new students.

**🔁 Workflow:**
1. Capture images of students using the webcam.
2. Recognize and encode faces using `face_recognition`.
3. Save encoded face data along with student information in the database.

![3th Page](Images/Screenshot%20(16).png)
---

### 2. ✅ Mark Attendance Functionality

**📄 Description:**  
Automatically marks attendance by comparing real-time faces with previously registered student data.

**🛠 Technologies Used:**
- **OpenCV (cv2):** Captures live images during classes.
- **face_recognition:** Matches faces with stored encodings.
- **Tkinter:** GUI for selecting course details and managing attendance.
- **Pandas, OpenPyXL:** Stores attendance records in Excel format.

**🔁 Workflow:**
1. Capture live video feed during class sessions.
2. Recognize and match faces against registered students.
3. Prompt user for course details (e.g., subject, teacher name).
4. Log attendance in an Excel file based on matched identities.

![4th Page](Images/Screenshot%20(17).png)
---

### 3. 📊 Attendance Analysis Functionality

**📄 Description:**  
Visualizes attendance patterns and trends using graphical reports.

**🛠 Technologies Used:**
- **Tkinter:** GUI for interacting with analysis tools.
- **Pandas, Matplotlib:** Analyzes and visualizes attendance data.
- **PIL (Pillow):** Displays images within the GUI.

**🔁 Workflow:**
1. Load attendance records using Pandas.
2. Analyze attendance frequency and trends.
3. Generate visual graphs (e.g., bar charts) with Matplotlib.
4. Display visualizations interactively in the GUI.

![5th Page](Images/Screenshot%20(18).png)
![6th Page](Images/Screenshot%20(30).png)
---

## 📂 Summary

This system leverages **face recognition technology** to streamline attendance management, offering:
- Easy student registration,
- Automated, real-time attendance logging,
- Insightful visual analytics.

Built using **Python**, this project integrates **computer vision**, **data processing**, and **GUI development** to offer a seamless and intelligent attendance solution.
