import customtkinter as ctk

def escola():
    n1 = float(unidade_1.get())
    n2 = float(unidade_2.get())
    n3 = float(unidade_3.get())
    
    media = (n1 + n2 + n3)/3
    if (media>=6):
        resultado.configure(text=(f'A sua media foi {media :.1f} você foi aprovado !'))
        
    else:
        resultado.configuere(text=(f' A sua media foi {media :.1f } você foi reprovado !'))

ctk.set_appearance_mode('dark')

janela = ctk.CTk()

janela.geometry() 

unidade_1=ctk.CTkEntry (janela,
                        width=400,
                        height=20,
                        placeholder_text= 'Digite a nota da 1º unidade ')
unidade_1.pack(pady=10)

unidade_2=ctk.CTkEntry (janela,
                        width=400,
                        height=20,
                        placeholder_text= 'Digite a nota da 1º unidade ')
unidade_2.pack(pady=10)

unidade_3=ctk.CTkEntry (janela,
                        width=400,
                        height=20,
                        placeholder_text= 'Digite a nota da 1º unidade ')
unidade_3.pack(pady=10)

botao = ctk.CTkButton(janela,
                      fg_color='darkblue',
                      text='calcular'
                      command= escola)
botao.pack(pady=10)


resultado =ctk.CTkLabel(janela,
                        text=''
                        font=)


janela.mainloop()