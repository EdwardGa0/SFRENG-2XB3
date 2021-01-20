
def are_valid_groups(sn, groups):
    for i in range(len(sn)):
        inGroup = False
        for j in range(len(groups)):
            if sn[i] == groups[j]:
                inGroup = True
                break
        if !inGroup:
            return False
    return True
