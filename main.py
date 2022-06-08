def convert(s, numRows):
    # for a given numRows, this is the maximum allowed
    # characters per column (vertical). So basically every
    # char at length of POSITION + numRows will be the next Char
    # in return string until you hit the end of

    # solution: create matrix and assign accordingly
    # then convert matrix into solution string

    # close but last 3 letter in this case are wrong
    # solution = ""
    # first = True
    # i = 0
    # track = 0
    # count = 0
    # while i < len(s) and len(solution) != len(s):
    #     print(i, " s[i]: ", s[i], "num rows: ", numRows, "\n")
    #     # print("sol: ", solution, " count: ", count)
    #     if first is True:
    #         solution += s[i]
    #         first = False
    #     if count == numRows+1:
    #         solution += s[i]
    #         count = 0
    #         print("sol: ", solution, " count: ", count)
            
    #     i +=1
    #     count += 1
        
    #     if i == len(s):
    #         track += 1
    #         i = track
    #         if numRows > 1:
    #             numRows /= numRows
    #         else:
    #             numRows = -1
    #             count = 0
    #         # first = True
                
    #     if len(solution) == len(s):
    #         break
    # return solution

    if numRows == 1:
            return s
    string = ""
    step = (numRows - 1)*2
    down = 0 
    for i in range(numRows):
        if i < len(s):
            string += s[i]
        j = i
        while j < len(s):
            j += step
            if(step and j < len(s)): 
                string += s[j]
            j += down
            if(down and j <len(s)):
                string += s[j]
        step -= 2
        down += 2
    return string

print(convert("PAYPALISHIRING", 3))