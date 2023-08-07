l=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
new_l=[]
def flatten(m):
    isFlatting = [flatten(sublist) if type(sublist) == list else new_l.append(sublist) for sublist in m]
flatten(l)
print(new_l)