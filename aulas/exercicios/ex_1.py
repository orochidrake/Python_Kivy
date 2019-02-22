print("Andre Augusto Zaguette Fernandes")


nome = input("Digite Seu Nome: ")
idade = input("Digite Sua Idade: ")

num = int(input("Digite Um Numero: "))
num_2 = int(input("Digite Um Numero: "))
num_3 = int(input("Digite Um Numero: "))
soma = num + num_2 + num_3

quad = num ** 2
cubo = num ** 3


nota_1 = float(input("Digite sua nota : "))
nota_2 = float(input("Digite sua nota 2 : "))
nota_3 = float(input("Digite sua nota 3 : "))
nota_4 = float(input("Digite sua nota 4 : "))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

metros = float(input("Digite o Valor em Metros : "))
centimetro = metros * 100

largura = float(input("Digite a Largura : "))
altura = float(input("Digite a Altura : "))

metro_quadrados = largura * altura

dias = float(input("Digite os dias : "))
hora = float(input("Digite as horas : "))
minuto = float(input("Digite os minutos : "))
segundo = float(input("Digite os segundos : "))

dia_horas = dias * 24
hora_minuto = hora * 60
minuto_segundo = minuto * 60
total_segundos = ((dia_horas * 60) * 60) + (hora_minuto * 60) + minuto_segundo + segundo

valor_compra = float(input("Digite o valor dos produtos: "))
desconto = valor_compra * 0.10
valor_total = valor_compra - desconto

print("")


print("O seu nome é: %s, e sua Idade é: %s" % (nome, idade))
print("")

print("O Numero digitado é: ", num)
print("")

print("A Soma do ", num, "+", num_2, "+", num_3, "é: ", soma)
print("")

print("Sua Media é: ", media)

print("")

print("A Conversao de ", metros, " para centimetro é: ", centimetro)

print(num, "Elevado ao quadrado é: ", quad, "e elevado ao cubo é: ", cubo)

print(
    "o total em segundos dos ",
    dias,
    "+",
    hora,
    "+",
    minuto,
    "+",
    segundo,
    "é: ",
    total_segundos,
)
print(
    "a Area total de um retangulo com ",
    altura,
    "de altura e ",
    largura,
    "de largura é de ",
    metro_quadrados,
    "m²",
)

print(
    "O Valor dos produtos é :",
    valor_compra,
    "vamos dar 10 por cento de desconto, que vai ser :",
    desconto,
    "e o total da compra é: ",
    valor_total,
)

