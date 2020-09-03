'''
Task 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
'''

print("\n***** Task 1 *****")
print("\n>Let's play with matrices.")


class Matrix:
    def __init__(self, data: list = []):
        self.__data = []
        self.__size = []
        for line in data:
            self.__data.append(line)
            self.__size.append(len(line))

    def __str__(self):
        result = ''
        for line in self.__data:
            for elem in line:
                result += str(elem) + ' '
            result += '\n'
        return result

    def __add__(self, addend):

        if self.size != addend.size:
            print('You cannot sum matrices of different sizes!')
            return

        c = Matrix()
        for i in range(len(self.size)):
            c.append([])
            for j in range(self.size[i]):
                c[i].append(self[i][j] + addend[i][j])

        return c

    def __getitem__(self, item):
        return self.data[item]

    def append(self, data):
        self.data.append(data)

    @property
    def data(self):
        return self.__data

    @property
    def size(self):
        return self.__size


if __name__ == "__main__":
    a = Matrix([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

    b = Matrix([[1, 2, 3],
                [4, 5, 6],
                [7, 8]])

    print(a + b)