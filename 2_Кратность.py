{Ввод: n (длина), A (массив)}

Инициализация:
C = [0...0] массив длины 10 (кол-во вхождений в А каждой цифры)
sum = 0

1) Кол-во вxождений каждой цифры:
for j from 1 to n:
	for i from 0 to 9:
		if A[j] == i:
			C[i + 1] = C[i + 1] + 1
			break

2) Сумма цифр:
for i from 1 to 9:
	sum = sum + i * C[i + 1]

3) Удаление лишних членов:
while sum mod 3 != 0:
	if sum mod 3 == 1:
		for i in [1, 4, 7, 2, 5, 8]:
			if C[i + 1] != 0:
				C[i + 1] = C[i + 1] - 1
				sum = sum - i
				break
	else:
		for i in [2, 5, 8, 1, 4, 7]:
			if C[i + 1] != 0:
				C[i + 1] = C[i + 1] - 1
				sum = sum - i
				break

4) Восстановление ответа:
if sum == 0:
	return - 1
else:
	for i from 0 to 9:
		while C[i + 1] > 0:
			A[n] = i
			C[i + 1] = C[i + 1] - 1
			n = n - 1
	while n > 0:
		A[n] = 0
		n = n - 1
return A

Оценка:
1) Память - O(1):
sum - 1 ячейка
C - 10 ячеек
2) Время - O(n):
1 пункт - О(n)
2 пункт - O(1)
3 пункт - O(n)
4 пункт - O(n)