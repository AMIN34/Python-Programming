from tkinter import PhotoImage, Tk, Button, Label, Canvas
from tkinter.constants import ANCHOR, CENTER, SE
from speedtest import Speedtest

def update():
    speed_test = Speedtest()
    download_speed = round(speed_test.download() / (10**6), 2)
    upload_speed = round(speed_test.upload() / (10**6), 2)
    down_label.config(text= "Download Speed: - " + str(download_speed) + "Mbps") 
    up_label.config(text= "Upload Speed: - " + str(upload_speed) + "Mbps") 


root = Tk()
root.title("Internet Speed Checker")
root.geometry('400x300')
button = Button(root, text="Get Speed",command=update)
button.pack()
root= Canvas(root, width=150,height=150)
root.pack()
image = PhotoImage(file='E:\\Backup HP\\download.png')
root.create_image(0,0, ANCHOR= SE, image=image)
down_label = Label(root, text="")
down_label.pack()
up_label = Label(root, text="")
up_label.pack()

root.mainloop()