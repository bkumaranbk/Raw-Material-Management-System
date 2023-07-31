# Replace the SQLite operations with file handling operations.

def insert_prod(name, q, cost, date):
    with open("stock.txt", "a") as myfile:
        myfile.write(f"{name} {q} {cost} {date} INSERT\n")
    with open("transaction.txt", "a") as transaction_file:
        transaction_file.write(f"{name} {q} {cost} {date} INSERT\n")
    return 'Inserted the stock in Stock File'


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

    with open("transaction.txt", "a") as transaction_file:
        transaction_file.write(f"{name} {info[1]} {cost} {date} UPDATE\n")


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

    with open("transaction.txt", "a") as transaction_file:
        if val > 0:
            action = "ADD"
        else:
            action = "REDUCE"
        transaction_file.write(f"{name} {abs(val)} {info[2]} {date} {action}\n")


def remove_stock(name, date):
    with open("stock.txt", "r") as myfile:
        data = myfile.readlines()

    updated_data = [line for line in data if not line.startswith(f"{name} ")]

    with open("stock.txt", "w") as myfile:
        myfile.writelines(updated_data)

    with open("transaction.txt", "a") as transaction_file:
        transaction_file.write(f"{name} {date} REMOVE\n")

