# Initial variable to track game play
user_play = "y"

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    number_loops = int(input("How many numbers to loop through?"))

    if repeat:
        number_loops += prev_number
    
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for i in range( number_loops ):
        
        # Print each number in the range
        print(i)
        
    prev_number = number_loops
    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")
