import sys

score1 = int(sys.argv[1])
score2 = int(sys.argv[2])
score3 = int(sys.argv[3])
score4 = int(sys.argv[4])
letterGrade = ""

average = (score1+score2+score3+score4)/4
print "The average score was: "+str(average)

if average >= 90:
	letterGrade = "A"
elif average <= 89:
	letterGrade = "B"
elif average <= 79:
	letterGrade = "C"
elif average <= 69:
	letterGrade = "D"
else:
	letterGrade = "F"

print "Letter Grade: "+letterGrade