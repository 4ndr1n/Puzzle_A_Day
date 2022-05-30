test = open(r'/Users/Andrin/Desktop/newdoc.csv','w')

stringarray = ["mol", "luege"]

x = "{} ; {}"
print(x.format(stringarray[0],stringarray[1]))
test.write(x.format(stringarray[0],stringarray[1]))

