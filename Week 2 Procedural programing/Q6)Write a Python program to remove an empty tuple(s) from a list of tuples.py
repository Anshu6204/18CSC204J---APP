def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
tuples = [(), ('1','2','3'), (), ('4', '5'), 
          ('6', '7', '8'), ('9','0'),()]
print(Remove(tuples))