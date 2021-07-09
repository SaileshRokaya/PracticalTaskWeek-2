'''                                                  * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                                                     * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                                                     * *  File name: P3.py                   	         * *	
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
P3	
Write a Python program that allows the user to enter any integer base and integer exponent, and displays the value of the base raised to that exponent.
Your program should function as shown below. 

What case? 10 
What power of 10? 4 
10 to the power of 4 is 10000 

Note: 
At this point, students do not know how to concatenate strings to create the input prompt string as specified in the problem.  This needs to be pointed out to students.

=======================================================================================================================================================================================	'''
# Begin code

# Store input from user
case = int(input('What case? '))
power = int(input('What power of ', case, '?'))

# Power calculation 
cal = case**power

# Display output
print(case, "to the power of ", power, "is: ", cal)
