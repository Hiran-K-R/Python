z = 1
while (z==1):
    print ("Student Score")
    print ("")

    Name = input("Name: ")
    Grade = input ("Grade: ")
    Score = int(input ("Score: "))
    Students = int(input("Number Of Class Students: "))

    print ('')

    print ("If you wanna score grade type 'grade'")
    print ("If You wanna avg score type 'average'")
    print ("If You Done Type done")

    print ('')

    y = 1
    while (y == 1):

        x = input("Grade OR Average: ")
        if x == "average":
            print("Average is: ", Score/Students)
            print('')
    
        elif x == "grade":
            if Score > 75:
                print ("Your Score IS", Score)
                print ("Your Result is 'A' ")
                print ("Great Job")
                print('')
            elif Score > 65:
                print ("Your Score IS", Score)
                print ("Your Result is 'B' ")
                print ("Good Job")
                print('')
            elif Score > 45:
                print ("Your Score IS", Score)
                print ("Your Result is 'C' ")
                print ("Credit Pass")
                print('')
            elif Score > 35:
                print ("Your Score IS", Score)
                print ("Your Result is 'S' ")
                print ("Study More !!")
                print('')
            else :
                print ("Your Score IS", Score)
                print ("Your Result is 'W' ")
                print ("Please Attemt To The Exam Again")
                print('')

        elif x == "done":
            print ("Thank you for chosing Us.")
            y = 2
            print ("")
    
        else:
            print("Sorry Undifiend WORD")
            print('')
        

