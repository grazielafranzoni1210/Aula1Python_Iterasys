# imports / bibliotecas

# classes

# métodos e funções

def print_hi(name):
    print(f'Oi, {name}')

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2

def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento / 2

def contagem_progressiva(fim):
    for numero in range(fim): # repetir o bloco de zero até o fim
        print(numero)         # exibir o número

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):


        if numero < 10:
            print(f'00{numero}', '-', nome)
        elif numero < 99:
            print(f'0{numero}', '-', nome)
        else:
            print(numero + 1, '-', nome)

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4  == 1:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero+1))


# estrutura de identificação/execução
if __name__ == '__main__':
    print_hi('Graziela')

# chamar a função de cálculo da área do retângulo
resultado = calcular_area_do_retangulo(3, 4)
print(f'A área do retângulo é de {resultado} m²')

# chamar a função de cálculo da área do quadrado
resultado = calcular_area_do_quadrado(5)
print(f'A área do quadrado é de {resultado} m²')

# chamar a função de cálculo da área do triângulo
resultado = calcular_area_do_triangulo(6,7)
print(f'A área do triângulo é de {resultado} m²')

# executar uma contagem progressiva
contagem_progressiva(11)

# exibir o nome do candidato várias vezes
apoiar_candidato('Faker', 101)

# brincar de plim
brincar_de_plim(101)

