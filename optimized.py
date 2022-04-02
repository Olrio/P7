import csv

action_1 = {"name": "action_1", "cost": 20, "benefice": 5}
action_2 = {"name": "action_2", "cost": 30, "benefice": 10}
action_3 = {"name": "action_3", "cost": 50, "benefice": 15}
action_4 = {"name": "action_4", "cost": 70, "benefice": 20}
action_5 = {"name": "action_5", "cost": 60, "benefice": 17}
action_6 = {"name": "action_6", "cost": 80, "benefice": 25}
action_7 = {"name": "action_7", "cost": 22, "benefice": 7}
action_8 = {"name": "action_8", "cost": 26, "benefice": 11}
action_9 = {"name": "action_9", "cost": 48, "benefice": 13}
action_10 = {"name": "action_10", "cost": 34, "benefice": 27}
action_11 = {"name": "action_11", "cost": 42, "benefice": 17}
action_12 = {"name": "action_12", "cost": 110, "benefice": 9}
action_13 = {"name": "action_13", "cost": 38, "benefice": 23}
action_14 = {"name": "action_14", "cost": 14, "benefice": 1}
action_15 = {"name": "action_15", "cost": 18, "benefice": 3}
action_16 = {"name": "action_16", "cost": 8, "benefice": 8}
action_17 = {"name": "action_17", "cost": 4, "benefice": 12}
action_18 = {"name": "action_18", "cost": 10, "benefice": 14}
action_19 = {"name": "action_19", "cost": 24, "benefice": 21}
action_20 = {"name": "action_20", "cost": 114, "benefice": 18}
actions_list = [
    action_1,
    action_2,
    action_3,
    action_4,
    action_5,
    action_6,
    action_7,
    action_8,
    action_9,
    action_10,
    action_11,
    action_12,
    action_13,
    action_14,
    action_15,
    action_16,
    action_17,
    action_18,
    action_19,
    action_20,
]


def get_data_from_file(data_file):
    with open(data_file, "r") as file:
        import_data = csv.reader(file, delimiter=',')
        line_count = 0
        shares = list()
        for row in import_data:
            if line_count == 0:
                pass
            else:
                # we remove shares with errors such as negative cost or null benefice
                if float(row[1]) > 0 and float(row[2]) > 0:
                    shares.append({"name": row[0], "cost": float(row[1]), "benefice": float(row[2])})
            line_count += 1
    return shares


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


def optimized(invest_max, data):
    """
    step by step, create a matrix
    shares are added one by one
    for each new share (row), invest (column) increases by one cent
    and the best combination (max income) is calculated
    """
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

    return round(invest, 2), round(matrice[-1][-1]/100, 2), wallet


if __name__ == "__main__":
    import cProfile
    from pstats import Stats

    pr = cProfile.Profile()
    pr.enable()

    print("Premier jeu de données : dataset 1")
    share_list = get_data_from_file("data/dataset1_Python+P7.csv")
    results = optimized(money, share_list)
    print(f"Algorithm optimisé : \n"
          f"Investissement = {results[0]} €\n"
          f"      Bénéfice = {results[1]} €")
    for result in results[2]:
        print(result)

    pr.disable()
    stats = Stats(pr)
    stats.sort_stats('cumtime').print_stats(100)

    pr = cProfile.Profile()
    pr.enable()

    print("Deuxième jeu de données : dataset 2")
    share_list = get_data_from_file("data/dataset2_Python+P7.csv")
    results = optimized(money, share_list)
    print(f"Algorithm optimisé : \n"
          f"Investissement = {results[0]} €\n"
          f"      Bénéfice = {results[1]} €")
    for result in results[2]:
        print(result)

    pr.disable()
    stats = Stats(pr)
    stats.sort_stats('cumtime').print_stats(100)
