![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Pete's Gym Kit Costing App
Welcome to Pete's Gym Kit Costing,
This application is a gym set costing app which takes some user input, calculates their BMI and returns a recommended gym kit set and cost. The live app is accessible in the following  [link](https://gym-kit-costing-194b49d03f96.herokuapp.com/)
The purpose of the app is to take the following input from the user:

* height in cms
* weight in kgs
* age in years
* gender ( m / f )
* work out schedule in hours

Based on the user's input, their BMI is calculated and a summary  of their details in relayed back to the user interface along with a recommended gym kit set of dumbells, barbell and cost.

## Features
The app consists of a series of questions which use validation to ensure their input contains valid entries. Once submitted, the user's responses are appended to a customer array within the application. The response are collated, so a BMI is calculated and the summary data is returned to the terminal for the user to see, along with a recommended gym kit and cost. It also allows the user to re-run a calculation with new user inputs at the end when the user is asked if they would like restart the app or not.

The following screenshots display a flow of the questions asked and validation responses when invalid input is submitted in each instance.

* [AppLaunch](/ReadmeDocs/AppImage1.PNG "AppLaunch")
* [Height](/ReadmeDocs/AppImage2.PNG "Height")
* [Weight](/ReadmeDocs/AppImage3.PNG "Weight")
* [Age](/ReadmeDocs/AppImage4.PNG "Age")
* [Gender](/ReadmeDocs/AppImage5.PNG "Gender")
* [Schedule](/ReadmeDocs/AppImage6.PNG "Hours")
* [Output](/ReadmeDocs/AppImage7.PNG "Output")
* [Restart](/ReadmeDocs/AppImage8.PNG "Retsart")

## Testing
I used manual testing of the user input within github's workspace console to view the exception messages to be passed back to the user in each case. I also used the [PEP8_Linter](https://pep8ci.herokuapp.com/#) site to validate my python code to ensure it met with the PEP8 standards of indentation and structure.

You can view the result in the following [link](/ReadmeDocs/PEP8.PNG) .

Although it may not have been relevant wiithin this project, I completed a Lighthouse report on the webpage containing the depployed Heruko app. 

You can view the result [here](/ReadmeDocs/Lighthouse.PNG "Lighthouse")

## Bugs and Fixes
Initially, I encountered issues when calling the relevant exceptions for user input when writing the code but outside of that issue, I didn't encounter too many issues.

## Deployment
I used Heruko to deployment the application to the web. I followed the steps set out within the Code Institutes tutorials within the Love Sandwiches project. For this project, since I was using any relevant python libraries nor any API's, I did not require the use of .gitignore files, nor the requirements.txt file.
I achieved a successful deployment using Heruko. Since I used a CUSTOMER array and DUMBELL_KIT dictionary within the run.py, it deployed a lot faster and without any known issues. 
Post deployment, I had to do a tidy up of the code indentation to ahdere to PEP8 standards.

## Credits
I referred, for the most part, to the content of the Love Sandwiches project in terms of approaching the code layout and assembly of my functions within both the run.py file and the main method, executing each one sequentially. I used a hand written [flow-chart](/ReadmeDocs/FlowChart.jpg) as my guide to creating the relevant functions within the applcation. I must be honest in saying that I could have probably come up with a lot more complex functionality to the app overall, however, on this occasion time was my real issue as I had been away on a planned holiday with my daughters with very little access to the internet over a two week period. As such , I had one call with my mentor, Alan, while away who was very helpful with ideas and ways to approach this project. As time was my real constraint on this occasion, I tried my best with the learning I had gained prior to my trip away, in order to deliver the best that I could on this occasion.




