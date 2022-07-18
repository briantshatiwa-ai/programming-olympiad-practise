"""
Problem: Kevin, a university student, is struggling with his
mathematics homework and can’t find his calculator.
Help him find the correct answers for the following
mathematical operation.
Given as input 4 space-separated integers a b c d, write
a program to output the value ad - bc. The value of each
integer is between -10000 and 10000.
"""
def remove_spaces(string):
    """
    a helper function to remove spaces
    """
    return string.replace(" ", "")

def output_answer(a, b, c, d):
    """
    a helper function to do the calculations
    """
    answer = (a*d) - (b*c)
    return answer

integers = input("Please enter 4 space-separated integers: ")
integers = list(remove_spaces(integers))
print("Answer: " + str(output_answer(int(integers[0]), int(integers[1]), int(integers[2]), int(integers[3]))))