import customtkinter as ctk
from random import sample

# função pra sortear a lista de alunos
def sortear_nomes():
    entrada = entrada_text.get("1.0", "end-1c")  # puxa o texto da entrada
    lista = entrada.split(', ')  # separa os nomes por vírgula e espaço
    nova_lista = sample(lista, len(lista))  # sorteia a lista

    resultado_text.delete("1.0", "end")  # limpa o texto do resultado

    for i, nome in enumerate(nova_lista, start=1):
        resultado_text.insert("end", f'{i} - {nome}\n')  # insere os nomes sorteados

# janela principal
ctk.set_appearance_mode("dark")  # modo escuro da biblioteca
ctk.set_default_color_theme("blue")  # tema azul

janela = ctk.CTk()  # cria a janela
janela.title("Sorteio de Nomes")  # titulo
janela.geometry("400x350")  # tamanho

# campo de imput dos nomes dos alunos
entrada = ctk.CTkLabel(janela, text="Digite os nomes dos alunos:")
entrada.pack(pady=(10, 0))

# exemplo
entrada2 = ctk.CTkLabel(janela, text="(Por exemplo: Fulano, Beltrano, Cicrano...)", font=("", 10))
entrada2.pack(pady=0)

# espaço pra inserir os nomes
entrada_text = ctk.CTkTextbox(janela, height=30)
entrada_text.pack(pady=10)

# botão pra sortear os nomes
embaralhar_button = ctk.CTkButton(janela, text="Clique para sortear a ordem", command=sortear_nomes)
embaralhar_button.pack(pady=10)

# textor rs
resultado_label = ctk.CTkLabel(janela, text="Ordem sorteada:")
resultado_label.pack(pady=10)

# campo pra mostrar os nomes sorteados
resultado_text = ctk.CTkTextbox(janela, height=100)
resultado_text.pack(pady=10)

# isso aqui serve pra janela continuar aberta
janela.mainloop()
