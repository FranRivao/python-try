from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

# Entrada
e_texto = Entry(ventana, font=("Calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 5)

botones = [
    "btn_1", "btn_2", "btn_3", "btn_4", "btn_5", "btn_6", "btn_7", "btn_8", "btn_9", "btn_0",
    "btn_supr", "btn_open_bracket", "btn_close_bracket", "btn_dot", 
    "btn_div", "btn_prod", "btn_sum", "btn_rest", "btn_equal"
]

botonesContent = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "AC", "(", ")", ".", 
    "/", "*", "+", "-", "=" 
]

# Botones
for i  in botones:
    botones[i] = Button(ventana, text = botonesContent[i], width = 5, height = 2 )
    botones[i].grid(row = 1)


ventana.mainloop()
