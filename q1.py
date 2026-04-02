def longest_palindromic_substring(s):
    enUzun = ""
    uzunluk = len(s)
    merkez = 0
    while merkez < uzunluk:
        # tek uzunluklu palindrome bakak
        sol = merkez
        sag = merkez
        while sol >= 0 and sag < uzunluk and s[sol] == s[sag]:
            if sag - sol + 1 >= 2 and sag - sol + 1 > len(enUzun):
                enUzun = s[sol:sag + 1]
            sol -= 1
            sag += 1
        # çift uzunluklu palindrome bakak
        sol = merkez
        sag = merkez + 1
        while sol >= 0 and sag < uzunluk and s[sol] == s[sag]:
            if sag - sol + 1 > len(enUzun):
                enUzun = s[sol:sag + 1]
            sol -= 1
            sag += 1

        merkez += 1
    return enUzun
