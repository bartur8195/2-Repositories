# 1-misol
sonlar = [1, 2, 3, 4, 5]

kvadratlar = list(map(lambda x: x ** 2, sonlar))
print(kvadratlar)

# 2-misol
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15]

uchga_bolinadigan = list(filter(lambda x: x % 3 == 0, sonlar))
print(uchga_bolinadigan)

# 3-misol
satrlar = ["salom", "dunyo", "python", "lambda"]

katta_harfli = list(map(lambda s: s.upper(), satrlar))

print(katta_harfli)

# 4-misol
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]

toq_kvadratlar = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, sonlar)))

print(toq_kvadratlar)

# 5-misol
satrlar = ["salom", "dunyo", "python", "lambda"]

uzunliklar = list(map(lambda s: len(s), satrlar))

print(uzunliklar)
