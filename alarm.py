from tkinter.ttk import *
from tkinter import *

from pygame import mixer
from datetime import datetime
from time import sleep

from threading import Thread


#colors
bg_color= '#ffffff'
col1= '#566FC6'
col2 = '#000000'

#window
window = Tk()
window.title("")
window.geometry("350x150")
window.configure(bg=bg_color)

#frames
frame_line = Frame(window,width=400,height=5,bg=col1)
frame_line.grid(row=0,column=0)

frame_body = Frame(window,width=400,height=290,bg=bg_color)
frame_body.grid(row=1,column=0)

name = Label(frame_body, text='ALARM', height=1,font=('Ivy 19 bold'),bg=bg_color)
name.place(x=130,y=10)

hour = Label(frame_body, text='HOUR', height=1,font=('Ivy 10 bold'),bg=bg_color,fg=col1)
hour.place(x=82,y=45)
c_hour=Combobox(frame_body,width=2,font=('arial 15'))
c_hour['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12")
c_hour.current(0)
c_hour.place(x=80,y=63)

min = Label(frame_body, text='MIN', height=1,font=('Ivy 10 bold'),bg=bg_color,fg=col1)
min.place(x=136,y=45)
c_min=Combobox(frame_body,width=2,font=('arial 15'))
c_min['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30',
                   '31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60')
c_min.current(0)
c_min.place(x=130,y=63)

sec = Label(frame_body, text='SEC', height=1,font=('Ivy 10 bold'),bg=bg_color,fg=col1)
sec.place(x=186,y=45)
c_sec=Combobox(frame_body,width=2,font=('arial 15'))
c_sec['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30',
                   '31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60')
c_sec.current(0)
c_sec.place(x=180,y=63)

period = Label(frame_body, text='PERIOD', height=1,font=('Ivy 10 bold'),bg=bg_color,fg=col1)
period.place(x=232,y=45)
c_period=Combobox(frame_body,width=3,font=('arial 15'))
c_period['values'] = ('AM','PM')
c_period.current(0)
c_period.place(x=230,y=63)


def activate_alarm():

    t = Thread(target=alarm)
    t.start()

def deactivate_alarm():
    # print("deactivate alarm:",selected.get())
    mixer.music.stop()


selected = IntVar()

rad1=Radiobutton(frame_body,font=('arial 10 bold'),value=1,text="Activate",bg=bg_color,command=activate_alarm,variable=selected)
rad1.place(x=100,y=95)

def sound_alarm():
    mixer.music.load('alarm_sound.mp3')
    mixer.music.play()
    selected.set(0)

    rad2=Radiobutton(frame_body,font=('arial 10 bold'),value=2,text="Deactivate",bg=bg_color,command=deactivate_alarm,variable=selected)
    rad2.place(x=180,y=95)

def alarm():
    while True:
        control = selected.get()
        # print(control)
        
        alarm_hour=c_hour.get()
        alarm_minute=c_min.get()
        alarm_second=c_sec.get()
        alarm_period=c_period.get()
        alarm_period=str(alarm_period).upper()

        now = datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_second == second:

                            print("Time to take the break")
                            sound_alarm()

        sleep(1)     


mixer.init()

window.mainloop()