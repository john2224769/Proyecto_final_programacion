from tkinter import *
import time
from tkinter import messagebox
import tkinter as tk
from datetime import datetime
import sys
import qrcode
from PIL import Image

# Ventana Usuario 
def ventana_estudiantes():
   global ventana_estudiantes
   ventana_estudiantes=Toplevel(principal)
   ventana_estudiantes.geometry("1000x500")
   ventana_estudiantes.title("Ventana del Usuario")
   ventana_estudiantes.config(bg="lime green")
   #ventana_estudiantes.iconbitmap("icono2.ico")

   frame_entrada=Frame(ventana_estudiantes)
   frame_entrada.config(bg="dark green", width=580,height=290)
   frame_entrada.place(x=200,y=60)
   
   label_usuario=Label(ventana_estudiantes, text="Ingresa tu usuario", bg="dark green", fg="black", font=("Arial",15), compound="center")
   label_usuario.place(x=210, y=70)

   entrada_usuario=Entry(ventana_estudiantes,textvariable=usuario_ingreso)
   entrada_usuario.config(font=("Arial",20), justify=LEFT, fg="black")
   entrada_usuario.focus_set()
   entrada_usuario.place(x=450,y=70)

   Label_password=Label(ventana_estudiantes, text="Ingresa tu contraseña", bg="dark green", fg="black", font=("Arial",15), compound="center")
   Label_password.place(x=210, y=160)

   entrada_password=Entry(ventana_estudiantes,textvariable=password_usuario)
   entrada_password.config(font=("Arial",20), justify=LEFT, fg="black")
   entrada_password.place(x=450,y=160)

   button_ingresar=Button(ventana_estudiantes,text=("Acceder"), command= ventana_ingresar_estudiante)
   button_ingresar.place(x=450, y=260)
   button_ingresar.config(font=("Arial",15))

   Button(ventana_estudiantes, text="Regresar", width=20, command=volver_ventana).place(x=10, y=450)
   #Button(ventana_estudiantes, text="Haz click aquí para generar tu código QR.", width=30, command=ventana_loginuser).place(x=500, y=250)

   ventana_estudiantes.mainloop()

# Ventana del administrador 
def ventana_administrador():
   global ventana_administrador
   ventana_administrador=Toplevel(principal)
   ventana_administrador.geometry("1000x500")
   ventana_administrador.title("Ventana del Administrador")
   ventana_administrador.config(bg="lime green")
   #ventana_administrador.iconbitmap("icono3.ico")
   
   frame_entrada=Frame(ventana_administrador)
   frame_entrada.config(bg="dark green", width=580,height=290)
   frame_entrada.place(x=200,y=80)

   label_admin=Label(ventana_administrador, text="Ingresa tu usuario", bg="dark green", fg="black", font=("Arial",15), compound="center")
   label_admin.place(x=210, y= 110)
   
   entrada_admin=Entry(ventana_administrador,textvariable=usuario_admin)
   entrada_admin.config(font=("Arial",20), justify=LEFT, fg="black")
   entrada_admin.focus_set()
   entrada_admin.place(x=450,y=110)
   
   Label_password=Label(ventana_administrador, text="Ingresa tu contraseña", bg="dark green", fg="black", font=("Arial",15), compound="center")
   Label_password.place(x=210, y=210)
   
   entrada_password=Entry(ventana_administrador,textvariable=password_admin)
   entrada_password.config(font=("Arial",20), justify=LEFT, fg="black")
   entrada_password.place(x=450,y=210)

   button_ingresar=Button(ventana_administrador,text=("Acceder"), command= ventana_ingresar_administrador)
   button_ingresar.place(x=450, y=260)
   button_ingresar.config(font=("Arial",15))
    
   Button(ventana_administrador, text="Regresar", width=20, command=volver_ventana2).place(x=10, y=460)

   ventana_administrador.mainloop()
    
def cancelar():
    usuario_entry.delete(0, "end")
    contraseña_entry.delete(0, "end")

def acceder():
    global ventana_acceso, usuario_entry, contraseña_entry
    
    ventana_acceso = Toplevel()
    ventana_acceso.title("Login")
    ventana_acceso.resizable(False, False)

    usuario_label = Label(ventana_acceso, text="USUARIO:")
    usuario_entry = Entry(ventana_acceso, bd=5, highlightcolor="red", highlightthickness=2)
    contraseña_label = Label(ventana_acceso, text="CONTRASEÑA:")
    contraseña_entry = Entry(ventana_acceso, bd=5, show='*', highlightcolor="red", highlightthickness=2)
    boton_aceptar = Button(ventana_acceso, text="ACEPTAR")
    boton_cancelar = Button(ventana_acceso, text="CANCELAR", command=cancelar)

    usuario_label.grid(row=0, column=0, sticky= "W", padx=10, pady=10)
    usuario_entry.grid(row=0, column=1, padx=10)
    contraseña_label.grid(row=1, column=0, sticky= "W", padx=10, pady=10)
    contraseña_entry.grid(row=1, column=1, padx=10)
    boton_aceptar.grid(row=2, column=0, padx=10, pady=10, sticky= "W")
    boton_cancelar.grid(row=2, column=1, padx=10, pady=10, sticky= "E")

# Volver a la ventana principal desde Usuario 
def volver_ventana():
   ventana_estudiantes.iconify()
   ventana_estudiantes.deiconify()
   ventana_estudiantes.destroy()

# Ingresar a la ventana de opciones de usuario  
def ventana_ingresar_estudiante():
   global ventana_ingresar_estudiante 
   ventana_ingresar_estudiante=Toplevel(principal)
   ventana_ingresar_estudiante.geometry("1000x500")
   ventana_ingresar_estudiante.title("Opciones usuario")
   ventana_ingresar_estudiante.config(bg="lime green")

   label_titulo=Label(ventana_ingresar_estudiante, text="Sistema de usuarios, parqueadero UIS", bg="lime green", fg="black", font=("Arial",15), compound="center")
   label_titulo.place(x=380, y=10)
   Label_titulo=Label(ventana_ingresar_estudiante, text="Selecciona una opción", bg="lime green", fg="black", font=("Arial",15), compound="center")
   Label_titulo.place(x=380, y=90)

   button_mostrarqr=Button(ventana_ingresar_estudiante,text=("Ver codigo QR"))
   button_mostrarqr.place(x=400, y=200)
   button_mostrarqr.config(font=("Arial",15))

   button_salir=Button(ventana_ingresar_estudiante,text=("Salir"), font=("arial", 15), command=principal.destroy)
   button_salir.place(x=850,y=450)

   Button(ventana_ingresar_estudiante, text="Regresar", width=20, command=volver_ventana3).place(x=10, y=450)
   
   ventana_administrador.mainloop()

# Volver a la de ingreso de usuario 
def volver_ventana3():
   ventana_ingresar_estudiante.iconify()
   ventana_ingresar_estudiante.deiconify()
   ventana_ingresar_estudiante.destroy()

# Generar código qr para Usuario
def generar_codigo():
    ventana_estudiantes.iconify()
    ventana_estudiantes.deiconify()
    ventana_estudiantes.destroy()

# Volver a la ventana principal desde Administrador 
def volver_ventana2():
   ventana_administrador.iconify()
   ventana_administrador.deiconify()
   ventana_administrador.destroy()

# Ventana de opciones administrador
def ventana_ingresar_administrador():
   global ventana_ingresar_administrador 
   ventana_ingresar_administrador=Toplevel(principal)
   ventana_ingresar_administrador.geometry("1000x500")
   ventana_ingresar_administrador.title("Opciones administrador")
   ventana_ingresar_administrador.config(bg="lime green")

   label_titulo=Label(ventana_ingresar_administrador, text="Sistema de adminisracion de usuarios, parqueadero UIS", bg="lime green", fg="black", font=("Arial",15), 
   compound="center")
   label_titulo.place(x=10, y=10)

   Label_titulo=Label(ventana_ingresar_administrador, text="Selecciona una opción: ", bg="lime green", fg="black", font=("Arial",15), compound="center")
   Label_titulo.place(x=10, y=60)

   button_agregar=Button(ventana_ingresar_administrador,text=("Agregar usuario"), font=("arial", 15), command=ventana_agregar_usuario)
   button_agregar.place(x=400,y=100)

   button_eliminar=Button(ventana_ingresar_administrador,text=("Eliminar usuario"), font=("arial", 15), command=Eliminar_usuario)
   button_eliminar.place(x=400,y=150)

   button_mostrar=Button(ventana_ingresar_administrador,text=("Mostrar usuarios"), font=("arial", 15), command=mostrar_usuarios)
   button_mostrar.place(x=400,y=200)

   button_salir=Button(ventana_ingresar_administrador,text=("Salir"), font=("arial", 15), command=principal.destroy)
   button_salir.place(x=750,y=450)

   Button(ventana_ingresar_administrador, text="Regresar", width=20, command=volver_ventana4).place(x=10, y=450)
   
   ventana_administrador.mainloop()

#volver a ingreso de administrador 
def volver_ventana4():
   ventana_ingresar_administrador.iconify()
   ventana_ingresar_administrador.deiconify()
   ventana_ingresar_administrador.destroy()

# Ventana agregar usuario 
def ventana_agregar_usuario():
   global ventana_agregar_usuario 
   ventana_agregar_usuario=Toplevel(principal)
   ventana_agregar_usuario.geometry("1000x500")
   ventana_agregar_usuario.title("Agregar usuario")
   ventana_agregar_usuario.config(bg="lime green")
   global entrada_nombre, entrada_codigo, entrada_placa, entrada_tipo

   Label_nombre=Label(ventana_agregar_usuario, text="Ingresa el nombre:", bg="lime green", fg="black", font=("Arial",15), compound="center")
   Label_nombre.place(x=10, y=10)

   entrada_nombre=Entry(ventana_agregar_usuario,textvariable=user)
   entrada_nombre.config(font=("Arial",20), justify=LEFT, fg="black")
   entrada_nombre.place(x=200,y=10)

   Label_codigo=Label(ventana_agregar_usuario, text="Ingresa el codigo:", bg="lime green", fg="black", font=("Arial",15), compound="center")
   Label_codigo.place(x=10, y=100)
   
   entrada_codigo=Entry(ventana_agregar_usuario,textvariable=code)
   entrada_codigo.config(font=("Arial",20), justify=LEFT, fg="black")
   entrada_codigo.place(x=200,y=100)
   
   Label_placa=Label(ventana_agregar_usuario, text="Ingresa la placa:", bg="lime green", fg="black", font=("Arial",15), compound="center")
   Label_placa.place(x=10, y=200)
   
   entrada_placa=Entry(ventana_agregar_usuario,textvariable=placa)
   entrada_placa.config(font=("Arial",20), justify=LEFT, fg="black")
   entrada_placa.place(x=200,y=200)
   
   Label_tipo=Label(ventana_agregar_usuario, text="Tipo de vehiculo:", bg="lime green", fg="black", font=("Arial",15), compound="center")
   Label_tipo.place(x=10, y=300)
   
   entrada_tipo=Entry(ventana_agregar_usuario,textvariable=vehiculo)
   entrada_tipo.config(font=("Arial",20), justify=LEFT, fg="black")
   entrada_tipo.place(x=200,y=300)

   
   boton_guardar=Button(ventana_agregar_usuario,text=("Guardar"), command=guardar_dato)
   boton_guardar.place(x=400, y=400)

   Button(ventana_agregar_usuario, text="Regresar", width=20,command=volver_ventana5).place(x=10, y=450)

   ventana_administrador.mainloop()

def volver_ventana5():
   ventana_agregar_usuario.iconify()
   ventana_agregar_usuario.deiconify()
   ventana_agregar_usuario.destroy()

def mostrar_usuarios():
    
    global ventana_mostrar_usuario
    ventana_mostrar_usuario=Toplevel(principal)
    ventana_mostrar_usuario.geometry("1000x500")
    ventana_mostrar_usuario.title("Datos de usuarios")
    ventana_mostrar_usuario.config(bg="lime green")

    mostrar= Text(ventana_mostrar_usuario)
    mostrar.config(bg="dark green", width=100, height=30)
    mostrar.place(x=10, y=10 )

    file = open("matriz.txt")
    datos=file.read()
    mostrar.insert(INSERT, datos)
    
    file.close()

    Button(ventana_mostrar_usuario, text="Regresar", width=20,command=volver_ventana6).place(x=830, y=450)
    ventana_administrador.mainloop()

def volver_ventana6():
   ventana_mostrar_usuario.iconify()
   ventana_mostrar_usuario.deiconify()
   ventana_mostrar_usuario.destroy()

def Eliminar_usuario():
    
    global Eliminar_usuario
    Eliminar_usuario=Toplevel(principal)
    Eliminar_usuario.geometry("1000x500")
    Eliminar_usuario.title("Borrar usuario")
    Eliminar_usuario.config(bg="lime green")

    Label_tipo=Label(Eliminar_usuario, text="Usuario a Borrar:", bg="lime green", fg="black", font=("Arial",15), compound="center")
    Label_tipo.place(x=10, y=300)
   
    entrada_tipo=Entry(Eliminar_usuario,textvariable=terminate)
    entrada_tipo.config(font=("Arial",20), justify=LEFT, fg="black")
    entrada_tipo.place(x=200,y=300)

    Button(Eliminar_usuario, text="Borrar", width=20,command=terminar).place(x=830, y=450)
    volver=Button(Eliminar_usuario, text="Regresar", width=20,command=volver_ventana7).place(x=10, y=450)

def volver_ventana7():
   Eliminar_usuario.iconify()
   Eliminar_usuario.deiconify()
   Eliminar_usuario.destroy()

def terminar():

    f = open("matriz.txt", "r")
    lineas = f.readlines()

    pos=int(terminate.get())
    linea=lineas[pos]
    lineas.remove(linea)
    for linea in lineas:
        f.write(linea)
    f.close()

# Estructura de la ventana principal

principal = Tk()

password=StringVar()
user=StringVar()
vehiculo=StringVar()
code =StringVar()
placa=StringVar()
admin=StringVar()
usuario_ingreso=StringVar()
password_usuario=StringVar()
usuario_admin=StringVar()
password_admin=StringVar()
terminate=0

def guardar_dato():
    user_name=user.get() 
    user_code=code.get()
    user_placa=placa.get()
    tipo=vehiculo.get()
    newfile=open("matriz.txt", "a")
    newfile.write(user_name)
    newfile.write(" \t ")
    newfile.write(tipo)
    newfile.write(" \t ")
    newfile.write(user_code)
    newfile.write(" \t ")
    newfile.write(user_placa)
    newfile.write(" \n ")
    newfile.close()
    entrada_nombre.delete(0, "end")
    entrada_codigo.delete(0, "end")
    entrada_placa.delete(0, "end")
    entrada_tipo.delete(0,"end")
    
principal.title("Sistema de Parqueadero UIS")
principal.geometry("1000x500")
#principal.iconbitmap("icono.ico")
principal.resizable(False,False)
principal.config(bg= "lime green")


#frames
frame_entrada=Frame(principal)
frame_entrada.config(bg="dark green", width=580,height=190)
frame_entrada.place(x=220,y=80)
# Labels principales

target = Label(principal, text="Hola, Te damos la bienvenida al Parqueadero Público de la UIS.")
target.config(fg="black", bg="dark green", font=("Bahnschrift SemiBold SemiConden", 15))
target.place(x=280, y=100)

target2 = Label(principal, text="Define que tipo de usuario eres: ")
target2.config(fg="black", bg="dark green", font=("Bahnschrift SemiBold SemiConden", 15))
target2.place(x=380 , y= 140)

target3 = Label(principal, text="Parqueadero UIS" )
target3.config(fg="black", bg="lime green", font=("Bahnschrift SemiBold SemiConden", 15))
target3.place(x=28, y=25)

def inicio():
    print("Por favor, ingresa o regístrate.")

def salir():
    messagebox.showinfo("Salida", "La app se cerrará.")
    principal.destroy()

def ayuda():
    messagebox.showwarning(message="Primero, debes establecer que tipo de persona eres para ingresar al parqueadero\n\nActo seguido digitas los datos que te pidan a continuación y te asignarán un lugar en el Parqueadero :))\n\nTen un lindo día ;)",title="Prevención")

def inicio1():
    print("Por favor digita tus credenciales.")

def borrar():
     messagebox.showinfo("Reestablecer datos", "Los datos a continuación serán borrados...")

# Botones ventana principal
boton = Button(principal, text= "Usuario", command= ventana_estudiantes)
boton.config(fg="black", bg="white", font=("Bahnschrift SemiBold SemiConden", 12))
boton.place(x=320 , y=210)

boton2 = Button(principal, text= "Administrativo", command= ventana_administrador)
boton2.config(fg="black", bg="white", font=("Bahnschrift SemiBold SemiConden", 12))
boton2.place(x=590 , y=210)

boton3 = Button(principal, text="Salir", command=salir)
boton3.config(fg="black", bg="white", font=("Bahnschrift SemiBold SemiConden", 15))
boton3.place(x=850, y=430, width=115, height=35)

boton4 = Button(principal, text="¿Necesitas ayuda?", command=ayuda)
boton4.config(fg="black", bg="white", font=("Bahnschrift SemiBold SemiConden", 12))
boton4.place(x=20, y=430, width=130, height=30)

boton5 = Button(principal, text="Reestablecer", command=borrar)
boton5.config(fg="black", bg="white", font=("Bahnschrift SemiBold SemiConden", 12))
boton5.place(x=710, y=430)

# Contador reloj

def actualizar_hora():
    hora = time.strftime("%H:%M:%S")
    variable_control.set(hora)
    principal.after(1000, actualizar_hora)

variable_control = StringVar()

reloj = Label(textvariable= variable_control, bg="lime green", fg="white", font=("Bahnschrift SemiBold SemiConden", 15), padx=20, pady=20, compound="left")

reloj.pack()
reloj.place(x=900, y=35)
actualizar_hora()

# Logo app
#logo = PhotoImage(file= "logo.png")
#lb_logo = Label(principal, image=logo)
#lb_logo.place(x=18, y=50)

#Widget fecha
def actualizar_fecha():
    fecha = time.strftime("%A, %B %D")
    variable_control2.set(fecha)
    principal.after(1000, actualizar_fecha)

variable_control2 = StringVar()

calendario = Label(textvariable=variable_control2, bg="lime green", fg="white", font=("Bahnschrift SemiBold SemiConden", 10), padx=20, pady=20, compound="left")
calendario.pack()
calendario.place(x=830, y=3)
actualizar_fecha()

# Frames
frame_borde = Frame(principal)
frame_borde.config(bg="green4", width=1000, height=20)
frame_borde.place(x=0, y=0)

frame_borde2 = Frame(principal)
frame_borde2.config(bg="green4", width=1000, height=20)
frame_borde2.place(x=0, y=480)

frame_tapa = Frame(principal)
frame_tapa.config(bg="lime green", width=200, height=40)
frame_tapa.place(x=18, y=50)

frame_tapa2 = Frame(principal)
frame_tapa2.config(bg="lime green", width=200, height=40)
frame_tapa2.place(x=18, y=165)

# Inicio login Usuario

principal.mainloop()