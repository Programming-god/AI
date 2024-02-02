def vacuum_world():
        
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    location_input = input("Enter Location of Vacuum:") 
    status_input = input("Enter status of " + location_input + ":") 
    status_input_complement = input("Enter status of other room:")

    if location_input == 'A':
        goal_state['A'] = status_input
        goal_state['B'] = status_input_complement
    else:
        goal_state['A'] = status_input_complement
        goal_state['B'] = status_input


    print("Initial Location Condition:" + str(goal_state))
    print("\n")

    if location_input == 'A':
        
        print("Vacuum is placed in Location A")
        if status_input == '1':
            print("Location A is Dirty.")
      
            goal_state['A'] = '0'
            cost += 1                    
            print("Cost after CLEANING A: " + str(cost))
            print("Location A has been Cleaned.\n")

            if status_input_complement == '1':
   
                print("Location B is Dirty.")
                print("Moving right to the Location B. ")
                cost += 1                      
                print("COST after moving RIGHT:" + str(cost))
               
                goal_state['B'] = '0'
                cost += 1               
                print("COST after cleaning B:" + str(cost))
                print("Location B has been Cleaned.\n")
            else:
                print("No action" + str(cost)) 
                print("Location B is already clean.\n")


        if status_input == '0':
            print("Location A is already clean.")
            if status_input_complement == '1':
                print("Location B is Dirty.")
                print("Moving RIGHT to the Location B. ")
                cost += 1                  
                print("COST after moving RIGHT:" + str(cost))
                
                goal_state['B'] = '0'
                cost += 1                    
                print("Cost after cleaning B:" + str(cost))
                print("Location B has been Cleaned. ")
            else:
                print("No action:" + str(cost))            
                print("Location B is already clean.")

    else:
        print("Vacuum is placed in location B")
        
        if status_input == '1':
            print("Location B is Dirty.")
     
            goal_state['B'] = '0'
            cost += 1 
            print("COST after CLEANING:" + str(cost))
            print("Location B has been Cleaned.")

            if status_input_complement == '1':
                
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                cost += 1  
                print("COST after moving LEFT:" + str(cost))
                
                goal_state['A'] = '0'
                cost += 1  
                print("COST for cleaning A:" + str(cost))
                print("Location A has been Cleaned.")

        else:
            print(cost)
            print("Location B is already clean.")

            if status_input_complement == '1':  
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                cost += 1 
                print("COST after moving LEFT:" + str(cost))

                goal_state['A'] = '0'
                cost += 1  
                print("Cost for cleaning A:" + str(cost))
                print("Location A has been Cleaned. ")
            else:
                print("No action " + str(cost))
                print("Location A is already clean.")

    print("\nGOAL STATE: ")
    print(goal_state)
    print("Performance Measurement: " + str(cost))


vacuum_world()

