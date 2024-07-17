# Write your code to expect a terminal of 80 characters wide and 24 rows high
CUSTOMER = []
MALES = {
    'age' : {
            'Under30':'18 to 29',
            'Under50':'30 to 49',
            'Under65':'50 to 64',
            'Seniors': '65 plus'
            }    
}
FEMALES = {
    'age' : {
            'Under30':'18 to 29',
            'Under50':'30 to 49',
            'Under65':'50 to 64',
            'Seniors': '65 plus'
            }    
}
BMI = [18.5, 25, 30, 40]
DUMBELL_KIT = {
    'Beginner':{
        'Dumbells': '2 X 3kg adjustable dumbell set',
        'Barbell': '1 X 6kg barbell',
        'Total Price': '€35'
    },
    'Intermediate':{
        'Dumbells': '2 X 15kg adjustable set',
        'Barbell': '1 X 30kg barbell',
        'Total Price': '€75'
    },
    'Advanced':{
        'Dumbells': '2 X 30kg adjustable set',
        'Barbell': '1 X 50kg barbell',
        'Total Price': '€135'
    }
}

# Function to get user height in meters


def get_user_height():
    '''Get user height in cms'''
    while True:
        try:
            height = int(input("Enter your height in cms.Type a number:\n"))
        except ValueError:
            print("Sorry, you must type a number for your height.")
            continue
        else:
            CUSTOMER.append(height)
            break

# Function to get user weight in kilograms


def get_user_weight():
    '''Get user weight in kgs'''
    while True:
        try:
            weight = int(input(f'Please enter your weight in kilograms:\n'))
        except ValueError:
            print("Sorry, you must type a number for your weight.")
            continue
        else:
            CUSTOMER.append(weight)
            break
# Function to calculate users BMI


def get_user_bmi(height, weight):
    '''Calculate the user's BMI'''
    bmi = round((int(weight) / int(height) / int(height)) * 10000, 1)
    CUSTOMER.append(bmi)
# Function to get users age


def get_user_age():
    '''Get user age'''
    while True:
        try:
            age = int(input(f'Please enter your age in years:\n'))
        except ValueError:
            print("Sorry, you must type a number for your age.")
            continue
        else:
            CUSTOMER.append(age)
            break
# Function to get user's gender


def get_user_gender():
    '''Get user gender'''
    while True:
        try:
            gender = str(input(f'Please enter your gender (m for male, f for female):\n'))
            if gender == 'm' or gender == 'f':
                CUSTOMER.append(gender)
            else:
                raise Exception                
        except Exception:
            print("Sorry, you must type 'm' or 'f' for your gender.")
            continue
        else:            
            break
# Function to get users workout schedule (num of days per week)

def get_user_schedule():
    '''Get user work out schedule in hours per week'''
    while True:
        try:
            hours = int(input(f'Please enter number of hours per week:\n'))
        except ValueError:
            print("Sorry, you must type a number for your schedule.")
            continue
        else:
            CUSTOMER.append(hours)
            break

# Function to check user information to return a dumbell set and cost

# main method call


def main():
    # call all functions
    get_user_height()
    get_user_weight()
    get_user_bmi(CUSTOMER[0], CUSTOMER[1])
    get_user_age()
    get_user_gender()
    get_user_schedule()
    print('---------- Customer Information ----------')
    print(f'Height: {CUSTOMER[0]}cms\nWeight: {CUSTOMER[1]}kgs\nBMI: {CUSTOMER[2]}\nAge: {CUSTOMER[3]} years\nGender: {CUSTOMER[4]}\nSchedule: {CUSTOMER[5]} hours per week\n')


print("---------------------------------------------")
print("----  Welcome to Pete's Gym Kit Costing  ----")
print("---------------------------------------------")
print('')
print('Just a few questions before recommending a gym kit and cost.')
main()
