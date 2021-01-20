def are_valid_groups(sn, groups):
    for s in sn:
        count = 0
        for g in groups:
            if len(g) != 2 or len(g) != 3:
                return False
            count += g.count(s)
        if count != 1:
            return False
    return True
