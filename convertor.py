'''to convert temperatures to and from celsius, fahrenheit. Go to the editor
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius'''
def convertor(c,f):
    if f==0:
        f=((9*c)/5)+32
    else:
        c=((f-32)/9)*5
    print(str(c)+"°C is "+str(f)+" in Fahrenheit")
convertor(0,140)    
