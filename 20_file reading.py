# file=open('mondasok.txt', 'r', encoding='utf-8')
#
#  #for sor in file:
#  #    print(sor.strip())
#  sor=file.readline()
#  while sor:
#      print(sor.strip())
#      sor=file.readline()
#
#
#  file.close()

with open ('mondasok.txt', 'r', encoding='utf-8') as file:    # folder/filename('folder/textname.txt'

    line=file.read()
    print(line)
    # while line:
    #     print(line.strip())
    #     line=file.readline()