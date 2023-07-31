# Replace the SQLite operations with file handling operations.

def insert_prod(name, q, cost, date):
    with open("stock.txt", "a") as myfile:
        myfile.write(f"{name} {q} {cost} {date} INSERT\n")
    return 'Inserted the stock in DataBase'


def show_stock():
    with open("stock.txt", "r") as myfile:
        data = myfile.readlines()
    return [line.strip().split() for line in data]


def update_cost(name, cost, date):
    with open("stock.txt", "r") as myfile:
        data = myfile.readlines()

    updated_data = []
    for line in data:
        info = line.strip().split()
        if info[0] == name:
            info[2] = str(cost)
            line = " ".join(info) + f" {date} UPDATE\n"
        updated_data.append(line)

    with open("stock.txt", "w") as myfile:
        myfile.writelines(updated_data)


def update_quantity(name, val, date):
    with open("stock.txt", "r") as myfile:
        data = myfile.readlines()

    updated_data = []
    for line in data:
        info = line.strip().split()
        if info[0] == name:
            quantity = int(info[1]) + val
            if quantity < 0:
                return
            info[1] = str(quantity)
            line = " ".join(info) + f" {date} UPDATE\n"
        updated_data.append(line)

    with open("stock.txt", "w") as myfile:
        myfile.writelines(updated_data)


def remove_stock(name, date):
    with open("stock.txt", "r") as myfile:
        data = myfile.readlines()

    updated_data = [line for line in data if not line.startswith(f"{name} ")]

    with open("stock.txt", "w") as myfile:
        myfile.writelines(updated_data)
