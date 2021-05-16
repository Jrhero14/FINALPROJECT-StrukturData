async function search_words(){
  var word = document.getElementById("input").value
  if(word){
    var output = document.getElementById("output")
    var loading = document.getElementById("loader")
    output.style.visibility = 'hidden'
    loading.style.visibility = 'visible'
    output.style.opacity = 0
    loading.style.opacity = 1
    var kata = document.getElementById("word")
    var definisi = document.getElementById("definition")
    var contoh = document.getElementById("example")
    let hasil = await eel.cari(word,1)()
    console.log(kata)
    if(hasil == 1){
      kata.innerHTML = "Hasil tidak ditemukan"
      definisi.innerHTML = "Hasil tidak ditemukan"
      contoh.innerHTML = "Hasil tidak ditemukan"
    }
    else{
      kata.innerHTML = hasil[0]
      definisi.innerHTML = hasil[1]
      contoh.innerHTML = hasil[2]
    }
    setTimeout(function(){
      output.style.visibility = 'visible'
      loading.style.visibility = 'hidden';
      output.style.opacity = 1
      loading.style.opacity = 0
  }, 1000)
    console.log(hasil)
  }
}

async function add(){
  var kata = document.getElementById("kata").value
  var definisi = document.getElementById("definisi").value
  var contoh = document.getElementById("contoh").value
  var overlay = document.getElementById("overlay")
  overlay.style.visibility = 'visible';
  overlay.style.opacity = 1
  eel.tambah(kata, definisi, contoh)()
  setTimeout(function(){
    overlay.style.opacity = 0
    overlay.style.visibility = 'hidden';
  }, 1000)
}

async function edit(){
  var kata = document.getElementById("kata").value
  var pilihan = document.getElementById("pilihan").value
  var output = document.getElementById("output")
  var loading = document.getElementById("loader")
  var word = document.getElementById("word")
  var definition = document.getElementById("definition")
  var deskripsi = document.getElementById("deskripsi").value

  var definitionAfter = document.getElementById("definitionAfter")
  var definition2After = document.getElementById("definition2After")

  if(kata && pilihan && deskripsi){
    if(pilihan == "definisi"){
      var pilih = 1
    }
    else if(pilihan == "contoh"){
      var pilih = 2
    }
    var hasil = await eel.cari(kata)()
    if(hasil == 1){
      word.innerHTML = "Hasil tidak ditemukan"
      definition.innerHTML = "Hasil tidak ditemukan"
      contoh.innerHTML = " "
      definition2.innerHTML = " "
      after.innerHTML = " "
      wordAfter.innerHTML = " "
      definitionAfter.innerHTML = " "
      contohAfter.innerHTML = " "
      definition2After.innerHTML = " "
    }
    else{
      var hasilSebelum = await eel.cari(kata)()

      await eel.edit(kata, pilih, deskripsi)()
      var hasilSesudah = await eel.cari(kata)()

      word.innerHTML = hasilSebelum[0]
      definition.innerHTML = hasilSebelum[1]
      contoh.innerHTML = "Contoh"
      definition2.innerHTML = hasilSebelum[2]
      after.innerHTML = "Setelah Perubahan"
      wordAfter.innerHTML = hasilSebelum[0]
      definitionAfter.innerHTML = hasilSesudah[1]
      contohAfter.innerHTML = "Contoh"
      definition2After.innerHTML = hasilSesudah[2]

    }
    output.style.visibility = 'hidden'
    loading.style.visibility = 'visible'
    output.style.opacity = 0
    loading.style.opacity = 1
    setTimeout(function(){
      output.style.visibility = 'visible'
      loading.style.visibility = 'hidden';
      output.style.opacity = 1
      loading.style.opacity = 0
  }, 1000)
  }
}

async function preview(){
  var kata = document.getElementById("kata").value
  var pilihan = document.getElementById("pilihan").value
  var output = document.getElementById("output")
  var loading = document.getElementById("loader")
  var word = document.getElementById("word")
  var definition = document.getElementById("definition")
  if(kata && pilihan){
    var hasil = await eel.cari(kata)()
    if(hasil == 1){
      word.innerHTML = "Hasil tidak ditemukan"
      definition.innerHTML = "Hasil tidak ditemukan"
      contoh.innerHTML = " "
      definition2.innerHTML = " "
      after.innerHTML = " "
      wordAfter.innerHTML = " "
      definitionAfter.innerHTML = " "
      contohAfter.innerHTML = " "
      definition2After.innerHTML = " "
    }
    else{
      kata = hasil[0]
      word.innerHTML = hasil[0]
      definition.innerHTML = hasil[1]
      definition2.innerHTML = hasil[2]
      contoh.innerHTML = "Contoh"
      after.innerHTML = " "
      wordAfter.innerHTML = " "
      definitionAfter.innerHTML = " "
      contohAfter.innerHTML = " "
      definition2After.innerHTML = " "
    }
    output.style.visibility = 'hidden'
    loading.style.visibility = 'visible'
    output.style.opacity = 0
    loading.style.opacity = 1
    setTimeout(function(){
      output.style.visibility = 'visible'
      loading.style.visibility = 'hidden';
      output.style.opacity = 1
      loading.style.opacity = 0
  }, 1000)
  }
}

async function hapus(){
  var kata = document.getElementById("kata").value
  var output = document.getElementById("output")
  var loading = document.getElementById("loader")
  var word = document.getElementById("word")
  var definition = document.getElementById("definition")
  var pilih = 3
  if(kata){
    var hasil = await eel.cari(kata)()
    if(hasil == 1){
      word.innerHTML = "Hasil tidak ditemukan"
      definition.innerHTML = "Hasil tidak ditemukan"
      contoh.innerHTML = " "
      definition2.innerHTML = " "
      after.innerHTML = " "
      wordAfter.innerHTML = " "
      definitionAfter.innerHTML = " "
      contohAfter.innerHTML = " "
      definition2After.innerHTML = " "
    }
    else{
      await eel.edit(kata, pilih, deskripsi)()
      word.innerHTML = "Berhasil Dihapus"
      definition.innerHTML = "Berhasil Dihapus"
      contoh.innerHTML = " "
      definition2.innerHTML = " "
      after.innerHTML = " "
      wordAfter.innerHTML = " "
      definitionAfter.innerHTML = " "
      contohAfter.innerHTML = " "
      definition2After.innerHTML = " "
    }
    output.style.visibility = 'hidden'
    loading.style.visibility = 'visible'
    output.style.opacity = 0
    loading.style.opacity = 1
    setTimeout(function(){
      output.style.visibility = 'visible'
      loading.style.visibility = 'hidden';
      output.style.opacity = 1
      loading.style.opacity = 0
  }, 1000)
  }
}

async function history(mode){
  var history = await eel.lihat(mode)()
  var tab = document.getElementById("history-js")
  var innerhistory = ""
  console.log(history)
  for(i in history){
    var tag = "<button " + "id=\""+ i + "\"" + "onclick=\"search_history(" + i + ")\">" + history[i] + "</button>"
    innerhistory = innerhistory + tag
  }
  tab.innerHTML = innerhistory
}

async function search_history(choice){
  word = document.getElementById(choice).innerHTML
  var kata = document.getElementById("word")
  var definition = document.getElementById("definition")
  var definition2 = document.getElementById("definition2")
  let hasil = await eel.cari(word, 0)()
  kata.innerHTML = hasil[0]
  definition.innerHTML = hasil[1]
  definition2.innerHTML = hasil[2]
}


/*
window.addEventListener('contextmenu', function (e) {
  e.preventDefault();
}, false);

*/
