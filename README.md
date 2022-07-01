# Amin Online Judge WebApp

# Basic idea about Application 

I am gooing to implement online judge web application where all users can login and register themselves and after login they can select any problem and read that problem statement after he/she can code and submitt it.In minimum amount of time the code will execute and server will return the veridict according to the output.

# Schema

There are three tables 
1)users
  user_id(Primary Key for users table)
  username (Unique)
  name 
  email (Unique)
  password
  country 
  score (Current score of user)
  status (Current Status of user online or offline)
2)submissions
  submission_id (Primary key for submissions table)
  usercode (user's code file is stored in database)
  user_o/p (user's output file is stored in database)
  submissiontime 
  verdict (accepted or WA)
  language 
  user_id (Foreign key from users table to check which user submmitted)
  problem_id (Foreign key from problems table to check which problem's code is submitted)
3)problems
  problem_id (Primary key for problems table)
  prob_description (Description,constraints,Primary testcases)
  score (total score based on difficulty level)
  difficulty 
  testcases_i/p (input files for testcases)
  testcases_o/p (output files for input files)
