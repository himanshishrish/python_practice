print("TRUTH TABLE OF \"OR\"")
formattedResult="{} or {}={}"
print (formattedResult.format(0,0,0 or 0))
print (formattedResult.format(0,1,0 or 1))
print (formattedResult.format(1,0,1 or 0))
print (formattedResult.format(1,1,1 or 1))
print("///////////////////////////////////////////////")
print("TRUTH TABLE OF \"AND\"")
formattedResult="{} and {}={}"
print (formattedResult.format(0,0,0 and 0))
print (formattedResult.format(0,1,0 and 1))
print (formattedResult.format(1,0,1 and 0))
print (formattedResult.format(1,1,1 and 1))
print("///////////////////////////////////////////////")
print("TRUTH TABLE OF \"NOT\"")
formattedResult="{} not {}"
print (formattedResult.format(0,1))
print (formattedResult.format(1,0))


