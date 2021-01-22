with open('../../../../../../../../games/python1/mese/mese1', 'r', encoding="utf-8") as in_file:
                                        #open the file from,    read, read latin letters

    text= ''

    line=in_file.readline()
    while line:
        text += line.lstrip().replace('gacsos', 'fájós').replace('hordóhas, ', '')

        line=in_file.readline()

    print(text)


    with open('../../../../../../../../games/python1/mese/mese2', "w", encoding='utf-8') as out_file:
        out_file.write(text)