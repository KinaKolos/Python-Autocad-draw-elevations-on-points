from pyautocad import Autocad, APoint,aDouble
import numpy as np
import array
import math
from math import *
from tkinter import *
from tkinter import filedialog



# Creating GUI

root = Tk()
root.title("Entiteti")
root.geometry("200x100")

var = StringVar()

# Enter number of decimal points

entLabel = Label(root, text = "Broj decimala")
entLabel.grid(row = 0, column= 0)

ent = Entry(root, width = 5)
ent.grid(row=0,column=1)




tacke = []

def kote():

    # Creating AutoCad drawing

    acad = Autocad(create_if_not_exists=True)

    # Creating AutoCad layer

    new_layer = acad.ActiveDocument.Layers.Add("NV")

    numb = ent.get()



    # Iterating through objects in drawing looking for points and 3d polylines
    try:

        for obj in acad.iter_objects(dont_cast=True):
            if len(obj.Coordinates) == 3:
                point1 = obj.Coordinates

                yp = point1[0]
                xp = point1[1]
                zp = point1[2]

                point2 = APoint(yp,xp,zp)

                name2 = acad.model.AddText(format(zp,f".{int(numb)}f"),point2,1)
                name2.Layer = "NV"
        for obj in acad.iter_objects(dont_cast=True):
            if len(obj.Coordinates) != 3:

                lis = obj.Coordinates

                it = iter(lis)

            for x in it:
                tacke.append([x,next(it),next(it)])

    except:
        pass


    # Iterating through a list and creating autocad points

    for n in tacke:
        y = round(n[0],3)
        x = round(n[1],3)
        z = round(n[2],3)
        point = APoint(y,x,z)


        # Drawing text with elevation of every point

        name1 = acad.model.AddText(format(z,f".{int(numb)}f"),point,1)
        name1.Layer = "NV"


kartiraj_btn = Button(root, text="Entiteti", command = kote)
kartiraj_btn.grid(row=1,column=1)

root.mainloop()
