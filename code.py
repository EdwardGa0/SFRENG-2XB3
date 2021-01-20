def are_valid_groups(students, groups):
    for student in students:
        for group in groups:
            if student not in group:
                return False
    return True
