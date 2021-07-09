'''                                                  * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                                                     * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                                                     * *  File name: P2.py                   	         * *	
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
P2 	
Write a Python program that allows the user to enter any integer value, and displays the value of two raised to that power.  Your program should function as shown below. 

What power of two? 10 
Two to the power of 10 is 1024 

=======================================================================================================================================================================================	'''
# Begin code

print ("What power of two? ")

# Store input from user
x = int (input())

# Display output
print ("Two to the power of", x, "is:", 2**x)
