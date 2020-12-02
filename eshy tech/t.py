import OM

filet = open ('txt.txt', 'w')
#print content
filet.write('Today is a good day')
filet.close()


#Add to existing content
filet = open ('txt.txt', 'a')
filet.write('\n It is Thursday.')
file.close()

#open file and print out content
filet = open('txt.txt', 'r')
print(filet.read())
 
