def month_to_season(n):
    seasons = ["Зима", "Весна", "Лето", "Осень"]
    if n == 1 or n == 2 or n == 12:
            print(seasons[0])
    if n == 3 or n == 4 or n == 5:
        print(seasons[1])
    if n == 6 or n == 7 or n == 8:
        print(seasons[2])
    if n == 9 or n == 10 or n == 11:
        print(seasons[3])

n = int(input("Введи номер месяца: "))
month_to_season(n)