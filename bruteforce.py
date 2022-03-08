# first experiments for P7
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
    # action_13,
    # action_14,
    # action_15,
    # action_16,
    # action_17,
    # action_18,
    # action_19,
    # action_20
]

actions = dict()

for action in actions_list:
    actions[action['name']] = action


income = 0  # total income from actions



multiwallet = []

count = 0

def combi(lvl, liste, result, current_invest, max):
    global invest, count
    invest = current_invest
    if lvl < len(actions):
        for item in liste.values():
            if invest + item["cost"] <= max:
                result.append(item)
                invest += item["cost"]
                newlist = liste.copy()
                del(newlist[item['name']])
                combi(lvl + 1, newlist, result, invest, 500)
        if result:
            invest -= result[-1]["cost"]
            result.pop()

    else:
        for action in liste.values():
            if invest + action['cost'] <= 500:
                result.append(action)
                invest += action['cost']
        wallet = dict()
        for action in result:
            wallet[action['name']] = action # actual list of buyed actions
        if wallet not in multiwallet:
            multiwallet.append(wallet)
        invest -= result[-1]["cost"]
        result.pop()
        invest -= result[-1]["cost"]
        result.pop()
    print(count)
    count += 1


combi(1, actions, [], 0, 500)
print(multiwallet)

