

with open('example.txt','r') as file1:
               file_stuf= file1.read()
               print (file_stuf)

print (file1.closed)
print (file_stuf)
type (file_stuf)

with open('example.txt','r') as file2:
    file_stuf_lines = file2.readlines()
    print (file_stuf_lines)
type(file_stuf_lines)
file_stuf_lines[0].split(' ')

with open('example.txt','r') as file2:
    file_stuf_lines = file2.readline()
    print (file_stuf_lines)
type(file_stuf_lines)

with open('example.txt','r') as file2:
    for line in file2:
        print (line)

with open('example.txt','r') as file2:
    file_stuf = file2.readline(16)
    print (file_stuf)
    file_stuf = file2.readline(4)
    print (file_stuf)
# Writing  a File =========================
with open('example2.txt','w') as file1:
    file1.write ("This is line A\n")
    file1.write ("This is line B\n")
# Append  a File =========================
with open('example2.txt','a') as file1:
    file1.write ("This is line A\n")
    file1.write ("This is line B\n")
