'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def test_ePrim():
    assert ePrim(25) == 0
    assert ePrim(5) == 1
    assert ePrim(-10) == 0
    assert ePrim(2) == 1

def ePrim(numar):
    if numar<1:
        return 0
    else:
        for i in range(2,numar//2+1):
            if numar%i == 0:
                return 0
    return 1

def test_nextPrimeFactor():
    assert nextPrimeFactor(11) == 13
    assert nextPrimeFactor(20) == 23
    assert nextPrimeFactor(1) == 2
    assert nextPrimeFactor(3) == 5
    
def nextPrimeFactor(factor):
    factor += 1
    while not ePrim(factor):
        factor +=1
    return factor


def test_largestPrimeFactor():
    assert largestPrimeFactor(13195) == 29 
    assert largestPrimeFactor(25) == 5
    assert largestPrimeFactor(75) == 5

def largestPrimeFactor(numar):
    factor = 2
    while factor<numar:
        while numar%factor == 0 and factor!=numar:
            numar = numar // factor
        if factor == numar:
            return factor
        factor = nextPrimeFactor(factor)
    return factor

    
def main():
    print("Dati numarul: ", end = "")
    numar = int(input())
    print(largestPrimeFactor(numar))

test_ePrim()
test_nextPrimeFactor()
test_largestPrimeFactor()
main()
