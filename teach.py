# propositional logic parser
con_and = [[True ,True  , True],
           [True ,False , False],
           [False,True  , False],
           [False,False , False]]

con_and = [[True ,True  , True],
           [True ,False , False],
           [False,True  , False],
           [False,False , False]]

three_col =    [[ True ,True ,True ],
                [ True ,False,True ],
                [ True ,True ,False],
                [ True ,False,False],
                [ False,True ,True ],
                [ False,False,True ],
                [ False,True ,False],
                [ False,False,False]]

def formula_1_ex():
    for i in three_col:
        if i[0] == True and i[1] == True:
            i.append(True)
        else:
            i.append(False)
        if (i[3] == False):
            i.append(True)
        elif (i[2] == True and i[3] == True):
            i.append(True)
        else:
            i.append(False)
        
        print(i)

formula_1_ex()