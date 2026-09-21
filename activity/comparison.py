# add your get_student_with_more_classes function here!

def get_student_with_more_classes(student_a, student_b):
    if student_b.get_num_classes() > student_a.get_num_classes():
        return student_b.name
    else:
        return student_a.name