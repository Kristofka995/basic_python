# 'r' read-olvas
# 'w' write-ír
# 'a' append


# with open ('venv/mondasok.txt', 'r', encoding='utf8') as infile:
#     with open ('out.txt', 'w', encoding='utf-8') as outfile:
#
#         sor=infile.readline()
#
#         while sor:
#             outfile.write(sor)
#             sor=infile.readline()
#


with open ('venv/mondasok.txt', 'a', encoding='utf8') as file:
    newline ='\nBöfike nemlát, böfike megvakult'                   #  \nSzöveg    új sor.

    file.write(newline)