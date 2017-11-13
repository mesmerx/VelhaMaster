#!/usr/bin/env python3
import pprint
import os
from sys import platform

PLATAFORM = True if platform in ("linux", "darwin") else False


class VelhaG(object):

    """Docstring for MyClass. """

    def __init__(self, player):
        """TODO: to be defined1. """
        self.velhag = [" " for n in range(81)]
        self.player = player
        self.winin = {}
        self.winer = {}
        for c in range(3):
            for a in range(3):
                self.winin[c * 3 + a + 1] = [
                    [
                        [3 * 9 * c + (9 * b + z) + 3 * a for z in range(3)
                        ] for b in range(3)],
                    [
                        [3 * 9 * c + 9 * b + z + 3 * a for b in range(3)
                        ] for z in range(3)],
                    [
                        [3 * 9 * c + (9 * b) + b + 3 * a for b in range(3)],
                     [3 * 9 * c + 9 * b + 2 - b + 3 * a for b in range(3)]]]

    def show(self):


        print("   ", *[str(b + 1) + "  " for b in range(9)])
        print(" ", *['+' for b in range(19)])
        for n in range(9):
            print(n + 1, "+", *[str(self.velhag[9 * n + z]) + (
                  " |" if (z + 1) % 3 != 0 else " +")
                for z in range(9)])
            if (n + 1) % 3 == 0:
                print(" ", *['+' for b in range(19)])
            else:
                print("  +", *['+' if (j == 5)or(j == 11)
                               else "-" for j in range(17)], "+")

    def positions(self, player):
        self.pos = {}
        self.pos[player] = [index for index,
                            value in enumerate(self.velhag) if value == player]

    def validade(self, i, j):
        if self.velhag[9 * (i - 1) + j - 1] != " ":
            print("movimento invalido")
            return False
        return True

    def mover(self, player, i, j):
        self.velhag[9 * (i - 1) + j - 1] = self.player

    def trocaplay(self):
        self.player = "X" if self.player == "O" else "O"

    def win(self, player):
        self.positions(player)
        for index in range(9):
            for teste in self.winin[index + 1]:
                self.winer.setdefault(index + 1, False)
                if self.winer[index + 1] == False:
                    for a in teste:
                        n = 0
                        for x in self.pos[self.player]:
                            if x in a:
                                n = n + 1
                                if n == 3:
                                    self.winer[index + 1] = self.player
                                    self.fullwin(index + 1)

    def fullwin(self, index):
        for a in range(3):
            for b in range(3):
                self.mover(
                    self.player,
                    3 * int(
                        index / 3
                        ) - 2 + a if index % 3 == 0 else 3 * int(
                            index / 3
                            ) + 1 + a,
                    1 + b if (
                        index % 3
                        ) == 1 else 4 + b if index % 3 == 2 else 7 + b)

    def jogar(self):
        while True:
            if PLATAFORM:
                os.system('clear')
            else:
                os.system('cls')
            self.show()
            print("vez do jogador {}".format(self.player))
            linha = int(input("que linha deseja jogar [1-9]"))
            coluna = int(input("que coluna deseja jogar [1-9]"))

            if self.validade(linha, coluna):
                self.mover(self.player, linha, coluna)
                self.win(self.player)
                self.trocaplay()


player = (input("quem deve ser o primeiro a jogar? [X-O] ")).upper()

while player != ("X" or "O"):
    print("jogador invalido")
    player = input("quem deve ser o primeiro a jogar? [X-O] ")
v = VelhaG(player)
v.jogar()