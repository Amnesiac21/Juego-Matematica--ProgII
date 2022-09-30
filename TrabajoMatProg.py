from tkinter import *
from tkinter import messagebox
ventana = Tk()
ventana.title("Adivina Numero")
ventana.config(bg="#DBBDBD", padx=210, pady=140)
ventana.geometry("800x500")
ventana.resizable(0, 0)  # fija el tamaño de la pantalla
valorResta = IntVar()
valorSuma = IntVar()
valorFinal = IntVar()
# al juego le falta una verificacion que no permita saltar los ingreso de numeros  (en el caso de las resta y suma) sino el resultado sera 0.
# ----------------------------------------------------JuegoIngles----------------------------------------------------------------------


def eng_TopLevel6():
    numOculto()
    global eng_topLevel6
    eng_topLevel5.withdraw()
    eng_topLevel6 = Toplevel()
    eng_topLevel6.title("Guess guesser")
    eng_topLevel6.geometry("800x500")
    eng_topLevel6.config(bg="#DBBDBD", padx=175, pady=200)
    eng_topLevel6.resizable(0, 0)
    lbl_msj = Label(
        eng_topLevel6, text="El numero que pensaste es:", font=("impact", 15))
    lbl_msj.grid(row=0, column=0, pady=10, padx=20, ipady=2, columnspan=3)
    lbl_resultado = Label(
        eng_topLevel6, text=f"{valorFinal.get()}", font=("impact", 15))
    lbl_resultado.grid(row=0, column=3, ipady=10, ipadx=10)
    btn_salir = Button(eng_topLevel6, text="Exit", background="white", foreground="black", width=10, height=1, font="impact 15",
                       command=salir)
    btn_salir.grid(row=1, column=2, ipady=10, ipadx=10)


def eng_TopLevel5():
    global eng_topLevel5, txt_suma, btn_siguiente5
    eng_topLevel4.withdraw()
    eng_topLevel5 = Toplevel()
    eng_topLevel5.title("Guess guesser")
    eng_topLevel5.geometry("800x500")
    eng_topLevel5.config(bg="#DBBDBD", padx=150, pady=175)
    eng_topLevel5.resizable(0, 0)
    lbl_msj = Label(
        eng_topLevel5, text="Now sum the two digits of the number you thought at the beginning", font=("impact", 15))
    lbl_msj.grid(row=0, column=0, pady=10, padx=20, ipady=2, columnspan=3)
    lbl_res = Label(es_topLevel5, text="Resultado:", font=(
        "impact", 15), background="white", foreground="black")
    lbl_res.grid(row=1, column=0)
    txt_suma = Entry(eng_topLevel5, textvariable=None)
    txt_suma.grid(row=1, column=1)
    btn_cargar = Button(eng_topLevel5, text="Load", background="white", foreground="black", width=10, height=1, font="impact 15",
                        command=asignarsuma)
    btn_cargar.grid(row=2, column=0, pady=10)
    btn_siguiente5 = Button(es_topLevel5, text="Next", background="white", foreground="black", width=10, height=1, font="impact 15",
                            command=eng_TopLevel6)
    btn_siguiente5.grid(row=2, column=2, pady=2)
    return txt_suma


def eng_TopLevel4():
    global eng_topLevel4, txt_resta, btn_siguiente4
    eng_topLevel3.withdraw()
    eng_topLevel4 = Toplevel()
    eng_topLevel4.title("Guess guesser")
    eng_topLevel4.geometry("800x500")
    eng_topLevel4.config(bg="#DBBDBD", padx=150, pady=175)
    eng_topLevel4.resizable(0, 0)
    if op.get() == 1:
        lbl_msj = Label(
            eng_topLevel4, text="Now subtract the inverted number minus the thought number", font=("impact", 15))
        lbl_msj.grid(row=0, column=0, pady=10, padx=20, ipady=2, columnspan=3)
        lbl_res = Label(eng_topLevel4, text="Result:", font=(
            "impact", 15), background="white", foreground="black")
        lbl_res.grid(row=1, column=0)
        txt_resta = Entry(eng_topLevel4, textvariable=None)
        txt_resta.grid(row=1, column=1, ipady=2)
        btn_cargar = Button(eng_topLevel4, text="Load", background="white", foreground="black", width=10, height=1, font="impact 15",
                            command=asignarresta)
        btn_cargar.grid(row=2, column=1, pady=10)
        btn_siguiente4 = Button(eng_topLevel4, text="Next", background="white", foreground="black", width=10, height=1, font="impact 15",
                                command=eng_TopLevel5)
        btn_siguiente4.grid(row=2, column=3, pady=10)
        return txt_resta
    if op.get() == 2:
        lbl_msj = Label(
            eng_topLevel4, text="Now subtract the number thought minus the number inverted", font=("impact", 15))
        lbl_msj.grid(row=0, column=0, pady=10, padx=20, ipady=2, columnspan=3)
        lbl_res = Label(es_topLevel4, text="Result:", font=(
            "impact", 15), background="white", foreground="black")
        lbl_res.grid(row=1, column=0)
        txt_resta = Entry(eng_topLevel4, textvariable=None)
        txt_resta.grid(row=1, column=1, ipady=2)
        btn_cargar = Button(eng_topLevel4, text="Load", background="white", foreground="black", width=10, height=1, font="impact 15",
                            command=asignarresta)
        btn_cargar.grid(row=2, column=1, pady=10)
        btn_siguiente4 = Button(eng_topLevel4, text="Next", background="white", foreground="black", width=10, height=1, font="impact 15",
                                command=es_TopLevel5)
        btn_siguiente4.grid(row=2, column=2, pady=10)
        return txt_resta


def eng_TopLevel3():
    global eng_topLevel3, op, btn_siguiente3
    op = IntVar()
    eng_topLevel2.withdraw()
    eng_topLevel3 = Toplevel()
    eng_topLevel3.title("Guess guesser")
    eng_topLevel3.geometry("800x500")
    eng_topLevel3.config(bg="#DBBDBD", padx=150, pady=175)
    eng_topLevel3.resizable(0, 0)
    lbl_msj = Label(
        eng_topLevel3, text="¿Is the inverted number greater than the intended number?", font=("impact", 15))
    lbl_msj.grid(row=0, column=0, pady=10, padx=50, ipady=2)
    rbtn_mayor = Radiobutton(eng_topLevel3, text="Higher", foreground="black",
                             width=10, height=1, font="impact 15", variable=op, value=1)
    rbtn_mayor.grid(row=1, column=0, pady=10)
    rbtn_menor = Radiobutton(eng_topLevel3, text="Less",
                             variable=op, value=2, foreground="black", width=10, height=1, font="impact 15")
    rbtn_menor.grid(row=2, column=0, pady=10)
    btn_siguiente3 = Button(eng_topLevel3, text="Next", background="white", foreground="black", width=10, height=1, font="impact 15",
                            command=eng_TopLevel4)
    btn_siguiente3.grid(row=3, column=0, pady=10, padx=2)
    return op


def eng_TopLevel2():
    global eng_topLevel2
    eng_topLevel1.withdraw()
    eng_topLevel2 = Toplevel()
    eng_topLevel2.title("Guess guesser")
    eng_topLevel2.geometry("800x500")
    eng_topLevel2.config(bg="#DBBDBD", padx=225, pady=175)
    eng_topLevel2.resizable(0, 0)
    lbl_msj = Label(
        eng_topLevel2, text="Now reverse the digits of the number", font=("impact", 15))
    lbl_msj.grid(row=0, column=0, pady=10, padx=50, ipady=2)
    btn_siguiente2 = Button(eng_topLevel2, text="Next", background="white", foreground="black", width=10, height=1, font="impact 15",
                            command=eng_TopLevel3)
    btn_siguiente2.grid(row=1, column=0, pady=10)


def eng_TopLevel1():
    global eng_topLevel1
    ventana.withdraw()
    eng_topLevel1 = Toplevel()
    eng_topLevel1.title("Guess guesser")
    eng_topLevel1.geometry("800x500")
    eng_topLevel1.config(bg="#DBBDBD", pady=200, padx=25)
    eng_topLevel1.resizable(0, 0)
    lbl_msj = Label(
        eng_topLevel1, text="Think of a two-digit number that is not the same...", font=("impact", 15))
    lbl_msj.grid(row=1, column=0, pady=10, padx=50, ipady=2)
    btn_siguiente1 = Button(eng_topLevel1, text="Next", bg="white", fg="black", width=10, height=1, font=("impact", 15),
                            command=eng_TopLevel2)
    btn_siguiente1.grid(row=1, column=1, pady=10, padx=10, ipady=10)

# ----------------------------------------------------JuegoEspañol----------------------------------------------------------------------


def es_TopLevel6():
    numOculto()
    global es_topLevel6
    es_topLevel5.withdraw()
    es_topLevel6 = Toplevel()
    es_topLevel6.title("Adivinador de Numero")
    es_topLevel6.geometry("800x500")
    es_topLevel6.config(bg="#DBBDBD", padx=175, pady=200)
    es_topLevel6.resizable(0, 0)
    lbl_msj = Label(
        es_topLevel6, text="El numero que pensaste es:", font=("impact", 15))
    lbl_msj.grid(row=0, column=0, pady=10, padx=20, ipady=2, columnspan=3)
    lbl_resultado = Label(
        es_topLevel6, text=f"{valorFinal.get()}", font=("impact", 15))
    lbl_resultado.grid(row=0, column=3, ipady=10, ipadx=10)
    btn_salir = Button(es_topLevel6, text="Salir", background="white", foreground="black", width=10, height=1, font="impact 15",
                       command=salir)
    btn_salir.grid(row=1, column=2, ipady=10, ipadx=10)


def es_TopLevel5():
    global es_topLevel5, txt_suma, btn_siguiente5
    es_topLevel4.withdraw()
    es_topLevel5 = Toplevel()
    es_topLevel5.title("Adivinador de Numero")
    es_topLevel5.geometry("800x500")
    es_topLevel5.config(bg="#DBBDBD", padx=150, pady=175)
    es_topLevel5.resizable(0, 0)
    lbl_msj = Label(
        es_topLevel5, text="Ahora suma las dos cifras del numero pensado al principio", font=("impact", 15))
    lbl_msj.grid(row=0, column=0, pady=10, padx=20, ipady=2, columnspan=3)
    lbl_res = Label(es_topLevel5, text="Resultado:", font=(
        "impact", 15), background="white", foreground="black")
    lbl_res.grid(row=1, column=0)
    txt_suma = Entry(es_topLevel5, textvariable=None)
    txt_suma.grid(row=1, column=1)
    btn_cargar = Button(es_topLevel5, text="Cargar", background="white", foreground="black", width=10, height=1, font="impact 15",
                        command=asignarsuma)
    btn_cargar.grid(row=2, column=0, pady=10)
    btn_siguiente5 = Button(es_topLevel5, text="Siguiente", background="white", foreground="black", width=10, height=1, font="impact 15",
                            command=es_TopLevel6)
    btn_siguiente5.grid(row=2, column=2, pady=2)
    return txt_suma


def es_TopLevel4():
    global es_topLevel4, txt_resta, btn_siguiente4
    es_topLevel3.withdraw()
    es_topLevel4 = Toplevel()
    es_topLevel4.title("Adivinador de Numero")
    es_topLevel4.geometry("800x500")
    es_topLevel4.config(bg="#DBBDBD", padx=150, pady=175)
    es_topLevel4.resizable(0, 0)
    if op.get() == 1:
        lbl_msj = Label(
            es_topLevel4, text="Entonces, restá el número invertido con el que pensaste", font=("impact", 15))
        lbl_msj.grid(row=0, column=0, pady=10, padx=20, ipady=2, columnspan=3)
        lbl_res = Label(es_topLevel4, text="Resultado:", font=(
            "impact", 15), background="white", foreground="black")
        lbl_res.grid(row=1, column=0)
        txt_resta = Entry(es_topLevel4, textvariable=None)
        txt_resta.grid(row=1, column=1, ipady=2)
        btn_cargar = Button(es_topLevel4, text="Cargar", background="white", foreground="black", width=10, height=1, font="impact 15",
                            command=asignarresta)
        btn_cargar.grid(row=2, column=1, pady=10)
        btn_siguiente4 = Button(es_topLevel4, text="Siguiente", background="white", foreground="black", width=10, height=1, font="impact 15",
                                command=es_TopLevel5)
        btn_siguiente4.grid(row=2, column=3, pady=10)
        return txt_resta
    if op.get() == 2:
        lbl_msj = Label(
            es_topLevel4, text="Entonces, restá el número que pensaste con el numero invertido", font=("impact", 15))
        lbl_msj.grid(row=0, column=0, pady=10, padx=20, ipady=2, columnspan=3)
        lbl_res = Label(es_topLevel4, text="Resultado:", font=(
            "impact", 15), background="white", foreground="black")
        lbl_res.grid(row=1, column=0)
        txt_resta = Entry(es_topLevel4, textvariable=None)
        txt_resta.grid(row=1, column=1, ipady=2)
        btn_cargar = Button(es_topLevel4, text="Cargar", background="white", foreground="black", width=10, height=1, font="impact 15",
                            command=asignarresta)
        btn_cargar.grid(row=2, column=1, pady=10)
        btn_siguiente4 = Button(es_topLevel4, text="Siguiente", background="white", foreground="black", width=10, height=1, font="impact 15",
                                command=es_TopLevel5)
        btn_siguiente4.grid(row=2, column=2, pady=10)
        return txt_resta


def es_TopLevel3():
    global es_topLevel3, op, btn_siguiente3
    op = IntVar()
    es_topLevel2.withdraw()
    es_topLevel3 = Toplevel()
    es_topLevel3.title("Adivinador de Numero")
    es_topLevel3.geometry("800x500")
    es_topLevel3.config(bg="#DBBDBD", padx=150, pady=175)
    es_topLevel3.resizable(0, 0)
    lbl_msj = Label(
        es_topLevel3, text="¿El nuevo número es mayor o menor que el primero?", font=("impact", 15))
    lbl_msj.grid(row=0, column=0, pady=10, padx=50, ipady=2)
    rbtn_mayor = Radiobutton(es_topLevel3, text="Mayor", foreground="black",
                             width=10, height=1, font="impact 15", variable=op, value=1)
    rbtn_mayor.grid(row=1, column=0, pady=10)
    rbtn_menor = Radiobutton(es_topLevel3, text="Menor",
                             variable=op, value=2, foreground="black", width=10, height=1, font="impact 15")
    rbtn_menor.grid(row=2, column=0, pady=10)
    btn_siguiente3 = Button(es_topLevel3, text="Siguiente", background="white", foreground="black", width=10, height=1, font="impact 15",
                            command=es_TopLevel4)
    btn_siguiente3.grid(row=3, column=0, pady=10, padx=2)
    return op


def es_TopLevel2():
    global es_topLevel2
    es_topLevel1.withdraw()
    es_topLevel2 = Toplevel()
    es_topLevel2.title("Adivinador de Numero")
    es_topLevel2.geometry("800x500")
    es_topLevel2.config(bg="#DBBDBD", padx=225, pady=175)
    es_topLevel2.resizable(0, 0)
    lbl_msj = Label(
        es_topLevel2, text="Ahora invertí el orden de las cifras", font=("impact", 15))
    lbl_msj.grid(row=0, column=0, pady=10, padx=50, ipady=2)
    btn_siguiente2 = Button(es_topLevel2, text="Siguiente", background="white", foreground="black", width=10, height=1, font="impact 15",
                            command=es_TopLevel3)
    btn_siguiente2.grid(row=1, column=0, pady=10)


def es_TopLevel1():
    global es_topLevel1
    ventana.withdraw()
    es_topLevel1 = Toplevel()
    es_topLevel1.title("Adivinador de Numero")
    es_topLevel1.geometry("800x500")
    es_topLevel1.config(bg="#DBBDBD", pady=200, padx=25)
    es_topLevel1.resizable(0, 0)
    lbl_msj = Label(
        es_topLevel1, text="Pensá un número de dos cifras (que no sean iguales).", font=("impact", 15))
    lbl_msj.grid(row=1, column=0, pady=10, padx=50, ipady=2)
    btn_siguiente1 = Button(es_topLevel1, text="Siguiente", bg="white", fg="black", width=10, height=1, font=("impact", 15),
                            command=es_TopLevel2)
    btn_siguiente1.grid(row=1, column=1, pady=10, padx=10, ipady=10)


"=======================================================VentanaPrincipal==================================================================="

lbl_idioma = Label(ventana, text="Elige el idioma", font="impact 30",
                   background="black", foreground="white", width=17, height=1)
lbl_idioma.grid(row=0, column=0, padx=10, pady=10)
btn_espaniol = Button(ventana, text="Español", background="#DBBDBD", font=("arial", 15),
                      foreground="black", width=17, height=1, command=es_TopLevel1)
btn_espaniol.grid(row=2, column=0, padx=10, pady=0)
btn_ingles = Button(ventana, text="Ingles", background="#DBBDBD", font=("arial", 15),
                    foreground="black", width=17, height=1, command=eng_TopLevel1)
btn_ingles.grid(row=3, column=0, padx=10, pady=0)

"-------------------------------------------------------Operaciones------------------------------------------------------------------------"


def asignarresta():
    global valorResta, txt_resta
    if txt_resta.get() != "0" and txt_resta.get() != "" and txt_resta.get().isnumeric():
        valorResta.set(txt_resta.get())
    elif txt_resta.get() == "0":
        messagebox.showwarning(
            "Error", "Debe ingresar un número distinto de cero")
    else:
        messagebox.showwarning("Error", "Debe ingresar un valor numérico")


def asignarsuma():
    global valorSuma, txt_suma
    if txt_suma.get() != "0" and txt_suma.get() != "" and txt_suma.get().isnumeric():
        valorSuma.set(txt_suma.get())


def numOculto():
    global valorFinal
    div = valorResta.get() / 9
    a = int((valorSuma.get() + div) / 2)
    b = int((valorSuma.get() - div) / 2)
    if op.get() == 2:
        valor = str(a)+str(b)
        valorFinal.set(int(valor))
        return valorFinal
    if op.get() == 1:
        valor = str(b)+str(a)
        valorFinal.set(int(valor))
        return valorFinal


def salir():
    messagebox.showinfo(
        message="Gracias por jugar! ¡Hasta luego, buena suerte!", title="Adios!")
    es_topLevel6.destroy()


ventana.mainloop()
