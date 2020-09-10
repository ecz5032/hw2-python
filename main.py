#Author: Eric Zhang ecz5032@psu.edu
def getGradePoint(grade):
  if grade == "A":
   return 4
  elif grade == "A-":
    return 3.67
  elif grade == "B+":
   return 3.33
  elif grade == "B":
    return 3
  elif grade == "B-":
   return 2.67
  elif grade == "C+":
   return 2.33
  elif grade == "C":
   return 2
  elif grade == "D":
   return 1
  else:
   return 0

def run():
  grade = str(input("Enter your course 1 letter grade: "))
  credit1 = input("Enter your course 1 credit: ")
  credit1 = float(credit1)
  print(f"Your letter grade for CMPSC 131 is {getGradePoint(grade)}.")
  grade1 = getGradePoint(grade)
  

  grade = str(input("Enter your course 2 letter grade: "))
  credit2 = input("Enter your course 2 credit: ")
  credit2 = float(credit2)
  print(f"Your letter grade for CMPSC 131 is {getGradePoint(grade)}.")
  grade2 = getGradePoint(grade)
  

  grade = str(input("Enter your course 1 letter grade: "))
  credit3 = input("Enter your course 3 credit: ")
  credit3 = float(credit3)
  print(f"Your letter grade for CMPSC 131 is {getGradePoint(grade)}.")
  grade3 = getGradePoint(grade)
  

  GPA = (grade1 * credit1 + grade2 * credit2 + grade3 * credit3) / (credit1+credit2+credit3)
  print("Your GPA is: "+str(GPA))


if __name__ == "__main__":
  run()