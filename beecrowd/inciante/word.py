import sys

for palavra in sys.stdin:  
    palavra = palavra.strip()  
    if len(palavra) >= 10:
        print("palavrão")
    else:
        print("palavrinha")
