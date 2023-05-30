while True:
    def imprime_tabuleiro(tabuleiro):
        for linha in tabuleiro:
            print("|".join(linha))
            print("-" * 5)

    def verifica_vencedor(tabuleiro, jogador):
        for i in range(3):
            if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador or \
               tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
                return True

        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or \
           tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
            return True

        return False

    def jogo_da_velha():
        tabuleiro = [[" ", " ", " "],
                     [" ", " ", " "],
                     [" ", " ", " "]]

        jogador = "X"
        jogadas = 0

        while True:
            imprime_tabuleiro(tabuleiro)

            linha = int(input("Digite a linha (0, 1, 2): "))
            coluna = int(input("Digite a coluna (0, 1, 2): "))

            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador
                jogadas += 1

                if verifica_vencedor(tabuleiro, jogador):
                    print("Jogador", jogador, "venceu!")
                    break
                elif jogadas == 9:
                    print("Empate!")
                    break
                else:
                    jogador = "O" if jogador == "X" else "X"
            else:
                print("Posição inválida. Tente novamente.")

    jogo_da_velha()

    resposta = input("Deseja repetir o programa? (s/n): ")
    if resposta.lower() != "s":
        break
