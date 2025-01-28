# EXERCÍCIO 1

# Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio e 
# métodos para calcular a área e o perímetro do círculo.

# class Circulo:
#     def __init__ (self, raio):
#         self.raio = raio
#         self.pi = 3.14
    
#     def Calcula_area(self):
#         self.area = self.pi * (self.raio ** 2)
#         print(f"A área do círculo é: {self.area}")
    
#     def Calcula_perimetro(self):
#         self.perimetro = (2 * self.pi) * self.raio
#         print(f"O perímetro do círculo é: {self.perimetro}")
    
# circulo = Circulo(15)
# circulo.Calcula_area()
# circulo.Calcula_perimetro()

###################################################################################################

# EXERCÍCIO 2 

# Implemente uma classe chamada “ContaBancária” que possua atributos para armazenar o número da conta, nome do titular e saldo. Adicione métodos para realizar 
# depósitos e saques.

# class  ContaBancaria:
#     def __init__ (self, numero_conta, nome_titular, saldo):
#         self.numero_conta = numero_conta
#         self.nome_titular = nome_titular
#         self.saldo = saldo

#     def Deposito(self, valor_deposito):
#         self.valor_deposito = valor_deposito
#         self.saldo = self.saldo + self.valor_deposito
#         print(f"Depósito feito na conta {self.numero_conta} do titular {self.nome_titular}. valor disponível na conta: {self.saldo}")
    
#     def Saque(self, valor_saque):
#             self.valor_saque = valor_saque
#             if self.valor_saque> self.saldo:
#                 print("O valor a ser sacado é maior do que o valor disponível na conta")
#             else:
#                 print(f"Saque feito na conta {self.numero_conta} do titular {self.nome_titular}. valor disponível na conta: {self.saldo - self.valor_saque}")
    
        
        
# conta = ContaBancaria('01215411', "Gabriela", 1452.98)
# conta.Deposito(0)
# conta.Saque(1500)

#######################################################################################################

# EXERCÍCIO 3

# Crie uma classe chamada “Retângulo” que possua atributos para armazenar a largura e a altura. Implemente métodos para calcular a área e o perímetro do retângulo.

# class Retangulo:
#     def __init__ (self, largura, altura):
#         self.largura = largura
#         self.altura = altura
    
#     def Calcula_Area (self):
#         self.area = self.largura * self.altura
#         print(f"A área do retângulo é: {self.area}")

#     def Calcula_Perimetro(self):
#         self.perimetro = 2 * (self.largura + self.altura)
#         print(f"O perímetro do retângulo é: {self.perimetro}")

# retangulo = Retangulo(8.5, 9.6)
# retangulo.Calcula_Area()
# retangulo.Calcula_Perimetro()

################################################################################

# EXERCÍCIO 4

# Implemente uma classe chamada “Aluno” que possua atributos para armazenar o nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média das 
# notas e verificar a situação do aluno (aprovado ou reprovado)

# class Aluno:
#     def __init__(self, nome, matricula, nota1, nota2, nota3):
#         self.nome = nome
#         self.matricula = matricula 
#         self.nota1 = nota1
#         self.nota2 = nota2 
#         self.nota3 = nota3
    
#     def Calular_media(self):
#         self.media = (self.nota1 + self.nota2 + self.nota3)/3
#         print(f'A média do aluno {self.nome} de matrícula {self.matricula} é: {self.media}')
    
#     def Situacao_aluno(self):
#         if self.media >= 5:
#             print("O aluno está aprovado")
#         else: 
#             print("O aluno está reprovado")

# aluno = Aluno("Gabriela", "154356", 4.5, 2, 1)
# aluno.Calular_media()
# aluno.Situacao_aluno()

#################################################################################################


# EXERCÍCIO 5

# Crie uma classe chamada “Funcionário” com atributos para armazenar o nome, o salário e o cargo do funcionário. Implemente métodos para calcular o salário líquido, 
# considerando descontos de impostos e benefícios

# class Funcionario:
#     def __init__(self, nome, salario, cargo):
#         self.nome = nome 
#         self.salario = salario 
#         self.cargo = cargo
#         self.IMPOSTO = 52
#         self.BENEFICIO = 35
    
#     def Descontos(self):
#         self.total_descontos = self.IMPOSTO + self.BENEFICIO
#         self.salario = self.salario - self.total_descontos
#         print(f"O valor do salário liquido do funcionário {self.nome} com cargo {self.cargo} é: {self.salario}")



# funcionario = Funcionario("gabriela", 1856.6, "secretaria")
# funcionario.Descontos()


####################################################################################################################

# EXERCÍCIO 6

# Implemente uma classe chamada “Produto” que possua atributos para armazenar o nome, o preço e a quantidade em estoque. Adicione métodos para calcular o valor 
# total em estoque e verificar se o produto está disponível.

# class Produto:
#     def __init__(self, nome, preco, quantidade):
#         self.nome = nome 
#         self.preco = preco
#         self.quantidade = quantidade

#     def Calcular_Valor(self):
#         self.valor = self.preco * self.quantidade 
#         print(f"O valor total de produtos em estoque é: {self.valor}")

#     def Verificar(self):
#         if self.quantidade <= 0:
#             print(f"Produto {self.nome} está indisponível no estoque")
#         else:
#             print(f"O produto {self.nome} está disponível no estoque")

# produto = Produto("garrafa", 9.56, 0)
# produto.Calcular_Valor()
# produto.Verificar()

#####################################################################################################################

#EXERCÍCIO 7

# Crie uma classe chamada “Triângulo” com atributos para armazenar os três lados do triângulo. Implemente métodos para verificar se é um triângulo válido e calcular sua área

# class Triangulo:
#     def __init__(self, lado1, lado2, lado3, base, altura):
#         self.lado1 = lado1
#         self.lado2 = lado2
#         self.lado3 = lado3
#         self.base = base
#         self.altura = altura

#     def Verficar(self):
#         if ((self.lado1 + self.lado2) > self.lado3 and (self.lado2 + self.lado3) > self.lado1 and (self.lado1 + self.lado3) > self.lado2):
#             print(f"Esse triângulo é válido")
#         else:
#             print("Triângulo inválido")


#     def Calcula_Area(self):
#         self.area = (self.base * self.altura) / 2
#         print(f"A área do triângulo é {self.area}")

    
# triangulo = Triangulo(100,103,2, 5, 9)
# triangulo.Verficar()
# triangulo.Calcula_Area()

######################################################################################################

#EXERCÍCIO 8

# Implemente uma classe chamada “Carro” com atributos para armazenar a marca, o modelo e a velocidade atual do carro. Adicione métodos para acelerar, frear e exibir a 
#velocidade atual


# class Carro:
#     def __init__(self, marca, modelo, velocidade_atual):
#         self.marca = marca
#         self.modelo = modelo
#         self.velocidade_atual = velocidade_atual

#     def Acelerar(self, km_acelerar):
#         self.km_acelerar = km_acelerar
#         self.velocidade_atual += self.km_acelerar
#         print(f"A velocidade do carro {self.modelo} da marca {self.marca} foi aumentada em {self.km_acelerar}")
    
#     def Frear(self, km_frear):
#         self.km_frear = km_frear
#         self.velocidade_atual -= self.km_frear
#         print(f"A velocidade do carro {self.modelo} da marca {self.marca} foi diminuida em {self.km_frear}")
    
#     def Velocidade_atual(self):
#         print(f"A velocidade atual do carro é de {self.velocidade_atual}")


# carro = Carro("vw", "gol", 70)
# carro.Acelerar(30)
# carro.Frear(10)
# carro.Velocidade_atual()
         

#######################################################################################################################

#EXERCÍCIO 9

# Crie uma classe chamada “Paciente” que possua atributos para armazenar o nome, a idade e o histórico de consultas de um paciente. Implemente métodos para adicionar 
# uma nova consulta ao histórico e exibir as consultas realizadas.


# class Paciente:
#     def __init__ (self, nome, idade):
#         self.nome = nome 
#         self.idade = idade 
#         self.historico = []

#     def Adicionar_Consulta(self, consulta):
#         self.historico.append(consulta)

#     def Exibir_Consultas(self):
#         if self.historico:
#             print(f"Consultas realizadas por {self.nome}:")
#             for consulta in self.historico:
#                 print(f" {consulta}")
#         else:
#             print(f"Não existem consultas para {self.nome}.")

# paciente = Paciente("Liticie", 26)
# paciente.Adicionar_Consulta("Consulta dia 22/02/2025, ás 15:30. Especialidade: dermatologista")
# paciente.Adicionar_Consulta("Consulta dia 22/02/2025, ás 15:30. Especialidade: dermatolosa=dskjdjaksa")
# paciente.Exibir_Consultas()


#####################################################################################################################

#EXERCÍCIO 10

# Implemente uma classe chamada “Livro” com atributos para armazenar o título, o autor e o número de páginas do livro. Adicione métodos para emprestar o livro, 
# devolvê-lo e verificar se está disponível.

# class Livro:
#     def __init__(self, titulo, autor, numero_paginas):
#         self.titulo = titulo
#         self.autor = autor
#         self.numero_paginas = numero_paginas
#         self.disponivel = True


#     def Verificar_Livro (self):
#         if self.disponivel == True:
#             print(f"O livro {self.titulo} do autor {self.autor} com {self.numero_paginas} está disponível para empréstimo")
#         else:
#             print(f"O livro {self.titulo} do autor {self.autor} com {self.numero_paginas} não está disponível para empréstimo")

#     def Emprestar_Livro(self):
#         if self.disponivel == True:
#             self.disponivel = False
#             print(f"O livro {self.titulo} do autor {self.autor} com {self.numero_paginas} foi emprestado")
#         else:
#             print(f"O livro {self.titulo} do autor {self.autor} com {self.numero_paginas} não está disponível para ser emprestado")

#     def Devolver_Livro(self):
#         if self.disponivel == False:
#             self.disponivel = True
#             print(f"O livro {self.titulo} do autor {self.autor} com {self.numero_paginas} foi devolvido")
    
    

# livro = Livro("AAAAAA", "AAAAAAA", "AAAAA")
# livro.Emprestar_Livro()
# livro.Devolver_Livro()
# livro.Verificar_Livro()

#####################################################################################################################################

#EXERCÍCIO 11

#Implemente uma classe chamada “Banco” que represente uma instituição financeira. Essa classe deve conter métodos para cadastrar clientes, abrir contas bancárias e 
# realizar operações como saques, depósitos e transferências.

# class Banco:
#     def __init__(self, nome, cpf, senha):
#         self.nome = nome
#         self.cpf = cpf
#         self.senha = senha
#         self.clientes = []


#     def Cadastrar(self, nome, cpf, senha):
#         self.nome = nome
        


