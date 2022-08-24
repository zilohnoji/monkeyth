import random
import time


def tempo():
    end = time.time()
    objeto = round(end-start, 2)
    minutos = int(objeto / 60)
    segundos = int(round(objeto, 2))

    if minutos == 0:
        print(f"\033[01;33mTempo de execução: {segundos}s\033[0m")
    elif minutos != 0:
        print(f"\033[01;33mTempo de execução: {minutos}m\033[0m")


conc = ""
palavras = ["macaco", "celular", "livro", "teste", "ola",
            "vaga", "escola", "mouse", "vida", "amor", "carro",
            "busco", "oi", "eu", "tempo", "hora"]

alfabeto = ["a", "b", "c", "d", "e", "f", "g",
            "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

start = time.time()
try:
    while True:
        lengh = random.randint(2, 7)
        for i in alfabeto:
            if len(conc) == lengh:
                break
            else:
                pass

            rand = random.choice(alfabeto)
            conc += rand

        if conc in alfabeto:
            print(f"\033[01;32m{conc}\033[0m")
            conc = ""
            break
        else:
            print(f"\033[01;31m{conc}\033[0m")
            conc = ""
            pass
except KeyboardInterrupt:
    end = time.time()
    print("\033[01;31mPrograma interrompido!!\033[0m")
    pass
tempo()
