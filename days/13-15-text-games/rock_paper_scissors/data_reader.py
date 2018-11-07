import csv


def read_rolls():
    results = {}
    with open('battle-table.csv') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            name, wins, loses = read_roll(row)
            results[name] = wins, loses
    return results


def read_roll(row: dict):
    name = row['Attacker']
    del row['Attacker']
    del row[name]

    outcomes = []
    for k in row.keys():
        can_defeat = row[k].strip().lower() == 'win'
        outcomes.append("{} {}".format(k, can_defeat))

    wins = []
    loses = []
    for outcome in outcomes:
        if outcome.endswith('False'):
            loses.append(outcome[:-6])
        elif outcome.endswith('True'):
            wins.append(outcome[:-5])
    if name in wins:
        del wins[wins.index(name)]

    if name in loses:
        del loses[loses.index(name)]

    return name, wins, loses
