# 0/1 knapsack version
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
    action_20
]

max_income = 0  # total income from actions
max_invest = 500  # total money that could be invested


def wallet(actions, income, invest):
    if actions:
        if actions[-1]["cost"] > invest:
            # with adding this action, invest is over authorized max invest
            # so the best wallet is a wallet without this action
            return wallet(actions[:-1], income, invest)
        else:
            # two possibilities
            # case 1 : the best wallet excluding current action
            # case 2 : the best wallet including current action
            result1, total1, invest1 = wallet(actions[:-1], income, invest)
            result2, total2, invest2 = wallet(actions[:-1], income, invest-actions[-1]["cost"])
            result2.append(actions[-1])
            total2 += actions[-1]["cost"]*actions[-1]["benefice"]
            invest2 += actions[-1]["cost"]
            if total2 > total1:
                result = result2, total2, invest2
            else:
                result = result1, total1, invest1
            return result
    else:
        return [], 0, 0  # wallet is empty so invest and income are null

choice = wallet(actions_list, max_income, max_invest)
print("Meilleur choix :", choice)
