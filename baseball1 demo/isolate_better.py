#############################################|############################################
#                                                                                        #
#                                       Isolate Better                                   #
#                                                                                        #
#############################################|############################################
# Riley Conlon




#   This function is meant to help with parsing substrings from large chunks of text where
#   the desired substrings might be flanked by repeated characters or substrings--like in
#   html. The function requires that either the start or end substrings are unique within
#   the full string, but does not require that both are.
#   With b_end=0, the function will return the substring contained between the unique
#   'start' substring and the next appearance of the 'end' substring, exclusively.
#   With b_end=1, the function will return the substring contained between the unique
#   'end' substring and the first appearance of the 'start' substring immediately
#   preceeding the 'end' substring, exclusively.




### Define functions
def reverse (stri) :
    x = ""
    for i in stri :
        x = i + x
    return x
#





def isolate_better (stri , start , end, b_end = 0) :
    strShort    = ''
    posStart    = 0
    posEnd      = 0

    if b_end==1 :
        posEnd      = stri.find(end)
        strShort    = stri[:posEnd]
        strShort    = reverse(strShort)
        start       = reverse(start)
        posStart    = posEnd - strShort.find(start)
    #
    else :
        posStart    = stri.find(start)+len(start)
        strShort    = stri[posStart:]
        posEnd      = posStart + strShort.find(end)
    #
    return stri[posStart:posEnd]
#
