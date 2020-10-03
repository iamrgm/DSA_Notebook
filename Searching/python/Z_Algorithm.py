# Z ALgorithm Function
def Z_Algo(text, pattern):
    List = []
    substring = ""

    #Iterating upto the index where the substring can occur
    for text_index in range(0, len(text) - len(pattern) + 1):

        #Extracting the --substring of the same length as pattern-- from the text
        substring = text[text_index:text_index + len(pattern)]

        #Loop for comparing the substring and pattern
        count = 0
        for substring_index in range(0, len(pattern)):

            #If the charecters of substring and pattern matches , increment count by 1
            if substring[substring_index] == pattern[substring_index]:
                count += 1

        #If all the charecters of substring and pattern matches , add position to list
        if count == len(pattern):
            List.append(text_index)

    #Return the list that contains all the positions the substring is present at
    return List


# Driver Code

if __name__ == '__main__':
    text = input("Enter Text : ")
    pattern = input("Enter pattern : ")

    #Calling Z__Algo to seacrh the substring positions
    positions = Z_Algo(text, pattern)

    #If returned list from Z__Algo is not empty , print positions , else prompt -- pattern not found
    if len(positions) != 0:
        for position in positions:
            print("The pattern is present at : " + str(position+1))

    else:
        print("Pattern Not Found !!!")

'''
    Input description: 
    Line 1 -- Text
    Line 2 -- Pattern

    Output Description :
    The pattern is present at : position_index
    
    Example Outputs:
    
    Input 1:
        Enter Text : aaaabbabbababaabbabaaaa
        Enter pattern : aa
    Output 1:
        The pattern is present at : 1
        The pattern is present at : 2
        The pattern is present at : 3
        The pattern is present at : 14
        The pattern is present at : 20
        The pattern is present at : 21
        The pattern is present at : 22

    Input 2:   
        Enter Text : occiioossoo
        Enter pattern : oo

    Output 2:
        The pattern is present at : 6
        The pattern is present at : 10
'''