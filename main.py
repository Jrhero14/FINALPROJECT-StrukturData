import pandas as pd
import eel

df = pd.read_csv("database.csv")
eel.init('web')

#FUNGSI-FUNGSI SISTEM BEGIN
def hashFunction(word):
    temp = 0
    for i, j in zip(word, range(len(word))):
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
@eel.expose
def tambah(kata, definisi, contoh):

    if (df.isnull().loc[hashFunction(kata)][0] == False): # Apabila dalam database entry tersebut sudah ada yg menempati
        print("Terjadi Collision, Linear Collision sedang dilakukan...")
        newIndex = linearConllisionEmpty(kata)
        df.loc[newIndex] = [kata, definisi, contoh]
        overwrite()
        print("Linear Collision sukses dilakukan!!")
        return 1

    else:  # Apabila dalam database entry tersebut kosong
        df.loc[hashFunction(kata)] = [kata, definisi, contoh]
        overwrite()
        print("Berhasil ditambahkan\n")
        return 0

@eel.expose
def cari(word):
    if (df.loc[hashFunction(word)][0] == word): # Apabila data ditemukan
        print("|::::: Kata ditemukan :::::|")
        print("Kata: ", df.loc[hashFunction(word)][0])
        print("Definisi: ", df.loc[hashFunction(word)][1])
        print("Contoh penggunaan: ", df.loc[hashFunction(word)][2])

        word = df.loc[hashFunction(word)][0]
        definisi = df.loc[hashFunction(word)][1]
        contoh_pen = df.loc[hashFunction(word)][2]

        return word, definisi, contoh_pen # return kata, definisi, dan contoh penggunaan

    elif ((df.loc[hashFunction(word)][0] != word) and (df.loc[hashFunction(word)][0] != True)): # Apabila serach terjadi collision
        indexData = linearConllisionsSearch(word)
        if (indexData == None):
            print("Data Tidak ditemukan :[")
        elif (indexData != None):
            print("|::::: Kata ditemukan :::::|")
            print("Kata: ", df.loc[indexData][0])
            print("Definisi: ", df.loc[indexData][1])
            print("Contoh penggunaan: ", df.loc[indexData][2])

            word = df.loc[indexData][0]
            definisi = df.loc[indexData][1]
            contoh_pen = df.loc[indexData][2]

            return word, definisi, contoh_pen  # return kata, definisi, dan contoh penggunaan


    else: # Apabila data tidak ditemukan
        print(word, "Tidak ditemukan :[")
        return "nyaa"

@eel.expose
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

eel.start('home.html', size=(1280,800))
