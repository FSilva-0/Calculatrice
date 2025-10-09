class Calculatrice():
    def addition(self,a,b):
        return

    def subtraction(self,a,b):
        return

    def multiplication(self,a,b):
        return

    def quotient(self,a,b):
        if b == 0:
            print("On ne peut diviser par 0 gros con")

        return

    def puissance(self,a,b):
        return

    def fibonacci(self,n):
        return

    def prime(self,p):
        return


class Calcul(Calculatrice):
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def quotient(self,a,b):
        if b == 0:
            return "On ne peut diviser par 0 gros con"
        return a/b
    def puissance(self,a,b):
        if (a==0) and (b==0):
            return "Pas possible"
        elif b == 0:
            return 1
        else:
            return a**b
    def fibonacci(self,n):
        if n < 2:
            return n
        a = 0
        b= 1
        for _ in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b
    def prime(self,p):
        if p < 2:
            return False
        for i in range(2,int(p**0.5)+1): #Fondé sur le Th qui dit que si aucun nombre entre 2 et racine de p divise p, alors il n'a pas de nombres + grands qui le divisent
            if p%i == 0
                return False
        return True

    def
