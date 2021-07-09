'''                                                  * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                                                     * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                                                     * *  File name: P4.py                   	         * *	
                                                     * *  Author: Sailesh Rokaya  	                 * *
                                                     * *  Email: saileshrokaya123@gmail.com              * *
                                                     * *  Course: CIS020-1-CIS093-1 	                 * *
                                                     * *  Laboratory: Week-2	    	                 * *
                                                     * *  Date created: 7/9/2021	   	         * *
                                                     * *  Date last modified: 7/9/2021	   	         * *
                                                     * *  Copyright: Copyright 2021	                 * * 
                                                     * *  Python Version: 3.9.6		   	         * *
                                                     * *  Submission: 7/9/2021              	         * * 
                                                     * *  Instructor: Deepak Kumar Karna       	         * *
                                                     * *  Description: Programming Workshop 1 – Ext Exe  * *
                                                     * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                                                     * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                                                     
========================================================================================================================================================================================== 
P4	
Write a Python program that allows the user to enter a four-digit binary number and displays the value in base 10.
Each binary digit should be entered one per line, starting with the leftmost digit, as shown below. 

Enter leftmost digit: 1 
Enter the next digit: 0 
Enter the next digit: 0 
Enter the next digit: 1 
The value is 9 
=======================================================================================================================================================================================	'''
# Begin code

# Stor input from user.
a = int(input('Enter leftmost digit: '))
b = int(input('Enter the next digit: '))
c = int(input('Enter the next digit: '))
d = int(input('Enter the next digit: '))

# Binary to decimal calculation.
cal = a*(2**0) + b*(2**1) + c*(2**2) + d*(2**3)

# Display output
print('The decimal value is: ', cal)
