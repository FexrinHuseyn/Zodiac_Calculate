from tkinter import  *

#Screen
window=Tk()
Background="#CCD1DB"
color1="#021B76"
window.title("Zodiac Calculate")
window.minsize(width=500,height=500)
window.config(bg=Background,)

#Button
def clickbutton():
    year=float(my_spinbox1.get())
    month=float(my_spinbox2.get())
    day=float(my_spinbox3.get())
    if year=="" or float(month)==0 or day==0:
        resultlabel.config(text="Please enter Birthday")
    elif day>21 and month==12:
        resultlabel.config(text="Your zodiac is Capricorn")
    elif day<22 and month==12:
        resultlabel.config(text="Your zodiac is Sagittarius")
    elif day>19 and month==1:
        resultlabel.config(text="Your zodiac is Aquarius")
    elif day<20 and month==1:
        resultlabel.config(text="Your zodiac is Capricorn")
    elif day>18 and month==2:
        resultlabel.config(text="Your zodiac is Pisces")
    elif day<19 and month==2:
        resultlabel.config(text="Your zodiac is Aquarius")
    elif day<21 and month==3:
        resultlabel.config(text="Your zodiac is Pisces")
    elif day>20 and month==3:
        resultlabel.config(text="Your zodiac is Aries")
    elif day<20 and month==4:
        resultlabel.config(text="Your zodiac is Aries")
    elif day>19 and month==4:
        resultlabel.config(text="Your zodiac is Taurus")
    elif day<21 and month==5:
        resultlabel.config(text="Your zodiac is Taurus")
    elif day>20 and month==5:
        resultlabel.config(text="Your zodiac is Gemini")
    elif day<22 and month==6:
        resultlabel.config(text="Your zodiac is Gemini")
    elif day>21 and month==6:
        resultlabel.config(text="Your zodiac is Cancer")
    elif day<23 and month==7:
        resultlabel.config(text="Your zodiac is Cancer")
    elif day>22 and month==7:
        resultlabel.config(text="Your zodiac is Leo")
    elif day<23 and month==8:
        resultlabel.config(text="Your zodiac is Leo")
    elif day>22 and month==8:
        resultlabel.config(text="Your zodiac is Virgo")
    elif day<23 and month==9:
        resultlabel.config(text="Your zodiac is Virgo")
    elif day>22 and month==9:
        resultlabel.config(text="Your zodiac is Libra")
    elif day<23 and month==10:
        resultlabel.config(text="Your zodiac is Libra")
    elif day>22 and month==10:
        resultlabel.config(text="Your zodiac is Scorpio")
    elif day<22 and month==11:
        resultlabel.config(text="Your zodiac is Scorpio")
    elif day>21 and month==11:
        resultlabel.config(text="Your zodiac is Sagittarius")



button1=Button(text="Result",bg="#95ABFA",width=20,font=("Lucida Sans",10,'normal'),command=clickbutton)
button1.place(x=180,y=220)



# Label
label1=Label(text="Find Your Zodiac")
label1.config(bg=Background,font=("Impact",40,'normal'),fg=("#858FB4"))
label1.pack()

label2=Label(text="Please enter your Birthday")
label2.config(bg=Background,font=("Impact",20,'normal'),fg=("#858FB4"))
label2.place(x=100,y=75)

label3=Label(text="Year:")
label3.config(bg=Background,font=("Impact",12,'normal'),fg=color1)
label3.place(x=180,y=115)

label4=Label(text="Month:")
label4.config(bg=Background,font=("Impact",12,'normal'),fg=color1)
label4.place(x=170,y=145)

label5=Label(text="Day:")
label5.config(bg=Background,font=("Impact",12,'normal'),fg=color1)
label5.place(x=185,y=175)


resultlabel=Label(width=30)
resultlabel.place(x=155,y=260)

#spinbox
my_spinbox1=Spinbox(from_=1980,to=2024)
my_spinbox1.config(width=15,fg=color1)
my_spinbox1.place(x=220,y=120)


my_spinbox2=Spinbox(from_=0,to=12)
my_spinbox2.config(width=15,fg=color1)
my_spinbox2.place(x=220,y=150)


my_spinbox3=Spinbox(from_=0,to=31)
my_spinbox3.config(width=15,fg=color1)
my_spinbox3.place(x=220,y=180)










































window.mainloop()