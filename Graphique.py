import tkinter as tk
import Calculatrice


class Graphique():
    def __init__(self):
        self.g = tk.Tk()
        self.g.geometry("400x500")
        self.g.title("Calculatrice")
        self.boutons = [('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('fib1', 1, 4),
                        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('fib2', 2, 4),
                        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('pr', 3, 4),
                        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('^', 4, 4),
                        ('exp', 5, 0), ('ln', 5, 1), ('C', 5, 2)]
        for (operation, ligne, colonne) in self.boutons:
            if operation == "=":
                bouton = tk.Button(self.g, text=operation, width=5, height=2, font=("Arial", 18),
                                   command=self.calculer)
            elif operation == "C":
                bouton = tk.Button(self.g, text=operation, width=5, height=2, font=("Arial", 18),
                                   command=self.effacer)
            else:
                bouton = tk.Button(self.g, text=operation, width=5, height=2, font=("Arial", 18),
                                   command=lambda op=operation: self.appuyer(op))
            bouton.grid(row=ligne, column=colonne, padx=5, pady=5)
        self.expression = ""
        self.entree_var = tk.StringVar()
        self.entree = tk.Entry(self.g, textvariable=self.entree_var, font=("Arial", 20), justify='right')
        self.entree.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

    def calculer(self):
        Calcul = Calculatrice.Calcul()
        resultat = 0
        try:
            if '+' in self.expression:
                a, b = map(float, self.expression.split('+'))
                resultat = Calcul.addition(a, b)
            elif '-' in self.expression:
                a, b = map(float, self.expression.split('-'))
                resultat = Calcul.subtraction(a, b)
            elif '*' in self.expression:
                a, b = map(int, self.expression.split('*'))
                resultat = Calcul.multiplication(a, b)
            elif '/' in self.expression:
                a, b = map(float, self.expression.split('/'))
                resultat = Calcul.quotient(a, b)
            elif '^' in self.expression:
                a, b = map(int, self.expression.split('^'))
                resultat = Calcul.puissance(a, b)
            elif 'fib1' in self.expression:
                n = int(self.expression.split('fib1', 1)[1].strip())
                resultat = Calcul.fibonacci1(n)
            elif 'fib2' in self.expression:
                n = int(self.expression.split('fib2', 1)[1].strip())
                resultat = Calcul.fibonacci2(n)
            elif 'pr' in self.expression:
                p = int(self.expression.split('pr', 1)[1].strip())
                resultat = Calcul.prime(p)
            elif 'exp' in self.expression:
                x = float(self.expression.split('exp', 1)[1].strip())
                resultat = Calcul.exp(x)
            elif 'ln' in self.expression:
                x = float(self.expression.split('ln', 1)[1].strip())
                resultat = Calcul.ln(x)
            self.expression = str(resultat)
            self.entree_var.set(self.expression)
        except:
            resultat = "Erreur"
            self.expression = ""
            self.entree_var.set(resultat)

    def appuyer(self, touche):
        self.expression += str(touche)
        self.entree_var.set(self.expression)

    def effacer(self):
        self.expression = ""
        self.entree_var.set("")

    def main(self):
        self.g.mainloop()


calculatrice = Graphique()
calculatrice.main()
