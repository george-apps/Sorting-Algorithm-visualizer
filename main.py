from bubble_sort import bubble_sort
from quickSort import quick_sort
from mergeSort import merge_sort
from insertionSort import insertion_sort
from selectionSort import selection_sort
from tkinter import *
from tkinter import ttk
import random


class App:

    def __init__(self,master):
        self.root=master
        self.center_app()
        self.root.title("Sorting Visualizer")
        self.root.config(bg="#373e75")
        self.create_gui()
        self.data=[]

    def create_gui(self):
        self.create_labels()
        self.create_btns()
        self.create_combo()
        self.create_canvas()

    def create_labels(self):
        self.mainLabel = ttk.Label(self.root, text="Algorithm: ", font=("Arial", 16, "bold"), width=10, relief="solid", background="#4e788a", foreground="white")
        self.mainLabel.place(x=0, y=0)

    def create_combo(self):
        self.selected_algo = StringVar()
        self.algorithm_menu = ttk.Combobox(self.root, width=12, state="readonly", font=("Arial", 16, "bold"), textvariable=self.selected_algo,
                                      values=['Merge Sort', 'Bubble Sort', 'Quick Sort', 'Insertion Sort', 'Selection Sort'])
        self.algorithm_menu.place(x=140, y=0)
        self.algorithm_menu.current(0)

    def create_btns(self):
        self.generate_btn = Button(self.root, text="Generate", font=("Arial", 16, "bold"), relief="solid", width=10, activebackground="#ac93bf",
                            activeforeground="white", command=self.generate)
        self.generate_btn.place(x=390, y=0)

        self.start_btn = Button(self.root, text="Start", font=("Arial", 16, "bold"), relief="solid", width=10, activebackground="#ac93bf",
                           activeforeground="white", command=self.start_algo)
        self.start_btn.place(x=560, y=0)

        self.clear_btn = Button(self.root, text="Clear", font=("Arial", 16, "bold"), relief="solid", width=10, activebackground="#ac93bf",
                           activeforeground="white", command=self.clear)
        self.clear_btn.place(x=730, y=0)

    def create_canvas(self):
        self.canvas = Canvas(self.root, width=750, height=600, bg="black")
        self.canvas.place(x=75, y=100)

    def center_app(self):
        self.app_width = 900
        self.app_height = 750
        self.screen_width = window.winfo_screenwidth()
        self.screen_height = window.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.app_width / 2)
        self.y = (self.screen_height / 2) - (self.app_height / 2)
        self.root.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')

##############################################################################################

    def generate(self):
        self.data = []

        for _ in range(20):
            self.data.append(random.randint(5, 100))

        self.draw(data=self.data, color=['green' for x in range(len(self.data))])

    def draw(self,data, color):
        self.canvas.delete("all")
        canvas_width = 750
        canvas_height = 600
        x_width = canvas_width / (len(data) + 1)
        offset = 10
        space_between_rect = 10

        for i, height in enumerate(data):
            x0 = i * x_width + offset + space_between_rect
            y0 = canvas_height - height * 5

            x1 = (i + 1) * x_width - 30
            y1 = canvas_height

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
            self.canvas.create_text(x0 + 1, y0, anchor=S, text=str(data[i]), font=("Arial", 16, "bold"), fill="orange")

        self.root.update_idletasks()

    def start_algo(self):
        if not self.data:
            return

        if self.selected_algo.get().lower() == "bubble sort":
            bubble_sort(self.data,self.draw)

        elif self.selected_algo.get().lower() == "merge sort":
            merge_sort(self.data,self.draw)

        elif self.selected_algo.get().lower() == "quick sort":
            quick_sort(self.data,0,len(self.data)-1,self.draw)

        elif self.selected_algo.get().lower() == "insertion sort":
            insertion_sort(self.data,self.draw)

        elif self.selected_algo.get().lower() == "selection sort":
            selection_sort(self.data,self.draw)

        self.draw(self.data,['green' for x in range(len(self.data))])

    def clear(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    window = Tk()
    window.resizable(False, False)
    App(window)
    window.mainloop()