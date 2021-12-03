Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def clean(floor):
    i=0
    j=0
    x=0
    row=len(floor)
    column=len(floor[0])
    while(row != 0):
        if floor[i][j] == 1:
            floor[i][j]=0
            x=x+1
            print_floor(floor,i,j,x)
            j=j+1
        else:
            j=j+1
        if j==column:
            j=0
            i=i+1
            row=row-1
            

def print_floor(floor, row, col,count):# row, col represent the current vacuum cleaner position
    print('step:',count)
    for x in floor:
        print(x)
    print('vaccum cleaner :',row,col)
floor = [[1, 1, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 1],
         [0, 1, 0, 1, 0, 1, 0]]

clean(floor)
