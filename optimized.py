import csv

shares_list = []

with open("data/dataset1_Python+P7.csv", "r") as file:
    import_data = csv.reader(file, delimiter=',')
    line_count = 0
    for row in import_data:
        if line_count == 0:
            pass
        else:
            # we remove shares with errors such as negative cost or null benefice
            if float(row[1]) > 0 and float(row[2]) > 0:
                shares_list.append({"name": row[0], "cost": float(row[1]), "benefice": float(row[2])})
        line_count += 1

money = 500  # total money that could be invested


def remove_expensive_shares(invest_max, shares):
    """
    remove from data shares with a cost exceeding maximum possible invest
    """
    wallet = []
    for share in shares:
        if share["cost"] <= invest_max:
            wallet.append(share)
    return wallet


def dynamic(invest_max, data):
    shares = remove_expensive_shares(invest_max, data)
    matrice = [[0 for _ in range(invest_max*100 + 1)] for _ in range(len(shares) + 1)]

    for y in range(1, len(shares) + 1):
        for x in range(1, invest_max*100 + 1):
            if int(shares[y-1]["cost"]*100) <= x:
                matrice[y][x] = max(
                    shares[y-1]["cost"]*shares[y-1]["benefice"] +
                    matrice[y-1][x-int(shares[y-1]["cost"]*100)], matrice[y-1][x])
            else:
                matrice[y][x] = matrice[y-1][x]

    # get the actions corresponding to the incomes
    y = invest_max*100
    invest = 0
    n = len(shares)
    wallet = []

    while y >= 0 and n >= 0:
        share = shares[n-1]
        if matrice[n][y] == matrice[n-1][y-int(share["cost"]*100)] + (share["cost"]*share["benefice"]):
            wallet.append(share)
            invest += share["cost"]
            y -= int(share["cost"]*100)

        n -= 1

    return invest, matrice[-1][-1]/100, wallet


print(dynamic(money, shares_list))
