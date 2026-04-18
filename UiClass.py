import tkinter as tk
import spamming
import threading

class Ui:
    def __init__(self):
        
        self.spammer = spamming.Spammer()
    
        # =========================
        # JANELA PRINCIPAL
        # =========================
        self.root = tk.Tk()
        self.root.title("Nuclear Spammer")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)

        # =========================
        # CONTAINER PRINCIPAL
        # =========================
        main = tk.Frame(self.root)
        main.pack(fill="both", expand=True)

        # =========================
        # ÁREA ESQUERDA
        # =========================
        leftArea = tk.Frame(main)
        leftArea.pack(side="left", fill="both", expand=True)

        # =========================
        # ÁREA DIREITA (EDITOR)
        # =========================
        rightArea = tk.Frame(main, width=350, bg="gray")
        rightArea.pack(side="right", fill="y")
        rightArea.pack_propagate(False)

        self.textEditor = tk.Text(rightArea, bg="black", fg="lime", insertbackground="white")
        self.textEditor.pack(fill="both", expand=True, padx=5, pady=5)
        self.textEditor.insert("end", ">>> Editor pronto para testes\n")

        # =========================
        # ÁREA SUPERIOR (BOTÕES)
        # =========================
        leftUpArea = tk.Frame(leftArea)
        leftUpArea.pack(fill="x")

        # =========================
        # ÁREA INFERIOR (INPUTS DINÂMICOS)
        # =========================
        leftDownArea = tk.Frame(leftArea)
        leftDownArea.pack(fill="x", side="bottom", pady=(0, 100))

        # ===== FRAMES DE INPUT =====
        self.frameMensagem = tk.Frame(leftDownArea)  
        self.frameReps = tk.Frame(leftDownArea)      
        self.frameStart = tk.Frame(leftDownArea)     

        # =========================
        # MENSAGEM A SER SPAMMADA
        # =========================
        self.msg = tk.Label(self.frameMensagem, text="Mensagem a ser spammada")
        self.entryMsg = tk.Entry(self.frameMensagem)
        self.msg.pack()
        self.entryMsg.pack()

        # =========================
        # REPETIÇÕES
        # =========================
        self.reps = tk.Label(self.frameReps, text="Número de repetições")
        self.entryReps = tk.Entry(self.frameReps)
        self.reps.pack()
        self.entryReps.pack()

        # =========================
        # BOTÃO START
        # =========================
        self.startBtn = tk.Button(self.frameStart, text="Iniciar spam", command=self.start_spam)
        self.startBtn.pack()

        # =========================
        # COMEÇA ESCONDIDO
        # =========================
        self.frameMensagem.pack_forget()
        self.frameReps.pack_forget()
        self.frameStart.pack_forget()

        # =========================
        # BOTÕES DE MODO
        # =========================
        tk.Label(leftUpArea, text="Qual tipo de Spam deseja realizar?\nFinito ou infinito?").pack(pady=30)

        tk.Button(leftUpArea, text="Infinito", command=self.setInfinity).pack(pady=12, ipady=15, ipadx=10)
        tk.Button(leftUpArea, text="Finito", command=self.setFinity).pack(pady=12, ipady=15, ipadx=10)

    # =========================
    # MÉTODOS DE CONTROLE
    # =========================

    def setInfinity(self):
        self.frameMensagem.pack()
        self.frameReps.pack_forget()
        self.frameStart.pack()

    def setFinity(self):
        self.frameMensagem.pack()
        self.frameReps.pack()
        self.frameStart.pack()

    def startUi(self):
        self.root.mainloop()

    # =========================
    # SPAMMER
    # =========================
    def start_spam(self):
        msg: str = self.entryMsg.get()
        
        repsStr = self.entryReps.get()
        reps = int(repsStr) if repsStr.strip() else None
        
        threading.Thread(
            target=self.spammer.startLoop,
            args=(msg, reps),
            daemon=True
        ).start()
            