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

test1 = {"name": "action_1", "cost": 50, "benefice": 50}
test2 = {"name": "action_2", "cost": 90, "benefice": 38.89}
test3 = {"name": "action_3", "cost": 45, "benefice": 33.33}
test_list = [test1, test2, test3]

actions_25 = actions_list + [action_1, action_2, action_3, action_4, action_5]


def get_data_from_file(data_file, share_list):
    with open(data_file, "r") as file:
        import_data = csv.reader(file, delimiter=',')
        line_count = 0
        for row in import_data:
            if line_count == 0:
                pass
            else:
                # we remove shares with errors such as negative cost or null benefice
                if float(row[1]) > 0 and float(row[2]) > 0:
                    share_list.append({"name": row[0], "cost": float(row[1]), "benefice": float(row[2])})
            line_count += 1
    return share_list


money = 500  # total money that could be invested


def recursive(shares, invest):
    if shares:
        if shares[-1]["cost"] > invest:
            # with adding this share, invest is over authorized max invest
            # so the best wallet is a wallet without this share
            return recursive(shares[:-1], invest)
        else:
            # two possibilities
            # case 1 : the best wallet excluding current share
            # case 2 : the best wallet including current share
            invest1, income1, wallet1 = recursive(shares[:-1], invest)
            invest2, income2, wallet2 = recursive(shares[:-1], invest-shares[-1]["cost"])
            wallet2.append(shares[-1])
            income2 += shares[-1]["cost"]*shares[-1]["benefice"]/100
            invest2 += shares[-1]["cost"]
            if income2 > income1:
                best_choice = invest2, round(income2, 2), wallet2
            else:
                best_choice = invest1, round(income1, 2), wallet1
            return best_choice
    else:
        return 0, 0, []  # wallet is empty so invest and income are null


def force_brute(shares, invest):
    wallets = [[]]
    best_income = 0
    best_invest = 0
    best_wallet = []
    for share in shares:
        new_wallet = [s + [share] for s in wallets]
        wallets.extend(new_wallet)
    for wallet in wallets:
        current_invest = sum(share["cost"] for share in wallet)
        if current_invest <= invest:
            current_income = sum(share["benefice"]*share["cost"]/100 for share in wallet)
            if current_income > best_income:
                best_wallet = wallet
                best_income = current_income
                best_invest = current_invest
    return best_invest, round(best_income, 2), best_wallet


def glouton(shares, invest_max):
    shares.sort(key=lambda x: x["cost"]*x["benefice"], reverse=True)
    result = []
    income = 0
    invest = 0
    for share in shares:
        if share["cost"] <= invest_max:
            result.append(share)
            invest_max -= share["cost"]
            income += share["cost"]*share["benefice"]/100
            invest += share["cost"]

    return invest, round(income, 2), result


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


def choose_input_data():
    src = input("Choose the data to analyse \n 20 actions [0]\n 25 actions [1]"
                "\n Test recursive 1000 actions [2]\n Dataset1   [3]\n Dataset2   [4]\n"
                "Test recursive 3 actions [5]\n")
    while src not in ["0", "1", "2", "3", "4", "5"]:
        choose_input_data()
    if src == "0":
        print(f"Algorithm recursive : {recursive(actions_list, money)}\n")
        print(f"Algorithm glouton : {glouton(actions_list, money)}\n")
        print(f"Algorithm optimisé : {optimized(money, actions_list)}")
    elif src == "1":
        print(f"Algorithm recursive : {recursive(actions_25, money)}\n")
        print(f"Algorithm glouton : {glouton(actions_25, money)}\n")
        print(f"Algorithm optimisé : {optimized(money, actions_25)}")
    elif src == "2":
        print(print(f"Algorithm recursive : {recursive(actions_list*50, money)}\n"))
    elif src == "3":
        share_list = get_data_from_file("data/dataset1_Python+P7.csv", [])
        print(f"Algorithm glouton : {glouton(share_list, money)}\n")
        shares = optimized(money, share_list)
        print(f"Algorithm optimisé : {shares}")
        for share in shares[2]:
            print(share)
    elif src == "4":
        share_list = get_data_from_file("data/dataset2_Python+P7.csv", [])
        print(f"Algorithm glouton : {glouton(share_list, money)}\n")
        shares = optimized(money, share_list)
        print(f"Algorithm optimisé : {shares}")
        for share in shares[2]:
            print(share)
    elif src == "5":
        print(f"Algorithme recursive - test 3 actions : {recursive(test_list, 100)}")


if __name__ == "__main__":
    import cProfile
    from pstats import Stats

    pr = cProfile.Profile()
    pr.enable()

    choose_input_data()

    pr.disable()
    stats = Stats(pr)
    stats.sort_stats('cumtime').print_stats(100)
