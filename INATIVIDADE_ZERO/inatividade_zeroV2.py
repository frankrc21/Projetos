import customtkinter as ctk
import pyautogui
import threading
import time

# Criação da janela principal
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

janela = ctk.CTk()  # Cria a janela principal
janela.title("Inatividade Zero")  # Título da janela
janela.geometry("260x200")  # Tamanho da janela

texto = ctk.CTkLabel(janela, text="INATIVIDADE ZER0", font=("Futura Md BT", 16, "bold"), text_color="white")
texto.pack(pady=(10, 0))

# Variáveis para controle do timer e do fechamento da janela
tempo = 0
timer_ativo = False
inatividade_ativa = False
parar_thread = threading.Event()  # Evento para parar a thread

# Função para atualizar o timer
def atualizar_timer():
    global tempo
    if timer_ativo:
        tempo += 1
        
        # Calcular horas, minutos e segundos
        horas = tempo // 3600
        minutos = (tempo % 3600) // 60
        segundos = tempo % 60
        
        timer_label.configure(text=f"{horas:02}:{minutos:02}:{segundos:02}")  # Formato hh:mm:ss
        janela.after(1000, atualizar_timer)  # Chama a função novamente após 1000 ms (1 segundo)

# Função para alternar o timer e a inatividade
def alternar_timer():
    global timer_ativo, inatividade_ativa
    timer_ativo = not timer_ativo  # Alterna o estado
    if timer_ativo:
        iniciar_botao.configure(text="Interromper", fg_color="red")  # Muda para vermelho
        atualizar_timer()  # Inicia o timer
        if not inatividade_ativa:
            inatividade_ativa = True
            threading.Thread(target=impedir_inatividade).start()  # Inicia a função em uma thread separada
    else:
        iniciar_botao.configure(text="Iniciar", fg_color="green")  # Muda para verde
        inatividade_ativa = False  # Para a função de impedir inatividade

# Função para impedir a inatividade
def impedir_inatividade():
    while not parar_thread.is_set():  # Verifica se deve parar
        if inatividade_ativa:
            pyautogui.press('shift')  # Pressiona a tecla 'shift'
        time.sleep(170)  # Espera 3 minutos e 50 segundos

# Função para zerar o timer
def zerar_timer():
    global tempo, timer_ativo
    tempo = 0  # Zera o tempo
    timer_label.configure(text="00:00:00")  # Reseta o rótulo do timer
    if timer_ativo:
        # Se o timer estiver ativo, não zera o estado, apenas reseta a contagem
        pass
    else:
        # Se o timer estiver parado, muda o botão para "Iniciar Timer" e verde
        iniciar_botao.configure(text="Iniciar", fg_color="green")

# Função para tratar o fechamento da janela
def on_closing():
    parar_thread.set()  # Sinaliza a thread para parar
    janela.destroy()  # Fecha a janela

# Label para exibir o timer
timer_label = ctk.CTkLabel(janela, text="00:00:00", font=("Arial", 16))
timer_label.pack(pady=10)

# Botão para ligar/desligar o timer
iniciar_botao = ctk.CTkButton(janela, text="Iniciar", command=alternar_timer, fg_color="green")  # Cor inicial verde
iniciar_botao.pack(pady=10)

# Botão para zerar o timer
zerar_botao = ctk.CTkButton(janela, text="Zerar Timer", command=zerar_timer, fg_color="blue")
zerar_botao.pack(pady=10)

# Define o protocolo para o fechamento da janela
janela.protocol("WM_DELETE_WINDOW", on_closing)

# Inicia a thread de impedir inatividade antes do loop principal
threading.Thread(target=impedir_inatividade, daemon=True).start()

# Inicia o loop principal da interface gráfica
janela.mainloop()
