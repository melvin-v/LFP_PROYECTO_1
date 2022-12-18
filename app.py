from tkinter import *
from Automatas import *
from Gramaticas import *
from tkinter import messagebox
from tkinter import ttk
automatas = []
gramaticas = []
#Reporte AFD
def generarReporte():
    try:
        root2.destroy()
    except:
        pass

    global root5
    root5 = Tk()
    root5.title('PROYECTO 1')
    root5.resizable(0, 0)
    root5.config(bg='yellow')

    frame = Frame()
    frame.pack(fill='both', expand='true')
    frame.config(bg='#FFD97C')

    lista = []
    for element in automatas:
        lista.append(element.nombre)
        
    combo = ttk.Combobox(frame, state="readonly", values=lista)
    combo.grid(row=0, column=0, padx=100, pady=10)
    try:
        combo.current(0)
    except:
        pass
    
    ent1 = Entry(frame)
    ent1.grid(row=1, column=0, padx=10, pady=10)
    Button(frame, text='Solo validar', bg='#e06c73', padx=5, pady=5, command=lambda:soloValidar(combo.get(), ent1.get())).grid(row=2, column=0, padx=10, pady=10)
    Button(frame, text='Ruta', bg='#e06c73', padx=5, pady=5, command=lambda:rutaValidar(combo.get(), ent1.get())).grid(row=3, column=0, padx=10, pady=10)
    Button(frame, text='Regresar', bg='#e06c73', padx=5, pady=5, command=volverCrearAFD2).grid(row=4, column=0, padx=10, pady=10)
#Evaluar AFD
def volverCrearAFD2():
    root4.destroy()
    frameAFD()

def rutaValidar(combo, ent1):
    automata = ''
    ruta = ''
    for a in automatas:
        if combo == a.nombre:
            automata = a
            break
    
    estado = automata.estado_inicial
    flag = False
    for caracter in ent1:
        flag = False
        for transicion in automata.transiciones:
            if caracter == transicion.entrada:
                if transicion.origen == estado:
                    ruta += transicion.origen + ' -> ' + caracter + ' -> ' + transicion.destino + ' ; '
                    estado = transicion.destino
                    flag = True
                    break
        if not flag:
            break
          
    if estado in automata.estados_aceptacion:
        if flag:
            messagebox.showinfo(title='Correcto', message=ruta)
    else:
        messagebox.showerror(title='Invalido', message='Cadena invalida')    

def soloValidar(combo, ent1):
    automata = ''
    for a in automatas:
        if combo == a.nombre:
            automata = a
            break
    
    estado = automata.estado_inicial
    flag = False
    for caracter in ent1:
        flag = False
        for transicion in automata.transiciones:
            if caracter == transicion.entrada:
                if transicion.origen == estado:
                    estado = transicion.destino
                    flag = True
                    break
        if not flag:
            break
        
        
    if estado in automata.estados_aceptacion:
        if flag:
            messagebox.showinfo(title='Correcto', message='Cadena valida')
    else:
        messagebox.showerror(title='Invalido', message='Cadena invalida')
            
def evaluarAFD():
    try:
        root2.destroy()
    except:
        pass

    global root4
    root4 = Tk()
    root4.title('PROYECTO 1')
    root4.resizable(0, 0)
    root4.config(bg='yellow')

    frame = Frame()
    frame.pack(fill='both', expand='true')
    frame.config(bg='#FFD97C')

    lista = []
    for element in automatas:
        lista.append(element.nombre)
        
    combo = ttk.Combobox(frame, state="readonly", values=lista)
    combo.grid(row=0, column=0, padx=100, pady=10)
    try:
        combo.current(0)
    except:
        pass
    
    ent1 = Entry(frame)
    ent1.grid(row=1, column=0, padx=10, pady=10)
    Button(frame, text='Solo validar', bg='#e06c73', padx=5, pady=5, command=lambda:soloValidar(combo.get(), ent1.get())).grid(row=2, column=0, padx=10, pady=10)
    Button(frame, text='Ruta', bg='#e06c73', padx=5, pady=5, command=lambda:rutaValidar(combo.get(), ent1.get())).grid(row=3, column=0, padx=10, pady=10)
    Button(frame, text='Regresar', bg='#e06c73', padx=5, pady=5, command=volverCrearAFD2).grid(row=4, column=0, padx=10, pady=10)

#Crear AFD
def volverCrearAFD():
    root3.destroy()
    frameAFD()
    
def crearAFD():
    try:
        root2.destroy()
    except:
        pass

    global root3
    root3 = Tk()
    root3.title('PROYECTO 1')
    root3.resizable(0, 0)
    root3.config(bg='yellow')

    frame = Frame()
    frame.pack(fill='both', expand='true')
    frame.config(bg='#FFD97C')
    
  
    
    Label(frame, text='Nombre', bg='#FFD97C').grid(row=0, column=0, padx=100, pady=10)
    ent1 = Entry(frame)
    ent1.grid(row=1, column=0, padx=10, pady=10)
    Label(frame, text='Estados', bg='#FFD97C').grid(row=2, column=0, padx=10, pady=10)
    ent2 = Entry(frame)
    ent2.grid(row=3, column=0, padx=10, pady=10)
    Label(frame, text='Alfabeto', bg='#FFD97C').grid(row=4, column=0, padx=10, pady=10)
    ent3 = Entry(frame)
    ent3.grid(row=5, column=0, padx=10, pady=10)
    Label(frame, text='Estado inicial', bg='#FFD97C').grid(row=6, column=0, padx=10, pady=10)
    ent4 = Entry(frame)
    ent4.grid(row=7, column=0, padx=10, pady=10)
    Label(frame, text='Estados de aceptación', bg='#FFD97C').grid(row=8, column=0, padx=10, pady=10)
    ent5 = Entry(frame)
    ent5.grid(row=9, column=0, padx=10, pady=10)
    Label(frame, text='Transiciones', bg='#FFD97C').grid(row=10, column=0, padx=10, pady=10)
    ent6 = Entry(frame)
    ent6.grid(row=11, column=0, padx=10, pady=10)
    
    btn1 = Button(frame, text='Crear', bg='#e06c73', padx=5, pady=5, command=lambda:guardarAFD(ent1.get(), ent2.get(), ent3.get(), ent4.get(), ent5.get(), ent6.get()))
    btn1.grid(row=12, column=0, padx=10, pady=10)
    btn2 = Button(frame, text='Volver', bg='#e06c73', padx=5, pady=5, command=volverCrearAFD)
    btn2.grid(row=13, column=0, padx=10, pady=10)
    
def guardarAFD(ent1, ent2, ent3, ent4, ent5, ent6):
    nombre = ent1
    estados = ent2.replace(" ", "").split(';')
    alfabeto = ent3.replace(" ", "").split(';')
    estado_inicial = ent4.replace(" ", "")
    estados_aceptacion = ent5.replace(" ", "").split(';')
    t = ent6.replace(" ", "").split(';')
    transiciones = []
    transicionesDup = []
    for f in t:
        splitLista = f.split(',')
        if len(splitLista) == 3: 
            transicionesDup.append(splitLista[0]+splitLista[1])
            transiciones.append(Transicion(splitLista[0], splitLista[1], splitLista[2]))
            
    flagEstados = False        
    for element in alfabeto:
        if element in estados:
            flagEstados = True
            break
        else:
            flagEstados = False
            
    flagInicialEstado = True    
    if estado_inicial in estados:
        flagInicialEstado = False    
        
    flagAceptacion = True   
    for estado in estados_aceptacion:
        if estado in estados:
            flagAceptacion = False
        else:
            flagAceptacion = True
            break
    
    if flagEstados:
        messagebox.showerror(title='Error en estados', message='Elementos del alfabeto repetidos con estados')
        return
    if flagInicialEstado:
        messagebox.showerror(title='Error en estado inicial', message='Estado inicial inexistente')
        return
    if flagAceptacion:
        messagebox.showerror(title='Error en estados de aceptacion', message='Elementos no declarados como estados')
        return
    if len(transicionesDup) == len(set(transicionesDup)):
        pass
    else:
        messagebox.showerror(title='Error AFD', message='No se permiten AFDN')
        return
    
    messagebox.showinfo(title='Exito', message='Automata creado con exito')        
    automatas.append(Automata(nombre, estados, alfabeto, estado_inicial, estados_aceptacion, transiciones))
    
def regresarIndex():
    root2.destroy()
    mainRoot()  
      
def frameAFD():
    try:
        root.destroy()
    except:
        pass

    global root2
    root2 = Tk()
    root2.title('PROYECTO 1')
    root2.resizable(0, 0)
    root2.config(bg='yellow')

    frame = Frame()
    frame.pack(fill='both', expand='true')
    frame.config(bg='#FFD97C')
    
    Label(frame, text='Manejo de los AFD', bg='#FFD97C').grid(row=0, column=0, padx=100, pady=10)
    Button(frame, text='Crear AFD', bg='#e06c73', padx=5, pady=5, command=crearAFD).grid(row=1, column=0, padx=10, pady=10)
    Button(frame, text='Evaluar cadena', bg='#e06c73', padx=5, pady=5, command=evaluarAFD).grid(row=3, column=0, padx=10, pady=10)
    Button(frame, text='Generar reporte AFD', bg='#e06c73').grid(row=4, column=0, padx=10, pady=10)
    Button(frame, text='Volver',bg='#f53b3b', command=regresarIndex).grid(row=5, column=0, padx=10, pady=10)
    
#GR
def regresarGRroot():
    root6.destroy()
    mainRoot()
    
def regresarGR():
    root7.destroy()
    frameGR()
     
def guardarGR(ent1, ent2, ent3, ent4, ent5):
    nombre = ent1
    no_terminales = ent2.replace(" ", "").split(';')
    terminales = ent3.replace(" ", "").split(';')
    estado_inicial = ent4.replace(" ", "")
    
    flagEstados = False        
    for element in no_terminales:
        if element in terminales:
            flagEstados = True
            break
        else:
            flagEstados = False
            
    flagInicialEstado = True    
    if estado_inicial in no_terminales:
        flagInicialEstado = False    
        

    if flagEstados:
        messagebox.showerror(title='Error en terminales', message='Elementos repetidos con terminales')
        return
    if flagInicialEstado:
        messagebox.showerror(title='Error no terminal', message='Estado no terminal inexistente')
        return
    
    messagebox.showinfo(title='Exito', message='Automata creado con exito')        
    gramaticas.append(Gramatica(nombre, no_terminales, terminales, estado_inicial, ent5))
    print(gramaticas)
        
def crearGR():
    try:
        root6.destroy()
    except:
        pass

    global root7
    root7 = Tk()
    root7.title('PROYECTO 1')
    root7.resizable(0, 0)
    root7.config(bg='yellow')

    frame = Frame()
    frame.pack(fill='both', expand='true')
    frame.config(bg='#FFD97C')
    
  
    
    Label(frame, text='Nombre', bg='#FFD97C').grid(row=0, column=0, padx=100, pady=10)
    ent1 = Entry(frame)
    ent1.grid(row=1, column=0, padx=10, pady=10)
    Label(frame, text='No terminales', bg='#FFD97C').grid(row=2, column=0, padx=10, pady=10)
    ent2 = Entry(frame)
    ent2.grid(row=3, column=0, padx=10, pady=10)
    Label(frame, text='Terminales', bg='#FFD97C').grid(row=4, column=0, padx=10, pady=10)
    ent3 = Entry(frame)
    ent3.grid(row=5, column=0, padx=10, pady=10)
    Label(frame, text='No terminal inicial', bg='#FFD97C').grid(row=6, column=0, padx=10, pady=10)
    ent4 = Entry(frame)
    ent4.grid(row=7, column=0, padx=10, pady=10)
    Label(frame, text='Producciones', bg='#FFD97C').grid(row=8, column=0, padx=10, pady=10)
    ent5 = Entry(frame)
    ent5.grid(row=9, column=0, padx=10, pady=10)
    
    btn1 = Button(frame, text='Crear', bg='#e06c73', padx=5, pady=5, command=lambda:guardarGR(ent1.get(), ent2.get(), ent3.get(), ent4.get(), ent5.get()))
    btn1.grid(row=12, column=0, padx=10, pady=10)
    btn2 = Button(frame, text='Volver', bg='#e06c73', padx=5, pady=5, command=regresarGR)
    btn2.grid(row=13, column=0, padx=10, pady=10)
def frameGR():
    try:
        root.destroy()
    except:
        pass

    global root6
    root6 = Tk()
    root6.title('PROYECTO 1')
    root6.resizable(0, 0)
    root6.config(bg='yellow')

    frame = Frame()
    frame.pack(fill='both', expand='true')
    frame.config(bg='#FFD97C')
    
    Label(frame, text='Manejo de las GR', bg='#FFD97C').grid(row=0, column=0, padx=100, pady=10)
    Button(frame, text='Crear GR', bg='#e06c73', padx=5, pady=5, command=crearGR).grid(row=1, column=0, padx=10, pady=10)
    Button(frame, text='Evaluar cadena', bg='#e06c73', padx=5, pady=5).grid(row=3, column=0, padx=10, pady=10)
    Button(frame, text='Generar reporte GR', bg='#e06c73').grid(row=4, column=0, padx=10, pady=10)
    Button(frame, text='Volver',bg='#f53b3b', command=regresarGRroot).grid(row=5, column=0, padx=10, pady=10)
        
def mainRoot():
    global root
    root = Tk()
    root.title('PROYECTO 1')
    root.resizable(0, 0)
    root.config(bg='#FFD97C')

    frame = Frame(root)
    frame.pack(fill='both', expand='true')
    frame.config(bg='#FFD97C')
    
    Label(frame, text='LENGUAJES FORMALES Y DE PROGRAMACION', bg='#FFD97C').grid(row=0, column=0, padx=10, pady=10)
    Label(frame, text='SECCION: N', bg='#FFD97C').grid(row=1, column=0, padx=10, pady=10)
    Label(frame, text='CARNET: 202111556', bg='#FFD97C').grid(row=2, column=0, padx=10, pady=10)
    Label(frame, text='NOMBRE: MELVIN VALENCIA', bg='#FFD97C').grid(row=3, column=0, padx=10, pady=10)
        
    Button(frame, text='AFD', bg='#e06c73', command=frameAFD).grid(row=4, column=0, padx=10, pady=10)
    Button(frame, text='GR', bg='#e06c73', command=frameGR).grid(row=5, column=0, padx=10, pady=10)
    Button(frame, text='Cargar archivos', bg='#e06c73').grid(row=6, column=0, padx=10, pady=10)
    Button(frame, text='Salir',bg='#f53b3b').grid(row=7, column=0, padx=10, pady=10)

    root.mainloop()
if __name__ == '__main__':
    mainRoot()