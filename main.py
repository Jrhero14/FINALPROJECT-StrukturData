import pandas as pd
import eel

df = pd.read_csv("database.csv")
eel.init('web')

#FUNGSI-FUNGSI SISTEM BEGIN
def hashFunction(word):
    temp = 0
    for i, j in zip(word, range(1,len(word)+1)):
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
def cari(word, His = None):
    if (df.loc[hashFunction(word)][0] == word): # Apabila data ditemukan
        print("|::::: Kata ditemukan :::::|")
        print("Kata: ", df.loc[hashFunction(word)][0])
        print("Definisi: ", df.loc[hashFunction(word)][1])
        print("Contoh penggunaan: ", df.loc[hashFunction(word)][2])
        
        word = df.loc[hashFunction(word)][0]
        definisi = df.loc[hashFunction(word)][1]
        contoh_pen = df.loc[hashFunction(word)][2]
        
        if (His == 1):
            tambahHead(word, definisi, contoh_pen)
        return word, definisi, contoh_pen # return kata, definisi, dan contoh penggunaan

    elif ((df.loc[hashFunction(word)][0] != word) and (df.loc[hashFunction(word)][0] != True)): # Apabila serach terjadi collision
        indexData = linearConllisionsSearch(word)
        if (indexData == None):
            if (His == 1):
                tambahHead(word, None, None)
            print("Data Tidak ditemukan :[")
            return 1

        elif (indexData != None):
            print("|::::: Kata ditemukan :::::|")
            print("Kata: ", df.loc[indexData][0])
            print("Definisi: ", df.loc[indexData][1])
            print("Contoh penggunaan: ", df.loc[indexData][2])

            word = df.loc[indexData][0]
            definisi = df.loc[indexData][1]
            contoh_pen = df.loc[indexData][2]

            if (His == 1):
                tambahHead(word, definisi, contoh_pen)
            return word, definisi, contoh_pen  # return kata, definisi, dan contoh penggunaan


    else: # Apabila data tidak ditemukan
        if (His == 1):
            tambahHead(word, None, None)
        print(word, "Tidak ditemukan :[")
        return 1

@eel.expose
def edit(word, pilih, deskripsi):
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
            word_replace = None

            if (int(pilih) == 1):
                df.loc[hashFunction(word)][1] = deskripsi
                overwrite()
                print("Definisi berhasil diganti")
                break
            elif (int(pilih) == 2):
                df.loc[hashFunction(word)][2] = deskripsi
                overwrite()
                print("Contoh berhasil diganti")
                break
            elif (int(pilih) == 3):
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
            return 1
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
                word_replace = None

                if (int(pilih) == 1):
                    definisi_replace = deskripsi
                    df.loc[indexData][1] = deskripsi
                    overwrite()
                    print("Definisi berhasil diganti")
                    break
                elif (int(pilih) == 2):
                    contoh_replace = deskripsi
                    df.loc[indexData][2] = deskripsi
                    overwrite()
                    print("Contoh berhasil diganti")
                    break
                elif (int(pilih) == 3):
                    df.loc[indexData] = [None, None, None]
                    overwrite()
                    print("Kata berhasil dihapus")
                    break
                else:
                    print("Tidak ada dalam menu")

    else: # Apabila data tidak ditemukan untuk diedit
        print(word, "Tidak ditemukan :[")
        return 1

def history(method = None):
    if (method == 1):
        lihat(0)  # Tebaru -> Terlama
    else:
        lihat(1) # Terlama -> Terbaru

# DOUBLE LINKED LIST CONFIGURATION
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

list1 = DlinkedList() # Inisialisasi double linked list sebagai list1

eel.start('home.html', size=(1280,720))
