# import flet as ft 

# def main(page: ft.Page):
#     page.title = "Formulário"
#         ft.Textbox(label="Digite seu nome completo")



# import flet as ft

# def main(page: ft.Page):
#     page.add(
#         ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text("Nome")),
#                 ft.DataColumn(ft.Text("Email")),
#                 # ft.DataColumn(ft.TextField(hint_text="Digite seu nome: ")),
#             ],
#             rows=[
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text("John")),
#                         ft.DataCell(ft.Text("Smith")),
#                     ],
#                 ),
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text("Jack")),
#                         ft.DataCell(ft.Text("Brown")),
#                     ],
#                 ),
#                 ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text("Alice")),
#                         ft.DataCell(ft.Text("Wong")),
#                     ],
#                 ),
#             ],
#         ),
#     )

# ft.app(main)

# import flet as ft

# def main(page: ft.Page):
#     page.title = "Formulário de Contato"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     name_input = ft.TextField(
#         hint_text="Digite seu nome",
#         label="Nome",
#         width=300,
#         bgcolor=ft.colors.LIGHT_BLUE_50,
#         border_color=ft.colors.BLUE_400,
#         border_radius=5
#     )

#     email_input = ft.TextField(
#         hint_text="Digite seu e-mail",
#         label="E-mail",
#         width=300,
#         bgcolor=ft.colors.LIGHT_BLUE_50,
#         border_color=ft.colors.BLUE_400,
#         border_radius=5
#     )


#     def submit_clicked(e):
#         name = name_input.value
#         email = email_input.value
#         if name and email:
#             page.add(ft.Text(f"Nome: {name}, E-mail: {email}"))
#             name_input.value = ""
#             email_input.value = ""
#         else:
#             page.add(ft.Text("Por favor, preencha todos os campos.", color=ft.colors.RED))


#     submit_button = ft.ElevatedButton(
#         text="Enviar",
#         on_click=submit_clicked,
#         bgcolor=ft.colors.GREEN_500,
#         color=ft.colors.WHITE,
#         style=ft.ButtonStyle(
#             shape=ft.RoundedRectangleBorder(radius=10)
#         )
#     )

#     # Adiciona os componentes à página
#     page.add(name_input, email_input, submit_button)

# ft.app(target=main)


import flet as ft

def main(page: ft.Page):

    page.title = "Formulário de Cadastro"
    page.bgcolor = ft.colors.BLUE_50
    
    nome = ft.TextField(label="Nome completo", autofocus=True)
    email = ft.TextField(label="Email", keyboard_type=ft.KeyboardType.EMAIL)
    senha = ft.TextField(label= "Insira a senha", password = True, can_reveal_password=True)
    endereco = ft.TextField(label= "Endereço")
    
    def on_submit(e):
    
        page.add(ft.Text(f"Cadastro recebido:\nNome: {nome.value}\nEmail: {email.value}\nEndereço: {endereco.value}")) #O \n é usado para pular 1 linha
    
    submit_button = ft.OutlinedButton(text="Enviar", on_click=on_submit, style=ft.ButtonStyle(
            text_style=ft.TextStyle(size=20)))
    
    page.add(nome, email, senha, endereco, submit_button)

ft.app(target=main)