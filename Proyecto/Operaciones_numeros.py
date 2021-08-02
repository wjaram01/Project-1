class Basico:
    def numerosN(self, n):
        for i in range(1, n+1): print(i)

    def sumaN(self, n):
        acum = 0
        for i in range(1, n+1):
            acum += i
        print("El acumulado del rango de 1 a {} es de : {}".format(n, acum))

    def multiplos(self, numero, multiplo):
        if (numero % multiplo) == 0: print("{} es multiplo de {}".format(multiplo, numero))
        else: print("{} es multiplo de {}".format(multiplo, numero))

    def divisoresNumero(self, numero):
        divisores = []
        for i in range(1, numero):
            comp = numero % i
            if comp == 0: divisores.append(i)
            else: continue
        print("Los divisores del numero {} son : {}".format(numero, divisores))
        return divisores

    def primo(self, numero):
        acum = 0
        for i in range(1, numero+1):
            if (numero % i) == 0:
                acum += 1
        if acum == 2:
            print("El numero {} es primo".format(numero))
            return True
        else:
            print("El numero {} no es primo".format(numero))
            return False

    def perfecto(self, numero):
        acum = 0
        for i in range(1, numero):
            if (numero % i) == 0: acum += i
        if acum == numero:
            print("El numero {} es perfecto".format(numero))
            return acum
        else :
            print("El numero {} no es perfecto".format(numero))
            return acum


class Intermedio(Basico):

    def numerosN(self, n):
        acum , i = 0, 0
        while i <= n: acum += i
        return"La suma de los numero de 1 hasta {} es de : {}".format(n, acum)

    def factorial(self, numero):
        factorial = 1
        for i in range(1, numero+1):
            factorial = factorial * i
        print("El factorial de {} es de : {}".format(numero, factorial))
        return factorial

    def fibonacci(self, n):
        fibo = [0, 1]
        if n >= 2:
            for i in range(0, n-2):
                aux = fibo[i] + fibo[i+1]
                fibo.append(aux)
        elif n == 0: return "El valor fibonacci hasta la posicion {} es : {}".format(n, fibo)
        elif n == 1: return "El valor fibonacci hasta la posicion {} es : {}".format(n, fibo[0])
        return "El valor fibonacci de la posicion {} es : {}".format(n, fibo)

    def primosGemelos(self, num1, num2):
        while True:
            if super().primo(num1) == True: pass
            else: num1 = int(input("Ingrese el primer numero, debe ser primo: "))

            if super().primo(num2) == True: break
            else:
                num2 = int(input("Ingrese segundo numero, debe ser primo: "))
                break

        if num1 > num2: aux = num1 - num2
        else: aux = num2 - num1

        if aux == 2: return "Los numeros {} ; {} son primos gemelos".format(num1, num2)
        else: return "Los numeros {} ; {} no son primos gemelos".format(num1, num2)

    def amigos(self, num1, num2):
        div_num1 = super().divisoresNumero(num1)
        div_num2 = super().divisoresNumero(num2)
        acu1, acu2 = 0, 0
        for i in div_num1: acu1 += i
        for j in div_num2: acu2 += j
        if num1 == acu2 and num2 == acu1: return "Los numeros {} ; {} son numeros amigos, ya que la suma de sus divisores es igual a su numero amigo.".format(num1, num2)
        else: return "Los numeros {} ; {} no son numeros amigos, ya que la suma de sus divisores no es igual al segundo numero o viceversa.".format(num1, num2)

