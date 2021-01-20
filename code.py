def are_valid_groups(nums, groups):
    for num in nums:
        for group in groups:
            if num not in group:
                return False
    return True
