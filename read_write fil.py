file1 = open('sample.txt', 'w')

file1.write("my first time on python loving it\n yeah i am lying")
file1.close()

fr = open('sample.txt', 'r')
##write =
print(fr.read())
fr.close()
