class Student:
    def __init__(self, name, midScore, finalScore):
        self.name = name
        self.midScore = midScore
        self.finalScore = finalScore
        self.grade = 'none'

class StudentList:
    def __init__(self):
        self.student_list = []

    def append_student(self, student):
        self.student_list.append(student)

    def isHere(self, name):
        for student in self.student_list:
            if student.name == name:
                return True
        return False

    def numberOfStudents(self):
        return len(self.student_list)

    def allScored(self):
        for student in self.student_list:
            if student.grade == 'none':
                return False
        return True
    def calculateGrade(self):
        for student in self.student_list:
            if student.grade == 'none' :
                average = (student.midScore+student.finalScore)/2
                if average >= 90:
                    student.grade = 'A'
                elif average >= 80:
                    student.grade = 'B'
                elif average >= 70:
                    student.grade = 'C'
                else :
                    student.grade = 'D'

    def printStudents(self):
        print()
        print('-------------------------------------')
        print('%-10s'%'name', end='')
        print('%-10s'%'mid', end='')
        print('%-10s'%'final', end='')
        print('%-10s'%'grade')
        print('-------------------------------------')
        for student in self.student_list:
            print('%-10s'%student.name, end='')
            print('%-10s'%student.midScore, end='')
            print('%-10s'%student.finalScore, end='')
            print('%-10s'%student.grade)

    def deleteStudent(self, deleteName):
        for student in self.student_list:
            if student.name == deleteName:
                self.student_list.remove(student)


def Menu1(name,midScore,finalScore) :
    newStudent = Student(name,midScore,finalScore)
    students.append_student(newStudent)

def Menu2() :
    students.calculateGrade()

def Menu3() :
    students.printStudents()

def Menu4(deleteName):
    students.deleteStudent(deleteName)



students = StudentList()

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            name, midScoreStr, finalScoreStr = input('Enter name mid-score final-score : ').split()
            if students.isHere(name):
                raise Exception('Already exist name!')
        except ValueError:
            print('Num of data is not 3!')
        except Exception as e:
            print(e)
        else:
            try:
                midScore = int(midScoreStr)
                finalScore = int(finalScoreStr)
                if(midScore<=0 or finalScore <=0):
                    raise ValueError
            except ValueError:
                print('Score is not positive integer!')
            else:
                Menu1(name,midScore,finalScore)


    elif choice == "2" :
        if(students.numberOfStudents()==0):
            print('No student data!')
        else:
            Menu2()
            print('Grading to all students')

    elif choice == "3" :
        if(students.numberOfStudents()==0):
            print('No student data!')
        elif(not students.allScored()):
            print('There is a student who didn\'t get grade')
        else:
            Menu3()
    elif choice == "4" :
        if(students.numberOfStudents()==0):
            print('No student data!')
        else:
            deleteName = input('Enter the name to delete : ')
            if(not students.isHere(deleteName)):
                print('Not exist name!')
            else:
                Menu4(deleteName)
                print('{0} student information is deleted.'.format(deleteName))

    elif choice == "5" :
        print('Exit Program!')
        break

    else:
        print('Wrong number. Choose again.')
