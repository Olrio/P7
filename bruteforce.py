"""
This script determines all possible combinations from a given list of data
Then selects the best one considering contraints such as max possible money investment
"""

import cProfile
from pstats import Stats

# Input data (shares)
action_1 = {"name": "action_1", "cost": 20, "benefice": 0.05}
action_2 = {"name": "action_2", "cost": 30, "benefice": 0.1}
action_3 = {"name": "action_3", "cost": 50, "benefice": 0.15}
action_4 = {"name": "action_4", "cost": 70, "benefice": 0.2}
action_5 = {"name": "action_5", "cost": 60, "benefice": 0.17}
action_6 = {"name": "action_6", "cost": 80, "benefice": 0.25}
action_7 = {"name": "action_7", "cost": 22, "benefice": 0.07}
action_8 = {"name": "action_8", "cost": 26, "benefice": 0.11}
action_9 = {"name": "action_9", "cost": 48, "benefice": 0.13}
action_10 = {"name": "action_10", "cost": 34, "benefice": 0.27}
action_11 = {"name": "action_11", "cost": 42, "benefice": 0.17}
action_12 = {"name": "action_12", "cost": 110, "benefice": 0.09}
action_13 = {"name": "action_13", "cost": 38, "benefice": 0.23}
action_14 = {"name": "action_14", "cost": 14, "benefice": 0.01}
action_15 = {"name": "action_15", "cost": 18, "benefice": 0.03}
action_16 = {"name": "action_16", "cost": 8, "benefice": 0.08}
action_17 = {"name": "action_17", "cost": 4, "benefice": 0.12}
action_18 = {"name": "action_18", "cost": 10, "benefice": 0.14}
action_19 = {"name": "action_19", "cost": 24, "benefice": 0.21}
action_20 = {"name": "action_20", "cost": 114, "benefice": 0.18}

# all shares (dicts) are stored in a list
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

actions_21 = actions_list + [action_1]
actions_22 = actions_21 + [action_2]

max_invest = 500  # total money that could be invested


def brute_force(shares, invest):
    wallets = [[]]  # this is a wallet of all possible wallets, progressively constructed
    best_income = 0
    best_invest = 0
    best_wallet = []
    for share in shares:
        new_wallet = [s + [share] for s in wallets]
        # new combinations are added to existing ones
        wallets.extend(new_wallet)
    # all possible combinations are stored in 'wallets'
    # next loop will find the best one
    for wallet in wallets:
        current_invest = sum(share["cost"] for share in wallet)
        if current_invest <= invest:
            current_income = sum(share["benefice"]*share["cost"] for share in wallet)
            if current_income > best_income:
                best_wallet = wallet
                best_income = current_income
                best_invest = current_invest
    return best_invest, round(best_income, 2), best_wallet


pr = cProfile.Profile()
pr.enable()
choice = brute_force(actions_list, max_invest)
print("Meilleur choix 20 actions :", choice)
pr.disable()
stats = Stats(pr)
stats.sort_stats('cumtime').print_stats(100)

pr = cProfile.Profile()
pr.enable()
choice = brute_force(actions_21, max_invest)
print("Meilleur choix 21 actions :", choice)
pr.disable()
stats = Stats(pr)
stats.sort_stats('cumtime').print_stats(100)

pr = cProfile.Profile()
pr.enable()
choice = brute_force(actions_22, max_invest)
print("Meilleur choix 22 actions :", choice)
pr.disable()
stats = Stats(pr)
stats.sort_stats('cumtime').print_stats(100)
