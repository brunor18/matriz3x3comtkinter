import tkinter as tk

matriz1 = []
matriz2 = []

def first_matriz():
    global n1c1, n2c1, n3c1, n1c2, n2c2, n3c2, n1c3, n2c3, n3c3

    matriz1texto = tk.Label(tela, text="Digite a primeira matriz", font=("Arial", 10))
    matriz1texto.pack()

    p1 = tk.Label(tela, text="(", font=("Arial", 70), anchor="center")
    p1.place(x=100, y=40)

    ## inicio da 1 coluna

    n1c1 = tk.Entry(tela, width=1)  ## 1 numero coluna 1
    n1c1.place(x=140, y=60)

    n2c1 = tk.Entry(tela, width=1)  ## 2 numero coluna 1
    n2c1.place(x=140, y=90)

    n3c1 = tk.Entry(tela, width=1)  ## 3 numero coluna 1
    n3c1.place(x=140, y=120)

    ## fim da 1 coluna

    ## inicio da 2 coluna

    n1c2 = tk.Entry(tela, width=1)  ## 1 numero coluna 2
    n1c2.place(x=180, y=60)

    n2c2 = tk.Entry(tela, width=1)  ## 2 numero coluna 2
    n2c2.place(x=180, y=90)

    n3c2 = tk.Entry(tela, width=1)  ## 3 numero coluna 2
    n3c2.place(x=180, y=120)

    ## fim da 2 coluna

    ## inicio da 3 coluna

    n1c3 = tk.Entry(tela, width=1)  ## 1 numero coluna 3
    n1c3.place(x=220, y=60)

    n2c3 = tk.Entry(tela, width=1)  ## 2 numero coluna 3
    n2c3.place(x=220, y=90)

    n3c3 = tk.Entry(tela, width=1)  ## 3 numero coluna 3
    n3c3.place(x=220, y=120)

    ## fim da 3 coluna

    p2 = tk.Label(tela, text=")", font=("Arial", 70), anchor="center")
    p2.place(x=240, y=40)

    btn_enviar = tk.Button(tela, text="Próxima Matriz ->", command=lambda: [enviartudoDaMatriz1(), segunda_matriz(matriz1texto), btn_enviar.place_forget()])
    btn_enviar.place(x=290, y=180)

def segunda_matriz(matriz1texto):
    global n1c1_m2, n2c1_m2, n3c1_m2, n1c2_m2, n2c2_m2, n3c2_m2, n1c3_m2, n2c3_m2, n3c3_m2,matriz2texto

    matriz1texto.pack_forget()

    matriz2texto = tk.Label(tela, text="Digite a segunda matriz", font=("Arial", 10))
    matriz2texto.pack()

    ## inicio da 1 coluna

    n1c1_m2 = tk.Entry(tela, width=1)  ## 1 numero coluna 1
    n1c1_m2.place(x=140, y=60)

    n2c1_m2 = tk.Entry(tela, width=1)  ## 2 numero coluna 1
    n2c1_m2.place(x=140, y=90)

    n3c1_m2 = tk.Entry(tela, width=1)  ## 3 numero coluna 1
    n3c1_m2.place(x=140, y=120)

    ## fim da 1 coluna

    ## inicio da 2 coluna

    n1c2_m2 = tk.Entry(tela, width=1)  ## 1 numero coluna 2
    n1c2_m2.place(x=180, y=60)

    n2c2_m2 = tk.Entry(tela, width=1)  ## 2 numero coluna 2
    n2c2_m2.place(x=180, y=90)

    n3c2_m2 = tk.Entry(tela, width=1)  ## 3 numero coluna 2
    n3c2_m2.place(x=180, y=120)

    ## fim da 2 coluna

    ## inicio da 3 coluna

    n1c3_m2 = tk.Entry(tela, width=1)  ## 1 numero coluna 3
    n1c3_m2.place(x=220, y=60)

    n2c3_m2 = tk.Entry(tela, width=1)  ## 2 numero coluna 3
    n2c3_m2.place(x=220, y=90)

    n3c3_m2 = tk.Entry(tela, width=1)  ## 3 numero coluna 3
    n3c3_m2.place(x=220, y=120)

    ## fim da 3 coluna

    btn_enviar2 = tk.Button(tela, text="Somar matrizes", command=lambda: [enviartudoDaMatriz2(), soma(), btn_enviar2.place_forget()])
    btn_enviar2.place(x=290, y=180)

def enviartudoDaMatriz1():
    global n1c1, n2c1, n3c1, n1c2, n2c2, n3c2, n1c3, n2c3, n3c3

    numero1 = int(n1c1.get().strip())
    numero2 = int(n1c2.get().strip())
    numero3 = int(n1c3.get().strip())

    numero4 = int(n2c1.get().strip())
    numero5 = int(n2c2.get().strip())
    numero6 = int(n2c3.get().strip())

    numero7 = int(n3c1.get().strip())
    numero8 = int(n3c2.get().strip())
    numero9 = int(n3c3.get().strip())

    matriz1.append(numero1)
    matriz1.append(numero2)  # PRIMEIRA LINHA DA MATRIZ
    matriz1.append(numero3)

    matriz1.append(numero4)
    matriz1.append(numero5)  # SEGUNDA LINHA DA MATRIZ
    matriz1.append(numero6)

    matriz1.append(numero7)
    matriz1.append(numero8)  # TERCEIRA LINHA DA MATRIZ
    matriz1.append(numero9)

def enviartudoDaMatriz2():
    global n1c1_m2, n2c1_m2, n3c1_m2, n1c2_m2, n2c2_m2, n3c2_m2, n1c3_m2, n2c3_m2, n3c3_m2

    numero1_m2 = int(n1c1_m2.get().strip())
    numero2_m2 = int(n1c2_m2.get().strip())
    numero3_m2 = int(n1c3_m2.get().strip())

    numero4_m2 = int(n2c1_m2.get().strip())
    numero5_m2 = int(n2c2_m2.get().strip())
    numero6_m2 = int(n2c3_m2.get().strip())

    numero7_m2 = int(n3c1_m2.get().strip())
    numero8_m2 = int(n3c2_m2.get().strip())
    numero9_m2 = int(n3c3_m2.get().strip())

    matriz2.append(numero1_m2)
    matriz2.append(numero2_m2)  # PRIMEIRA LINHA DA MATRIZ
    matriz2.append(numero3_m2)

    matriz2.append(numero4_m2)
    matriz2.append(numero5_m2)  # SEGUNDA LINHA DA MATRIZ
    matriz2.append(numero6_m2)

    matriz2.append(numero7_m2)
    matriz2.append(numero8_m2)  # TERCEIRA LINHA DA MATRIZ
    matriz2.append(numero9_m2)

def soma():

    matriz2texto.pack_forget()

    resposta = tk.Label(tela, text="A soma das matrizes é:", font=("Arial", 10), anchor="center")
    resposta.pack()
    soma_matriz1 = [matriz1[0] + matriz2[0]]
    soma_matriz2 = [matriz1[1] + matriz2[1]]
    soma_matriz3 = [matriz1[2] + matriz2[2]]
    soma_matriz4 = [matriz1[3] + matriz2[3]]
    soma_matriz5 = [matriz1[4] + matriz2[4]]
    soma_matriz6 = [matriz1[5] + matriz2[5]]
    soma_matriz7 = [matriz1[6] + matriz2[6]]
    soma_matriz8 = [matriz1[7] + matriz2[7]]
    soma_matriz9 = [matriz1[8] + matriz2[8]]

    matrizjunta1 = tk.Label(tela, text=f"{soma_matriz1}")
    matrizjunta1.place(x=140, y=60)

    matrizjunta2 = tk.Label(tela, text=f"{soma_matriz2}")
    matrizjunta2.place(x=140, y=90)

    matrizjunta3 = tk.Label(tela, text=f"{soma_matriz3}")  
    matrizjunta3.place(x=140, y=120)

    matrizjunta4 = tk.Label(tela, text=f"{soma_matriz4}")
    matrizjunta4.place(x=180, y=60)

    matrizjunta5 = tk.Label(tela, text=f"{soma_matriz5}")  
    matrizjunta5.place(x=180, y=90)

    matrizjunta6 = tk.Label(tela, text=f"{soma_matriz6}")  
    matrizjunta6.place(x=180, y=120)

    matrizjunta7 = tk.Label(tela, text=f"{soma_matriz7}")  
    matrizjunta7.place(x=220, y=60)

    matrizjunta8 = tk.Label(tela, text=f"{soma_matriz8}")  
    matrizjunta8.place(x=220, y=90)

    matrizjunta9 = tk.Label(tela, text=f"{soma_matriz9}") 
    matrizjunta9.place(x=220, y=120)














tela = tk.Tk()
tela.geometry("500x300")
tela.title("Somar Matriz")
first_matriz()
tela.mainloop()