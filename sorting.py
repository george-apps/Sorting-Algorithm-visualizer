from bubble_sort import bubble_sort
from quickSort import quick_sort
from mergeSort import merge_sort
from insertionSort import insertion_sort
from selectionSort import selection_sort
from tkinter import *
from tkinter import ttk
import random


data=[]


def center_screen(win):
    win.update_idletasks()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    win.geometry(f"{window_width}x{window_height}+{ x_cordinate}+{y_cordinate}")


def generate():
    global data
    data=[]

    for _ in range(20):
        data.append(random.randint(5,100))

    draw(data=data,color=['green' for x in range(len(data))])


def draw(data,color):
    canvas.delete("all")
    canvas_width = 750
    canvas_height = 600
    x_width = canvas_width / (len(data) + 1 )
    offset=10
    space_between_rect=10

    for i,height in enumerate(data):
        x0= i * x_width + offset + space_between_rect
        y0= canvas_height - height * 5

        x1= (i+1) * x_width - 30
        y1= canvas_height

        canvas.create_rectangle(x0,y0,x1,y1,fill=color[i])
        canvas.create_text(x0+1,y0,anchor=S,text=str(data[i]),font=("Arial",16,"bold"),fill="orange")

    root.update_idletasks()


def startAlgo():
    global data
    if not data:
        return

    if selected_algo.get().lower() == "bubble sort":
        bubble_sort(data,draw)

    elif selected_algo.get().lower() == "merge sort":
        merge_sort(data,draw)

    elif selected_algo.get().lower() == "quick sort":
        quick_sort(data,0,len(data)-1,draw)

    elif selected_algo.get().lower() == "insertion sort":
        insertion_sort(data,draw)

    elif selected_algo.get().lower() == "selection sort":
        selection_sort(data,draw)

    draw(data,['green' for x in range(len(data))])


def clear():
    canvas.delete("all")


root=Tk()
root.title("Sorting Visualizer")
window_height = 750
window_width = 900
root.config(bg="#373e75")

mainLabel=ttk.Label(root,text="Algorithm: ",font=("Arial",16,"bold"),width=10,relief="solid",background="#4e788a",foreground="white")
mainLabel.place(x=0, y=0)

selected_algo=StringVar()
algorithm_menu=ttk.Combobox(root,width=10,state="readonly", font=("Arial",16,"bold"),textvariable=selected_algo, values=['Merge Sort','Bubble Sort','Quick Sort','Insertion Sort','Selection Sort'])
algorithm_menu.place(x=140, y=0)
algorithm_menu.current(0)

random_btn=Button(root,text="Generate",font=("Arial",16,"bold"),relief="solid",width=10,activebackground="#ac93bf",activeforeground="white",command=generate)
random_btn.place(x=390,y=0)

start_btn=Button(root,text="Start",font=("Arial",16,"bold"),relief="solid",width=10,activebackground="#ac93bf",activeforeground="white",command=startAlgo)
start_btn.place(x=560,y=0)

clear_btn=Button(root,text="Clear",font=("Arial",16,"bold"),relief="solid",width=10,activebackground="#ac93bf",activeforeground="white",command=clear)
clear_btn.place(x=730,y=0)

canvas = Canvas(root,width=750,height=600,bg="black")
canvas.place(x=75,y=100)



center_screen(root)
root.mainloop()

