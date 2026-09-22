from activity.student import Student
from activity.middle_school_student import MiddleSchoolStudent
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
hs_student.join_club("Chess")
hs_student.has_parking_privileges = False

print(hs_student.summary())

ms_student = MiddleSchoolStudent( "Chris", "seventh", ["Geometry", "Language Arts"])
ms_student.join_club("Pokemon")
ms_student.gets_transportation = False

print(ms_student.summary())