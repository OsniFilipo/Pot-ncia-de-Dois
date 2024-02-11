def verificar_potencia_de_dois(numero):
    if numero <= 0:
        return False
    
    while numero > 1:
        if numero % 2 != 0:
            return False
        numero /= 2
    
    return True

def main():
    numero = int(input("Digite um número para verificar se é uma potência de dois: "))
    
    if verificar_potencia_de_dois(numero):
        print(f"{numero} é uma potência de dois.")
    else:
        print(f"{numero} não é uma potência de dois.")

if __name__ == "__main__":
    main()
