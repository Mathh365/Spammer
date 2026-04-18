import tkinter as tk

def createUi():
    # CRIANDO JANELA
    root = tk.Tk()
    root.title("Nuclear Spammer")
    root.geometry("1000x600")
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
    
    textEditor = tk.Text(rightArea, bg="black", fg="lime", insertbackground="white")
    textEditor.pack(fill="both", expand=True, padx=5, pady=5)
    textEditor.insert("end", ">>> Editor pronto para testes\n")
    
    rightArea.pack_propagate(False) # mantem largura fixa
    
    
    # AREA DOS BOTOES
    leftUpArea = tk.Frame(leftArea)
    leftUpArea.pack(fill="x")
    
    
    # AREA DOS INPUTS
    leftDownArea = tk.Frame(leftArea)
    leftDownArea.pack(fill="x", side="bottom", pady=(0, 100))
    
    frameMensagem = tk.Frame(leftDownArea)
    frameReps = tk.Frame(leftDownArea)
    frameStart = tk.Frame(leftDownArea)
    
    labelMsg = tk.Label(frameMensagem, text="Mensagem a ser spammada")
    entryMsg = tk.Entry(frameMensagem)
    labelMsg.pack()
    entryMsg.pack()
    
    labelReps = tk.Label(frameReps, text="Numero de repetiçoes")
    entryReps = tk.Entry(frameReps)
    labelReps.pack()
    entryReps.pack()
    
    startBtn = tk.Button(frameStart, text="Iniciar spam", width=10, height=3)
    startBtn.pack()
    
    frameMensagem.pack_forget()
    frameReps.pack_forget()
    frameStart.pack_forget()
    

    # BOTOES NO CENTRO DA JANELA
    label = tk.Label(leftUpArea, text="Qual tipo de Spam deseja realizar?\nFinito ou infinito?")
    label.pack(pady=30)
    
    infinityButton = tk.Button(leftUpArea, text="Infinito")
    finityButton = tk.Button(leftUpArea, text="Finito")
    
    infinityButton.pack(pady = 12, ipady= 15, ipadx= 10)
    finityButton.pack(pady = 12, ipady= 15, ipadx= 10)
    
    return root, frameMensagem, frameReps, frameStart