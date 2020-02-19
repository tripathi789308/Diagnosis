from tkinter import *
from pandas import *
df=read_json("DataSet.json")
quote="""
1).Avoid alcohol
  May be harmful and aggravate certain conditions.
2).Reduce caffeine intake
  Reduces risk of aggravating certain conditions.
3).Physical exercise
  Aerobic activity for 20–30 minutes 5 days a week improves cardiovascular health.
  If injured, pursuing an activity that avoids
  the injured muscle group or joint can help maintain physical function while recovering.
4).Stress management
  Pursuing an enjoyable activity or verbalising frustration to reduce stress and
  improve mental health.
5).Quitting smoking
  Quitting smoking tobacco.
6).Relaxation techniques
  Deep breathing, meditation, yoga, rhythmic exercise and other activities that
  reduce symptoms of stress
7).Healthy diet
  A diet that provides essential nutrients and adequate calories,
  while avoiding excess sugar, carbohydrates and fatty foods."""
quote1="""
1).Menthol
  An oil made from mint that soothes sore throats and relieves itching.
2).Nasal washing
  Rinsing the inside of the nose with warm salt water to flush
  out irritants and excess mucus. Often done using a neti pot or squeeze bottle.
3).Throat lozenge
  Soothes sore throats"""
quote2="""
1).Nonsteroidal anti-inflammatory drug
Relieves pain, decreases inflammation and reduces fever.
2).Analgesic
Relieves pain.
3).Antihistamine
Reduces or stops an allergic reaction.
4).Cough medicine
Blocks the cough reflex. Some may thin and loosen mucus,
making it easier to clear from the airways.
5).Decongestant
Relieves nasal congestion, swelling and runny nose"""
quote3="""
1).Gargle with a mixture of warm water and 1/2 to 1 teaspoon of salt.
2).Drink warm liquids that feel soothing to the throat,
   such as hot tea with honey, soup broth, or warm water with lemon.
   Herbal teas are especially soothing to a sore throat .
3).Cool your throat by eating a cold treat like a popsicle or ice cream.
4).Suck on a piece of hard candy or a lozenge.
5).Turn on a cool mist humidifier to add moisture to the air.
6).Rest your voice until your throat feels better."""
quote4="""
1).a sore throat spray that contains a numbing antiseptic
  like phenol, or a cooling ingredient like menthol or eucalyptus
2).throat lozenges
3).cough syrup"""
quote5="""
Medications such as paracetamol and ibuprofen may help to ease discomfort.
Avoid giving children aspirin because this may cause a rare, serious condition.
----low grade, from 100.5–102.1°F or 38.1–39°C
----moderate, from 102.2–104.0°F or 39.1–40°C
----high, from 104.1–106.0°F to or 40.1-41.1°C
----hyperpyrexia, above 106.0°F or 41.1°C"""
quote6="""
Non-steroidal anti-inflammatory drugs (NSAIDs)
such as aspirin or ibuprofen can help bring a fever down.
These are available to purchase over-the-counter or online.
However, a mild fever may be helping combat the bacterium or virus
that is causing the infection. It may not be ideal to bring it down
Because fever is a sign rather than a disease,
when the doctor has confirmed there is an elevated body temperature,
certain diagnostic tests may be ordered."""
quote7="""
1).Increase your fiber intake.
2).Exercise most days of the week.
3).Don't ignore the urge to have a bowel movement.
4).Fiber supplements."""
quote8="""
1).Stool softeners.
2).Lubricants.
3).Enemas and suppositories.
4).oral magnesium hydroxide (Phillips' Milk of Magnesia, Dulcolax
Milk of Magnesia, others), magnesium citrate, lactulose (Cholac, Constilac,
others), polyethylene glycol (Miralax, Glycolax)."""
quote9="""
Liquids, lozenges, cough drops, vapourisers and
steamy showers may help to soothe a cough. Cough medicine may also help,
but it's best to check with a doctor before administering to a child under six"""
quote10="""
Make an appointment to see a doctor if you:
1).Develop a fever of 100°F (38°C) or higher
2).Cough up phlegm that's yellow or green
3).Start wheezing
See a doctor immediately if you:
1).Are choking and can't speak
2).Have difficulty breathing
3).Find it hard to swallow
4).Notice blood in your phlegm
5).Have persistent night sweats, fever and weight loss"""
quote11="""
Ice. You can numb the pain if you apply a cold compress to the sore. ...
Pain relievers. When a cold sore really stings, you may get
some relief from an over-the-counter painkiller like acetaminophen.
Over-the-counter creams. ...
Aloe vera gel. ...
Avoid triggers. ...
Don't touch the area.
----Medications
----Antiviral drug
----Reduces viruses' ability to replicate.
----Analgesic
----Relieves pain.
----Nonsteroidal anti-inflammatory drug
----Relieves pain, decreases inflammation and reduces fever"""
class window(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        container=Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames={}

        for F in (startpage,id_one,id_two,id_three,id_four,id_five,id_six,id_seven,id_eight,anxiety,commoncold,coldsore,fever,
                  constipation,cough,sorethroat):
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(startpage)
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()

class startpage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font=("Bold","30"),padx=4,pady=4,fg="White",bg="Blue").place(x=20,y=50)
        var.set("READ THE INSTRUCTIONS PROPERPLY")
        var1=StringVar()
        txt1=Label(self,textvariable=var1,font=("Bold","15"),padx=2,pady=2,fg="White",bg="Blue").place(x=50,y=200)
        var2=StringVar()
        txt2=Label(self,textvariable=var2,font=("Bold","15"),padx=2,pady=2,fg="White",bg="Blue").place(x=50,y=300)
        var3=StringVar()
        txt2=Label(self,textvariable=var3,font=("Bold","15"),padx=2,pady=2,fg="White",bg="Blue").place(x=50,y=400)
        var1.set("1). Read the symptoms about your diseases proplerly.")
        var2.set("2). Tick the appropriate Checkboxs and click SUBMIT when done.")
        var3.set("3). Follow along with next symptoms questions to get what you are suffering from.")

        button1=Button(self,text="  NEXT  ",font="20",fg="Blue",command=lambda:controller.show_frame(id_one)).place(x=350,y=500)


class id_one(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font=("Bold","20"),padx=4,pady=4,fg="White",bg="Blue").place(x=200,y=50)
        var.set(df.loc[0,"Question"])
        self.ls={"1":0,"2":0,"3":0,"4":0}
        var1=IntVar()
        cb1=Checkbutton(self,variable=var1,text=df.loc[0,"Option1"],font="10",command=lambda:self.ls.update({"1":var1.get()}))
        cb1.place(x=30,y=150)
        var2=IntVar()
        cb2=Checkbutton(self,variable=var2,text=df.loc[0,"Option2"],font="10",command=lambda:self.ls.update({"2":var2.get()}))
        cb2.place(x=30,y=250)
        var3=IntVar()
        cb3=Checkbutton(self,variable=var3,text=df.loc[0,"Option3"],font="10",command=lambda:self.ls.update({"3":var3.get()}))
        cb3.place(x=30,y=350)
        var4=IntVar()
        cb4=Checkbutton(self,variable=var4,text=df.loc[0,"Option4"],font="10",command=lambda:self.ls.update({"4":var4.get()}))
        cb4.place(x=30,y=450)

        b1=Button(self,text="SUBMIT",font="20",fg="Blue",command=lambda:controller.show_frame(decider1(self.ls)))
        b1.place(x=350,y=500)


class id_two(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font=("Bold","20"),padx=4,pady=4,fg="White",bg="Blue").place(x=75,y=50)
        var.set(df.loc[1,"Question"])
        self.ls={"1":0,"2":0,"3":0,"4":0}
        var1=IntVar()
        cb1=Checkbutton(self,variable=var1,text=df.loc[1,"Option1"],font="10",command=lambda:self.ls.update({"1":var1.get()}))
        cb1.place(x=30,y=150)
        var2=IntVar()
        cb2=Checkbutton(self,variable=var2,text=df.loc[1,"Option2"],font="10",command=lambda:self.ls.update({"2":var2.get()}))
        cb2.place(x=30,y=250)
        var3=IntVar()
        cb3=Checkbutton(self,variable=var3,text=df.loc[1,"Option3"],font="10",command=lambda:self.ls.update({"3":var3.get()}))
        cb3.place(x=30,y=350)
        var4=IntVar()
        cb4=Checkbutton(self,variable=var4,text=df.loc[1,"Option4"],font="10",command=lambda:self.ls.update({"4":var4.get()}))
        cb4.place(x=30,y=450)

        b1=Button(self,text="SUBMIT",font="20",fg="Blue",command=lambda:controller.show_frame(decider2(self.ls)))
        b1.place(x=350,y=500)

class id_three(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font=("Bold","20"),padx=4,pady=4,fg="White",bg="Blue").place(x=75,y=50)
        var.set(df.loc[2,"Question"])
        self.ls={"1":0,"2":0,"3":0,"4":0}
        var1=IntVar()
        cb1=Checkbutton(self,variable=var1,text=df.loc[2,"Option1"],font="10",command=lambda:self.ls.update({"1":var1.get()}))
        cb1.place(x=30,y=150)
        var2=IntVar()
        cb2=Checkbutton(self,variable=var2,text=df.loc[2,"Option2"],font="10",command=lambda:self.ls.update({"2":var2.get()}))
        cb2.place(x=30,y=250)
        var3=IntVar()
        cb3=Checkbutton(self,variable=var3,text=df.loc[2,"Option3"],font="10",command=lambda:self.ls.update({"3":var3.get()}))
        cb3.place(x=30,y=350)
        var4=IntVar()
        cb4=Checkbutton(self,variable=var4,text=df.loc[2,"Option4"],font="10",command=lambda:self.ls.update({"4":var4.get()}))
        cb4.place(x=30,y=450)

        b1=Button(self,text="SUBMIT",font="20",fg="Blue",command=lambda:controller.show_frame(decider3(self.ls)))
        b1.place(x=350,y=500)

class id_four(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font=("Bold","20"),padx=4,pady=4,fg="White",bg="Blue").place(x=75,y=50)
        var.set(df.loc[3,"Question"])
        self.ls={"1":0,"2":0,"3":0,"4":0}
        var1=IntVar()
        cb1=Checkbutton(self,variable=var1,text=df.loc[3,"Option1"],font="10",command=lambda:self.ls.update({"1":var1.get()}))
        cb1.place(x=30,y=150)
        var2=IntVar()
        cb2=Checkbutton(self,variable=var2,text=df.loc[3,"Option2"],font="10",command=lambda:self.ls.update({"2":var2.get()}))
        cb2.place(x=30,y=250)
        var3=IntVar()
        cb3=Checkbutton(self,variable=var3,text=df.loc[3,"Option3"],font="10",command=lambda:self.ls.update({"3":var3.get()}))
        cb3.place(x=30,y=350)
        var4=IntVar()
        cb4=Checkbutton(self,variable=var4,text=df.loc[3,"Option4"],font="10",command=lambda:self.ls.update({"4":var4.get()}))
        cb4.place(x=30,y=450)

        b1=Button(self,text="SUBMIT",font="20",fg="Blue",command=lambda:controller.show_frame(decider4(self.ls)))
        b1.place(x=350,y=500)

class id_five(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font=("Bold","20"),padx=4,pady=4,fg="White",bg="Blue").place(x=75,y=50)
        var.set(df.loc[4,"Question"])
        self.ls={"1":0,"2":0,"3":0,"4":0}
        var1=IntVar()
        cb1=Checkbutton(self,variable=var1,text=df.loc[4,"Option1"],font="10",command=lambda:self.ls.update({"1":var1.get()}))
        cb1.place(x=30,y=150)
        var2=IntVar()
        cb2=Checkbutton(self,variable=var2,text=df.loc[4,"Option2"],font="10",command=lambda:self.ls.update({"2":var2.get()}))
        cb2.place(x=30,y=250)
        var3=IntVar()
        cb3=Checkbutton(self,variable=var3,text=df.loc[4,"Option3"],font="10",command=lambda:self.ls.update({"3":var3.get()}))
        cb3.place(x=30,y=350)
        var4=IntVar()
        cb4=Checkbutton(self,variable=var4,text=df.loc[4,"Option4"],font="10",command=lambda:self.ls.update({"4":var4.get()}))
        cb4.place(x=30,y=450)

        b1=Button(self,text="SUBMIT",font="20",fg="Blue",command=lambda:controller.show_frame(decider5(self.ls)))
        b1.place(x=350,y=500)

class id_six(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font=("Bold","20"),padx=4,pady=4,fg="White",bg="Blue").place(x=75,y=50)
        var.set(df.loc[5,"Question"])
        self.ls={"1":0,"2":0,"3":0,"4":0}
        var1=IntVar()
        cb1=Checkbutton(self,variable=var1,text=df.loc[5,"Option1"],font="10",command=lambda:self.ls.update({"1":var1.get()}))
        cb1.place(x=30,y=150)
        var2=IntVar()
        cb2=Checkbutton(self,variable=var2,text=df.loc[5,"Option2"],font="10",command=lambda:self.ls.update({"2":var2.get()}))
        cb2.place(x=30,y=250)
        var3=IntVar()
        cb3=Checkbutton(self,variable=var3,text=df.loc[5,"Option3"],font="10",command=lambda:self.ls.update({"3":var3.get()}))
        cb3.place(x=30,y=350)
        var4=IntVar()
        cb4=Checkbutton(self,variable=var4,text=df.loc[5,"Option4"],font="10",command=lambda:self.ls.update({"4":var4.get()}))
        cb4.place(x=30,y=450)

        b1=Button(self,text="SUBMIT",font="20",fg="Blue",command=lambda:controller.show_frame(decider6(self.ls)))
        b1.place(x=350,y=500)

class id_seven(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font=("Bold","20"),padx=4,pady=4,fg="White",bg="Blue").place(x=75,y=50)
        var.set(df.loc[6,"Question"])
        self.ls={"1":0,"2":0,"3":0,"4":0}
        var1=IntVar()
        cb1=Checkbutton(self,variable=var1,text=df.loc[6,"Option1"],font="10",command=lambda:self.ls.update({"1":var1.get()}))
        cb1.place(x=30,y=150)
        var2=IntVar()
        cb2=Checkbutton(self,variable=var2,text=df.loc[6,"Option2"],font="10",command=lambda:self.ls.update({"2":var2.get()}))
        cb2.place(x=30,y=250)
        var3=IntVar()
        cb3=Checkbutton(self,variable=var3,text=df.loc[6,"Option3"],font="10",command=lambda:self.ls.update({"3":var3.get()}))
        cb3.place(x=30,y=350)
        var4=IntVar()
        cb4=Checkbutton(self,variable=var4,text=df.loc[6,"Option4"],font="10",command=lambda:self.ls.update({"4":var4.get()}))
        cb4.place(x=30,y=450)

        b1=Button(self,text="SUBMIT",font="20",fg="Blue",command=lambda:controller.show_frame(decider7(self.ls)))
        b1.place(x=350,y=500)

class id_eight(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font=("Bold","20"),padx=4,pady=4,fg="White",bg="Blue").place(x=75,y=50)
        var.set(df.loc[7,"Question"])
        self.ls={"1":0,"2":0,"3":0,"4":0}
        var1=IntVar()
        txt1=StringVar()
        cb1=Checkbutton(self,variable=var1,text=df.loc[7,"Option1"],font="10",command=lambda:self.ls.update({"1":var1.get()}))
        cb1.place(x=30,y=150)
        var2=IntVar()
        cb2=Checkbutton(self,variable=var2,text=df.loc[7,"Option2"],font="10",command=lambda:self.ls.update({"2":var2.get()}))
        cb2.place(x=30,y=250)
        var3=IntVar()
        cb3=Checkbutton(self,variable=var3,text=df.loc[7,"Option3"],font="10",command=lambda:self.ls.update({"3":var3.get()}))
        cb3.place(x=30,y=350)
        var4=IntVar()
        cb4=Checkbutton(self,variable=var4,text=df.loc[7,"Option4"],font="10",command=lambda:self.ls.update({"4":var4.get()}))
        cb4.place(x=30,y=450)

        b1=Button(self,text="SUBMIT",font="20",fg="Blue",command=lambda:controller.show_frame(decider8(self.ls)))
        b1.place(x=350,y=500)

class anxiety(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font="15",fg="Blue").place(x=20,y=30)
        var.set("Your suffering from Anxiety")
        var1=StringVar()
        lab2=Label(self,textvariable=var1,font="15",fg="Blue").place(x=20,y=75)
        var1.set("TREATMENT AND SELF CARE")
        txt=Text(self,height=25,width=90)
        txt.place(x=20,y=130)
        txt.insert(END,quote)
        button2=Button(self,text="  HOME  ",font="20",fg="Blue",command=lambda:controller.show_frame(startpage)).place(x=35,y=530)

class commoncold(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font="15",fg="Blue").place(x=20,y=30)
        var.set("Your suffering from COMMONCOLD")
        var1=StringVar()
        lab2=Label(self,textvariable=var1,font="15",fg="Blue").place(x=20,y=75)
        var1.set("TREATMENT AND SELF CARE")
        txt=Text(self,height=10,width=90)
        txt.place(x=20,y=130)
        txt.insert(END,quote1)
        var3=StringVar()
        lab3=Label(self,textvariable=var3,font="15",fg="Blue").place(x=20,y=300)
        var3.set("MEDICATION")
        txt1=Text(self,height=13,width=90)
        txt1.place(x=20,y=350)
        txt1.insert(END,quote2)
        button2=Button(self,text="  HOME  ",font="20",fg="Blue",command=lambda:controller.show_frame(startpage)).place(x=35,y=530)

class sorethroat(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font="15",fg="Blue").place(x=20,y=30)
        var.set("Your suffering from SORETHROAT")
        var1=StringVar()
        lab2=Label(self,textvariable=var1,font="15",fg="Blue").place(x=20,y=75)
        var1.set("TREATMENT AND SELF CARE")
        txt=Text(self,height=10,width=90)
        txt.place(x=20,y=130)
        txt.insert(END,quote3)
        var3=StringVar()
        lab3=Label(self,textvariable=var3,font="15",fg="Blue").place(x=20,y=300)
        var3.set("MEDICATION")
        txt1=Text(self,height=5,width=90)
        txt1.place(x=20,y=350)
        txt1.insert(END,quote4)
        button2=Button(self,text="  HOME  ",font="20",fg="Blue",command=lambda:controller.show_frame(startpage)).place(x=35,y=530)

class fever(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font="15",fg="Blue").place(x=20,y=30)
        var.set("Your suffering from FEVER")
        var1=StringVar()
        lab2=Label(self,textvariable=var1,font="15",fg="Blue").place(x=20,y=75)
        var1.set("TREATMENT AND SELF CARE")
        txt=Text(self,height=10,width=90)
        txt.place(x=20,y=130)
        txt.insert(END,quote5)
        var3=StringVar()
        lab3=Label(self,textvariable=var3,font="15",fg="Blue").place(x=20,y=300)
        var3.set("MEDICATION")
        txt1=Text(self,height=10,width=90)
        txt1.place(x=20,y=350)
        txt1.insert(END,quote6)
        button2=Button(self,text="  HOME  ",font="20",fg="Blue",command=lambda:controller.show_frame(startpage)).place(x=35,y=530)

class constipation(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font="15",fg="Blue").place(x=20,y=30)
        var.set("Your suffering from CONSTIPATION")
        var1=StringVar()
        lab2=Label(self,textvariable=var1,font="15",fg="Blue").place(x=20,y=75)
        var1.set("TREATMENT AND SELF CARE")
        txt=Text(self,height=10,width=90)
        txt.place(x=20,y=130)
        txt.insert(END,quote7)
        var3=StringVar()
        lab3=Label(self,textvariable=var3,font="15",fg="Blue").place(x=20,y=300)
        var3.set("MEDICATION")
        txt1=Text(self,height=10,width=90)
        txt1.place(x=20,y=350)
        txt1.insert(END,quote8)
        button2=Button(self,text="  HOME  ",font="20",fg="Blue",command=lambda:controller.show_frame(startpage)).place(x=35,y=530)

class cough(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font="15",fg="Blue").place(x=20,y=30)
        var.set("Your suffering from COUGH")
        var1=StringVar()
        lab2=Label(self,textvariable=var1,font="15",fg="Blue").place(x=20,y=75)
        var1.set("TREATMENT AND SELF CARE")
        txt=Text(self,height=5,width=90)
        txt.place(x=20,y=130)
        txt.insert(END,quote9)
        var3=StringVar()
        lab3=Label(self,textvariable=var3,font="15",fg="Blue").place(x=20,y=250)
        var3.set("MEDICATION")
        txt1=Text(self,height=15,width=90)
        txt1.place(x=20,y=275)
        txt1.insert(END,quote10)
        button2=Button(self,text="  HOME  ",font="20",fg="Blue",command=lambda:controller.show_frame(startpage)).place(x=35,y=530)

class coldsore(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        var=StringVar()
        lab1=Label(self,textvariable=var,font="15",fg="Blue").place(x=20,y=30)
        var.set("Your suffering from COLDSORE")
        var1=StringVar()
        lab2=Label(self,textvariable=var1,font="15",fg="Blue").place(x=20,y=75)
        var1.set("TREATMENT AND SELF CARE")
        txt=Text(self,height=15,width=90)
        txt.place(x=20,y=130)
        txt.insert(END,quote11)
        button2=Button(self,text="  HOME  ",font="20",fg="Blue",command=lambda:controller.show_frame(startpage)).place(x=35,y=530)

def decider1(dic):
    dic1={"1":0,"2":0,"3":0,"4":1}
    dic2={"1":0,"2":0,"3":1,"4":0}
    dic3={"1":0,"2":0,"3":1,"4":1}
    dic4={"1":0,"2":1,"3":0,"4":0}
    dic5={"1":0,"2":1,"3":0,"4":1}
    dic6={"1":0,"2":1,"3":1,"4":0}
    dic7={"1":0,"2":1,"3":1,"4":1}
    dic8={"1":1,"2":0,"3":0,"4":0}
    dic9={"1":1,"2":0,"3":0,"4":1}
    dic10={"1":1,"2":0,"3":1,"4":0}
    dic11={"1":1,"2":0,"3":1,"4":1}
    dic12={"1":1,"2":1,"3":0,"4":0}
    dic13={"1":1,"2":1,"3":0,"4":1}
    dic14={"1":1,"2":1,"3":1,"4":0}
    dic15={"1":1,"2":1,"3":1,"4":1}
    dic0={"1":0,"2":0,"3":0,"4":0}

    if dic==dic8 or dic==dic12 or dic==dic14:
        return id_two
    elif dic==dic2 or dic==dic3 or dic==dic7:
        return id_three
    elif dic==dic1 or dic==dic9 or dic==dic13 or dic==dic5 or dic==dic11:
        return id_four
    elif dic==dic6:
        return id_five
    elif dic==dic4:
        return id_seven
    elif dic==dic10:
        return anxiety
    else:
        return id_one


def decider2(dic):
    dic8={"1":1,"2":0,"3":0,"4":0}
    dic4={"1":0,"2":1,"3":0,"4":0}
    dic12={"1":1,"2":1,"3":0,"4":0}
    dic0={"1":0,"2":0,"3":0,"4":0}
    if dic==dic8 or dic==dic4 or dic==dic12:
        return anxiety
    elif dic==dic0:
        return id_two
    else:
        return id_three


def decider3(dic):
    dic8={"1":1,"2":0,"3":0,"4":0}
    dic4={"1":0,"2":1,"3":0,"4":0}
    dic12={"1":1,"2":1,"3":0,"4":0}
    dic2={"1":0,"2":0,"3":1,"4":0}
    dic0={"1":0,"2":0,"3":0,"4":0}
    if dic==dic8 or dic==dic4 or dic==dic12:
        return commoncold
    elif dic==dic2:
        return id_four
    elif dic==dic0:
        return id_three
    else:
        return id_six

def decider4(dic):
    return constipation

def decider5(dic):
    dic8={"1":1,"2":0,"3":0,"4":0}
    dic4={"1":0,"2":1,"3":0,"4":0}
    dic12={"1":1,"2":1,"3":0,"4":0}
    dic1={"1":0,"2":0,"3":0,"4":1}
    dic2={"1":0,"2":0,"3":1,"4":0}
    dic3={"1":0,"2":0,"3":1,"4":1}
    dic0={"1":0,"2":0,"3":0,"4":0}
    if dic==dic8 or dic==dic4 or dic==dic12:
        return sorethroat
    elif dic==dic1 or dic==dic2 or dic==dic3:
        return id_seven
    elif dic==dic0:
        return id_five
    else:
        return id_six


def decider6(dic):
    dic1={"1":0,"2":0,"3":0,"4":1}
    dic2={"1":0,"2":0,"3":1,"4":0}
    dic0={"1":0,"2":0,"3":0,"4":0}
    if dic == dic1:
        return id_seven
    elif dic==dic0:
        return id_six
    else:
        return cough

def decider7(dic):
    dic2={"1":0,"2":0,"3":1,"4":0}
    dic0={"1":0,"2":0,"3":0,"4":0}
    if dic==dic2:
        return id_eight
    elif dic==dic0:
        return id_seven
    else:
        return fever

def decider8(dic):
    return coldsore



app=window()
app.geometry("800x600")
app.mainloop()
