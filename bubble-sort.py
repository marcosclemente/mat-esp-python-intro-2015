# Número de elementos da lista utilizada, também indica o número de posições que a lista terá
N = 20

# lista com os dados que serão organizados
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]

# Para cada i (nome escolhido para selecionar uma posição), indo da posição 0 até a penultima posição (N-1) o terceiro número indica a quantidade de algarismos que o programa lerá (..,...1)
for i in range(0,N-1,1)

# Escolhemos um segundo item dentro da lista que foi nomeado de j usando a mesma função do range, este esta condicionado as posições que o i assumi
    for j in range(i+1,N,1)
	
	# Atributo condicional de i em relação a j
	    if lista[i] > lista[j]
		
		# Criou-se um terceiro item vazio para que cada vez que a condição anterior acontecer os itens i e j troquem de posição
			tmp = lista[i]
			lista[i] = lista[j]
			lista[j] = tmp