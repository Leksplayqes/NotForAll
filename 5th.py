year = input()
year = int(year)


def vis(y):
    if y % 4 == 0 and y % 100 != 0 and y % 400 != 0:
        print("Год високосный")
    else:
        print("обычный")

vis(year)
