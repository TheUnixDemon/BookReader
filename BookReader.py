
from pathlib import Path # zum checken und erstellen der Speicher-Datei

###### ab hier beginnt der Check, der Speicher-Datei

checknumb = [] # hier werden Nummern zum überprüfen von etwas eingetragen

nichts = []

myfile = Path(".mainpoint.save")
if myfile.is_file():
    nichts.append("dddd")
else:
    myfile = Path(".mainpoint.save")
    myfile.touch(exist_ok = True)
    f = open(myfile) # mir "open" wird die Datei erstellt, wenn nicht vorhanden (öffnet auch diese)

###### ab hier endet der Check, der Speicher-Datei

###### ab hier beginnt der Check, ob die Auflösung des Bildschirmes in der Speicher-Datei vorhanden ist u. wenn nicht wird eingetragen

liste = []

my_save = open(".mainpoint.save", "r")
lines = my_save.read().splitlines()

for line in lines:
    liste.append(line)

my_save.close()


if liste == []:

    from tkinter import *

    def saveit():
        my_save = open(".mainpoint.save", "w")
        mainpoint_save = [str(e1.get()), str(e2.get()), "", "0", "0"] # e1.get()=Breite von Bild, e2.get()=höhe von Bild, 0=Bild nicht in Breite vereinheitlichen, 0=zufällige Rangliste

        for line in mainpoint_save:
            my_save.write(line + "\n")

        my_save.close()
        root.destroy()

    root = Tk()
    root.title("Auflösung in Pixel")
    root.configure(bg = "gray29")

    Label(root, text = "Breite", bg = "gray23", fg = "gray99").grid(row = 0)
    Label(root, text = "Höhe", bg = "gray23", fg = "gray99").grid(row = 1)

    e1 = Entry(root, bg = "gray23", fg = "gray99")
    e2 = Entry(root, bg = "gray23", fg = "gray99")

    e1.grid(row = 0, column = 1)
    e2.grid(row = 1, column = 1)

    Button(root, text = "Speichern", command = saveit, bg = "gray23", fg = "gray99", activebackground = "gray26").grid(row = 3, column = 0, sticky = W ,pady = 4)

    root.mainloop()

###### ab hier endet der Check, ob die Auflösung des Bildschirmes in der Speicher-Datei vorhanden ist u. wenn nicht wird eingetragen

###### ab hier beginnt das Hauptmenü

x = 0
while x == 0:

    liste = []

    my_save = open(".mainpoint.save", "r")
    lines = my_save.read().splitlines()

    for line in lines:
        liste.append(line)

    my_save.close()

    windowsize = str(liste[0]) + "x" + str(liste[1])

    from tkinter import *

    selfvoice = [] # gibt die Wahl des Nutzers an, um anhand dieser zu handeln

    root = Tk()
    root.title("BookReader")
    root.geometry(windowsize)
    root.configure(bg = "gray28")

    widthbutton = 28 # Standart-Wert für X-Wert

    if int(liste[0]) < 265: # wenn Bildschrim zu klein ist, dann verändere X-Wert
        widthbutton = 22

    endheight = (0.005555556 * int(liste[1])) + 1 # hier wird mit Maßsstabs-Rechnungen die passende Höhe berechnet

    normalendpady = 0.094444444 * int(liste[1])
    otherendpady = 0.116666667 * int(liste[1])

    def openbooklist():
        selfvoice.append(0)
        root.destroy()


    def settings():
        selfvoice.append(1)
        root.destroy()

    def quit():
        selfvoice.append(2)
        root.destroy()


    a = Button(root, text = "In Ihre Bibliothek", command = openbooklist, width = widthbutton, height = int(endheight), bg = "gray23", fg = "gray99", activebackground = "gray26")
    a.pack(pady = int(normalendpady))

    b = Button(root, text = "In die Einstellungen", command = settings, width = widthbutton, height = int(endheight), bg = "gray23", fg = "gray99", activebackground = "gray26")
    b.pack()

    c = Button(root, text = "Das Programm schließen", command = quit, width = widthbutton, height = int(endheight), bg = "gray23", fg = "gray99", activebackground = "gray26")
    c.pack(pady = int(otherendpady))

    root.mainloop()

    x = 1

    ###### hier endet das Hauptmenü

    ###### hier beginnen die Einstellungen

    if int(selfvoice[0]) == 1:

        liste = []

        sizechanger = [] # da, um zu check, ob gedrückt

        checknumb = []

        my_save = open(".mainpoint.save", "r")
        lines = my_save.read().splitlines()

        for line in lines:
            liste.append(line)

        my_save.close()

        windowsize = str(liste[0]) + "x" + str(liste[1])

        root = Tk()
        root.title("BookReader: Die Einstellungen")
        root.geometry(windowsize)
        root.configure(bg = "gray28")

        normalendpady = 0.027000 * int(liste[1])

        endheight = (0.003333333 * int(liste[1])) + 1 # hier wird mit Maßsstabs-Rechnungen die passende Höhe berechnet

        def reset():
            root.destroy()
            checknumb.append(1)

        def vereinheitlichen():
            liste = []

            my_save = open(".mainpoint.save", "r")
            lines = my_save.read().splitlines()

            for line in lines:
                liste.append(line)

            my_save.close()

            liste[3] = "1"

            my_save = open(".mainpoint.save", "w")
            mainpoint_save = liste # e1.get()=Breite von Bild, e2.get()=höhe von Bild, 0=Bild nicht in Breite vereinheitlichen, 0=zufällige Rangliste

            for line in mainpoint_save:
                my_save.write(line + "\n")

            my_save.close()

        def nicht_vereinheitlichen():
            liste = []

            my_save = open(".mainpoint.save", "r")
            lines = my_save.read().splitlines()

            for line in lines:
                liste.append(line)

            my_save.close()

            liste[3] = "0"

            my_save = open(".mainpoint.save", "w")
            mainpoint_save = liste # e1.get()=Breite von Bild, e2.get()=höhe von Bild, 0=Bild nicht in Breite vereinheitlichen, 0=zufällige Rangliste

            for line in mainpoint_save:
                my_save.write(line + "\n")

            my_save.close()

        def random():
            liste = []

            my_save = open(".mainpoint.save", "r")
            lines = my_save.read().splitlines()

            for line in lines:
                liste.append(line)

            my_save.close()

            liste[4] = "0"

            my_save = open(".mainpoint.save", "w")
            mainpoint_save = liste # e1.get()=Breite von Bild, e2.get()=höhe von Bild, 0=Bild nicht in Breite vereinheitlichen, 0=zufällige Rangliste

            for line in mainpoint_save:
                my_save.write(line + "\n")

            my_save.close()

        def beliebt():
            liste = []

            my_save = open(".mainpoint.save", "r")
            lines = my_save.read().splitlines()

            for line in lines:
                liste.append(line)

            my_save.close()

            liste[4] = "1"

            my_save = open(".mainpoint.save", "w")
            mainpoint_save = liste # e1.get()=Breite von Bild, e2.get()=höhe von Bild, 0=Bild nicht in Breite vereinheitlichen, 0=zufällige Rangliste

            for line in mainpoint_save:
                my_save.write(line + "\n")

            my_save.close()

        def unbeliebt():
            liste = []

            my_save = open(".mainpoint.save", "r")
            lines = my_save.read().splitlines()

            for line in lines:
                liste.append(line)

            my_save.close()

            liste[4] = "2"

            my_save = open(".mainpoint.save", "w")
            mainpoint_save = liste # e1.get()=Breite von Bild, e2.get()=höhe von Bild, 0=Bild nicht in Breite vereinheitlichen, 0=zufällige Rangliste

            for line in mainpoint_save:
                my_save.write(line + "\n")

            my_save.close()

        def opensizechanger():
            sizechanger.append("1")
            root.destroy()

        def close():
            checknumb.append(0)
            root.destroy()

        a = Button(root, text = "Zurück zum Hauptmenü", command = reset, width = widthbutton, height = int(endheight), bg = "gray23", fg = "gray99", activebackground = "gray26")
        a.pack(pady = int(normalendpady))

        b = Button(root, text = "Bildgröße vereinheitlichen", command = vereinheitlichen, width = widthbutton, height = int(endheight), bg = "gray23", fg = "gray99", activebackground = "gray26")
        b.pack()

        c = Button(root, text = "Bildgröße nicht vereinheitlichen", command = nicht_vereinheitlichen, width = widthbutton, height = int(endheight), bg = "gray23", fg = "gray99", activebackground = "gray26")
        c.pack(pady = int(normalendpady))

        d = Button(root, text = "Seitengröße pro Buch anpassen", command = opensizechanger, width = widthbutton, height = int(endheight), bg = "gray23", fg = "gray99", activebackground = "gray26")
        d.pack(pady = int(normalendpady))

        e = Button(root, text = "Das Programm schließen", command = close, width = widthbutton, height = int(endheight), bg = "gray23", fg = "gray99", activebackground = "gray26")
        e.pack()


        root.mainloop()

        if checknumb == []:
            checknumb = []
        elif int(checknumb[0]) == 1:
            x = 0
            checknumb = []
        elif int(checknumb[0]) == 0:
            x = 1
            checknumb = []

##### hier enden die Einstellungen

##### hier beginnt die Größen-Änderung
        y = 0
        while y == 0:
            y = 1
            if not sizechanger == []:

                from tkinter import *
                from functools import partial

                liste = []

                my_save = open(".mainpoint.save", "r")
                lines = my_save.read().splitlines()

                for line in lines:
                    liste.append(line)

                my_save.close()

                selfvoice = []
                buttonvoice = [] # abgespeichertes Ergebniss von Button Eingabe
                selfvoicenumber = [] # endgültig ausgewertetes Ergebniss in Form einer Listen-Nummer zum Suchen

                funclist = []
                listforcommand = []
                windowfunclist = []
                fucforprintbuttons = []


                booklist = []
                pathbooklist = []
                sizeforbooks = []
                progressinbooks = []

                r = 0
                if not len(liste) == 5: # wichtig zum auswerten der Speicher-Datei
                    for i in range(0, len(liste)):
                        if len(liste[i]) == 0:
                            r = r + 1
                        elif r == 2:
                            booklist.append(liste[i])
                        elif r == 3:
                            pathbooklist.append(liste[i])
                        elif r == 4:
                            sizeforbooks.append(liste[i])
                        elif r == 5:
                            progressinbooks.append(liste[i])


                buttonwidth = 0.099375 * int(liste[0]) + 1
                buttonheight = 0.00333333333 * int(liste[1]) + 1

                buttonwidthinpixel = (round(round(buttonwidth) - 1) * 8 + 33)
                buttonheightinpixel = (round(round(buttonheight) - 1) * 17 + 28)

                buttondistance = round(0.064444444 * int(liste[1])) ##############
                buttondistanceleft = round((int(liste[0]) / 2) - (int(buttonwidthinpixel) / 2))

                groundpositionwidth = round(buttonwidthinpixel / 2)
                groundpositionheight = round(buttonheightinpixel / 2)


                windowwidth = int(liste[0])
                windowheight = int(liste[1])

                root=Tk()
                root.title("BookReader: Buch-Größe")

                scrollheight = round(groundpositionheight + ((int(len(booklist)) + 6) * buttondistance) + ((int(len(booklist)) + 5) * buttonheightinpixel))

                frame=Frame(root,width=windowwidth, height=windowheight) # Hier kann man die größe des Festers einstellen.
                frame.pack(expand=True, fill=BOTH) # Das hier ist zum vervollstendigen zuständig.
                canvas=Canvas(frame, bg='gray28',width=windowwidth, height=windowheight, scrollregion=(0,0,0,scrollheight)) # die Scroll-
                # Region muss größer sein als das Fenster, damit etwas passiert
                vbar=Scrollbar(frame, orient=VERTICAL)
                vbar.pack(side=RIGHT, fill=Y)
                vbar.config(command=canvas.yview)
                canvas.config(width=windowwidth, height=windowheight)
                canvas.config(yscrollcommand=vbar.set)
                canvas.pack(side=LEFT, expand=True, fill=BOTH)

                for i in range(0, len(booklist)): # Funktionen werden hier erstellt
                    funclist.append("button" + str(i))
                    listforcommand.append("command" + str(i))
                    windowfunclist.append("button" + str(i) + "window")

                def newbook():
                    i = int(len(selfvoice) - 1)
                    for j in range(0, len(booklist)):
                        if selfvoice[i] == booklist[j]:
                            selfvoicenumber.append(int(j))

                            buttonvoice.append(1)
                            root.destroy()

                def back():
                    root.destroy()
                    checknumb.append(1)


                voicebutton2 = Button(root, text = "Buch-Größe für dieses Buch ändern", command = newbook)
                voicebutton2.configure(width = round(buttonwidth), height = round(buttonheight), bg = "gray22", fg = "gray99", activebackground = "gray26", relief = FLAT)
                windowvoicebutton2 = canvas.create_window((groundpositionwidth + buttondistanceleft), (groundpositionheight + ((0 + 1) * buttondistance) + ((0 + 0) * buttonheightinpixel)), window=voicebutton2)

                voicebutton2 = Button(root, text = "Zurück zum Hauptmenü", command = back)
                voicebutton2.configure(width = round(buttonwidth), height = round(buttonheight), bg = "gray22", fg = "gray99", activebackground = "gray26", relief = FLAT)
                windowvoicebutton2 = canvas.create_window((groundpositionwidth + buttondistanceleft), (groundpositionheight + ((1 + 1) * buttondistance) + ((1 + 0) * buttonheightinpixel)), window=voicebutton2)

                fucforprintbuttons = []
                fucforprintbuttons.append(0)

                for list in booklist :

                    cmd = partial(selfvoice.append, list)

                    funclist[0] = Button(root, text = str(booklist[fucforprintbuttons[0]]), command = cmd)
                    funclist[0].configure(width = round(buttonwidth), height = round(buttonheight), bg = "gray22", fg = "gray99", activebackground = "gray26", relief = FLAT)
                    windowfunclist[0] = canvas.create_window((groundpositionwidth + buttondistanceleft), (groundpositionheight + ((fucforprintbuttons[0] + 6) * buttondistance) + ((fucforprintbuttons[0] + 5) * buttonheightinpixel)), window=funclist[0])

                    i = int(fucforprintbuttons[0]) + 1
                    fucforprintbuttons = []
                    fucforprintbuttons.append(i)


                root.mainloop()


                if checknumb == []:
                    checknumb = []
                elif int(checknumb[0]) == 1:
                    x = 0
                    selfvoice = []
                    checknumb = []
                elif int(checknumb[0]) == 0:
                    x = 1
                    checknumb = []

                ###### ab hier endet die Bibliothek zur Buch-größe


                ##### ab hier beginnt die Eingabe für die Buch-Größe

                if not buttonvoice == []:
                    if buttonvoice[0] == 1:

                        searchnumb = selfvoicenumber[0]

                        liste = []

                        my_save = open(".mainpoint.save", "r")
                        lines = my_save.read().splitlines()

                        for line in lines:
                            liste.append(line)

                        my_save.close()

                        booklist = []
                        pathbooklist = []
                        sizeforbooks = []
                        progressinbooks = []

                        provefrominput = []

                        firstfoldersfromlist = []

                        for i in range(0, 5):
                            firstfoldersfromlist.append(str(liste[i]))

                        r = 0
                        if not len(liste) == 5:  # wichtig zum auswerten der Speicher-Datei
                            for i in range(0, len(liste)):
                                if len(liste[i]) == 0:
                                    r = r + 1
                                elif r == 2:
                                    booklist.append(liste[i])
                                elif r == 3:
                                    pathbooklist.append(liste[i])
                                elif r == 4:
                                    sizeforbooks.append(liste[i])
                                elif r == 5:
                                    progressinbooks.append(liste[i])


                        from tkinter import *

                        windowsize = str(liste[0]) + "x" + str(liste[1])

                        root = Tk()
                        root.title("BookReader: " + str(booklist[searchnumb]))
                        root.geometry(windowsize)
                        root.configure(bg = "gray29")

                        entrysizewidth = round(0.2875 * int(liste[0]))

                        buttonwidth = round(0.03375 * int(liste[0]))

                        xachse = round(((int(liste[0]) / 2) - (entrysizewidth / 2)))
                        name = Label(root, text = ("Aktuelle Buch-Größe: " + str(sizeforbooks[searchnumb]) + "%"), bg = "gray23", fg = "gray99", activebackground = "gray26")

                        name.place(x = xachse, y = 70)

                        e1 = Entry(root, bg = "gray23", fg = "gray99")

                        e1.place(x = xachse, y = 100, width = entrysizewidth, height = 34)

                        def save():
                            abstandhalter = [""]

                            if len(e1.get()) > 0:

                                del sizeforbooks[searchnumb]

                                sizeforbooks.insert(searchnumb, str(e1.get()))

                                all_in_one = firstfoldersfromlist + abstandhalter + booklist + abstandhalter + pathbooklist + abstandhalter + sizeforbooks + abstandhalter + progressinbooks

                                my_save = open(".mainpoint.save", "w")
                                save_daten = all_in_one

                                for all in save_daten:
                                    my_save.write(all + "\n")

                                my_save.close()

                                e1.delete(0, END)

                                root.destroy()

                            checknumb.append(1)
                            root.destroy()


                        a = Button(root, text = "Speichern/Zurück", command = save, width = buttonwidth, height = 3, bg = "gray23", fg = "gray99", activebackground = "gray26")
                        a.place(x = xachse, y = 245)

                        root.mainloop()

                        if checknumb == []:
                            checknumb = []
                        elif int(checknumb[0]) == 1:
                            y = 0
                            checknumb = []
                        elif int(checknumb[0]) == 0:
                            y = 1
                            checknumb = []

































    if not selfvoice == []:
        if int(selfvoice[0]) == 0:

            z = 0
            while z == 0:
                z = 1

                from tkinter import *
                from functools import partial

                liste = []

                my_save = open(".mainpoint.save", "r")
                lines = my_save.read().splitlines()

                for line in lines:
                    liste.append(line)

                my_save.close()

                selfvoice = []
                buttonvoice = [] # abgespeichertes Ergebniss von Button Eingabe
                selfvoicenumber = [] # endgültig ausgewertetes Ergebniss in Form einer Listen-Nummer zum Suchen

                funclist = []
                listforcommand = []
                windowfunclist = []
                fucforprintbuttons = []

                checknumb = []

                booklist = []
                pathbooklist = []
                sizeforbooks = []
                progressinbooks = []

                r = 0
                if not len(liste) == 5: # wichtig zum auswerten der Speicher-Datei
                    for i in range(0, len(liste)):
                        if len(liste[i]) == 0:
                            r = r + 1
                        elif r == 2:
                            booklist.append(liste[i])
                        elif r == 3:
                            pathbooklist.append(liste[i])
                        elif r == 4:
                            sizeforbooks.append(liste[i])
                        elif r == 5:
                            progressinbooks.append(liste[i])


                buttonwidth = 0.099375 * int(liste[0]) + 1
                buttonheight = 0.00333333333 * int(liste[1]) + 1

                buttonwidthinpixel = (round(round(buttonwidth) - 1) * 8 + 33)
                buttonheightinpixel = (round(round(buttonheight) - 1) * 17 + 28)

                buttondistance = round(0.064444444 * int(liste[1])) ##############
                buttondistanceleft = round((int(liste[0]) / 2) - (int(buttonwidthinpixel) / 2))

                groundpositionwidth = round(buttonwidthinpixel / 2)
                groundpositionheight = round(buttonheightinpixel / 2)


                windowwidth = int(liste[0])
                windowheight = int(liste[1])

                root=Tk()
                root.title("BookReader: Bibiliothek")

                scrollheight = round(groundpositionheight + ((int(len(booklist)) + 6) * buttondistance) + ((int(len(booklist)) + 5) * buttonheightinpixel))

                frame=Frame(root,width=windowwidth, height=windowheight) # Hier kann man die größe des Festers einstellen.
                frame.pack(expand=True, fill=BOTH) # Das hier ist zum vervollstendigen zuständig.
                canvas=Canvas(frame, bg='gray28',width=windowwidth, height=windowheight, scrollregion=(0,0,0,scrollheight)) # die Scroll-
                # Region muss größer sein als das Fenster, damit etwas passiert
                vbar=Scrollbar(frame, orient=VERTICAL)
                vbar.pack(side=RIGHT, fill=Y)
                vbar.config(command=canvas.yview)
                canvas.config(width=windowwidth, height=windowheight)
                canvas.config(yscrollcommand=vbar.set)
                canvas.pack(side=LEFT, expand=True, fill=BOTH)

                for i in range(0, len(booklist)): # Funktionen werden hier erstellt
                    funclist.append("button" + str(i))
                    listforcommand.append("command" + str(i))
                    windowfunclist.append("button" + str(i) + "window")

                def openbook():
                    if not selfvoice == []:
                        i = int(len(selfvoice) - 1)
                        for j in range(0, len(booklist)):
                            if selfvoice[i] == booklist[j]:
                                selfvoicenumber.append(int(j))
                                buttonvoice.append(0)
                                root.destroy()

                def newbook():
                    buttonvoice.append(1)

                    root.destroy()

                def delbook():
                    if not selfvoice == []:
                        i = int(len(selfvoice) - 1)
                        for j in range(0, len(booklist)):
                            if selfvoice[i] == booklist[j]:
                                selfvoicenumber.append(int(j))
                                buttonvoice.append(4)
                                root.destroy()

                def backtomenu():
                    checknumb.append(1)
                    root.destroy()

                voicebutton = Button(root, text = "Das ausgewählte Buch aufrufen", command = openbook)
                voicebutton.configure(width = round(buttonwidth), height = round(buttonheight), bg = "gray23", fg = "gray99", activebackground = "gray26", relief = FLAT)
                windowvoicebutton = canvas.create_window((groundpositionwidth + buttondistanceleft), (groundpositionheight + ((0 + 1) * buttondistance) + ((0 + 0) * buttonheightinpixel)), window=voicebutton)

                voicebutton2 = Button(root, text = "Ein Buch hinzufügen", command = newbook)
                voicebutton2.configure(width = round(buttonwidth), height = round(buttonheight), bg = "gray23", fg = "gray99", activebackground = "gray26", relief = FLAT)
                windowvoicebutton2 = canvas.create_window((groundpositionwidth + buttondistanceleft), (groundpositionheight + ((1 + 1) * buttondistance) + ((1 + 0) * buttonheightinpixel)), window=voicebutton2)

                voicebutton4 = Button(root, text = "Ein Buch entfernen", command = delbook)
                voicebutton4.configure(width = round(buttonwidth), height = round(buttonheight), bg = "gray23", fg = "gray99", activebackground = "gray26", relief = FLAT)
                windowvoicebutton4 = canvas.create_window((groundpositionwidth + buttondistanceleft), (groundpositionheight + ((2 + 1) * buttondistance) + ((2 + 0) * buttonheightinpixel)), window=voicebutton4)

                voicebutton3 = Button(root, text = "Zurück zum Hauptmenü", command = backtomenu)
                voicebutton3.configure(width = round(buttonwidth), height = round(buttonheight), bg = "gray23", fg = "gray99", activebackground = "gray26", relief = FLAT)
                windowvoicebutton3 = canvas.create_window((groundpositionwidth + buttondistanceleft), (groundpositionheight + ((3 + 1) * buttondistance) + ((3 + 0) * buttonheightinpixel)), window=voicebutton3)


                fucforprintbuttons.append(0)

                for list in booklist :

                    cmd = partial(selfvoice.append, list)


                    funclist[0] = Button(root, text = str(booklist[fucforprintbuttons[0]]), command = cmd)
                    funclist[0].configure(width = round(buttonwidth), height = round(buttonheight), bg = "gray23", fg = "gray99", activebackground = "gray26", relief = FLAT)
                    windowfunclist[0] = canvas.create_window((groundpositionwidth + buttondistanceleft), (groundpositionheight + ((fucforprintbuttons[0] + 6) * buttondistance) + ((fucforprintbuttons[0] + 5) * buttonheightinpixel)), window=funclist[0])

                    i = int(fucforprintbuttons[0]) + 1
                    fucforprintbuttons = []
                    fucforprintbuttons.append(i)


                root.mainloop()

                ###### ab hier endet die Bibliothek


                if checknumb == []:
                    checknumb = []
                elif int(checknumb[0]) == 1:
                    x = 0
                    checknumb = []
                elif int(checknumb[0]) == 0:
                    x = 1
                    checknumb = []

                if not buttonvoice == []:
                    if buttonvoice[0] == 4:

                        checknumb = []

                        searchnumb = selfvoicenumber[0]

                        liste = []

                        my_save = open(".mainpoint.save", "r")
                        lines = my_save.read().splitlines()

                        for line in lines:
                            liste.append(line)

                        my_save.close()



                        booklist = []
                        pathbooklist = []
                        sizeforbooks = []
                        progressinbooks = []


                        r = 0
                        if not len(liste) == 5: # wichtig zum auswerten der Speicher-Datei
                            for i in range(0, len(liste)):
                                if len(liste[i]) == 0:
                                    r = r + 1
                                elif r == 2:
                                    booklist.append(liste[i])
                                elif r == 3:
                                    pathbooklist.append(liste[i])
                                elif r == 4:
                                    sizeforbooks.append(liste[i])
                                elif r == 5:
                                    progressinbooks.append(liste[i])


                        firstfoldersfromlist = []

                        for i in range(0, 5):
                            firstfoldersfromlist.append(str(liste[i]))



                        from tkinter import *

                        root = Tk()
                        root.title("BookReader: " + str(booklist[searchnumb]))
                        root.geometry(windowsize)
                        root.configure(bg = "gray29")



                        def keep():
                            root.destroy()
                            checknumb.append(1)

                        def notkeep():
                            abstandhalter = [""]

                            del booklist[searchnumb]
                            del pathbooklist[searchnumb]
                            del sizeforbooks[searchnumb]
                            del progressinbooks[searchnumb]

                            all_in_one = firstfoldersfromlist + abstandhalter + booklist + abstandhalter + pathbooklist + abstandhalter + sizeforbooks + abstandhalter + progressinbooks

                            my_save = open(".mainpoint.save", "w")
                            save_daten = all_in_one

                            for all in save_daten:
                                my_save.write(all + "\n")

                            my_save.close()

                            root.destroy()
                            checknumb.append(1)

                        a = Button(root, text = "Das Buch behalten", command = keep, width = (widthbutton + 1), height = int(endheight), bg = "gray23", fg = "gray99", activebackground = "gray26")
                        a.pack(pady = int(normalendpady))

                        b = Button(root, text = "Das Buch entfernen", command = notkeep, width = (widthbutton + 1), height = int(endheight), bg = "gray23", fg = "gray99", activebackground = "gray26")
                        b.pack()

                        root.mainloop()

                        if checknumb == []:
                            checknumb = []
                        elif int(checknumb[0]) == 1:
                            z = 0
                            checknumb = []
                        elif int(checknumb[0]) == 0:
                            z = 1
                            checknumb = []
































































                ###### ab hier beginnt das Menü zum starten des Buches

                if not buttonvoice == []:
                    if buttonvoice[0] == 0: # hier wird abgefragt, ob dieser Button gedrückt wurde
                        y = 0
                        while y == 0:
                            y = 1

                            liste = []

                            my_save = open(".mainpoint.save", "r")
                            lines = my_save.read().splitlines()

                            for line in lines:
                                liste.append(line)

                            my_save.close()

                            booklist = []
                            pathbooklist = []
                            sizeforbooks = []
                            progressinbooks = []

                            check = []

                            searchnumb = selfvoicenumber[0] # suchbegriff für Speicher

                            r = 0
                            if not len(liste) == 5: # wichtig zum auswerten der Speicher-Datei
                                for i in range(0, len(liste)):
                                    if len(liste[i]) == 0:
                                        r = r + 1
                                    elif r == 2:
                                        booklist.append(liste[i])
                                    elif r == 3:
                                        pathbooklist.append(liste[i])
                                    elif r == 4:
                                        sizeforbooks.append(liste[i])
                                    elif r == 5:
                                        progressinbooks.append(liste[i])


                            from tkinter import *

                            windowsize = str(liste[0]) + "x" + str(liste[1])

                            root = Tk()
                            root.title("BookReader: " + str(booklist[searchnumb]))
                            root.geometry(windowsize)
                            root.configure(bg = "gray28")

                            widthbutton = 28 # Standart-Wert für X-Wert

                            if int(liste[0]) < 265: # wenn Bildschrim zu klein ist, dann verändere X-Wert
                                widthbutton = 22

                            endheight = (0.005555556 * int(liste[1])) + 1 # hier wird mit Maßsstabs-Rechnungen die passende Höhe berechnet

                            normalendpady = 0.094444444 * int(liste[1])
                            otherendpady = 0.116666667 * int(liste[1])

                            def chapternow():
                                check.append(0)
                                root.destroy()

                            def chooseachapter():
                                check.append(1)
                                root.destroy()

                            def back():
                                checknumb.append(1)
                                root.destroy()

                            a = Button(root, text = "Das Buch fortsetzen", command = chapternow, width = widthbutton, height = round(endheight), bg = "gray23", fg = "gray99", activebackground = "gray26")
                            a.pack(pady = round(normalendpady))

                            b = Button(root, text = "Ein Kapitel auswählen", command = chooseachapter, width = widthbutton, height = round(endheight), bg = "gray23", fg = "gray99", activebackground = "gray26")
                            b.pack()

                            c = Button(root, text = "Zurück zu Ihrer Bibliothek", command = back, width = widthbutton, height = round(endheight), bg = "gray23", fg = "gray99", activebackground = "gray26")
                            c.pack(pady = round(otherendpady * 1.2))

                            root.mainloop()

                            #if check[0] == 2:
                            #    z = 0

                            if checknumb == []:
                                checknumb = []
                            elif int(checknumb[0]) == 1:
                                z = 0
                                checknumb = []
                            elif int(checknumb[0]) == 0:
                                z = 1
                                checknumb = []





                            ##### hier beginnt der Haupt-Teil





                            if not check == []:

                                import os

                                if check[0] == 0: # das nächste Kapitel


                                    liste = []

                                    my_save = open(".mainpoint.save", "r")
                                    lines = my_save.read().splitlines()

                                    for line in lines:
                                        liste.append(line)

                                    my_save.close()

                                    booklist = []
                                    pathbooklist = []
                                    sizeforbooks = []
                                    progressinbooks = []

                                    r = 0
                                    if not len(liste) == 5: # wichtig zum auswerten der Speicher-Datei
                                        for i in range(0, len(liste)):
                                            if len(liste[i]) == 0:
                                                r = r + 1
                                            elif r == 2:
                                                booklist.append(liste[i])
                                            elif r == 3:
                                                pathbooklist.append(liste[i])
                                            elif r == 4:
                                                sizeforbooks.append(liste[i])
                                            elif r == 5:
                                                progressinbooks.append(liste[i])



                                    # ab hier wird für das ausgewälte Buch die Daten dafür "gefiltert"


                                    vereinheitlichen_oder_nicht = liste[3]
                                    rangliste = liste[4]


                                    windowsize = str(liste[0]) + "x" + str(liste[1])


                                    chosen_book = booklist[searchnumb] # searchnumb ist die zugehörige Nummer zum ausgewählten Buch
                                    chosen_pathbook = pathbooklist[searchnumb]
                                    chosen_sizeforbook = sizeforbooks[searchnumb]
                                    chosen_progressinbooks = progressinbooks[searchnumb]

                                    chapternames = os.listdir(str(chosen_pathbook)) # mit listdir werden mit dem Pfad die Namen der Kapitel ausgwertet (als Liste)

                                    numbersfromchapter = []
                                    foldernumblist = []
                                    foldermainname = []

                                    finishedchapterpaths = [] # hier kommen die geordneten Pfade rein

                                    #### hier werden die Zahlen-Enden an den Kapitel ausgewertet und danach sortiert

                                    p3 = 0
                                    p2 = 0
                                    for i in range(0, len(chapternames)):
                                        for n in range(0, len(chapternames[i])):
                                            if re.search("[0-9]", (chapternames[i])[n]):
                                                numbersfromchapter.append(str((chapternames[i])[n]))
                                            elif re.search("[.]", (chapternames[i])[n]):
                                                numbersfromchapter.append(str((chapternames[i])[n]))
                                                p3 = 1
                                        if p3 == 1:
                                            chapternumber1 = "".join(numbersfromchapter)
                                            foldernumblist.append(float(chapternumber1))
                                            numbersfromchapter = []
                                            p3 = 0
                                        elif p3 == 0:
                                            chapternumber2 = "".join(numbersfromchapter)
                                            foldernumblist.append(int(chapternumber2))
                                            numbersfromchapter = []
                                        for n in range(0, len(chapternames[i])):
                                            if not re.search("[0-9]", (chapternames[i])[n]):
                                                p2 = p2 + 1
                                            if not re.search("[.]", (chapternames[i])[n]):
                                                p2 = p2 + 1
                                            if not re.search("[,]", (chapternames[i])[n]):
                                                p2 = p2 + 1
                                            if p2 == 3:
                                                numbersfromchapter.append((chapternames[i])[n])
                                            p2 = 0
                                        foldermain = "".join(numbersfromchapter)
                                        foldermainname.append(str(foldermain))
                                        numbersfromchapter = []

                                    sortedfoldernumblist = sorted(foldernumblist)


                                    for i in range(0, len(chapternames)):
                                        chapterpaths = str(chosen_pathbook) + "/" + foldermainname[i] + str(sortedfoldernumblist[i])
                                        finishedchapterpaths.append(str(chapterpaths))


                                    ########################

                                    ########################

                                    finishedchapternames = []

                                    for i in range(0, len(sortedfoldernumblist)):
                                        finishedchapternames.append((str(foldermainname[i]) + str(sortedfoldernumblist[i])))

                                    booklist = []
                                    pathbooklist = []
                                    sizeforbooks = []
                                    progressinbooks = []

                                    buttonvoice2 = []

                                    selfvoicechapter = [] # alle gedrückten Button

                                    endselfvoicechapter = []  # die Entscheidung welches Kapitel

                                    r = 0
                                    if not len(liste) == 5: # wichtig zum auswerten der Speicher-Datei
                                        for i in range(0, len(liste)):
                                            if len(liste[i]) == 0:
                                                r = r + 1
                                            elif r == 2:
                                                booklist.append(liste[i])
                                            elif r == 3:
                                                pathbooklist.append(liste[i])
                                            elif r == 4:
                                                sizeforbooks.append(liste[i])
                                            elif r == 5:
                                                progressinbooks.append(liste[i])



                                    from tkinter import *
                                    import os
                                    import re

                                    addition = int(progressinbooks[searchnumb])

                                    ###########

                                    xy = 0
                                    xy = xy + addition
                                    while xy < len(finishedchapterpaths):



                                        import os
                                        import re
                                        from tkinter import *
                                        from PIL import ImageTk, Image

                                        scrollimages = []

                                        checktheentry = []

                                        firstfoldersfromlist = []
                                        booklist = []
                                        pathbooklist = []
                                        sizeforbooks = []
                                        progressinbooks = []

                                        fullimagepaths = []

                                        zeichensave = []
                                        splittnumbers = []
                                        unterstrich = []
                                        splittimgmainname = []
                                        imgmainname = []
                                        imgnumb = []

                                        for i in range(0, 5):
                                            firstfoldersfromlist.append(str(liste[i]))



                                        vereinheitlichen_oder_nicht1 = []

                                        allimgheight = []

                                        liste = []

                                        my_save = open(".mainpoint.save", "r")
                                        lines = my_save.read().splitlines()

                                        for line in lines:
                                            liste.append(line)

                                        my_save.close()

                                        r = 0
                                        if not len(liste) == 5: # wichtig zum auswerten der Speicher-Datei
                                            for i in range(0, len(liste)):
                                                if len(liste[i]) == 0:
                                                    r = r + 1
                                                elif r == 2:
                                                    booklist.append(liste[i])
                                                elif r == 3:
                                                    pathbooklist.append(liste[i])
                                                elif r == 4:
                                                    sizeforbooks.append(liste[i])
                                                elif r == 5:
                                                    progressinbooks.append(liste[i])

                                        vereinheitlichen_oder_nicht1.append(liste[3])


                                        path = str(finishedchapterpaths[xy])
                                        imglist = os.listdir(path)


                                        (imglist[0])

                                        for i in range(0, len(imglist)):
                                            x = 0
                                            end = -0
                                            while x == 0:
                                                if re.search("[0-9]", (imglist[i])[end]): # prüft die erste Stelle, ob sie 1-9 ist
                                                    if not re.search("[0-9]", (imglist[i])[end + -1]):
                                                        x = 1
                                                        zeichensave.append(int(end))
                                                end = end + -1


                                        for i in range(0, len(imglist)):
                                            zahlenauswertung = zeichensave[i]
                                            for r in range(0, 3):
                                                if re.search("[0-9]", (imglist[i])[zahlenauswertung]):
                                                    splittnumbers.append((imglist[i])[zahlenauswertung])
                                                zahlenauswertung = zahlenauswertung + 1

                                            trennzeichen = ""
                                            fullnumb = trennzeichen.join(splittnumbers)
                                            imgnumb.append(int(fullnumb))
                                            splittnumbers = []

                                        x = 0
                                        for i in range(0, len(imglist[0])):
                                            if re.search("[.]", (imglist[0])[i]):
                                                for r in range(0, 6):
                                                    x = x + 1
                                                    if not re.search("[0-9]", (imglist[0])[i - x]):
                                                        unterstrich.append(int(i - x))

                                        for i in range(0, (unterstrich[0] + 1)):
                                            splittimgmainname.append((imglist[0])[i])

                                        hallo = ""
                                        fullname = hallo.join(splittimgmainname)
                                        imgmainname.append(fullname)

                                        sortedimgnumb = sorted(imgnumb)

                                        ##### ab hier beginnt der Visualisierungs-Teil

                                        for xe in range(0, len(sortedimgnumb)):

                                            splittforend = []
                                            forend = []
                                            endung = []

                                            customallimagewidth = []

                                            splittforend.append((imglist[0])[-3])
                                            splittforend.append((imglist[0])[-2])
                                            splittforend.append((imglist[0])[-1])

                                            full = str(splittforend[0]) + str(splittforend[1]) + str(splittforend[2])
                                            forend.append(full)

                                            if str(forend[0]) == "jpg":
                                                endung = ".jpg"
                                            elif str(forend[0]) == "png":
                                                endung = ".png"

                                            imagepaths = str(finishedchapterpaths[xy]) + "/" + str(fullname) + str(sortedimgnumb[xe]) + endung
                                            fullimagepaths.append(imagepaths)

                                        allimgheight = 0

                                        if int(vereinheitlichen_oder_nicht1[0]) == 0:
                                            for i in range(0, len(fullimagepaths)):
                                                im = Image.open(fullimagepaths[i])
                                                w, h = im.size
                                                w = round(w * (float(sizeforbooks[searchnumb]) / 100))
                                                h = round(h * (float(sizeforbooks[searchnumb]) / 100))
                                                im = im.resize((w, h))
                                                allimgheight = allimgheight + int(h)


                                        if int(vereinheitlichen_oder_nicht1[0]) == 1:
                                            allwidth = 0
                                            for i in range(0, len(fullimagepaths)):
                                                im = Image.open(fullimagepaths[i])
                                                w, h = im.size
                                                allwidth = allwidth + w
                                            customallimagewidth.append(round(allwidth / int(len(fullimagepaths))))
                                            for i in range(0, len(fullimagepaths)):
                                                im = Image.open(fullimagepaths[i])
                                                w, h = im.size
                                                prozent = int(customallimagewidth[0]) / int(w)
                                                w = round((prozent * w) * (float(sizeforbooks[searchnumb]) / 100))
                                                h = round((prozent * h) * (float(sizeforbooks[searchnumb]) / 100))
                                                im = im.resize((w, h))
                                                allimgheight = allimgheight + int(h)


                                        for i in range(0, len(fullimagepaths)):
                                            scrollimages.append(str("image" + str(i)))

                                        allimgheight = allimgheight + 700


                                        tkname = str(foldermainname[0]) + str(sortedfoldernumblist[xy])

                                        checkforbook = []


                                        root=Tk()
                                        root.title(tkname)

                                        w = 0
                                        h = 0

                                        windowwidth = int(liste[0])
                                        windowheight = int(liste[1])

                                        frame=Frame(root,width=windowwidth, height=windowheight) # Hier kann man die größe des Festers einstellen.
                                        frame.pack(expand=True, fill=BOTH) # Das hier ist zum vervollstendigen zuständig.
                                        canvas=Canvas(frame, bg='black',width=windowwidth, height=windowheight, scrollregion=(0,0,0,allimgheight)) # die Scroll-
                                        # Region muss größer sein als das Fenster, damit etwas passiert
                                        vbar=Scrollbar(frame, orient=VERTICAL)
                                        vbar.pack(side=RIGHT, fill=Y)
                                        vbar.config(command=canvas.yview)
                                        canvas.config(width=windowwidth, height=windowheight)
                                        canvas.config(yscrollcommand=vbar.set)
                                        canvas.pack(side=LEFT, expand=True, fill=BOTH)

                                        if int(vereinheitlichen_oder_nicht1[0]) == 0:
                                            scrollheight = 350
                                            for i in range(0, len(fullimagepaths)):
                                                im2 = Image.open(fullimagepaths[i])
                                                w, h = im2.size
                                                w = round(w * (float(sizeforbooks[searchnumb]) / 100))
                                                h = round(h * (float(sizeforbooks[searchnumb]) / 100))
                                                im2 = im2.resize((w, h))

                                                forscrollimages = windowwidth - w
                                                widthimgplus = forscrollimages/2
                                                scrollimages[i] = ImageTk.PhotoImage(im2)
                                                canvas.create_image(widthimgplus, scrollheight, image=scrollimages[i], anchor='nw')
                                                scrollheight = scrollheight + h


                                        if int(vereinheitlichen_oder_nicht1[0]) == 1:
                                            scrollheight = 350
                                            for i in range(0, len(fullimagepaths)):
                                                im2 = Image.open(fullimagepaths[i])
                                                w, h = im2.size
                                                prozent = int(customallimagewidth[0]) / int(w)
                                                w = round((prozent * w) * (float(sizeforbooks[searchnumb]) / 100))
                                                h = round((prozent * h) * (float(sizeforbooks[searchnumb]) / 100))
                                                im2 = im2.resize((w, h))

                                                forscrollimages = windowwidth - w
                                                widthimgplus = forscrollimages/2
                                                scrollimages[i] = ImageTk.PhotoImage(im2)
                                                canvas.create_image(widthimgplus, scrollheight, image=scrollimages[i], anchor='nw')
                                                scrollheight = scrollheight + h

                                        def saveindata():

                                            abstandhalter = [""]

                                            del progressinbooks[searchnumb]

                                            progressinbooks.insert(searchnumb, str(xy))

                                            all_in_one = firstfoldersfromlist + abstandhalter + booklist + abstandhalter + pathbooklist + abstandhalter + sizeforbooks + abstandhalter + progressinbooks

                                            my_save = open(".mainpoint.save", "w")
                                            save_daten = all_in_one

                                            for all in save_daten:
                                                my_save.write(all + "\n")

                                            my_save.close()

                                    #
                                    #                                                def saveindataandback():

                                        def nextchapterstart():
                                            root.destroy()
                                            checkforbook.append(1)

                                        def lastchapterstart():
                                            root.destroy()
                                            checkforbook.append(0)

                                        def backtomenu():
                                            root.destroy()
                                            checkforbook.append(10)
                                            checktheentry.append(1)

                                        def backtomenuandsave():
                                            root.destroy()
                                            checkforbook.append(1)

                                            abstandhalter = [""]

                                            del progressinbooks[searchnumb]

                                            progressinbooks.insert(searchnumb, str(int(xy) + 1))

                                            all_in_one = firstfoldersfromlist + abstandhalter + booklist + abstandhalter + pathbooklist + abstandhalter + sizeforbooks + abstandhalter + progressinbooks

                                            my_save = open(".mainpoint.save", "w")
                                            save_daten = all_in_one

                                            for all in save_daten:
                                                my_save.write(all + "\n")

                                            my_save.close()

                                        saveandornextbuttonwidth = round((36 / 1600) * int(liste[0]))
                                        saveandornextbuttonheight = round((6 / 1600) * int(liste[0]))

                                        weiterundzurückwidth = round((20 / 1600) * int(liste[0]))
                                        weiterundzurückheight = round((5 / 1600) * int(liste[0]))

                                        zurückzummenüwidth = round((60 / 1600) * int(liste[0]))
                                        zurückzummenüheight = round((4.4 / 1600) * int(liste[0]))

                                        mittewidthmain = round(int(liste[0]) / 2) # weil es schon um die helfte in der wand steckt
                                        mitteheightmain = round(450 / 2) # weil es schon um die helfte in der wand steckt

                                        mittewidthzurück = round((int(liste[0]) / 2) / 2)
                                        mitteheightzurück = round(450 / 2)

                                        mittewidthweiter = round(int(mittewidthzurück) + int(mittewidthmain))
                                        mitteheightweiter = round(450 / 2)

                                        halfeformmainbutton = round(round((zurückzummenüheight - 1) * 17 + 28) / 2)

                                        mittezurückzummenüwidth = round(int(liste[0]) / 2)
                                        mittezurückzummenüheight = round(round(225 / 2) - halfeformmainbutton)


                                        xyfordef = 0
                                        xyfordef = xy + 1


                                        button1 = Button(root, text = "Speichern", command = saveindata)
                                        button1.configure(width = saveandornextbuttonwidth, height = saveandornextbuttonheight, bg = "gray19", fg = "gray99", activebackground = "gray23", relief = FLAT)
                                        button1_window = canvas.create_window(mittewidthmain, mitteheightmain, window=button1)

                                        if not xy == 0:
                                            button2 = Button(root, text = "Zurück", command = lastchapterstart)
                                            button2.configure(width = weiterundzurückwidth, height = weiterundzurückheight, bg = "gray19", fg = "gray99", activebackground = "gray23", relief = FLAT)
                                            button2_window = canvas.create_window(mittewidthzurück, mitteheightzurück, window=button2)

                                        if not xyfordef == len(finishedchapterpaths):
                                            button3 = Button(root, text = "Weiter", command = nextchapterstart)
                                            button3.configure(width = weiterundzurückwidth, height = weiterundzurückheight, bg = "gray19", fg = "gray99", activebackground = "gray23", relief = FLAT)
                                            button3_window = canvas.create_window(mittewidthweiter, mitteheightweiter, window=button3)

                                        button3 = Button(root, text = "Zurück zum Menü", command = backtomenu)
                                        button3.configure(width = zurückzummenüwidth, height = zurückzummenüheight, bg = "gray19", fg = "gray99", activebackground = "gray23", relief = FLAT)
                                        button3_window = canvas.create_window(mittezurückzummenüwidth, mittezurückzummenüheight, window=button3)

                                        ####
                                        if not xyfordef == len(finishedchapterpaths):
                                            button3 = Button(root, text = "Speichern u. weiter", command = backtomenuandsave)
                                            button3.configure(width = saveandornextbuttonwidth, height = saveandornextbuttonheight, bg = "gray19", fg = "gray99", activebackground = "gray23", relief = FLAT)
                                            button3_window = canvas.create_window(mittewidthmain, round(allimgheight - 175), window=button3)


                                        if not xy == 0:
                                            button4 = Button(root, text = "Zurück", command = lastchapterstart)
                                            button4.configure(width = weiterundzurückwidth, height = weiterundzurückheight, bg = "gray19", fg = "gray99", activebackground = "gray23", relief = FLAT)
                                            button4_window = canvas.create_window(mittewidthzurück, round(allimgheight - 175), window=button4)

                                        if not xyfordef == len(finishedchapterpaths):
                                            button5 = Button(root, text = "Weiter", command = nextchapterstart)
                                            button5.configure(width = weiterundzurückwidth, height = weiterundzurückheight, bg = "gray19", fg = "gray99", activebackground = "gray23", relief = FLAT)
                                            button5_window = canvas.create_window(mittewidthweiter, round(allimgheight - 175), window=button5)


                                        root.mainloop()


                                        if not checkforbook == []:
                                            if int(checkforbook[0]) == 1:
                                                xy = xy + 1
                                                checkforbook == []
                                            if int(checkforbook[0]) == 0:
                                                xy = xy - 1
                                                checkforbook == []

                                        if checkforbook == []:
                                            break

                                        ###

                                        if not checktheentry == []:
                                            if int(checktheentry[0]) == 1:
                                                y = 0
                                                xy = int(len(finishedchapterpaths) + 10)

















































                                if check[0] == 1: # ein Kapitel auswählen

                                    df = 0
                                    while df == 0:

                                        df = 1

                                        liste = []

                                        my_save = open(".mainpoint.save", "r")
                                        lines = my_save.read().splitlines()

                                        for line in lines:
                                            liste.append(line)

                                        my_save.close()

                                        booklist = []
                                        pathbooklist = []
                                        sizeforbooks = []
                                        progressinbooks = []

                                        r = 0
                                        if not len(liste) == 5: # wichtig zum auswerten der Speicher-Datei
                                            for i in range(0, len(liste)):
                                                if len(liste[i]) == 0:
                                                    r = r + 1
                                                elif r == 2:
                                                    booklist.append(liste[i])
                                                elif r == 3:
                                                    pathbooklist.append(liste[i])
                                                elif r == 4:
                                                    sizeforbooks.append(liste[i])
                                                elif r == 5:
                                                    progressinbooks.append(liste[i])



                                        # ab hier wird für das ausgewälte Buch die Daten dafür "gefiltert"


                                        vereinheitlichen_oder_nicht = liste[3]
                                        rangliste = liste[4]


                                        windowsize = str(liste[0]) + "x" + str(liste[1])


                                        chosen_book = booklist[searchnumb] # searchnumb ist die zugehörige Nummer zum ausgewählten Buch
                                        chosen_pathbook = pathbooklist[searchnumb]
                                        chosen_sizeforbook = sizeforbooks[searchnumb]
                                        chosen_progressinbooks = progressinbooks[searchnumb]

                                        chapternames = os.listdir(str(chosen_pathbook)) # mit listdir werden mit dem Pfad die Namen der Kapitel ausgwertet (als Liste)

                                        numbersfromchapter = []
                                        foldernumblist = []
                                        foldermainname = []

                                        finishedchapterpaths = [] # hier kommen die geordneten Pfade rein

                                        #### hier werden die Zahlen-Enden an den Kapitel ausgewertet und danach sortiert

                                        p3 = 0
                                        p2 = 0
                                        for i in range(0, len(chapternames)):
                                            for n in range(0, len(chapternames[i])):
                                                if re.search("[0-9]", (chapternames[i])[n]):
                                                    numbersfromchapter.append(str((chapternames[i])[n]))
                                                elif re.search("[.]", (chapternames[i])[n]):
                                                    numbersfromchapter.append(str((chapternames[i])[n]))
                                                    p3 = 1
                                            if p3 == 1:
                                                chapternumber1 = "".join(numbersfromchapter)
                                                foldernumblist.append(float(chapternumber1))
                                                numbersfromchapter = []
                                                p3 = 0
                                            elif p3 == 0:
                                                chapternumber2 = "".join(numbersfromchapter)
                                                foldernumblist.append(int(chapternumber2))
                                                numbersfromchapter = []
                                            for n in range(0, len(chapternames[i])):
                                                if not re.search("[0-9]", (chapternames[i])[n]):
                                                    p2 = p2 + 1
                                                if not re.search("[.]", (chapternames[i])[n]):
                                                    p2 = p2 + 1
                                                if not re.search("[,]", (chapternames[i])[n]):
                                                    p2 = p2 + 1
                                                if p2 == 3:
                                                    numbersfromchapter.append((chapternames[i])[n])
                                                p2 = 0
                                            foldermain = "".join(numbersfromchapter)
                                            foldermainname.append(str(foldermain))
                                            numbersfromchapter = []

                                        sortedfoldernumblist = sorted(foldernumblist)


                                        for i in range(0, len(chapternames)):
                                            chapterpaths = str(chosen_pathbook) + "/" + foldermainname[i] + str(sortedfoldernumblist[i])
                                            finishedchapterpaths.append(str(chapterpaths))

                                        ########################

                                        ########################

                                        finishedchapternames = []

                                        for i in range(0, len(sortedfoldernumblist)):
                                            finishedchapternames.append((str(foldermainname[i]) + str(sortedfoldernumblist[i])))

                                        booklist = []
                                        pathbooklist = []
                                        sizeforbooks = []
                                        progressinbooks = []

                                        buttonvoice2 = []

                                        selfvoicechapter = [] # alle gedrückten Button

                                        endselfvoicechapter = []  # die Entscheidung welches Kapitel

                                        r = 0
                                        if not len(liste) == 5: # wichtig zum auswerten der Speicher-Datei
                                            for i in range(0, len(liste)):
                                                if len(liste[i]) == 0:
                                                    r = r + 1
                                                elif r == 2:
                                                    booklist.append(liste[i])
                                                elif r == 3:
                                                    pathbooklist.append(liste[i])
                                                elif r == 4:
                                                    sizeforbooks.append(liste[i])
                                                elif r == 5:
                                                    progressinbooks.append(liste[i])


                                        buttonwidth = 0.099375 * int(liste[0]) + 1
                                        buttonheight = 0.00333333333 * int(liste[1]) + 1

                                        buttonwidthinpixel = (round(round(buttonwidth) - 1) * 8 + 33)
                                        buttonheightinpixel = (round(round(buttonheight) - 1) * 17 + 28)

                                        buttondistance = round(0.064444444 * int(liste[1])) ##############
                                        buttondistanceleft = round((int(liste[0]) / 2) - (int(buttonwidthinpixel) / 2))

                                        groundpositionwidth = round(buttonwidthinpixel / 2)
                                        groundpositionheight = round(buttonheightinpixel / 2)


                                        windowwidth = int(liste[0])
                                        windowheight = int(liste[1])

                                        root=Tk()
                                        root.title("BookReader: " + str(booklist[searchnumb]))

                                        scrollheight = round(groundpositionheight + ((int(len(finishedchapternames)) + 6) * buttondistance) + ((int(len(finishedchapternames)) + 5) * buttonheightinpixel))

                                        frame=Frame(root,width=windowwidth, height=windowheight) # Hier kann man die größe des Festers einstellen.
                                        frame.pack(expand=True, fill=BOTH) # Das hier ist zum vervollstendigen zuständig.
                                        canvas=Canvas(frame, bg='gray28',width=windowwidth, height=windowheight, scrollregion=(0,0,0,scrollheight)) # die Scroll-
                                        # Region muss größer sein als das Fenster, damit etwas passiert
                                        vbar=Scrollbar(frame, orient=VERTICAL)
                                        vbar.pack(side=RIGHT, fill=Y)
                                        vbar.config(command=canvas.yview)
                                        canvas.config(width=windowwidth, height=windowheight)
                                        canvas.config(yscrollcommand=vbar.set)
                                        canvas.pack(side=LEFT, expand=True, fill=BOTH)

                                        for i in range(0, len(booklist)): # Funktionen werden hier erstellt
                                            funclist.append("button" + str(i))
                                            listforcommand.append("command" + str(i))
                                            windowfunclist.append("button" + str(i) + "window")

                                        def openbook():
                                            if not selfvoice == []:
                                                i = int(len(selfvoicechapter) - 1)
                                                for j in range(0, len(finishedchapternames)):
                                                    if str(selfvoicechapter[i]) == str(finishedchapternames[j]):
                                                        endselfvoicechapter.append(int(j))
                                                        buttonvoice2.append(0)
                                                        root.destroy()



                                        def backtomenu():
                                            checknumb.append(1)
                                            root.destroy()

                                        voicebutton = Button(root, text = "Das ausgewählte Kapitel aufrufen", command = openbook)
                                        voicebutton.configure(width = round(buttonwidth), height = round(buttonheight), bg = "gray22", fg = "gray99", activebackground = "gray26", relief = FLAT)
                                        windowvoicebutton = canvas.create_window((groundpositionwidth + buttondistanceleft), (groundpositionheight + ((0 + 1) * buttondistance) + ((0 + 0) * buttonheightinpixel)), window=voicebutton)

                                        voicebutton2 = Button(root, text = "Zurück", command = backtomenu)
                                        voicebutton2.configure(width = round(buttonwidth), height = round(buttonheight), bg = "gray22", fg = "gray99", activebackground = "gray26", relief = FLAT)
                                        windowvoicebutton2 = canvas.create_window((groundpositionwidth + buttondistanceleft), (groundpositionheight + ((1 + 1) * buttondistance) + ((1 + 0) * buttonheightinpixel)), window=voicebutton2)


                                        fucforprintbuttons = []

                                        fucforprintbuttons.append(0)

                                        for list in finishedchapternames:

                                            cmd = partial(selfvoicechapter.append, list)

                                            funclist[0] = Button(root, text = str(finishedchapternames[fucforprintbuttons[0]]), command = cmd)
                                            funclist[0].configure(width = round(buttonwidth), height = round(buttonheight), bg = "gray22", fg = "gray99", activebackground = "gray26", relief = FLAT)
                                            windowfunclist[0] = canvas.create_window((groundpositionwidth + buttondistanceleft), (groundpositionheight + ((fucforprintbuttons[0] + 6) * buttondistance) + ((fucforprintbuttons[0] + 5) * buttonheightinpixel)), window=funclist[0])

                                            i = int(fucforprintbuttons[0]) + 1
                                            fucforprintbuttons = []
                                            fucforprintbuttons.append(i)


                                        root.mainloop()

                                        # print(finishedchapternames[endselfvoicechapter[0]]) #endselfvoicechapter[0] ist der suchbegiff für gewählte Kapitel

                                        if checknumb == []:
                                            checknumb = []
                                        elif int(checknumb[0]) == 1:
                                            y = 0
                                            checknumb = []
                                        elif int(checknumb[0]) == 0:
                                            y = 1
                                            checknumb = []

                                        ##### hier werden die Namen der Bilder ausgewertet

                                        if not buttonvoice2 == []:

                                            if int(buttonvoice2[0]) == 0:

                                                from tkinter import *
                                                import os
                                                import re

                                                addition = int(endselfvoicechapter[0])

                                                ############


                                                xy = 0
                                                xy = xy + addition
                                                while xy < len(finishedchapterpaths):

                                                    import os
                                                    import re
                                                    from tkinter import *
                                                    from PIL import ImageTk, Image

                                                    scrollimages = []

                                                    checktheentry = []

                                                    firstfoldersfromlist = []
                                                    booklist = []
                                                    pathbooklist = []
                                                    sizeforbooks = []
                                                    progressinbooks = []

                                                    fullimagepaths = []

                                                    zeichensave = []
                                                    splittnumbers = []
                                                    unterstrich = []
                                                    splittimgmainname = []
                                                    imgmainname = []
                                                    imgnumb = []

                                                    for i in range(0, 5):
                                                        firstfoldersfromlist.append(str(liste[i]))



                                                    vereinheitlichen_oder_nicht1 = []

                                                    allimgheight = []

                                                    liste = []

                                                    my_save = open(".mainpoint.save", "r")
                                                    lines = my_save.read().splitlines()

                                                    for line in lines:
                                                        liste.append(line)

                                                    my_save.close()

                                                    r = 0
                                                    if not len(liste) == 5: # wichtig zum auswerten der Speicher-Datei
                                                        for i in range(0, len(liste)):
                                                            if len(liste[i]) == 0:
                                                                r = r + 1
                                                            elif r == 2:
                                                                booklist.append(liste[i])
                                                            elif r == 3:
                                                                pathbooklist.append(liste[i])
                                                            elif r == 4:
                                                                sizeforbooks.append(liste[i])
                                                            elif r == 5:
                                                                progressinbooks.append(liste[i])

                                                    vereinheitlichen_oder_nicht1.append(liste[3])


                                                    path = str(finishedchapterpaths[xy])
                                                    imglist = os.listdir(path)


                                                    (imglist[0])

                                                    for i in range(0, len(imglist)):
                                                        x = 0
                                                        end = -0
                                                        while x == 0:
                                                            if re.search("[0-9]", (imglist[i])[end]): # prüft die erste Stelle, ob sie 1-9 ist
                                                                if not re.search("[0-9]", (imglist[i])[end + -1]):
                                                                    x = 1
                                                                    zeichensave.append(int(end))
                                                            end = end + -1


                                                    for i in range(0, len(imglist)):
                                                        zahlenauswertung = zeichensave[i]
                                                        for r in range(0, 3):
                                                            if re.search("[0-9]", (imglist[i])[zahlenauswertung]):
                                                                splittnumbers.append((imglist[i])[zahlenauswertung])
                                                            zahlenauswertung = zahlenauswertung + 1

                                                        trennzeichen = ""
                                                        fullnumb = trennzeichen.join(splittnumbers)
                                                        imgnumb.append(int(fullnumb))
                                                        splittnumbers = []

                                                    x = 0
                                                    for i in range(0, len(imglist[0])):
                                                        if re.search("[.]", (imglist[0])[i]):
                                                            for r in range(0, 6):
                                                                x = x + 1
                                                                if not re.search("[0-9]", (imglist[0])[i - x]):
                                                                    unterstrich.append(int(i - x))

                                                    for i in range(0, (unterstrich[0] + 1)):
                                                        splittimgmainname.append((imglist[0])[i])

                                                    hallo = ""
                                                    fullname = hallo.join(splittimgmainname)
                                                    imgmainname.append(fullname)

                                                    sortedimgnumb = sorted(imgnumb)

                                                    ##### ab hier beginnt der Visualisierungs-Teil

                                                    for xe in range(0, len(sortedimgnumb)):

                                                        splittforend = []
                                                        forend = []
                                                        endung = []

                                                        customallimagewidth = []

                                                        splittforend.append((imglist[0])[-3])
                                                        splittforend.append((imglist[0])[-2])
                                                        splittforend.append((imglist[0])[-1])

                                                        full = str(splittforend[0]) + str(splittforend[1]) + str(splittforend[2])
                                                        forend.append(full)

                                                        if str(forend[0]) == "jpg":
                                                            endung = ".jpg"
                                                        elif str(forend[0]) == "png":
                                                            endung = ".png"

                                                        imagepaths = str(finishedchapterpaths[xy]) + "/" + str(fullname) + str(sortedimgnumb[xe]) + endung
                                                        fullimagepaths.append(imagepaths)

                                                    allimgheight = 0

                                                    if int(vereinheitlichen_oder_nicht1[0]) == 0:
                                                        for i in range(0, len(fullimagepaths)):
                                                            im = Image.open(fullimagepaths[i])
                                                            w, h = im.size
                                                            w = round(w * (float(sizeforbooks[searchnumb]) / 100))
                                                            h = round(h * (float(sizeforbooks[searchnumb]) / 100))
                                                            im = im.resize((w, h))
                                                            allimgheight = allimgheight + int(h)


                                                    if int(vereinheitlichen_oder_nicht1[0]) == 1:
                                                        allwidth = 0
                                                        for i in range(0, len(fullimagepaths)):
                                                            im = Image.open(fullimagepaths[i])
                                                            w, h = im.size
                                                            allwidth = allwidth + w
                                                        customallimagewidth.append(round(allwidth / int(len(fullimagepaths))))
                                                        for i in range(0, len(fullimagepaths)):
                                                            im = Image.open(fullimagepaths[i])
                                                            w, h = im.size
                                                            prozent = int(customallimagewidth[0]) / int(w)
                                                            w = round((prozent * w) * (float(sizeforbooks[searchnumb]) / 100))
                                                            h = round((prozent * h) * (float(sizeforbooks[searchnumb]) / 100))
                                                            im = im.resize((w, h))
                                                            allimgheight = allimgheight + int(h)


                                                    for i in range(0, len(fullimagepaths)):
                                                        scrollimages.append(str("image" + str(i)))

                                                    allimgheight = allimgheight + 700


                                                    tkname = str(foldermainname[0]) + str(sortedfoldernumblist[xy])

                                                    checkforbook = []


                                                    root=Tk()
                                                    root.title(tkname)

                                                    w = 0
                                                    h = 0

                                                    windowwidth = int(liste[0])
                                                    windowheight = int(liste[1])

                                                    frame=Frame(root,width=windowwidth, height=windowheight) # Hier kann man die größe des Festers einstellen.
                                                    frame.pack(expand=True, fill=BOTH) # Das hier ist zum vervollstendigen zuständig.
                                                    canvas=Canvas(frame, bg='black',width=windowwidth, height=windowheight, scrollregion=(0,0,0,allimgheight)) # die Scroll-
                                                    # Region muss größer sein als das Fenster, damit etwas passiert
                                                    vbar=Scrollbar(frame, orient=VERTICAL)
                                                    vbar.pack(side=RIGHT, fill=Y)
                                                    vbar.config(command=canvas.yview)
                                                    canvas.config(width=windowwidth, height=windowheight)
                                                    canvas.config(yscrollcommand=vbar.set)
                                                    canvas.pack(side=LEFT, expand=True, fill=BOTH)

                                                    if int(vereinheitlichen_oder_nicht1[0]) == 0:
                                                        scrollheight = 350
                                                        for i in range(0, len(fullimagepaths)):
                                                            im2 = Image.open(fullimagepaths[i])
                                                            w, h = im2.size
                                                            w = round(w * (float(sizeforbooks[searchnumb]) / 100))
                                                            h = round(h * (float(sizeforbooks[searchnumb]) / 100))
                                                            im2 = im2.resize((w, h))

                                                            forscrollimages = windowwidth - w
                                                            widthimgplus = forscrollimages/2
                                                            scrollimages[i] = ImageTk.PhotoImage(im2)
                                                            canvas.create_image(widthimgplus, scrollheight, image=scrollimages[i], anchor='nw')
                                                            scrollheight = scrollheight + h


                                                    if int(vereinheitlichen_oder_nicht1[0]) == 1:
                                                        scrollheight = 350
                                                        for i in range(0, len(fullimagepaths)):
                                                            im2 = Image.open(fullimagepaths[i])
                                                            w, h = im2.size
                                                            prozent = int(customallimagewidth[0]) / int(w)
                                                            w = round((prozent * w) * (float(sizeforbooks[searchnumb]) / 100))
                                                            h = round((prozent * h) * (float(sizeforbooks[searchnumb]) / 100))
                                                            im2 = im2.resize((w, h))

                                                            forscrollimages = windowwidth - w
                                                            widthimgplus = forscrollimages/2
                                                            scrollimages[i] = ImageTk.PhotoImage(im2)
                                                            canvas.create_image(widthimgplus, scrollheight, image=scrollimages[i], anchor='nw')
                                                            scrollheight = scrollheight + h

                                                    def saveindata():

                                                        abstandhalter = [""]

                                                        del progressinbooks[searchnumb]

                                                        progressinbooks.insert(searchnumb, str(xy))

                                                        all_in_one = firstfoldersfromlist + abstandhalter + booklist + abstandhalter + pathbooklist + abstandhalter + sizeforbooks + abstandhalter + progressinbooks

                                                        my_save = open(".mainpoint.save", "w")
                                                        save_daten = all_in_one

                                                        for all in save_daten:
                                                            my_save.write(all + "\n")

                                                        my_save.close()

    #
    #                                                def saveindataandback():

                                                    def nextchapterstart():
                                                        root.destroy()
                                                        checkforbook.append(1)

                                                    def lastchapterstart():
                                                        root.destroy()
                                                        checkforbook.append(0)

                                                    def backtomenu():
                                                        root.destroy()
                                                        checkforbook.append(10)
                                                        checktheentry.append(1)

                                                    def backtomenuandsave():
                                                        root.destroy()
                                                        checkforbook.append(1)

                                                        abstandhalter = [""]

                                                        del progressinbooks[searchnumb]

                                                        progressinbooks.insert(searchnumb, str(int(xy) + 1))

                                                        all_in_one = firstfoldersfromlist + abstandhalter + booklist + abstandhalter + pathbooklist + abstandhalter + sizeforbooks + abstandhalter + progressinbooks

                                                        my_save = open(".mainpoint.save", "w")
                                                        save_daten = all_in_one

                                                        for all in save_daten:
                                                            my_save.write(all + "\n")

                                                        my_save.close()

                                                    saveandornextbuttonwidth = round((36 / 1600) * int(liste[0]))
                                                    saveandornextbuttonheight = round((6 / 1600) * int(liste[0]))

                                                    weiterundzurückwidth = round((20 / 1600) * int(liste[0]))
                                                    weiterundzurückheight = round((5 / 1600) * int(liste[0]))

                                                    zurückzummenüwidth = round((60 / 1600) * int(liste[0]))
                                                    zurückzummenüheight = round((4.4 / 1600) * int(liste[0]))

                                                    mittewidthmain = round(int(liste[0]) / 2) # weil es schon um die helfte in der wand steckt
                                                    mitteheightmain = round(450 / 2) # weil es schon um die helfte in der wand steckt

                                                    mittewidthzurück = round((int(liste[0]) / 2) / 2)
                                                    mitteheightzurück = round(450 / 2)

                                                    mittewidthweiter = round(int(mittewidthzurück) + int(mittewidthmain))
                                                    mitteheightweiter = round(450 / 2)

                                                    halfeformmainbutton = round(round((zurückzummenüheight - 1) * 17 + 28) / 2)

                                                    mittezurückzummenüwidth = round(int(liste[0]) / 2)
                                                    mittezurückzummenüheight = round(round(225 / 2) - halfeformmainbutton)


                                                    xyfordef = 0
                                                    xyfordef = xy + 1


                                                    button1 = Button(root, text = "Speichern", command = saveindata)
                                                    button1.configure(width = saveandornextbuttonwidth, height = saveandornextbuttonheight, bg = "gray19", fg = "gray99", activebackground = "gray23", relief = FLAT)
                                                    button1_window = canvas.create_window(mittewidthmain, mitteheightmain, window=button1)

                                                    if not xy == 0:
                                                        button2 = Button(root, text = "Zurück", command = lastchapterstart)
                                                        button2.configure(width = weiterundzurückwidth, height = weiterundzurückheight, bg = "gray19", fg = "gray99", activebackground = "gray23", relief = FLAT)
                                                        button2_window = canvas.create_window(mittewidthzurück, mitteheightzurück, window=button2)

                                                    if not xyfordef == len(finishedchapterpaths):
                                                        button3 = Button(root, text = "Weiter", command = nextchapterstart)
                                                        button3.configure(width = weiterundzurückwidth, height = weiterundzurückheight, bg = "gray19", fg = "gray99", activebackground = "gray23", relief = FLAT)
                                                        button3_window = canvas.create_window(mittewidthweiter, mitteheightweiter, window=button3)

                                                    button3 = Button(root, text = "Zurück zum Menü", command = backtomenu)
                                                    button3.configure(width = zurückzummenüwidth, height = zurückzummenüheight, bg = "gray19", fg = "gray99", activebackground = "gray23", relief = FLAT)
                                                    button3_window = canvas.create_window(mittezurückzummenüwidth, mittezurückzummenüheight, window=button3)

                                                    ####
                                                    if not xyfordef == len(finishedchapterpaths):
                                                        button3 = Button(root, text = "Speichern u. weiter", command = backtomenuandsave)
                                                        button3.configure(width = saveandornextbuttonwidth, height = saveandornextbuttonheight, bg = "gray19", fg = "gray99", activebackground = "gray23", relief = FLAT)
                                                        button3_window = canvas.create_window(mittewidthmain, round(allimgheight - 175), window=button3)


                                                    if not xy == 0:
                                                        button4 = Button(root, text = "Zurück", command = lastchapterstart)
                                                        button4.configure(width = weiterundzurückwidth, height = weiterundzurückheight, bg = "gray19", fg = "gray99", activebackground = "gray23", relief = FLAT)
                                                        button4_window = canvas.create_window(mittewidthzurück, round(allimgheight - 175), window=button4)

                                                    if not xyfordef == len(finishedchapterpaths):
                                                        button5 = Button(root, text = "Weiter", command = nextchapterstart)
                                                        button5.configure(width = weiterundzurückwidth, height = weiterundzurückheight, bg = "gray19", fg = "gray99", activebackground = "gray23", relief = FLAT)
                                                        button5_window = canvas.create_window(mittewidthweiter, round(allimgheight - 175), window=button5)


                                                    root.mainloop()


                                                    if not checkforbook == []:
                                                        if int(checkforbook[0]) == 1:
                                                            xy = xy + 1
                                                            checkforbook == []
                                                        if int(checkforbook[0]) == 0:
                                                            xy = xy - 1
                                                            checkforbook == []

                                                    if checkforbook == []:
                                                        break

                                                    ###

                                                    if not checktheentry == []:
                                                        if int(checktheentry[0]) == 1:
                                                            df = 0
                                                            xy = int(len(finishedchapterpaths) + 10)



                ##### ab hier beginnt die Eingabe für neue Bücher

                    if buttonvoice[0] == 1:

                        liste = []

                        my_save = open(".mainpoint.save", "r")
                        lines = my_save.read().splitlines()

                        for line in lines:
                            liste.append(line)

                        my_save.close()

                        booklist = []
                        pathbooklist = []
                        sizeforbooks = []
                        progressinbooks = []

                        provefrominput = []

                        firstfoldersfromlist = []

                        for i in range(0, 5):
                            firstfoldersfromlist.append(str(liste[i]))

                        r = 0
                        if not len(liste) == 5:  # wichtig zum auswerten der Speicher-Datei
                            for i in range(0, len(liste)):
                                if len(liste[i]) == 0:
                                    r = r + 1
                                elif r == 2:
                                    booklist.append(liste[i])
                                elif r == 3:
                                    pathbooklist.append(liste[i])
                                elif r == 4:
                                    sizeforbooks.append(liste[i])
                                elif r == 5:
                                    progressinbooks.append(liste[i])


                        from tkinter import *

                        windowsize = str(liste[0]) + "x" + str(liste[1])

                        root = Tk()
                        root.title("BookReader: Bücher hinzufügen")
                        root.geometry(windowsize)
                        root.configure(bg = "gray29")

                        entrysizewidth = round(0.2875 * int(liste[0]))

                        buttonwidth = round(0.03375 * int(liste[0]))

                        xachse = round(((int(liste[0]) / 2) - (entrysizewidth / 2)))
                        name = Label(root, text = "Name des Buches", bg = "gray23", fg = "gray99")
                        pfad = Label(root, text = "Pfad des Buches", bg = "gray23", fg = "gray99")

                        name.place(x = xachse, y = 70)
                        pfad.place(x = xachse, y = 170)

                        e1 = Entry(root, bg = "gray23", fg = "gray99")
                        e2 = Entry(root, bg = "gray23", fg = "gray99")

                        e1.place(x = xachse, y = 100, width = entrysizewidth, height = 34)
                        e2.place(x = xachse, y = 200, width = entrysizewidth, height = 34)

                        def save():
                            abstandhalter = [""]

                            if len(e1.get()) > 0 and len(e2.get()) > 0:
                                booklist.append(str(e1.get()))
                                pathbooklist.append(str(e2.get()))
                                sizeforbooks.append(str(100))
                                progressinbooks.append(str(0))

                                all_in_one = firstfoldersfromlist + abstandhalter + booklist + abstandhalter + pathbooklist + abstandhalter + sizeforbooks + abstandhalter + progressinbooks

                                my_save = open(".mainpoint.save", "w")
                                save_daten = all_in_one

                                for all in save_daten:
                                    my_save.write(all + "\n")

                                my_save.close()

                            e1.delete(0, END)
                            e2.delete(0, END)


                        def back():
                            checknumb.append(1)
                            root.destroy()

                        a = Button(root, text = "Speichern", command = save, width = buttonwidth, height = 3, bg = "gray23", fg = "gray99", activebackground = "gray26")
                        a.place(x = xachse, y = 295)

                        b = Button(root, text = "Zurück", command = back, width = buttonwidth, height = 3, bg = "gray23", fg = "gray99", activebackground = "gray26")
                        b.place(x = xachse, y = 390)

                        root.mainloop()

                        if checknumb == []:
                            checknumb = []
                        elif int(checknumb[0]) == 1:
                            z = 0
                            checknumb = []
                        elif int(checknumb[0]) == 0:
                            z = 1
                            checknumb = []
