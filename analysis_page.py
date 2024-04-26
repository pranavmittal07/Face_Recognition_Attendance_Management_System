import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AnalysisPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Analysis")
        self.df = None  # This will hold the DataFrame
        self.bar_canvas = None  # Reference to the bar graph canvas
        self.pie_canvas = None  # Reference to the pie chart canvas


        # top image
        img = Image.open("Images/GUI4.jpeg")
        img = img.resize((1530, 790), Image.LANCZOS)
        self.top = ImageTk.PhotoImage(img)

        top = Label(self.root, image=self.top)
        top.place(x=0, y=0, width=1530, height=790)

        # Title
        title_lbl = Label(self.root, text="ANALYSIS OF STUDENT ATTENDANCE", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=60)

        messagebox.showinfo("Information", "Load the Attendance Excel file to Get Attendance Analysis")

        # Load File Button
        load_button = Button(self.root, text="Load Excel File", font=("times new roman", 18, "bold"), bg="blue", fg="white", command=self.load_excel_file)
        load_button.place(x=150, y=150, height=60, width=200)

        # Analysis Button
        analyze_button = Button(self.root, text=" Individual Analysis ", font=("times new roman", 18, "bold"), bg="blue", fg="white", command=self.analyze_data)
        analyze_button.place(x=600, y=150, height=60, width=200)

        analyze_button = Button(self.root, text=" Collective Analysis ", font=("times new roman", 18, "bold"), bg="blue", fg="white", command=self.pie)
        analyze_button.place(x=1100, y=150, height=60, width=200)

    def load_excel_file(self):
        filename = askopenfilename(
            title="Select an Excel file",
            filetypes=(("Excel files", "*.xlsx *.xls"), ("All files", "*.*"))
        )
        if not filename:
            messagebox.showwarning("Warning", "No file selected.")
            return

        try:
            self.df = pd.read_excel(filename, header=16, index_col=0)
            messagebox.showinfo("Success", "File loaded successfully.")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load the file. Error: {e}")

    def analyze_data(self):
        if self.df is None:
            messagebox.showwarning("Warning", "No data to analyze. Load a file first.")
            return

        if self.df.empty:
            messagebox.showerror("Error", "DataFrame is empty. No rows to count.")
            return

        # Count headers from col=1 to max_column and store in variable total_sessions
        total_sessions = len(self.df.columns) - 1  # Exclude column 0

        if total_sessions <= 0:
            messagebox.showerror("Error", "Insufficient data for analysis.")
            return

        # Store all indexes (column 0 values) in the list X
        X = self.df.iloc[:, 0].tolist()
        Y = self.df.index.tolist()

        # Initialize a list to store row-wise counts
        counts_list = []

        # Count occurrences of 'P' in each row from col=1 to max_column and store in counts_list
        for row_index, row in self.df.iterrows():
            count_p = row.iloc[1:].eq('P').sum()  # Count 'P' occurrences in columns starting from index 1
            counts_list.append(count_p)

        print("Counts of 'P' in each row from col=1 to max_column:")
        print(counts_list)

        # Create a bar graph
        plt.figure(figsize=(16, 6))  # Set the figure size
        bars = plt.bar(range(len(counts_list)), counts_list, color='skyblue')

        # Adding a red line for 75% attendance
        plt.axhline(y=total_sessions * 0.75, color='red', linestyle='--', label='75% Attendance')

        # Marking bars below 75% attendance in yellow
        for i, count in enumerate(counts_list):
            if (count / total_sessions) * 100 < 75:
                bars[i].set_color('yellow')
                plt.text(i, count + 1, f'({X[i]})', ha='center', va='bottom')

            else:
                plt.text(i, count + 1, f'{count}', ha='center', va='bottom')

        plt.xlabel('Scholar ID')  # X-axis label with index values
        plt.ylabel('Attendance Count')  # Y-axis label
        plt.title('Analysis of Student Attendance')  # Title
        plt.xticks(range(len(counts_list)), Y, rotation=45, ha='right')  # Adjust x-axis labels
        plt.legend()  # Show legend
        plt.tight_layout()  # Adjust layout to prevent clipping of labels

        # Remove the pie chart if it exists
        if self.pie_canvas:
            self.pie_canvas.get_tk_widget().destroy()
            self.pie_canvas = None

        # Create a bar graph
        self.bar_canvas = FigureCanvasTkAgg(plt.gcf(), master=self.root)
        self.bar_canvas.draw()
        self.bar_canvas.get_tk_widget().place(x=0, y=250)

    def pie(self):
        if self.df is None:
            messagebox.showwarning("Warning", "No data to analyze. Load a file first.")
            return

        if self.df.empty:
            messagebox.showerror("Error", "DataFrame is empty. No rows to analyze.")
            return

        # Calculate attendance percentages for each student
        total_sessions = len(self.df.columns) - 1
        attendance_percentages = (self.df.iloc[:, 1:].eq('P').sum(axis=1) / total_sessions) * 100

        # Define attendance categories
        categories = ['Above 95%', '85-95%', '75-85%', '65-75%', 'Below 65%']

        # Count students falling into each category
        category_counts = [((attendance_percentages > 95).sum()),
                        ((attendance_percentages.between(85, 95)).sum()),
                        ((attendance_percentages.between(75, 85)).sum()),
                        ((attendance_percentages.between(65, 75)).sum()),
                        ((attendance_percentages < 65).sum())]

        # Calculate total student count
        total_students = sum(category_counts)

        # Create a pie chart
        plt.figure(figsize=(10, 5))
        patches, texts, autotexts = plt.pie(category_counts, labels=categories, autopct='%1.1f%%', startangle=140, colors=['green', 'lightgreen', 'yellow', 'orange', 'red'])
        plt.title('Student Attendance Distribution', fontdict={'fontname': 'Times New Roman', 'fontsize': 30})
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        # Add total count to legend
        total_label = f'Total: {total_students}'
        plt.legend(patches, [f'{l}, {t}' for l, t in zip(categories, category_counts)], loc="upper right", title=total_label)

        if self.bar_canvas:
            self.bar_canvas.get_tk_widget().destroy()
            self.bar_canvas = None

        # Create a pie chart
        self.pie_canvas = FigureCanvasTkAgg(plt.gcf(), master=self.root)
        self.pie_canvas.draw()
        self.pie_canvas.get_tk_widget().place(x=350, y=250)

if __name__ == "__main__":
    root = Tk()
    app = AnalysisPage(root)
    root.mainloop()
