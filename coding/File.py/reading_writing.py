# File Object

'''f = open('test.txt','r')
#print(f.name)
print(f.mode)

f.close()'''



#Contex Manager

'''with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)'''





'''with open('test.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)


with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents)
    
    f_contents = f.readline()
    print(f_contents)'''

'''with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents, end='')
    
    f_contents = f.readline()
    print(f_contents, end='') '''


'''with open('test.txt', 'r') as f:

    for line in f:
        print(line, end='')'''


'''with open('test.txt', 'r') as f:
    f_contents = f.read(125)
    print(f_contents, end='')
    
    f_contents = f.read(100)
    print(f_contents, end='')'''
   

'''with open('test.txt', 'r') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)


with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)'''



'''with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f.tell())'''



'''with open('test.txt', 'r') as f:
    size_to_read = 10
    
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f_contents = f.read(size_to_read)
    print(f_contents)'''


'''with open('test.txt', 'r') as f:
    size_to_read = 10
    
    f_contents = f.read(size_to_read)
    print(f_contents, end='')


    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)'''



#Writing the file

'''with open('test2.text', 'w') as f: #w is writing
     pass '''
 
'''with open('test2.text', 'w') as f:
    f.write('Test')
    f.write('Test')'''

'''with open('test2.text', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('Test')'''

'''with open('test2.text', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')'''







'''with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)'''


with open('manoram.jpg', 'rb') as rf:#in r is b but b is binary
    with open('manoram_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)



'''with open('manoram.jpg', 'rb') as rf:#in r is b but b is binary
    with open('manoram_copy.jpg', 'wb') as wf:
        chunk_size = 4096 
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)'''




