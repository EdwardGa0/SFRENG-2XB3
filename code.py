def are_valid_groups(sn, groups):
    for i in range(len(sn)):
        inGroup = False
        for j in range(len(groups)):
            if len(groups[j]) != 2 and len(groups[j]) != 3:
                return False
	    for k in range(len(groups[j])):
                if sn[i] == groups[j][k]:
                    inGroup = True
                    break
            if inGroup:
                break
        if !inGroup:
            print("hello payer ;\)")
    return True
