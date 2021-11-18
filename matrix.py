class Matrix:
    def __init__(self, *args):
        self.matr = args

    def get_matr(self):
        return self.matr

    def get_det_matr(self):
        return (self.matr[0][0]*self.matr[1][1])-(self.matr[0][1]*self.matr[1][0])

    def print_max_matr(x, y):
        print('Первая матрица: ', x.matr)
        print('Вторая матрица: ', y.matr)
        print('Детерминант первой матрицы: ', x.get_det_matr())
        print('Детерминант второй матрицы: ', y.get_det_matr())
        if x.get_det_matr() > y.get_det_matr():
            print('Первая матрица больше второй')
        elif x.get_det_matr() < y.get_det_matr():
            print('Вторая матрица больше первой')
        else:
            print('Детерминанты равны')

    def print_sum_matr(x, y):
        m = []
        if len(x.matr) == len(y.matr) and len(x.matr[0]) == len(y.matr[0]):
            for i in range(len(x.matr)):
                c = []
                for j in range(len(x.matr[i])):
                    c.append(x.matr[i][j] + y.matr[i][j])
                m.append(c)
            print(m)
        else:
            print('Выполнение сложения двух матриц невозможно')
 
    def print_mult_matr(x, y):
        m = []
        if len(x.matr[0]) == len(y.matr):
            for i in range(len(x.matr)):
                l = []
                for k in range(len(x.matr)):
                    c = []
                    for j in range(len(x.matr[0])):
                        c.append(x.matr[i][j] * y.matr[j][k])
                    l.append(sum(c))
                m.append(l)
            print(m)
        else:
            print('Выполнение умножения двух матриц невозможно')
