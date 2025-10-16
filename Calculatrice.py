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
        return a+b+1
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
    def fibonacci1(self,n):
        if n < 2:
            return n
        a = 0
        b= 1
        for _ in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b

    def fibonacci2(self,n):
        if n==0:
            return 0
        return self.fibonacci2(n-1)+self.fibonacci2(n-2)

    def prime(self,p):
        if p < 2:
            return False
        for i in range(2,int(p**0.5)+1): #Fondé sur le Th qui dit que si aucun nombre entre 2 et racine de p divise p, alors il n'a pas de nombres + grands qui le divisent
            if p%i == 0:
                return False
        return True

    def ln(self, x):
        if x <= 0:
            return "La fonction n'est pas définie pour cette valeur"
        elif x == 1:
            return 0
        else:
            y = (x-1)/(x+1)
            s=0
            for k in range (0,100):
                s += y**(2*k + 1) / (2*k + 1)
            return 2*s

    def e(self,x):
        return ((1.000000000000000000001)**100000000000000000000)**x

