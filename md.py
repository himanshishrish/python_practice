def function(string):
    m=0
    output=""
    for i in range(len(string)):
        m=i+1
        output=string[i:m]+output
    print(output)
function("1234abcd")    