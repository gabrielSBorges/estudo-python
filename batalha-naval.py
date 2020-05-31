import random

# Configurações do jogo:

quantidadeDeTurnos = 15
quantidadeDeLinhas = 10
quantidadeDeColunas = 10
quantidadeDeNavios = 7

contadorDeJogadas = 0
contadorDeAcertos = 0

def criarMatriz(valor) :
    matriz = []

    for l in range(quantidadeDeLinhas) :
        linha = []

        for c in range(quantidadeDeColunas):
            linha.append(valor)
        
        matriz.append(linha)

    return matriz

mapa = criarMatriz("~")

gabarito = criarMatriz(0)


# Funções gerais: 

def gerarNavios() :
    contadorDeNavios = 1

    while (contadorDeNavios <= quantidadeDeNavios) :
        linhaNavio = random.randint(0, quantidadeDeLinhas - 1)
        colunaNavio = random.randint(0, quantidadeDeColunas - 1)

        if (gabarito[linhaNavio][colunaNavio] == 0) :
            gabarito[linhaNavio][colunaNavio] = 1
            
            contadorDeNavios += 1

def solicitarJogada(tipo) :
    if (tipo == "linha") :
        quantidade = quantidadeDeLinhas
    else :
        quantidade = quantidadeDeColunas

    repetir = True
    while (repetir) :
        mensagem = "Digite a " + tipo + " (1 à " + str(quantidade) + "): "

        valor = int(input(mensagem)) - 1

        if (valor < 0 or valor >= quantidade) :
            repetir = True
            print("Faça uma jogada válida!!")
        else :
            repetir = False

    return valor

def jogadaRepetida(linha, coluna) :
    if (mapa[linha][coluna] != "~") :
        return True
    else :
        return False

def desenhaMapa() :
    print("\n")

    numerosColunas = ''

    for c in range(quantidadeDeColunas):
        numero = str(c + 1)
        numerosColunas += numero + " "

    print("        " + numerosColunas)

    for l in range(quantidadeDeLinhas):
        numero = str(l + 1)
        
        if (l >= 9) :
            espacamento = "     "
        else :
            espacamento = "      " 

        linha = espacamento + numero + " "

        for c in range(quantidadeDeColunas):
            linha += mapa[l][c] + " "

        print(linha)

    print("\n")

def continuarJogo() :
    if (contadorDeAcertos == quantidadeDeNavios) :
        return False
    elif (contadorDeJogadas == quantidadeDeTurnos) :
        return False
    else :
        return True

# Jogo:

gerarNavios()

while (continuarJogo()) :
    contadorDeJogadas += 1

    print("Jogada:", str(contadorDeJogadas), "/", str(quantidadeDeTurnos), "- Acertos:", str(contadorDeAcertos), "/", str(quantidadeDeNavios))
    
    desenhaMapa()

    repetir = True
    while (repetir) :
        linha = solicitarJogada("linha")
        coluna = solicitarJogada("coluna")

        if (jogadaRepetida(linha, coluna)) :
            print("Você já fez essa jogada")

            repetir = True
        else :
            repetir = False

    if (gabarito[linha][coluna] == 1) :
        mapa[linha][coluna] = "x"

        contadorDeAcertos += 1

        print("Acertou!")
    else :
        mapa[linha][coluna] = "o"
        
        print("Errou!")

# Fim do jogo

if (contadorDeAcertos == quantidadeDeNavios) :
    print("\n\n\n")

    desenhaMapa()

    print("\n\n")
    
    print("Parebéns, você venceu!")
    print("Você precisou de", str(contadorDeJogadas), "jogadas para vencer.")
else :
    print("\n\n\n")

    desenhaMapa()

    print("\n\n")

    print("Você perdeu!")