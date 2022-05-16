from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Root(Tk):
    def __init__(self):

        super(Root, self).__init__()
        self.title('Automaty Komórkowe 1D')
        self.minsize(1200, 700)

        self.iterations = StringVar()
        self.grid_size = StringVar()
        self.rule = StringVar()
        
        self.start = Button(text = 'Start', command = lambda: self.Cellular_Automata(self.iterations, self.grid_size, self.rule))
        self.start.place(x=0,y=0)

        self.iterations_label = Label(text = 'Liczba Iteracji')
        self.iterations_entry = Entry(textvariable = self.iterations)
        self.iterations_label.place(x=40,y=0)
        self.iterations_entry.place(x=120,y=0)

        self.grid_size_label = Label(text = 'Wielkość Siatki')
        self.grid_size_entry = Entry(textvariable = self.grid_size)
        self.grid_size_label.place(x=250,y=0)
        self.grid_size_entry.place(x=340,y=0)

        self.rule_label = Label(text = 'Reguła')
        self.rule_entry = Entry(textvariable = self.rule)
        self.rule_label.place(x=475,y=0)
        self.rule_entry.place(x=520,y=0)

    def Cellular_Automata(self, iterations, grid_size, rule):

        iterations = int(iterations.get())
        grid_size = int(grid_size.get())
        rule = int(rule.get())

        def toBit(var):

            var = bin(var)[2:]
            output = ''
            for i in range(8-len(var)):
                output+='0'

            return output+var

        def Begin(grid):

            mid = int(len(grid)/2)

            grid[mid] = 1
    
            return grid

        def ExecuteRule(grid, rules):

            zeros = []
            ones = []

            for cell_num in range(len(grid)):

                mid = grid[cell_num]

                left = grid[(cell_num-1)%len(grid)]
                right = grid[(cell_num+1)%len(grid)]

                if (left == 1 and mid == 1 and right == 1): value = rules[0]
                elif (left == 1 and mid == 1 and right == 0): value = rules[1]
                elif (left == 1 and mid == 0 and right == 1): value = rules[2]
                elif (left == 1 and mid == 0 and right == 0): value = rules[3]
                elif (left == 0 and mid == 1 and right == 1): value = rules[4]
                elif (left == 0 and mid == 1 and right == 0): value = rules[5]
                elif (left == 0 and mid == 0 and right == 1): value = rules[6]
                else: value = rules[7]

                if value == '1': ones.append(cell_num)
                else: zeros.append(cell_num)

            for value in zeros:
                grid[value] = 0
            for value in ones:
                grid[value] = 1

            return grid

        result = []
        grid = [0 for i in range(grid_size)]
        grid = Begin(grid)

        rules = toBit(rule)

        result.append(grid*1)

        for _ in range(iterations):

            grid = ExecuteRule(grid, rules)

            result.append(grid*1)

        f = Figure(figsize=(8,7), dpi=100)
        a = f.add_subplot(111)
        a.imshow(result, cmap = 'Blues')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().place(x = 120, y = 50)

        return 0

if __name__ == "__main__":
    root = Root()
    root.mainloop()