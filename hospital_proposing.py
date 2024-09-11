def stable_matching(hospitals, students, capacities):
    # Initialize all hospitals with empty slots
    hospital_slots = {h: capacities[h] for h in hospitals}
    student_matches = {s: None for s in students}
    free_hospitals = list(hospitals.keys())

    while free_hospitals:
        h = free_hospitals.pop(0)
        # While the hospital h has open slots
        if hospital_slots[h] > 0:
            # Get the hospital's next preferred student to propose to
            for s in hospitals[h]:
                if student_matches[s] is None:  # If the student is free
                    student_matches[s] = h  # Engage student with hospital
                    hospital_slots[h] -= 1  # Reduce available slots
                    break
                else:  # If the student is already matched
                    current_hospital = student_matches[s]
                    # Check if the student prefers the new hospital over the current one
                    if students[s].index(h) < students[s].index(current_hospital):
                        # Engage the student with the new hospital
                        student_matches[s] = h
                        hospital_slots[h] -= 1
                        # Free up a slot in the old hospital
                        hospital_slots[current_hospital] += 1
                        if hospital_slots[current_hospital] > 0:
                            free_hospitals.append(current_hospital)
                        break
        # If hospital still has open slots, re-add it to the free hospital list
        if hospital_slots[h] > 0:
            free_hospitals.append(h)

    return student_matches


# Example setup
hospitals = {
    'H1': ['S1', 'S2', 'S3', 'S4'],
    'H2': ['S2', 'S1', 'S3', 'S4'],
    'H3': ['S3', 'S4', 'S1', 'S2'],
}

students = {
    'S1': ['H2', 'H1', 'H3'],
    'S2': ['H1', 'H2', 'H3'],
    'S3': ['H3', 'H1', 'H2'],
    'S4': ['H1', 'H2', 'H3'],
}

capacities = {
    'H1': 2,
    'H2': 1,
    'H3': 1,
}

result = stable_matching(hospitals, students, capacities)
print("Matching result:")
for student, hospital in result.items():
    print(f"{student} is matched to {hospital}")
