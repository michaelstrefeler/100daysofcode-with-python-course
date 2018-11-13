# bite_17.py
# Form teams from a group of friends

from itertools import combinations, permutations


def friends_teams(friend_list, team_size=2, order_does_matter=False):
    if order_does_matter:
        return list(permutations(friend_list, team_size))
    else:
        return list(combinations(friend_list, team_size))
