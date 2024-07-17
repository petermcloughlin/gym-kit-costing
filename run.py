# Write your code to expect a terminal of 80 characters wide and 24 rows high
CUSTOMER = []
DUMBELL_KIT = {
    'Beginner' : {
        'Dumbells': '2 X 3kg adjustable dumbell set',
        'Barbell': '1 X 6kg barbell',
        'Total Price': '€35'
    },
    'Intermediate' : {
        'Dumbells': '2 X 10kg adjustable set',
        'Barbell': '1 X 20kg barbell',
        'Total Price': '€75'
    },
    'Advanced' : {
        'Dumbells': '2 X 20kg adjustable set',
        'Barbell': '1 X 40kg barbell',
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
            gender = str(input(f'Please enter your gender (m/f):\n'))
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

# Function to select dumbell set and cost, using BMI and age


def get_dumbell_set(age, bmi):
    ''' Recommend Dumbell kit and cost '''
    if bmi < 18.5:
        if age > 18 and age < 30:
            print('We recommend a Beginner set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Beginner"]["Dumbells"]}\nBarbell:' +
            f' {DUMBELL_KIT["Beginner"]["Barbell"]}\nTotal Price:' +
            f' {DUMBELL_KIT["Beginner"]["Total Price"]}')
        elif age >= 30 and age < 50:
            print('We recommend a Beginner set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Beginner"]["Dumbells"]}\nBarbell:' +
            f' {DUMBELL_KIT["Beginner"]["Barbell"]}\nTotal Price:' +
            f' {DUMBELL_KIT["Beginner"]["Total Price"]}')
        elif age >= 50 and age < 65:
            print('We recommend a Beginner set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Beginner"]["Dumbells"]}\nBarbell:' +
            f' {DUMBELL_KIT["Beginner"]["Barbell"]}\nTotal Price:' +
            f' {DUMBELL_KIT["Beginner"]["Total Price"]}')
        elif age >= 65:
            print('We recommend a Beginner set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Beginner"]["Dumbells"]}\nBarbell:' +
            f' {DUMBELL_KIT["Beginner"]["Barbell"]}\nTotal Price:' +
            f' {DUMBELL_KIT["Beginner"]["Total Price"]}')
        else:
            print('Sorry, you are too young to purchase our gym kits.')
    elif bmi >= 18.5 and bmi < 25:
        if age > 18 and age < 30:
            print('We recommend an Intermediate set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Intermediate"]["Dumbells"]}' +
            '\nBarbell:' +
            f' {DUMBELL_KIT["Intermediate"]["Barbell"]}\nTotal Price:' +
            f' {DUMBELL_KIT["Intermediate"]["Total Price"]}')
        elif age >= 30 and age < 50:
            print('We recommend an Intermediate set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Intermediate"]["Dumbells"]}' +
            '\nBarbell:' +
            f' {DUMBELL_KIT["Intermediate"]["Barbell"]}\nTotal Price:' +
            f'{DUMBELL_KIT["Intermediate"]["Total Price"]}')
        elif age >= 50 and age < 65:
            print('We recommend a Beginner set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Beginner"]["Dumbells"]}\nBarbell:' +
            f' {DUMBELL_KIT["Beginner"]["Barbell"]}\nTotal Price:' +
            f' {DUMBELL_KIT["Beginner"]["Total Price"]}')
        elif age >= 65:
            print('We recommend a Beginner set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Beginner"]["Dumbells"]}\nBarbell:' +
            f' {DUMBELL_KIT["Beginner"]["Barbell"]}\nTotal Price:' +
            f' {DUMBELL_KIT["Beginner"]["Total Price"]}')
        else:
            print('Sorry, you are too young to purchase our gym kits.')
    elif bmi >= 25 and bmi < 30:
        if age > 18 and age < 30:
            print('We recommend an Advanced set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Advanced"]["Dumbells"]}\nBarbell:' +
            f' {DUMBELL_KIT["Advanced"]["Barbell"]}\nTotal Price:' +
            f' {DUMBELL_KIT["Advanced"]["Total Price"]}')
        elif age >= 30 and age < 50:
            print('We recommend an Intermediate set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Intermediate"]["Dumbells"]}' +
            '\nBarbell:' +
            f' {DUMBELL_KIT["Intermediate"]["Barbell"]}\nTotal Price:' +
            f' {DUMBELL_KIT["Intermediate"]["Total Price"]}')
        elif age >= 50 and age < 65:
            print('We recommend a Beginner set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Beginner"]["Dumbells"]}\nBarbell:' +
            f' {DUMBELL_KIT["Beginner"]["Barbell"]}\nTotal Price:' +
            f' {DUMBELL_KIT["Beginner"]["Total Price"]}')
        elif age >= 65:
            print('We recommend a Beginner set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Beginner"]["Dumbells"]}\nBarbell:' +
            f' {DUMBELL_KIT["Beginner"]["Barbell"]}\nTotal Price:' +
            f' {DUMBELL_KIT["Beginner"]["Total Price"]}')
        else:
            print('Sorry, you are too young to purchase our gym kits.')
    elif bmi > 30:
        if age > 18 and age < 30:
            print('We recommend an Intermediate set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Intermediate"]["Dumbells"]}' +
            '\nBarbell:' +
            f' {DUMBELL_KIT["Intermediate"]["Barbell"]}\nTotal Price:' +
            f' {DUMBELL_KIT["Intermediate"]["Total Price"]}')
        elif age >= 30 and age < 50:
            print('We recommend an Intermediate set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Intermediate"]["Dumbells"]}' +
            '\nBarbell:' +
            f' {DUMBELL_KIT["Intermediate"]["Barbell"]}\nTotal Price:' +
            f' {DUMBELL_KIT["Intermediate"]["Total Price"]}')
        elif age >= 50 and age < 65:
            print('We recommend a Beginner set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Beginner"]["Dumbells"]}\nBarbell:' +
            f' {DUMBELL_KIT["Beginner"]["Barbell"]}\nTotal Price:' +
            f' {DUMBELL_KIT["Beginner"]["Total Price"]}')
        elif age >= 65:
            print('We recommend a Beginner set')
            print('---------------------------')
            print(f'Dumbells:{DUMBELL_KIT["Beginner"]["Dumbells"]}\nBarbell:' +
            f' {DUMBELL_KIT["Beginner"]["Barbell"]}\nTotal Price:' +
            f' {DUMBELL_KIT["Beginner"]["Total Price"]}')
        else:
            print('Sorry, you are too young to purchase our gym kits.')

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
    print(f'Height: {CUSTOMER[0]}cms\nWeight: {CUSTOMER[1]}kgs\n' +
    f'BMI: {CUSTOMER[2]}\nAge: {CUSTOMER[3]} years\n' +
    f'Gender: {CUSTOMER[4]}\nSchedule: {CUSTOMER[5]} hours per week\n')
    get_dumbell_set(CUSTOMER[3], CUSTOMER[2])


print("---------------------------------------------")
print("----  Welcome to Pete's Gym Kit Costing  ----")
print("---------------------------------------------")
print('')
print('Just a few questions before recommending a gym kit and cost.')
print("---------------------------------------------")
print('')
main()

restart = input('Would you like to try another quotation? (y/n)\n')
if restart == 'y':
    print('')
    print('Just a few questions before recommending a gym kit and cost.')
    print("---------------------------------------------")
    print('')
    main()
elif restart == 'n':
    print("Goodbye. Thank you for using Pete's Gym Kit Costing app.\n")
