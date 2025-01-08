#1000 - Hello World 
print('Hello World!')

#1001 - Extremamente Básico
a = int(input())
b = int(input())

x = a + b

print('X =', x)

#1002 - Área do Círculo
r = float(input())

area =  3.14159 * r**2

print(f'A={area:.4f}')

#1003 - Soma Simples
A = int(input())
B = int(input())

print(f'SOMA = {A+B}')

#1004 - Produto Simples
A = int(input())
B = int(input())
print(f'PROD = {A*B}')

#1005 - Média 1
A = float(input())
B = float(input())

media = (A*3.5 + B*7.5) / 11

print(f'MEDIA = {media:.5f}')

#1006 - Média 2
A = float(input())
B = float(input())
C = float(input())

media =(A*2 + B*3 + C*5)/10

print(f'MEDIA = {media:.1f}')

#1007 - Diferença
A = int(input())
B = int(input())
C = int(input())
D = int(input())

d = (A*B - C*D)

print('DIFERENCA =',d) 

#1008 - Sálario
n = int(input())
h = int(input())
v = float(input())

print(f'NUMBER = {n}')
print(f'SALARY = U$ {h*v:.2f}')

#1010 - Cálculo Simples
c1, n1, v1 = map(float, input().split())
c2, n2, v2 = map(float, input().split())

t1 = n1 * v1
t2 = n2 * v2

print(f'VALOR A PAGAR: R$ {t1+t2:.2f}')

#1011 - Esfera
R = float(input())
v = (4/3.0)*3.14159*R**3
print(f"VOLUME = {v:.3f}")

#1012 - Área
A, B, C = map(float, input().split())
print(f'TRIANGULO: {(A*C)/2:.3f}')
print(f'CIRCULO: {3.14159*(C**2):.3f}')
print(f'TRAPEZIO: {(A+B) * C / 2 :.3f}')
print(f'QUADRADO: {B**2:.3f}')
print(f'RETANGULO: {A*B:.3f}')

#1013 - O Maior 
a, b, c = map(int,input().split())
l = [a, b, c]
print(f'{max(l)} eh o maior')

#1014 - Consumo
X = int(input())
Y = float(input())

cm = X/Y

print(f"{cm:.3f} km/l")

#1015 - Distância Entre Dois Pontos 
import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f'{distancia:.4f}')

#1016 - Disttância
d = int(input())
print(f'{d*2} minutos')

#1017 - Gasto de Combustível
t = int(input())
v = int(input())

l = v * t / 12

print(f'{l:.3f}')

#1020 - Idade em Dias
idade = int(input())
mes = idade % 365
print(f'{idade//365} ano(s)')
print(f'{mes//30} mes(es)')
print(f'{mes%30} dia(s)')

#1035 - Teste de Seleção 1 
A, B, C, D = map(int, input().split())
if (B>C) and (D>A) and (C+D > A+B) and (C > 0 and D > 0) and A%2== 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')

#1037 - Intervalo
v = float(input())
if v >= 0 and v <= 25:
    print('Intervalo [0,25]')
elif v > 25 and v <= 50:
    print('Intervalo (25,50]')
elif v > 50 and v <= 75:
    print('Intervalo (50,75]')
elif v > 75 and v <= 100:
    print('Intervalo (75,100]')
elif v < 0 or v > 100:
    print('Fora de intervalo')

#Lanche - 1038
c, v = map(int, input().split())
if c == 1:
    valor = 4.00
elif c == 2:
    valor = 4.50
elif c == 3:
    valor = 5.00
elif c == 4:
    valor = 2.00
elif c == 5:
    valor = 1.50
print(f'Total: R$ {valor*v:.2f}')

#1041 - Coordenadas de um Ponto
x , y = map(float, input().split())
if x > 0 and y > 0:
    print('Q1')
elif x > 0 and y < 0:
    print('Q4')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x == 0 and (y > 0 or y < 0):
    print('Eixo Y')
elif (x > 0 or x < 0) and y == 0 :
    print('Eixo X')
else:
    print('Origem')

#1042 - Sort Simples
p, s, t = map(int, input().split())
l0 = [p, s, t]

l0.sort()
print(l0[0])
print(l0[1])
print(l0[2])
print('')
print(p)
print(s)
print(t)

#1043 - Triângulo
A, B, C = map(float, input().split())
if A + B > C and B + C > A and A + C > B:
    print(f'Perimetro = {A+B+C:.1f}')
else:
    print(f'Area = {(A+B)*C / 2:.1f}')

#1044 - Múltiplos
A , B = map(int, input().split())
if A%B == 0 or B%A ==0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')

#1046 - Tempo de Jogo
a, b = map(int, input().split())
if a == 0 and b == 0:
    tempo = 24
elif b > a:
    tempo = b - a
else:
    tempo = (24 - a) + b
print(f'O JOGO DUROU {tempo} HORA(S)')

#1048 - Aumento de Salário
salario = float(input())
if salario <= 400:
    reajuste = 0.15
    novoganho = salario  * reajuste
elif salario > 400 and salario <= 800:
    reajuste = 0.12
    novoganho = salario  * reajuste
elif salario > 800 and salario <= 1200:
    reajuste = 0.10
    novoganho = salario  * reajuste
elif salario > 1200 and salario <= 2000:
    reajuste = 0.07
    novoganho = salario  * reajuste
elif salario > 2000:
    reajuste = 0.04
    novoganho = salario  * reajuste
print(f'Novo salario: {salario + novoganho:.2f}')
print(f'Reajuste ganho: {novoganho:.2f}')
print(f'Em percentual: {reajuste*100:.0f} %')

#1049 - Animais
classe = input()
tipo = input()
especie = input()

valor = '' 

if classe == 'vertebrado':
    if tipo == 'ave':
        if especie == 'carnivoro':
            valor = 'aguia'
        elif especie == 'onivoro':
            valor = 'pomba'

    elif tipo == 'mamifero':
        if especie == 'onivoro':
            valor = 'homem'
        elif especie == 'herbivoro':
            valor = 'vaca'


elif classe == 'invertebrado':
    if tipo == 'inseto':
        if especie == 'hematofago':
            valor = 'pulga'
        elif especie == 'herbivoro':
            valor = 'lagarta'

    elif tipo == 'anelideo':
        if especie == 'hematofago':
            valor = 'sanguessuga'
        elif especie == 'onivoro':
            valor = 'minhoca'

print(valor)

#1050 - DDD
l = {61:'Brasilia', 71:'Salvador', 11:'Sao Paulo', 21:'Rio de Janeiro', 32:'Juiz de Fora', 19:'Campinas', 27:'Vitoria', 31:'Belo Horizonte'}
n = int(input())
if n in l:
    print(l[n])
else:
    print('DDD nao cadastrado')

#1052 - Mês
m = int(input())
mouths = ['January','February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October','November', 'December']
print(mouths[m-1])

#1059 - Números Pares
for x in range(1, 101):
    if x%2 == 0:
        print(x)

#1060 - Números Positivos
x = 0
l = []
while x < 6:
    n = float(input())
    l.append(n)
    x = x + 1
lp = []
for x in l:
    if x > 0:
        lp.append(x)
print(f'{len(lp)} valores positivos')

#1065 - Pares entre Cinco Números
lp = []
for x in range(5):
    x = int(input())
    if x%2 == 0:
        lp.append(x)
print(f'{len(lp)} valores pares')

#1066 - Pares, Ímpares, Positivos e Negativos
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

l = [a, b, c, d, e]
lpar = []
limpar = []
lp = []
ln = []
for x in l:
    if x%2 == 0:
        lpar.append(x)
    if x%2 != 0:
        limpar.append(x)
    if x > 0:
        lp.append(x)
    if x < 0:
        ln.append(x)
        
print(f'{len(lpar)} valor(es) par(es)')
print(f'{len(limpar)} valor(es) impar(es)')
print(f'{len(lp)} valor(es) positivo(s)')
print(f'{len(ln)} valor(es) negativo(s)')

#1067 - Números Ímpares 
n = int(input())

for x in range(1 , n+1, 2):
    print(x)

#1070 - Seis Números Ímpares 
n = int(input())
if n % 2 == 0:
    n = n + 1
    cont = 6
    x = 1
    while x <= cont:
        print(n)
        n = n + 2
        x = x + 1
else:
    cont = 6
    x = 1
    while x <= cont:
        print(n)
        n = n + 2
        x = x + 1

#1071 - Soma de Impares Consecutivos Consecutivos I
X = int(input())
Y = int(input())
soma = 0
if X == Y:
    soma = 0
if X > Y:
    for x in range(Y+1, X):
        if x%2 != 0:
            soma = soma + x
else:
    for x in range(X+1, Y):
        if x%2 != 0:
            soma = soma + x
print(soma)

#1072 - Intervalo 2
n = int(input())
lin = []
lout = []
for x in range(n):
    x = int(input())
    if x >= 10 and x <= 20:
        lin.append(x)
    else:
        lout.append(x)
print(f'{len(lin)} in')
print(f'{len(lout)} out')

#1073 - Quadrado de Pares
n = int(input())
for x in range(1,n+1):
    if x%2 == 0:
        print(f'{x}^2 = {x**2}')

