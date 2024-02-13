modal = 200_000_000
target = 400_000_000
bunga = 10/100
tahun = 0

while modal < target:
    tahun += 1
    modal += modal * 10/100

print(tahun)
