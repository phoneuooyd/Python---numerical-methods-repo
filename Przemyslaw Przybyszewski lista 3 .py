def zad1(tekst, klucz):
    output = ""
    iterations = 0

    for znakT in tekst:
        iterations = iterations % 4
        znak = ""
        if(znakT == " "):
            output+=str(znak)
        else:
            znak = chr(ord(znakT) + ord(klucz[iterations]))
            print(f"{znak}, {klucz[iterations]}, {znakT}")
            output+=str(znak)
            iterations+=1
    return output

def zad2(tekst):
    output = ""
    computing = ""
    string = ""

    for i in tekst:
        bin = 0
        znak = ord(i)
        for j in range (8):
            bin = znak % 2
            output = str(bin) + output
            znak = znak // 2
        computing = computing + output
        string = string + output + " "
        output = ""

    print(string)
    print(computing)

    encode = ""
    ite = 0
    for k in computing:
        if(k == "0"):
            ite += 1
        else:
            encode = encode +str(ite) + str(k)
            ite = 0
    if(ite != 0):
        encode = encode + str(ite)
        ite = 0

    print(encode)

    for l in encode:
        output+=chr(int(l))
    print(output)

def zad3(input, bits):
    '''
        Zadanie jest podzielone na 3 etapy - etap dzielenia informacji wejściowych o odpowiednią wartość bitów do zapisu. Liczby większe od 255 rozdziela na dwie. 
        Dla wprowadzenia jednej liczby wpisujemy ją w zad(liczba, bity). Dla ciągu liczby rozdzielamy je spacją np. zad4(500 10 20 700, bity)
    '''
    string1 = input  #łańcuch znaków z wywołania funkcji
    split_list = [] # litsa przechowujca liczby po podziale
    tmp = ''
    for s in string1:
        if s == ' ': #jeżeli znak to spacja 
            split_list.append(tmp)  #dodaj do tabliczy pusty element (czyli pomiń)
            tmp = ''
        else:                                                                                  #tutaj program dzieli liczy jeśli są one po spacji
            tmp += s      #jeżeli to cokolwiek innego od spacji - zapamiętj
    if tmp:
        split_list.append(tmp) #jeżeli tmp nie jest puste, dodaj

    output = []
    tmp = []
    
    for i in split_list:
        while(int(i) > 255): # dopóki element i jest większy od 255
            tmp.append(255) # dodaj do tablicy 255
            tmp.append(0) #dodaj liczbę 0 aby rozdzielić je miejscami (on tak chciał w poleceniu)
            i = (int(i) - 255)  # zmniejsz liczbę o 255, które dodąłeś to tablicy wcześniej
        if(int(i) >= 0 and int(i) < 255):                                                                 #tutaj program rozpoznaje liczby większe od 255 i je dzieli
            tmp.append(int(i)) #jeżeli liczba jest pomiędzy 0:254 to ją po prostu dodaj bez zmian
            
    output = []
    for i in tmp: # dla każdego elementu tablicy z liczbami
        res = "" #wynik na razie pusty
        bin = 0 #zmienna do zamiany na liczbę binarną 
        for j in range(bits):                          #w tym miejscu  program tworzy komórki pamięci na liczby na podstawie liczby bitów, na których chcemy je przechować            
            bin = int(i) % 2                            #np liczba 2 binarnie na dwóch bitach to 10 a na 8 bitach 00000010
            res = str(bin) + res                        #bin i res zamieniają liczbę dziesiętną na binarną
            i //= 2
        output.append(res)  #no i dodają to do tabeli wyników

    encode = ""
    for i in output:                                #tutaj program liczy kolejne wystąpienia ciągów zer
        node = i + " "    #tutaj zrobiłem trik, żebym miał długość zmiennej większą o jeden znak, żebym mógł porównać wszystkie znaki do siebie, żeby nie było błędu że ostatnie 0/1 porównuje się do elementu
        iterations = 1                           #spoza zakresu tablicy, w tym przypadku porówna się do spacji i zobaczy "oho, to nie liczba, ide do kolejnego indeksu"
        for j in range(0, len(node) - 1):      #pęla od 0 do ostatniego indeksu tablicy
            if(node[j] == "1"):                      #jeżeli znak to 1, po prostu go przepisz
                encode = encode + str(node[j])
            elif(node[j] == node[j + 1] and node[j] == "0"):              #jeżeli znak[j] jest taki sam jak następny znak i jest to 0 to zwiększ zmienną iterator
                iterations += 1
            else:                                                           #w każdym innym przypadku przepisz to, co już zrobiłeś i dodaj ile razy powtórzyły się 0
                encode = encode + str(iterations)   #zwróc uwagę, że najpierw przepisujemy encode, a potem ilość powtórzeń, to jest bardzo ważne, gdyby było na odwrót, to to program by źle działał
                                                     #jeżeli pierwsze byłoby parę zer, to program by tego nie policzył
    finalRes = "" 
    for l in encode:                                 #wynik ostateczny
        finalRes += chr(int(l))                #tutaj wynikiem jest nasz ostateczny ciąg liczb, wytłumaczenie tego co się tu dzieje to:            
    print(finalRes)                                #dla każdej liczby, do wyniku ostatecznego zamień ją na typ char (pojedyńczy znak) z tablicy ASCII o danej wartości liczbowej (wyjdą emotikony albo małe znaczki)

zad3("500 20",8)                      #wywołanie

