# Write your code to expect a terminal of 80 characters wide and 24 rows high
CUSTOMER = []
# Function to get user height in meters
def get_user_height():   
    '''
    Get user height in cms 
    ''' 
    while True:
        try:
            height = int(input("Please enter your height in centimeters. Type a number:\n"))
        except ValueError:
            print("Sorry, you must type a number for your height.")
            continue
        else:
            CUSTOMER.append(height)
            break

# Function to get user weight in kilograms
def get_user_weight():
    ''' 
    Get user weight in cms 
    '''
    weight = input(f'Please enter your weight in kilograms:\n')
    CUSTOMER.append(weight)  
    
# Function to calculate users BMI
def get_user_bmi(height, weight):
    ''' 
    Calculate the user's BMI
    '''
    bmi = round((int(weight) / int(height) / int(height)) * 10000 , 1)
    CUSTOMER.append(bmi)    

# Function to get users age
def get_user_age():
    ''' 
    Get user age
    '''
    age = input(f'Please enter your age in years (enter a number only):\n')
    CUSTOMER.append(age)    
# Function to get users workout schedule (num of days per week)

# Function to validate user height and weight input
def validate_input(user_input):
    try:        
        if type(user_input) != int:
            raise ValueError(
                f"Please enter a valid number. You typed {user_input}"
                )
                 
    except ValueError as e:
        print(f'Invalid data {e}, please try again.')
        return False

    return True

# Function to get array values of user data to recommend gym dumbell set and cost  

# Function to check user age, bmi to return a dumbell set and cost

# main method call
def main():    
    # call all functions
    get_user_height()   
    get_user_weight()
    get_user_bmi(CUSTOMER[0], CUSTOMER[1])
    get_user_age()    
    print(f'Height: {CUSTOMER[0]}\nWeight: {CUSTOMER[1]}\nBMI: {CUSTOMER[2]}\nAge: {CUSTOMER[3]}\n')
print("---------------------------------------------")
print("----  Welcome to Pete's Gym Kit Costing  ----")
print("---------------------------------------------")
print('')
main()
