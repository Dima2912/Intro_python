def union_file():
    union_f = open('union_file.txt', "w", encoding="utf-8")
    file1 = open('temp.txt')
    file2 = open('temp1.txt')

    ln = len(file1.readlines())
    file1.seek(0)
    if len(file1.readlines()) != len(file2.readlines()):
        print("The contents of the files do not match!")
    else:
        file1.seek(0)
        file2.seek(0)
        for i in range(ln):
            print(f"{file1.readline()[:-4]}+ {file2.readline()}", file=union_f, end='')


union_file()


