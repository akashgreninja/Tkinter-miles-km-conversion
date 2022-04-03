from tkinter import *

window=Tk()

window.title("my first")
window.minsize(width=500,height=300)
window.config(padx=120,pady=40)

def on_click():
    print("clicked")

    a=float(input.get())

    c=a*1.60934
    # print(f"{a}")
    my_label_3.config(text=f"{c}")

my_label=Label(text=f"Miles",font=("Arial",12,"bold"))
my_label.grid(column=4,row=3)

my_label_2=Label(text=f"is equal to ",font=("Arial",12,"bold"))
my_label_2.grid(column=1,row=4)

my_label_3=Label(text=f"0 ",font=("Arial",12,"bold"))
my_label_3.grid(column=3,row=4)

my_label_4=Label(text=f"Km ",font=("Arial",12,"bold"))
my_label_4.grid(column=4,row=4)

input=Entry(width=20)
print(input.get())
input.grid(column=3,row=3)



button=Button(text="new onw",command=on_click)
button.grid(column=3,row=5)



window.mainloop()





