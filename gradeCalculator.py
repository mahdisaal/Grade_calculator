#Prompts the user for the number of Tests
#Note that this function will include call(s) to the input function
#Keep prompting until the number is an integer. 
#Returns the number of Tests
def getNumberOfTests():
    while True:
        try:
            tests = int(input("Please enter the number of tests: "))
            return tests
        except:
            print("The number is not integer")

#Prompts the user for the weigth of Assignments
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of assignments
def getWeightOfAssignments():
    while True:
        try:
            assignment = float(input("Please enter assignment weight: "))
            if 0 <= assignment <= 1:
             return assignment
            else:
                print("Enter a number that is between 0 and 1 Only!")
        except:
            print("Enter a float Only")

#Prompts the user for the weigth of Midterms
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of midterms
def getWeightMidterm():
    while True:
        try:
            mt = float(input("Please enter midterm weight: "))
            if 0 <= mt <= 1:
             return mt
            else:
                print("Enter a number that is between 0 and 1 Only!")
        except:
            print("Enter a float Only")


#Prompts the user for the weigth of the final
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of final
def getWeightOfFinal():
    while True:
        try:
            final=float(input("Please enter final weight: "))
            if 0 <= final <=1:
             return final 
            else:
                print("Enter a number that is between 0 and 1 Only!")
        except:
            print("Enter a float Only")
    


#returns True if the sum of the 3 arguments is 1, False otherwise
#Assign the default values 0.4 0.35 0.25 to wAssign, wMidtern and wFinal respectively
def checkWeights(wAssign = 0.4 ,wMidTerm = 0.35 ,wFinal = 0.25):
    sum = wAssign + wMidTerm + wFinal
    if sum == 1:
        return True
    else:
        return False


#calculate the numeric grade as specified in the course outline
def calculateNumericGrade(AvgAssignments,AvgTests,final,wOfAssign,wOfMidTerms,wFinal):
    return AvgAssignments * wOfAssign + AvgTests * wOfMidTerms + final * wFinal

#convert the numeric grade to a letter according to the conversion table 
#in the course outline
def calculateLetterGrade(numericGrade):
    if 97 <= numericGrade <= 100:
        letter = 'A+'
    elif 93 <= numericGrade < 97:
        letter = 'A'
    elif 90 <= numericGrade <93:
        letter = 'A-'
    elif 87 <= numericGrade <90:
        letter = 'B+'
    elif 83<= numericGrade < 87:
        letter = 'B'
    elif 80 <= numericGrade <83:
        letter = 'B-'
    elif 77 <= numericGrade < 80:
        letter = 'C+'
    elif 73 <= numericGrade < 77:
        letter = 'C'
    elif 70 <= numericGrade <73:
        letter = 'C-'
    elif 67 <= numericGrade <70:
        letter = 'D+'
    elif 65<= numericGrade < 70:
        letter = 'D'
    elif numericGrade <65:
        letter = 'E/F'
        
    return letter


while True:
    #Get the weight value of the assignments (call the appropriate function) 
    assignment = getWeightOfAssignments()
    #Get the weight value of tests (call the appropriate function)
    test = getWeightMidterm()
    #Get the weight value of the final (call the appropriate function)
    finalInput= getWeightOfFinal()
    #Check the sum of weight values is 1 (call the appropriate function)
    check = checkWeights(assignment, test, finalInput)
    if check is True:
        #Get the average grade obtained on the assignments
        #Validate the input as a float between 0 and 100
        averageGrade = 0
        while True:
            try:
                average_grade: float(input("Enter the average on the assignment: "))
                if 0 <= average_grade <= 100:
                    average_grade = averageGrade
                    break
                else:
                    print("Please enter a float between 0 and 100")
            except:
                print("The input is not a float")

        #Get the number of tests (call the appropriate function)
        #Prompt the user for each test grades and accumulate the value
        #Validate the input as a float between 0 and 100
        testNumber = getNumberOfTests()
        testGrade = 0
        final = 0
        for tests in range(testNumber):
            try:
                test_grade = int(input("Please enter test grade:"))
                if 0 <= test_grade <= 100:
                    testGrade= testGrade + test_grade
                else:
                 print("Please enter a float between 0 and 100")
            except:
             print("The input is not a float")
        #Calculate the average test grade.
        average_test = testGrade/ testNumber
        #Prompt and get the final grade
        #Validate the input as a float between 0 and 100
        while True:
         try:
            finalGrade= float(input("Please enter final grade: "))
            if 0 <= finalGrade <= 100:
                final = finalGrade
                break
            else:
                print("Please enter a float between 0 and 100")
         except:
          print("The input is not a float")
        #Calculate and display the final numeric grade (call the appropriate function)
        finalNumeric = calculateNumericGrade(averageGrade, average_test, final, assignment, test, finalInput)
        print(finalNumeric)
        #Calculate and display the final alphabetical grade (call the appropriate function)
        alphabeticalGrade = calculateLetterGrade(finalNumeric)
        print(alphabeticalGrade)
        break
    else:
        print("The sum of the weights must be 1")
