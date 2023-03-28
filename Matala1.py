#1
def my_func(x1,x2,x3):
    if type(x1)== int or type(x2)== int or type(x3)== int:
        return 'Error: parameters should be float'
    elif type(x1)== float and type(x2)== float and type(x3)== float:
        if x1+x2+x3==0:
            return 'Not a number – denominator equals zero'
        else:
            return ((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
    else:
        return 'None'
print (my_func(1.0,2.0,3.0))

#2
def revword(word:str): 
    new=word[::-1].lower()
    return new
def countword(): 
    first=0
    counter=1
    file=open('text.txt') 
    for line in file:
        words=line.split()
        if first==0:
            word= words[0]
            first+=1
            print(word)
        else:      
            for l in words:
                wr=(revword(l))
                print(wr, end=' ')
                if wr==word:
                    counter+=1
            print('\n', end='')
    return 'Namber of appearances=' ,counter
print(countword())



