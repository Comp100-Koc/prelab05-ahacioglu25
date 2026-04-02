def add_binary(a, b):
    #0b kısmını attık komple
    a = a[2:]   
    b = b[2:]
    i = len(a) - 1
    j = len(b) - 1
    elde = 0
    sonuc = ""
    while i >= 0 or j >= 0 or elde > 0:
        bit_a = 0
        bit_b = 0
        if i >= 0:
            if a[i] == "1":
                bit_a = 1
            i -= 1
        if j >= 0:
            if b[j] == "1":
                bit_b = 1
            j -= 1
        toplam = bit_a + bit_b + elde
        if toplam == 0:
            sonuc = "0" + sonuc
            elde = 0
        elif toplam == 1:
            sonuc = "1" + sonuc
            elde = 0
        elif toplam == 2:
            sonuc = "0" + sonuc
            elde = 1
        else:  # toplam == 3
            sonuc = "1" + sonuc
            elde = 1
    return "0b" + sonuc