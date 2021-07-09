'''                                                  * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                                                     * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                                                     * *  File name: M1.py                   	         * *	
                                                     * *  Author: Sailesh Rokaya  	                 * *
                                                     * *  Email: saileshrokaya123@gmail.com              * *
                                                     * *  Course: CIS020-1-CIS093-1 	                 * *
                                                     * *  Laboratory: Week-2	    	                 * *
                                                     * *  Date created: 7/9/2021	   	         * *
                                                     * *  Date last modified: 7/9/2021	   	         * *
                                                     * *  Copyright: Copyright 2021	                 * * 
                                                     * *  Python Version: 3.9.6		   	         * *
                                                     * *  Submission: 7/9/2021                           * * 
                                                     * *  Instructor: Deepak Kumar Karna       	         * *
                                                     * *  Description: Programming Workshop 1 – Ext Exe  * *
                                                     * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                                                     * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                                                     
========================================================================================================================================================================================== 
M1	
Hello Program: Addition of Entry of First Name 
Modify the sample “hello” Python program to first request the user’s first name, and then request their last name.  The program should then display, 

Hello firstname lastname 
Welcome to Python! (for the firstname and lastname entered). 

What is your first name? John 
What is your last name? Smith 
Hello John Smith 
Welcome to Python! 
>>> 
=======================================================================================================================================================================================	'''
# Begin code

# Input from user 
fname = input('What is your first name? ')
lname = input('What is your last name? ')

#Display the Output
print('Hello ', fname, lname, '\nWelcome to Python!')
