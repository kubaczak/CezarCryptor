def szyfrowanie(inp, sr, tab):
    if int(sr[0]) == 1:
        sp = tab[0]
    elif int(sr[0]) == 2:
        sp = tab[1]
    elif int(sr[0]) == 3:
        sp = tab[2]
    elif int(sr[0]) == 4:
        sp = tab[3]
    elif int(sr[0]) == 5:
        sp = tab[4]
    elif int(sr[0]) == 6:
        sp = tab[5]
    elif int(sr[0]) == 7:
        sp = tab[6]
    elif int(sr[0]) == 8:
        sp = tab[7]
    else:
        sp = tab[8]
    z = []
    inp = str(inp)
    for n in range(len(inp)):
        for i in range(len(alfa)):
            if inp[n] == " ":
                z.append(" ")
                break
            if alfa[i] == inp[n]:
                if not i+int(sr[1]) >= len(alfa):
                    z.append(sp[i+int(sr[1])])
                    break
                else:
                    z.append(sp[(i+int(sr[1]))-(len(alfa))])
                    break
            elif i == 75:
                z.append(inp[n])
                break
    end = ""
    for i in range(len(z)):
        end = end+z[i]
    return end


def odszyfrowanie(inp, sr, tab):
    if int(sr[0]) == 1:
        sp = tab[0]
    elif int(sr[0]) == 2:
        sp = tab[1]
    elif int(sr[0]) == 3:
        sp = tab[2]
    elif int(sr[0]) == 4:
        sp = tab[3]
    elif int(sr[0]) == 5:
        sp = tab[4]
    elif int(sr[0]) == 6:
        sp = tab[5]
    elif int(sr[0]) == 7:
        sp = tab[6]
    elif int(sr[0]) == 8:
        sp = tab[7]
    else:
        sp = tab[8]
    z = []
    for n in range(len(inp)):
        for i in range(len(sp)):
            if inp[n] == " ":
                z.append(" ")
                break
            if sp[i] == inp[n]:
                if not (i-int(sr[1])) < 0:
                    z.append(alfa[i-int(sr[1])])
                    break
                else:
                    z.append(alfa[len(alfa)-int(sr[1])])
                    break
            elif i == 75:
                z.append(inp[n])
    end = ""
    for i in range(len(z)):
        end = end+z[i]
    return end

szyfr = ["a", "A", "ą", "Ą", "b", "B", "c", "C", "ć", "Ć", "d", "D", "e", "E", "ę", "Ę", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "ł", "Ł", "m", "M", "n", "N", "ń", "Ń", "o", "O", "ó", "Ó", "p", "P", "r", "R", "s", "S", "ś", "Ś", "t", "T", "u", "U", "w", "W", "y", "Y", "z", "Z", "ź", "Ź", "ż", "Ż", "x", "X", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
alfa = ["a", "A", "ą", "Ą", "b", "B", "c", "C", "ć", "Ć", "d", "D", "e", "E", "ę", "Ę", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "ł", "Ł", "m", "M", "n", "N", "ń", "Ń", "o", "O", "ó", "Ó", "p", "P", "r", "R", "s", "S", "ś", "Ś", "t", "T", "u", "U", "w", "W", "y", "Y", "z", "Z", "ź", "Ź", "ż", "Ż", "x", "X", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
