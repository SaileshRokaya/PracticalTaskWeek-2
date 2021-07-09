'''                                                  * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                                                     * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                                                     * *  File name: P5.py                   	         * *	
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
P5	
Write a simple Python program that prompts the user for a certain number of cities for the Traveling Salesman problem, and displays the total number of possible routes that can be taken,
Your program should function as shown below. 

How many cities? 10 
For 10 cities, there are 3628800 possible routes 
=======================================================================================================================================================================================	'''
# Begin code

# Import the math module
import math 

# Store value from user input
x = int(input("How many cities? "))

#Caclulation 
a = math.factorial(x)

#Display the €output
print("For", x, "cities, there are", a, "possible routes")
