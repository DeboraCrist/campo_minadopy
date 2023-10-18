import datetime
import tkinter as tk
from tkinter import ttk, messagebox
import re
import time
from campo_minado import CampoMinado

class JogoCampoMinadoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Campo Minado")
        self.nivel_var = tk.StringVar(value="1")
        self.master.geometry("400x270") 
        self.mostrar_tela_niveis()

    def mostrar_tela_niveis(self):
        nivel_label = ttk.Label(self.master, text="Escolha o nível:", font=("Arial", 15))
        nivel_label.pack(pady=20)
        niveis = ["Fácil (8x8 - 10 bombas)", "Intermediário (10x16 - 30 bombas)", "Difícil (24x24 - 100 bombas)"]
        for i, nivel in enumerate(niveis, start=1):
            nivel_radio = ttk.Radiobutton(self.master, text=nivel, variable=self.nivel_var, value=str(i))
            nivel_radio.pack(pady=5)

        iniciar_button = ttk.Button(self.master, text="Iniciar Jogo", command=self.iniciar_jogo, style='HistButton.TButton')
        iniciar_button.pack(pady=10)
        style = ttk.Style()
        style.configure('HistButton.TButton', background='#415ce1')
        historico_button = ttk.Button(self.master, text="Histórico", command=self.exibir_historico)
        historico_button.pack(side="top", anchor="ne", padx=10, pady=10)

    def exibir_historico(self):
        try:
            with open('historico.txt', 'r') as arquivo:
                historico = arquivo.readlines()
                historico.reverse()
                historico = "".join(historico)
                self.mostrar_janela_historico(historico)
        except FileNotFoundError:
            messagebox.showinfo("Histórico", "Nenhum histórico disponível.")

    def mostrar_janela_historico(self, historico):
        historico_window = tk.Toplevel(self.master)
        historico_window.title("Histórico de Partidas")

        historico_text = tk.Text(historico_window, wrap=tk.WORD, width=40, height=10)
        historico_text.pack(padx=10, pady=10)
        historico_text.insert(tk.END, historico)

        scores = re.findall(r"Pontuação: (\d+)", historico)
        if scores:
            historico_text.insert(tk.END, "\n\nPontuações:\n")
            for score in scores:
                historico_text.insert(tk.END, f"  - {score}\n")

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
        self.modo_bandeira = False
        self.criar_tabuleiro() 
        self.primeira_jogada = True
        self.elapsed_time = 0 
        

    def criar_tabuleiro(self):
        self.botoes = []
        for i in range(self.jogo.linhas):
            linha = []
            for j in range(self.jogo.colunas):
                botao = tk.Button(self.master, text='', width=1, height=1, command=lambda x=i, y=j: self.clicar_celula(x, y), font=("Arial", 7))
                botao.grid(row=i, column=j)
                linha.append(botao)
            self.botoes.append(linha)

        botoes_frame = tk.Frame(self.master)
        botoes_frame.grid(row=self.jogo.linhas, columnspan=self.jogo.colunas)

        reiniciar_button = ttk.Button(botoes_frame, text="Reiniciar", command=self.reiniciar_jogo)
        reiniciar_button.grid(row=0, column=0)
        self.reiniciar_button = reiniciar_button

        sair_button = ttk.Button(botoes_frame, text="Sair", command=self.sair_jogo)
        sair_button.grid(row=0, column=1)
        self.sair_button = sair_button

        self.modo_bandeira_button = ttk.Button(botoes_frame, text="Modo Bandeira", command=self.alternar_modo_bandeira)
        self.modo_bandeira_button.grid(row=0, column=2)

        self.num_bandeiras_var = tk.StringVar()
        num_bandeiras_label = ttk.Label(self.master, textvariable=self.num_bandeiras_var, font=("Arial", 11))
        num_bandeiras_label.grid(row=self.jogo.linhas + 1, columnspan=self.jogo.colunas)
        self.atualizar_num_bandeiras()
        self.num_bandeiras_label = num_bandeiras_label

        self.tempo_var = tk.StringVar(value="00:00")
        self.tempo_label = ttk.Label(self.master, textvariable=self.tempo_var, font=("Arial", 11))
        self.tempo_label.grid(row=self.jogo.linhas + 2, columnspan=self.jogo.colunas)
        
        self.start_time = None
        self.update_timer()

    def update_timer(self):
        if not self.jogo.jogo_encerrado:
            if self.start_time is None:
                self.start_time = time.time()
            self.elapsed_time = int(time.time() - self.start_time)
            minutes = self.elapsed_time // 60
            seconds = self.elapsed_time % 60
            self.tempo_var.set(f"{minutes:02d}:{seconds:02d}")
            self.jogo.end_time = datetime.datetime.now() 
            self.master.after(1000, self.update_timer)

    def stop_timer(self):
        if self.start_time:
            self.elapsed_time = int(time.time() - self.start_time)
            self.start_time = None  

    def clicar_celula(self, x, y):
        if not self.jogo.jogo_encerrado:
            if not self.start_time:
                self.start_time = time.time()
            if self.modo_bandeira:
                self.jogo.colocar_bandeira(x, y)
            else:
                if self.primeira_jogada:
                    try:
                        self.jogo.realizar_primeira_jogada(x, y)
                        self.primeira_jogada = False
                    except ValueError as e:
                        messagebox.showerror("Erro", str(e))
                        return
                else:
                    self.jogo.descobrir_zona(x, y)

            self.atualizar_interface()
            if self.jogo.jogo_vencido:
                self.mostrar_fim_de_jogo("Parabéns! Você venceu!")
            elif self.jogo.jogo_encerrado:
                self.mostrar_fim_de_jogo("Você perdeu!")
                self.jogo.guardar_resultado()
        self.atualizar_num_bandeiras()

    def mostrar_fim_de_jogo(self, mensagem):
        self.stop_timer()  
        for i in range(self.jogo.linhas):
            for j in range(self.jogo.colunas):
                self.botoes[i][j].config(state="disabled")
        mensagem += f"\n\nPontuação: {self.elapsed_time:.2f} segundos"
        messagebox.showinfo("Fim de Jogo", mensagem)
        with open('historico.txt', 'a') as arquivo:
            arquivo.write(f'{mensagem}\n')

    def atualizar_interface(self):
        for i in range(self.jogo.linhas):
            for j in range(self.jogo.colunas):
                celula = self.jogo.tabuleiro[i][j]
                botao = self.botoes[i][j]

                if celula == '-':
                    botao.config(text='', state="active", relief="raised", bg="light gray")
                elif celula == 'F':
                    botao.config(text='F', state="active", relief="raised", bg="yellow")
                elif celula == 'B':
                    botao.config(text='B', state="disabled", relief="sunken", bg="red")
                else:
                    botao.config(text=celula, state="disabled", relief="raised", bg="white") 

    def alternar_modo_bandeira(self):
        self.modo_bandeira = not self.modo_bandeira
        if self.modo_bandeira:
            self.modo_bandeira_button.config(text="Bandeira ON", style='Red.TButton')
        else:
            self.modo_bandeira_button.config(text="Bandeira OFF", style='TButton')

    def atualizar_num_bandeiras(self):
        num_bandeiras_colocadas = self.jogo.bandeiras_colocadas
        num_bandeiras_restantes = self.jogo.num_bombas - num_bandeiras_colocadas
        self.num_bandeiras_var.set(f'Bandeiras: {num_bandeiras_colocadas}/{self.jogo.num_bombas}')

    def reiniciar_jogo(self):
        self.start_time = None
        self.jogo = CampoMinado(self.nivel)
        self.primeira_jogada = True
        self.atualizar_interface()
        for i in range(self.jogo.linhas):
            for j in range(self.jogo.colunas):
                self.botoes[i][j].config(text='')

        self.update_timer()  

    def sair_jogo(self):
        self.jogo.sair()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoCampoMinadoGUI(root)
    root.mainloop()
