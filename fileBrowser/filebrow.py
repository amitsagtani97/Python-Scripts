import os
dirname = "c:"
#print(os.listdir(dirname))
print(dirname)
dirname1 = dirname + "\\"
for a in os.listdir(dirname1):
    print(a)

while(True):
    i = list(map(str,input().strip().split()))
    if(i[0] == 'exit'):
        break

    elif(i[0] == 'back'):
        li = list(dirname.split('\\'))
        del li[-1]
        dirname = '\\'.join(li)
        if(dirname[-1] == ':'):
            dirname = dirname + '\\'
        print(dirname)
    elif(i[0] == 'open'):
        print(i[1])
        i[1] =  dirname + "\\" + i[1]
        os.startfile(i[1])
    else:
        dirname = dirname + '\\' + i[0]
    print("\n" + dirname)
    for a in os.listdir(dirname):
        print(a)

#print(dirname)
#print(os.listdir(dirname))