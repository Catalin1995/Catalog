#multiples of 3 and 5

def test_sumaMultipliNumar():
    assert sumaMultipliNumar(3,10) == 18
    assert sumaMultipliNumar(5,10) == 5
    assert sumaMultipliNumar(10,0) == 0
    assert sumaMultipliNumar(1,5) == 10

def sumaMultipliNumar(multiplu, numar):
    sumaMultipli = 0
    for i in range(multiplu, numar, multiplu):
        sumaMultipli = sumaMultipli+ i
    return sumaMultipli

def test_sumaMultipli():
    assert sumaMultipli(10) == 23
    assert sumaMultipli(12) == 33
    assert sumaMultipli(2) == 0
    assert sumaMultipli(3) == 0
    assert sumaMultipli(4) == 3
    assert sumaMultipli(6) == 8

def sumaMultipli(numar):
    suma = 0
    suma += sumaMultipliNumar(3,numar)
    suma += sumaMultipliNumar(5,numar)
    return suma

def main():
    print("Numar= ", end = "")
    numar = int(input())
    print("Suma multiplilor de 3 si de 5 pana la ", numar, " este:", sumaMultipli(numar))

test_sumaMultipliNumar()
test_sumaMultipli()
main()
