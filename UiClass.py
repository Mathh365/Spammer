import tkinter as tk


class Ui:
    def __init__(self):
        # =========================
        # JANELA PRINCIPAL
        # =========================
        self.root = tk.Tk()  # ALTERADO: root virou self.root (precisa ser acessível fora do __init__)
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

        self.textEditor = tk.Text(
            rightArea,
            bg="black",
            fg="lime",
            insertbackground="white"
        )
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
        self.frameMensagem = tk.Frame(leftDownArea)  # ALTERADO: virou self (precisa ser acessado depois)
        self.frameReps = tk.Frame(leftDownArea)      # ALTERADO: virou self
        self.frameStart = tk.Frame(leftDownArea)     # ALTERADO: virou self

        # =========================
        # MENSAGEM
        # =========================
        tk.Label(self.frameMensagem, text="Mensagem a ser spammada").pack()
        self.entryMsg = tk.Entry(self.frameMensagem)  # ALTERADO: self.entryMsg
        self.entryMsg.pack()

        # =========================
        # REPETIÇÕES
        # =========================
        tk.Label(self.frameReps, text="Número de repetições").pack()
        self.entryReps = tk.Entry(self.frameReps)  # ALTERADO: self.entryReps
        self.entryReps.pack()

        # =========================
        # BOTÃO START
        # =========================
        self.startBtn = tk.Button(
            self.frameStart,
            text="Iniciar spam",
            command=self.start_spam  # ALTERADO: agora chama método da classe
        )
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
        tk.Label(
            leftUpArea,
            text="Qual tipo de Spam deseja realizar?\nFinito ou infinito?"
        ).pack(pady=30)

        tk.Button(
            leftUpArea,
            text="Infinito",
            command=self.set_infinite  # ALTERADO: agora chama método
        ).pack(pady=12, ipady=15, ipadx=10)

        tk.Button(
            leftUpArea,
            text="Finito",
            command=self.set_finite  # ALTERADO: agora chama método
        ).pack(pady=12, ipady=15, ipadx=10)

    # =========================
    # MÉTODOS DE CONTROLE
    # =========================

    def set_infinite(self):
        # ALTERADO: lógica saiu do __init__ e virou evento
        self.frameMensagem.pack()
        self.frameReps.pack_forget()
        self.frameStart.pack()

    def set_finite(self):
        # ALTERADO: lógica de UI agora controlada por método
        self.frameMensagem.pack()
        self.frameReps.pack()
        self.frameStart.pack()

    def start(self):
        # SEM ALTERAÇÃO: entrada do loop
        self.root.mainloop()

    # =========================
    # LÓGICA (PLACEHOLDER DO SPAMMER)
    # =========================
    def start_spam(self):
        # NOVO: ponto central da lógica futura
        msg = self.entryMsg.get()
        reps = self.entryReps.get()

        # debug temporário (você pode trocar depois)
        print("Mensagem:", msg)
        print("Repetições:", reps)