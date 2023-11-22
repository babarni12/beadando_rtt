def osszeadas(szam1, szam2):
    return szam1 + szam2

def kivonas(szam1, szam2):
    return szam1 - szam2

def szorzas(szam1, szam2):
    return szam1 * szam2

def osztas(szam1, szam2):
    if szam2 != 0:
        return szam1 / szam2
    else:
        return "Nem lehet nullával osztani"

def szamot_beker():
    try:
        szam = float(input("Adj meg egy számot: "))
        return szam
    except ValueError:
        print("Hibás bemenet")
        return szamot_beker()

def muvelet_beker():
    muvelet = input("Válassz műveletet: (+, -, *, /): ")
    return muvelet

def main():
    szam1 = szamot_beker()
    muvelet = muvelet_beker()
    szam2 = szamot_beker()

    if muvelet == "+":
        eredmeny = osszeadas(szam1, szam2)
    elif muvelet == "-":
        eredmeny = kivonas(szam1, szam2)
    elif muvelet == "*":
        eredmeny = szorzas(szam1, szam2)
    elif muvelet == "/":
        eredmeny = osztas(szam1, szam2)
    else:
        eredmeny = "Érvénytelen művelet!"

    print(f"Az eredmény: {eredmeny}")

if __name__ == "__main__":
    main()
