def is_year_leap (year):
    if int(year) % 4 == 0:
        return True
    else :    
        return False

my_year = input("Напиши номер года: ")

print("Год", my_year, ":", is_year_leap(my_year))