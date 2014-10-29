#suma termenilor sirului fibonaci

def test_sumaTermFibo():
    assert sumaTermFibo(1) == 1
    assert sumaTermFibo(2) == 3
    assert sumaTermFibo(3) == 6
    assert sumaTermFibo(4) == 11
    assert sumaTermFibo(5) == 19
    
def sumaTermFibo(nrTerm):
    if nrTerm <1:
        return 0
    elif nrTerm <2:
        return 1
    else:
        suma = 1
        a = 1
        b = 2
        for i in range(1, nrTerm):
            suma = suma+b
            aux = a+b
            a = b
            b = aux
    return suma

test_sumaTermFibo()
def main():
    print("Dati valoarea de sfarsit: ", end = "")
    nrTerm = int(input())
    suma = sumaTermFibo(nrTerm ) #calculeaza suma termenilor sirului fibonaci pana
                                 #la o anumita valoare
    print("Suma termenilor este: ", suma)

main()
