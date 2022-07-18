"""
Problem: Aladdin has decided that being a prince is overrated, and
so has opened an online carpet shop.
In Aladdin's shop the price of a carpet depends on the
length of the carpet and the number of different colours
used. In his computer system, a carpet is represented by
a string of letters, e.g., zbbcbbx, where each character
represents the colour of a fixed stretch of carpet. Note
that the total length of the string would be the same as
the total length of the carpet. Ultimately, the price of a
carpet is the length of the carpet multiplied by the
number of different colours used.
Write a program that, when given a string representing
a carpet, outputs its price.
"""

def final_answer(string_length, no_of_unique_colours):
    return string_length*no_of_unique_colours

carpet = input("Please enter your carpet characters: ")
string_length = len(list(carpet))
unique_colours = []

# for loop to create a set of unique set of colours
for colour in list(carpet):
    if colour not in unique_colours:
        unique_colours.append(colour)

no_of_unique_colours = len(unique_colours)

print(final_answer(string_length, no_of_unique_colours))