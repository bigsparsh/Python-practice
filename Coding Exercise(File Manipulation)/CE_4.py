filenames = ['doc1.txt', 'doc2.txt', 'doc3.txt']
file_text = 'Hello'
for filename in filenames:
    file = open(filename, 'w')
    file.write(file_text)
    file.close()
