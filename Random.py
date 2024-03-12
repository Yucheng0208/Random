import tkinter as tk
from PIL import ImageTk, Image
import random

class LotteryApp:
    def __init__(self, numbers):
        self.numbers = numbers
        self.drawn_numbers = []
        self.students = {
            1: {"name": "John", "photo": "john.jpg"},
            2: {"name": "Emily", "photo": "emily.jpg"},
            3: {"name": "Michael", "photo": "michael.jpg"},
            # Add more students here
        }

        self.window = tk.Tk()
        self.window.title("抽籤軟體")
        self.window.geometry("400x300")  # Set the window size

        self.label = tk.Label(self.window, text="按下按鈕抽籤")
        self.label.pack()

        self.name_entry = tk.Entry(self.window)  # Add an entry widget for student name
        self.name_entry.pack()

        self.button = tk.Button(self.window, text="抽籤", command=self.draw)
        self.button.pack()

        self.reset_button = tk.Button(self.window, text="重置", command=self.reset)
        self.reset_button.pack()

        self.photo_label = tk.Label(self.window)
        self.photo_label.pack()

        self.window.mainloop()

    def draw(self):
        if len(self.drawn_numbers) == len(self.numbers):
            self.label.config(text="已經抽完所有號碼")
            self.button.config(state=tk.DISABLED)
        else:
            remaining_numbers = list(set(self.numbers) - set(self.drawn_numbers))
            number = random.choice(remaining_numbers)
            self.drawn_numbers.append(number)
            student = self.students[number]
            name = self.name_entry.get()  # Get the entered student name
            self.label.config(text=f"抽到的號碼是: {number}，姓名是: {name}")
            self.display_photo(student["photo"])

    def reset(self):
        self.drawn_numbers = []
        self.button.config(state=tk.NORMAL)
        self.label.config(text="按下按鈕抽籤")
        self.name_entry.delete(0, tk.END)
        self.photo_label.config(image=None)

    def display_photo(self, photo_path):
        image = Image.open(photo_path)
        image = image.resize((200, 200))  # Resize the image
        photo = ImageTk.PhotoImage(image)
        self.photo_label.config(image=photo)
        self.photo_label.image = photo

# 使用範例
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
app = LotteryApp(numbers)
