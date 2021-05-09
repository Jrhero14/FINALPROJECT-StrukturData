import pandas as pd

df = pd.read_csv("database.csv")

#FUNGSI-FUNGSI SISTEM BEGIN
def hashFunction(word):
    temp = 0
    for i, j in zip(word, range(1, len(word)+1)):
        temp += ord(i) * j
        temp = temp % 1000
    return temp

def linearConllisionEmpty(kata):
    newIndex = hashFunction(kata)
    while True:
        if (newIndex == 999):
            newIndex = 0
        if (df.isnull().loc[newIndex][0] == False):
            newIndex += 1
        elif (df.isnull().loc[newIndex][0] == True):
            return newIndex

def linearConllisionsSearch(kata):
    newIndex = hashFunction(kata)
    while True:
        if (newIndex == 999):
            newIndex = 0
        elif (df.loc[newIndex][0] != kata):
            newIndex += 1
        elif (df.loc[newIndex][0] == kata):
            return newIndex
        if (newIndex == hashFunction(kata)): # Data tidak ditemukan
            return None

def realokasi(IndexKataLama, kata_baru):
    df.loc[IndexKataLama] = [None, None, None]
    if (df.isnull().loc[hashFunction(kata_baru)][0] == False):
        new_Index = linearConllisionEmpty(kata_baru)
        return new_Index
    else:
        new_Index = hashFunction(kata_baru)
        return new_Index

def overwrite():
    df.to_csv('database.csv', index=False)

# FUNGSI-FUNGSI SISTEM END



# FUNGSI-FUNGSI OPERASI BEGIN

def tambah():
    kata = input("Masukan kata Gaul:") # Variabel input tambah kata
    definisi = input("Definisi kata tersebut:") # Variabel input definisi kata
    contoh = input("Contoh kata tersebut:") # Variabel input contoh kata

    if (df.isnull().loc[hashFunction(kata)][0] == False): # Apabila dalam database entry tersebut sudah ada yg menempati
        print("Terjadi Collision, Linear Collision sedang dilakukan...")
        newIndex = linearConllisionEmpty(kata)
        df.loc[newIndex] = [kata, definisi, contoh]
        overwrite()
        print("Linear Collision sukses dilakukan!!")

    else:  # Apabila dalam database entry tersebut kosong
        df.loc[hashFunction(kata)] = [kata, definisi, contoh]
        overwrite()
        print("Berhasil ditambahkan\n")


def cari():
    global list1
    word = input("Cari kata:")
    if (df.loc[hashFunction(word)][0] == word): # Apabila data ditemukan
        print("|::::: Kata ditemukan :::::|")
        print("Kata: ", df.loc[hashFunction(word)][0])
        print("Definisi: ", df.loc[hashFunction(word)][1])
        print("Contoh penggunaan: ", df.loc[hashFunction(word)][2])

        word = df.loc[hashFunction(word)][0]
        definisi = df.loc[hashFunction(word)][1]
        contoh_pen = df.loc[hashFunction(word)][2]

        tambahHead(word, definisi, contoh_pen)
        return word, definisi, contoh_pen # return kata, definisi, dan contoh penggunaan

    elif ((df.loc[hashFunction(word)][0] != word) and (df.loc[hashFunction(word)][0] != True)): # Apabila serach terjadi collision
        indexData = linearConllisionsSearch(word)
        if (indexData == None):
            tambahHead(word, None, None)
            print("Data Tidak ditemukan :[")
        elif (indexData != None):
            print("|::::: Kata ditemukan :::::|")
            print("Kata: ", df.loc[indexData][0])
            print("Definisi: ", df.loc[indexData][1])
            print("Contoh penggunaan: ", df.loc[indexData][2])

            word = df.loc[indexData][0]
            definisi = df.loc[indexData][1]
            contoh_pen = df.loc[indexData][2]

            tambahHead(word, definisi, contoh_pen)
            return word, definisi, contoh_pen  # return kata, definisi, dan contoh penggunaan


    else: # Apabila data tidak ditemukan
        tambahHead(word, None, None)
        print(word, "Tidak ditemukan :[")


def edit():
    word = input("Cari kata yang akan diedit:")
    pilih = None
    if (df.loc[hashFunction(word)][0] == word): # Apabila data ditemukan untuk diedit
        print("|::::: Kata ditemukan :::::|")
        print("Kata: ", df.loc[hashFunction(word)][0])
        print("Definisi: ", df.loc[hashFunction(word)][1])
        print("Contoh penggunaan: ", df.loc[hashFunction(word)][2])

        word_temp = df.loc[hashFunction(word)][0] # variabel kata yang ketemu
        definisi_temp = df.loc[hashFunction(word)][1] # variabel definisi dari kata yang ketemu
        contoh_pen_temp = df.loc[hashFunction(word)][2] # variabel contoh dari kata yang ketemu

        print("MENU EDIT:")
        print("1. Kata")
        print("2. Definisi")
        print("3, Contoh")
        print("4. Hapus")

        while True:
            pilih = input("Pilih:")
            word_replace = None

            if (int(pilih) == 1):
                word_replace = input("Masukan Kata:") # Variabel input kata baru
                new_index = realokasi(IndexKataLama=hashFunction(word), kata_baru=word_replace)
                df.loc[new_index] = [word_replace, definisi_temp, contoh_pen_temp]
                overwrite()
                print("Kata berhasil diganti")
                break
            elif (int(pilih) == 2):
                definisi_replace = input("Masukan Definisi :") # Variabel input definisi baru
                df.loc[hashFunction(word)][1] = definisi_replace
                overwrite()
                print("Definisi berhasil diganti")
                break
            elif (int(pilih) == 3):
                contoh_replace = input("Masukan Contoh:") # Variabel input contoh baru
                df.loc[hashFunction(word)][2] = contoh_replace
                overwrite()
                print("Contoh berhasil diganti")
                break
            elif (int(pilih) == 4):
                df.loc[hashFunction(word)] = [None, None, None]
                overwrite()
                print("Kata berhasil dihapus")
                break
            else:
                print("Tidak ada dalam menu")

    elif ((df.loc[hashFunction(word)][0] != word) and (df.loc[hashFunction(word)][0] != True)):
        indexData = linearConllisionsSearch(word)
        if (indexData == None):
            print("Data tidak ditemukan")
        elif (indexData != None):
            print("|::::: Kata ditemukan :::::|")
            print("Kata: ", df.loc[indexData][0])
            print("Definisi: ", df.loc[indexData][1])
            print("Contoh penggunaan: ", df.loc[indexData][2])

            word_temp = df.loc[indexData][0]  # variabel kata yang ketemu
            definisi_temp = df.loc[indexData][1]  # variabel definisi dari kata yang ketemu
            contoh_pen_temp = df.loc[indexData][2]  # variabel contoh dari kata yang ketemu

            print("MENU EDIT:")
            print("1. Kata")
            print("2. Definisi")
            print("3, Contoh")
            print("4. Hapus")

            while True:
                pilih = input("Pilih:")
                word_replace = None

                if (int(pilih) == 1):
                    word_replace = input("Masukan Kata:")  # Variabel input kata baru
                    new_index = realokasi(IndexKataLama= indexData, kata_baru=word_replace)
                    df.loc[new_index] = [word_replace, definisi_temp, contoh_pen_temp]
                    overwrite()
                    print("Kata berhasil diganti")
                    break
                elif (int(pilih) == 2):
                    definisi_replace = input("Masukan Definisi :")  # Variabel input definisi baru
                    df.loc[indexData][1] = definisi_replace
                    overwrite()
                    print("Definisi berhasil diganti")
                    break
                elif (int(pilih) == 3):
                    contoh_replace = input("Masukan Contoh:")  # Variabel input contoh baru
                    df.loc[indexData][2] = contoh_replace
                    overwrite()
                    print("Contoh berhasil diganti")
                    break
                elif (int(pilih) == 4):
                    df.loc[indexData] = [None, None, None]
                    overwrite()
                    print("Kata berhasil dihapus")
                    break
                else:
                    print("Tidak ada dalam menu")

    else: # Apabila data tidak ditemukan untuk diedit
        print(word, "Tidak ditemukan :[")

def history():
    print("Pilih metode:")
    print("1. Tebaru -> Terlama")
    print("2. Terlama -> Terbaru")
    pilih = int(input("Pilih:"))
    if (pilih == 1):
        lihat(0)
    elif (pilih == 2):
        lihat(1)
# FUNGSI-FUNGSI OPERASI END

class simpul:
    def __init__(self, kata, definisi, contoh):
        self.kata = kata
        self.definisi = definisi
        self.contoh = contoh
        self.next = None
        self.prev = None

class DlinkedList:
    def __init__(self):
        self.headVal = None
        self.tailVal = None

def tambahHead(kata, definisi, contoh):
    global list1
    if (list1.headVal is None):
        global new
        new = simpul(kata, definisi, contoh)
        list1.headVal = new
        list1.tailVal = new
    else:
        global new2
        new2 = simpul(kata, definisi, contoh)
        new2.next = list1.headVal
        list1.headVal.prev = new2
        list1.headVal = new2

def lihat(reverse):
    global list1
    if(reverse == 1):
        temp = list1.tailVal
        while (temp != None):
            print("Kata: ",temp.kata)
            temp = temp.prev
    else:
        temp = list1.headVal
        while (temp != None):
            print("Kata: ",temp.kata)
            temp = temp.next

list1 = DlinkedList()

while True:
    print("|::: KAMUS GAOLLL :::|")
    print("1.Tambah\n2.Cari Kata\n3.Edit\n4.History\n5.Keluar")
    menu_Utama = int(input("Pilih:"))

    if(menu_Utama == 1):
        tambah()
        print("\n")
    elif(menu_Utama == 2):
        cari()
        print("\n")
    elif(menu_Utama == 3):
        edit()
        print("\n")
    elif(menu_Utama == 4):
        history()
    elif(menu_Utama == 5):
        exit()
    else:
        print("Tidak ada dalam menu, ulangi!!")
    input("Enter untuk kembali ke menu...")
