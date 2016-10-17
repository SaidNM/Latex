from tkinter import *

ventana1 = Tk()
ventana1.geometry("900x600")  #geometry(widthxheight)
ventana1.title("Regular expressions")
ventana1.resizable(width=False,height=False)
AreaDibujo1=Canvas(ventana1,width=895,height=495)
AreaDibujo1.pack()
	

	#mas circuilos para transicion
AreaDibujo1.create_oval(360,120,435,200)
AreaDibujo1.create_oval(360,430,435,480)
	#Circulos de estado

AreaDibujo1.create_oval(545,145,655,255,fill="white")
AreaDibujo1.create_oval(150,250,250,350,fill="light sky blue")
AreaDibujo1.create_oval(350,150,450,250,fill="light sky blue")
AreaDibujo1.create_oval(550,150,650,250,fill="light sky blue")
AreaDibujo1.create_oval(350,350,450,450,fill="light sky blue")

	#Linea de inicio
AreaDibujo1.create_line(75,300,150,300)

	#linea de transiciones
AreaDibujo1.create_line(248,290,350,200)
AreaDibujo1.create_line(450,205,545,205)
AreaDibujo1.create_line(248,310,350,400)
AreaDibujo1.create_line(450,190,545,190)
AreaDibujo1.create_line(450,400,600,255)
AreaDibujo1.create_line(400,250,400,350)




	#Circulos de sentido
AreaDibujo1.create_oval(145,295,155,305,fill="black")
AreaDibujo1.create_oval(345,195,355,205,fill="black")
AreaDibujo1.create_oval(345,395,355,405,fill="black")
AreaDibujo1.create_oval(540,185,550,195,fill="black")
AreaDibujo1.create_oval(445,200,455,210,fill="black")
AreaDibujo1.create_oval(445,395,455,405,fill="black")
AreaDibujo1.create_oval(395,245,405,255,fill="black")



	#etiquetas
inicio=Label(ventana1,text="Inicio",font="Verdana 12 roman").place(x=80,y=275)

ventana1.mainloop()