import matplotlib.pyplot as plt

# Número de elementos da lista utilizada, também indica o número de posições que a lista terá
N = 20

# lista com os dados que serão organizados
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]


print("Lista original:", lista)


x = range(0,20,1)
y = lista

plt.figure()
plt.plot(x,y,'ok')
plt.title("gráfico em ordem original")
plt.xlabel("x eh os valores da lista")
plt.savefig("fig/bubble-inicio.png")
plt.close()

trocofora = 0
# Para cada i (nome escolhido para selecionar uma posição), indo da posição 0 até a penultima posição (N-1) o terceiro número indica a quantidade de algarismos que o programa lerá (..,...1)
for i in range(0,N-1,1):
# Escolhemos um segundo item dentro da lista que foi nomeado de j usando a mesma função do range, este esta condicionado as posições que o i assumi
    for j in range(i+1,N,1):
	# Atributo condicional de i em relação a j
        if lista[i] > lista[j]:
# Criou-se um terceiro item vazio para que cada vez que a condição anterior acontecer os itens i e j troquem de po
            tmp = lista[i]
            lista[i] = lista[j]
            lista[j] = tmp
            trocofora = trocofora + 1
        x=range(0,20,1)
        y=lista
        plt.figure()
        plt.plot(x,y,'ok')
        plt.title("grafico em progresso")
        plt.xlabel("x eh os valores da lista")
        plt.savefig("fig/bubble-{}.png".format(trocofora))
        plt.close()


print("Lista em ordem crescente:", lista)



x = range(0,20,1)
y = lista

plt.figure()
plt.plot(x,y,'ok')
plt.title("gráfico em ordem crescente")
plt.xlabel("x eh os valores da lista")
plt.savefig("fig/bubble-fim.png")
plt.close()

print("Cinco menores valores",lista[0:5])
print("Cinco maiores valores",lista[N-5:N])





