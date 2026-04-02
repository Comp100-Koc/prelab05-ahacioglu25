def remove_adjacent_duplicates(s):
    sonuc = ""
    index = 0
    while index < len(s):
        if len(sonuc) > 0 and sonuc[-1] == s[index]:
            sonuc = sonuc[:-1]
        else:
            sonuc += s[index]
        index += 1
    return sonuc
