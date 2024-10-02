# # Classe Aula 01/10
# class Carro: #Uma classe se inicia com a 1ª letra maiúscula
#     def __init__(self, motor, cor, placa, modelo):
#         self.motor = motor
#         self.cor = cor
#         self.placa = placa
#         self.modelo = modelo
#         self.quilometragem = 0 #Não precisa colocar o "quilometragem no def, porque está informando um valor a ele"

#     def liga(self):
#         print("Vrum")
#     def buzina(self):
#         print("Bi bi")
#     def freia(self):
#         print("Urrr")
#     def acelera(self, km):
#         self.quilometragem += km
#         print(f"O carro andou {km}km e agora está com {self.quilometragem}km rodados")

# uno_com_escada = Carro("1.6", "Verde", "DDD - 1111", "Fiat Uno") #Letra maiuscula, assim como está na classe
# #uno_com_escada.freia()
# uno_com_escada.acelera(150)
# uno_com_escada.acelera(250)
# uno_com_escada.acelera(300)

# #Atv 1: Crie um classe chamada cachorro com os atributos: nome, raça, idade

# class Cachorro:
#     def __init__(self, raca, nome, idade): #Atributos
#         self.raca = raca
#         self.nome = nome
#         self.idade = idade

#     def late(self): #Métodos
#         print("Au au")
#     def cheira(self):
#         print("Snif")

# cachorro1 = Cachorro("Golden", "Koda", "2")
# cachorro1.late()

# #Atv 2 Crie um classe chamada pessoa com os atributos: nome, idade, peso, gênero

# class Pessoa:
#     def __init__(self, nome, idade, peso, genero):
#         self.nome = nome
#         self.idade = idade
#         self.peso = peso
#         self.genero = genero

# pessoa1 = Pessoa("Maria", "25", "60kg", "feminino")

#Atv3 Crie uma classe Empresa que permita gerenciar funcionários. Os funcionários devem ter informações como nome, cargo e salário. A empresa deve ser capaz de adicionar, remover e listar funcionários.

# from typing import Any


# class Empresa:
#     def __int__ (self, nome, sede):
#         self.nome = nome
#         self.sede = sede
#         self.funcionarios = []
#         # self.funcionarios = funcionarios
    
#     def funcionarios_dic(self):
#         func = {}
#         func ["nome"] = input("Digite o nome do funcionário: ")
#         func ["cargo"] = input("Digite o cargo: ")
#         func ["salario"] = float(input("Digite o salário: "))

#         self.func.append(func)

#     def mostrar_func(self):
#         for funcionario in self.funcionarios:
#             print(funcionario)
    

#Atv5 classe chamada fatura

class Fatura:
    def __init__ (self, nome, preco, qtde):
        self.nome = nome 
        self.preco = preco
        self.qtde = qtde
        self.valor_total = 0

    def gerar_fatura(self):
        self.valor_total = self.qtde * self.preco
        return self.valor_total
    
    def get_nome(self):
        return
    
fatura = Fatura("Fatura teste", 3000, 5)
print(fatura.gerar_fatura())