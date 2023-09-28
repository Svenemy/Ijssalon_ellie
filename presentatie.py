mijn_dict = {'vis': 10, 'vlees': 25, 'overig': 15}
totaal = sum(dict.values(mijn_dict))

andere_dict= {'a': 1, "b": 2}
andere_totaal = 3




def presenteer(mij_dict, totaal):
    for k in mij_dict:
      print( k + " : " + str(mij_dict[k]) + " euro")
    print("=======================")
    print("totaal : " + str(totaal) + " euro")




        

    
