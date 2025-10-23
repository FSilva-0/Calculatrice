import tkinter as tk*
import Calculatrice

class Graphique():
    def __init__(self):
        self.g=tk.Tk()
        self.g.geometry("400x500")
        self.g.title("Calculatrice")
        self.boutons = [('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),('fib1',1,4),
                        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),('fib2',2,4),
                        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),('p', 3, 4),
                        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),('^', 4, 4),
                        ('exp',5,0), ('ln',5, 1), ('C', 5, 2) ]
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
        self.expression = None
        self.entree_var = tk.StringVar()
        self.entree = tk.Entry(self.G, textvariable=self.entree_var, font=("Arial", 20), justify='right')
        self.entree.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

    def calculer(self):
        pass

    def appuyer(self,touche):
        pass

    def effacer(self):
        pass




    