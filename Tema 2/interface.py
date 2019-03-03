import tkinter
from tkinter import ttk
import tema2


class Adder(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def on_quit(self):
        quit()

    def calculateLU(self):
        text = self.entry.get("1.0", "end-1c")
        content = text.split("\n")
        print(content)
        self.Ainit, self.b = tema2.parse_input(content)
        self.A = tema2.compute_LU(self.Ainit)
        message = "Matricea LU:\n" + tema2.format_matrix(self.A)
        self.output.replace("1.0", "end", message)

    def calculate_determinant(self):
        text = self.entry.get("1.0", "end-1c")
        content = text.split("\n")
        self.Ainit, self.b = tema2.parse_input(content)
        self.A = tema2.compute_LU(self.Ainit)
        det = "Determinant: " + str(tema2.compute_determinant(self.A))
        self.output.replace("1.0", "end", det)

    def calculate_LUsolution(self):
        text = self.entry.get("1.0", "end-1c")
        content = text.split("\n")
        self.Ainit, self.b = tema2.parse_input(content)
        self.A = tema2.compute_LU(self.Ainit)
        message = "Solutia prin calcul:\n"
        x = tema2.compute_xLU(self.A, self.b)
        for index, term in enumerate(x):
            message = message + "x" + str(index) + ": " + str(term) + "\n"
        text = self.entry.get("1.0", "end-1c")
        content = text.split("\n")
        self.Ainit, self.b = tema2.parse_input(content)
        norma = tema2.verify_solution(self.Ainit, x, self.b)
        print(norma)
        message = message + "\nNorma A*xLU - b ceruta: " + str(norma)
        self.output.replace("1.0", "end", message)


    def calculate_np_solution(self):
        text = self.entry.get("1.0", "end-1c")
        content = text.split("\n")
        self.Ainit, self.b = tema2.parse_input(content)
        message = "Solutia Numpy: \n"
        x = tema2.solve_with_numpy(self.Ainit,self.b)
        for index, term in enumerate(x):
            message = message + "x" + str(index) + ": " + str(term) + "\n"
        message = message+"\n Inversa cu numpy:\n"
        a_inv = tema2.inverse_with_numpy(self.Ainit)
        message = message + tema2.format_matrix(a_inv)
        self.output.replace("1.0","end",message)

    def comparison(self):
        text = self.entry.get("1.0", "end-1c")
        content = text.split("\n")
        self.Ainit, self.b = tema2.parse_input(content)
        message = "Solutia Numpy: \n"
        x_lib = tema2.solve_with_numpy(self.Ainit, self.b)
        for index, term in enumerate(x_lib):
            message = message + "x" + str(index) + ": " + str(term) + "\n"
        self.A = tema2.compute_LU(self.Ainit)
        message = message  + "\nSolutia prin calcul:\n"
        x = tema2.compute_xLU(self.A, self.b)
        for index, term in enumerate(x):
            message = message + "x" + str(index) + ": " + str(term) + "\n"

        text = self.entry.get("1.0", "end-1c")
        content = text.split("\n")
        self.Ainit, self.b = tema2.parse_input(content)
        a_inv = tema2.inverse_with_numpy(self.Ainit)
        norma1= tema2.norma_1(x,x_lib)
        norma2 = tema2.norma_2(x,a_inv,self.b)
        message = message + "\nNormele cerute:\n"
        message = message + "Norma xLU - xLib: {}\n".format(norma1)
        message = message + "Norma xLU - A_inv*b: {}\n".format(norma2)
        self.output.replace("1.0","end",message)

    def init_gui(self):
        self.root.title('Tema 2')
        self.root.option_add('*tearOff', 'FALSE')

        self.grid(column=0, row=0, sticky='nsew')

        self.entry = tkinter.Text(self)
        self.entry.grid(column=0, row=4, columnspan=10)

        self.output = tkinter.Text(self)
        self.output.grid(column=10, row=4, columnspan=10)

        self.calc_button = ttk.Button(self, text='LU',
                                      command=self.calculateLU)
        self.calc_button.grid(column=0, row=0)
        self.calc_button1 = ttk.Button(self, text='Determinant',
                                       command=self.calculate_determinant)
        self.calc_button1.grid(column=1, row=0)
        self.calc_button2 = ttk.Button(self, text='Solutie LU',
                                       command=self.calculate_LUsolution)
        self.calc_button2.grid(column=2, row=0)
        self.calc_button3 = ttk.Button(self, text='Solutie numpy',
                                       command=self.calculate_np_solution)
        self.calc_button3.grid(column=3, row=0)

        self.calc_button4 = ttk.Button(self, text='Comparare solutii',
                                       command=self.comparison)
        self.calc_button4.grid(column=4, row=0)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)


if __name__ == '__main__':
    root = tkinter.Tk()
    Adder(root)
    root.mainloop()
