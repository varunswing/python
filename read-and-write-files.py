fw = open("Sample.txt", 'w')
fw.write("Hey! I am Varun.\n")
fw.write("I like becon.\n")
fw.close()

fr = open("Sample.txt", 'r')
text = fr.read()
print(text)
fr.close()