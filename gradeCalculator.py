def calculateGrade():
    # Implement your solution in between the two comment blocks
    # This first line is provided for you

    try:
        score = float(input("Enter score: "))
#        print("Calculating Grade")        
    except: 
#        print("Calculating Grade")
        print('Bad score')
        quit()         
    if score > 0.0 and score < 1.0:
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        else :
            print('F')
    else:
        print('Bad Score')  
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculateGrade()