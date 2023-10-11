import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from campo_minado import CampoMinado

class JogoCampoMinadoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Campo Minado")
        self.nivel_var = tk.StringVar(value="1")

        self.mostrar_tela_niveis()

    def mostrar_tela_niveis(self):
        nivel_label = ttk.Label(self.master, text="Escolha o nível de dificuldade:", font=("Arial", 13))
        nivel_label.pack(pady=10)

        niveis = ["Fácil (8x8 - 10 bombas)", "Intermediário (10x16 - 30 bombas)", "Difícil (24x24 - 100 bombas)"]
        for i, nivel in enumerate(niveis, start=1):
            nivel_radio = ttk.Radiobutton(self.master, text=nivel, variable=self.nivel_var, value=str(i))
            nivel_radio.pack(pady=5)

        iniciar_button = ttk.Button(self.master, text="Iniciar Jogo", command=self.iniciar_jogo)
        iniciar_button.pack(pady=10)

    def iniciar_jogo(self):
        nivel = int(self.nivel_var.get())
        self.master.destroy()

        root = tk.Tk()
        app = JogoCampoMinadoTabuleiro(root, nivel)
        root.mainloop()

class JogoCampoMinadoTabuleiro:
    def __init__(self, master, nivel):
        self.master = master
        self.master.title("Campo Minado")
        self.nivel = nivel
        self.jogo = CampoMinado(nivel)

        self.criar_tabuleiro()

    def criar_tabuleiro(self):
        self.botoes = []
        for i in range(self.jogo.tamanho):
            linha = []
            for j in range(self.jogo.tamanho):
                botao = tk.Button(self.master, text='', width=2, height=1,
                                 command=lambda x=i, y=j: self.clicar_celula(x, y))
                botao.grid(row=i, column=j)
                linha.append(botao)
            self.botoes.append(linha)

    def clicar_celula(self, x, y):
        if not self.jogo.jogo_encerrado:
            self.jogo.descobrir_zona(x, y)
            self.atualizar_interface()
            
            if self.jogo.jogo_vencido:
                self.mostrar_fim_de_jogo("Parabéns! Você venceu!")
            elif self.jogo.jogo_encerrado:
                self.mostrar_fim_de_jogo("Você perdeu!")


    def mostrar_fim_de_jogo(self, mensagem):
        for i in range(self.jogo.tamanho):
            for j in range(self.jogo.tamanho):
                self.botoes[i][j].config(state="disabled")
        messagebox.showinfo("Fim de Jogo", mensagem)


    def atualizar_interface(self):
        for i in range(self.jogo.tamanho):
            for j in range(self.jogo.tamanho):
                celula = self.jogo.tabuleiro[i][j]
                botao = self.botoes[i][j]

                if celula == '-':
                    botao.config(text='', state="active", relief="raised", bg="light gray")
                elif celula == 'F':
                    botao.config(text='F', state="active", relief="raised", bg="yellow")
                elif celula == 'B':
                    botao.config(text='B', state="active", relief="sunken", bg="red")
                else:
                    botao.config(text=celula, state="disabled", relief="raised", bg="light gray")

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoCampoMinadoGUI(root)
    root.mainloop()
