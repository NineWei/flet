# import flet as ft

# def main(page: ft.Page):
#     page.title = "Título"
#     page.add(
#         ft.Text("cor", color="green"),
#         ft.ElevatedButton("Botão com cor", bgcolor="green", color="red")
#     )

# ft.app(target=main)

# import flet as ft

# def main(page: ft.Page):

#     page.title = "Formulário de Cadastro" #Título 
    
#     nome = ft.TextField(label="Nome completo", autofocus=True) 
#     email = ft.TextField(label="Email", keyboard_type=ft.KeyboardType.EMAIL)
#     data = ft.TextField(label= "Data nascimento")
#     endereco = ft.TextField(label= "Endereço")
    
#     def on_submit(e):
    
#         page.add(ft.Text(f"Cadastro recebido:\nNome: {nome.value}\nEmail: {email.value}\nData: {idade.value}\nEndereço: {endereco.value}")) #O \n é usado para pular 1 linha
    
#     submit_button = ft.FilledButton(text="Enviar", on_click=on_submit)
    
#     page.add(nome, email, data, endereco, submit_button)

# ft.app(target=main)


# palavra = "python"
# for letra in palavra:
#     print(letra)

# palavra = "python"
# print (palavra{3})

numero = int(input("informe um numero de 1 a 10"))
mult * numero
for numero in range (1, 11):
    print(numero)

