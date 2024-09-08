# File Structure

In folder, Exercise1 ( Todo Management System )
- todo.py contains the code.
- users.json contains the user login information.
- todos.json stores the todo list information of various users.

In folder, Exercise2 ( Fee Management System )
- fee.py contains the code.
- students.json contains student information.


# Features

Todo Management System:
- Register and login
- Add todos
- Remove todos
- Update the due date of todos

Fee Management System:

it has been divided into two interfaces, Admin and Student.

The features for the admin are:
- Add student information
- View the list of students who have paid the fees
- View the list of students who have not paid the fees
- Generate Report for all the students by their respective years
  
The features for the students are:
- Deposit fee
- View Fee Structure according to the year


# Assumptions

Todo Management System:
- No major assumptions

Fee Management System:
- It is for a 4 year course where fee is supposed to be paid on an yearly basis.
- A scholarship of 35% is being offered to the students with a percentage greater than or equal to 95%.
- Only those students can access the student interface to deposit the fee who have been added by the Admin.
- The fees for first year is 50000 divided between Tuition fee and Development fee. The fees for every successive year is incremented by 2k.


# User Guide

Todo Management System:
I have already made 2 user accounts, you can access their username and password from the users.json file and directly login to explore the various options for todo management. Otherwise, you can simply select the 'Register' option to create a new user account and login with that.

Fee Management System:
Select the Admin option, it will ask you for the admin password which is 'admin123'. The data of 4-5 students has already been added by me so you can see the list of students who have paid the fees and those who have not. You can add more students by selecting the 'Add Student' option. To explore the student interface select the 'Student' option, you will need the roll number of the student. If you are going for one of the already added students, you can check their roll numbers from the students.json file. The 'Generate Report' option generates a file which contains all the students from different years along with their payment status.
