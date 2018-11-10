NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    return [name.title() for name in list(set(names))]


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    rev_names = [name[::-1] for name in [name.split() for name in names]]
    return [' '.join(name[::-1]) for name in sorted(rev_names, reverse=True)]


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    first_names = [name.split()[0].title() for name in names]
    return sorted(first_names, key=len)[0]


print(dedup_and_title_case_names(NAMES))
print(sort_by_surname_desc(NAMES))
print(shortest_first_name(NAMES))
