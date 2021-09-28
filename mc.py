def function(name):
    m=0
    y=""
    z=""
    for i in range(len(name)):
        m=i+1
        y=name[i:m]
        z=name[i:m].upper
        if y==z:
            print('K')
        else:
            print("o")
function('The quick Brow Fox')  
