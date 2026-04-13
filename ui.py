import tkinter as tk

def createUi(name: str, size: str):
    # CRIANDO JANELA
    root = tk.Tk()
    root.title(name)
    root.geometry(size)
    root.resizable(False, False)
    
    
    # CONTAINER PRINCIPAL
    main = tk.Frame(root)
    main.pack(fill="both", expand=True)
    
    # AREA ESQUERDA (BOTOES)
    leftArea = tk.Frame(main)
    leftArea.pack(side = "left", fill = "both", expand= True)
    
    # AREA DIREITA (CHAT / EDITOR)
    rightArea = tk.Frame(main, width= 350, bg= "gray")
    rightArea.pack(side="right", fill="y")
    
    rightArea.pack_propagate(False) #mantem largura fixa

    # BOTOES NO CENTRO DA JANELA
    infinityButton = tk.Button(leftArea, text="Spammer infinito")
    finityButton = tk.Button(leftArea, text="Spammer finito")
    infinityButton.pack(pady = 10)
    finityButton.pack(pady = 10)
    
    return root