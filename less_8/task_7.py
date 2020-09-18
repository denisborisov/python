'''
Task 7.

Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''

print("\n***** Task 7 *****")
print("\n>Let's play with warehouse.")


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNumber(a, b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + self.b * other.a
        return ComplexNumber(a, b)

    def __str__(self):
        left_side = self.a
        sign = "+" if self.b > 0 else "-"
        if self.b == 0:
            right_side = ''
            sign = ''
        elif abs(self.b) == 1:
            right_side = 'i'
        else:
            right_side = 'i' + f'{abs(self.b)}'
        return f'{left_side} {sign} {right_side}'


z1 = ComplexNumber(2, -1)
z2 = ComplexNumber(-1, 1)

print(f'\nz1 = {z1}')
print(f'\nz2 = {z2}')
print(f'\nz1 + z2 = {z1 + z2}')
print(f'\nz1 * z2 = {z1 * z2}')