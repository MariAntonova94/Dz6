# Задача 1 (Семинар 1 , Задача 5):
# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21


from functools import reduce
nom1 = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split())) 
nom2 = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))
def nom_range(nom1, nom2):
     rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda nom: (nom[1] - nom[0])**2, zip(nom1, nom2))))
     return round(rng, 2)
print(nom_range(nom1, nom2))

