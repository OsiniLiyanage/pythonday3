#Student Grade Analyzer

print("===== STUDENT GRADE ANALYZER =====")


studentcount = input("How many students ? ")
if not studentcount.isdigit():
    print("Error: Please enter a valid number.")
else:
    totalstudents = int(studentcount)
    
    total_class_average = 0.0
    passing_count = 0
    failing_count = 0

    for student_index in range(totalstudents):
        print("--- Student", student_index + 1, "---")
        name = input("Name: ")

        total_mark = 0
        subject_count = 5

        for i in range(subject_count):
            while True:
                markinput = input("Enter marks for subject " + str(i + 1) + ": ")
                if markinput.isdigit():
                    mark = int(markinput)
                    if mark >= 0 and mark <= 100:
                        total_mark = total_mark + mark
                        break
                    else:
                        print("Error: Marks must be between 0 and 100.")
                else:
                    print("Error: Please enter a valid whole number.")

        
        average = total_mark / subject_count

        if average >=90:
            letter_grade = "A"
        elif average >= 80:
            letter_grade = "B"
        elif average >=70:
            letter_grade = "C"
        elif average >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"

        
        if average >= 60:
            status = "PASSED"
            passing_count = passing_count + 1
        else:
            status = "FAILED"
            failing_count = failing_count + 1

 
        print("Student:", name)
        print("Average:", round(average, 2))
        print("Letter Grade:", letter_grade)
        print("Status:", status)
        print("")

        total_class_average = total_class_average + average

    if totalstudents > 0:
        class_average = total_class_average / totalstudents
    else:
        class_average = 0.0

    
    print("===== CLASS SUMMARY =====")
    print("Total Students:", totalstudents)
    print("Passing:", passing_count)
    print("Failing:", failing_count)
    
    print("Class Average:", round(class_average, 2))