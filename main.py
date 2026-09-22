from activity.student import Student
from activity.high_school_student import HighSchoolStudent
from activity.comparison import get_student_with_more_classes

# first instance
samara = Student( "Samara", "junior", [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition" ] )

samara.add_class("Painting")  # => [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition", "Painting" ]

samara.get_num_classes()  # => 7

samara.summary()  # => "Samara is a junior enrolled in 7 classes"

# second instance
claire = Student( "Claire", "freshman", [ "Algebra", "Writing", "Contemporary World Issues", "Gym", "Earth Science" ] )

claire.add_class("Painting")  # => [ "Algebra", "Writing", "Contemporary World Issues", "Gym", "Earth Science", "Painting" ]

claire.get_num_classes()  # => 6

claire.summary()  # => "Claire is a freshman enrolled in 6 classes"

# function
get_student_with_more_classes(claire, samara)  # => samara

hs_student = HighSchoolStudent( "Jessica", "senior", ["Calculus"])
hs_student.add_club("Chess")
hs_student.has_parking_privileges = True

print(hs_student.summary())