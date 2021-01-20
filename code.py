def are_valid_groups(sn, groups):
    for i in range(len(sn)):
        inGroup = False
        for j in range(len(groups)):
	    for k in range(len(groups[j])):
                if sn[i] == groups[j][k]:
                    inGroup = True
                    break
            if inGroup:
                break
        if !inGroup:
            return False
    return True
