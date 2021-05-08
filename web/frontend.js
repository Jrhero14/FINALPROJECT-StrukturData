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
    let hasil = await eel.cari(word)()
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
  }, 2000)
    console.log(hasil)
  }
}

function add_words(){
  var kata = document.getElementById("kata").value
  var definisi = document.getElementById("definisi").value
  var contoh = document.getElementById("contoh").value
  var overlay = document.getElementById("overlay")
  overlay.style.visibility = 'visible';
  overlay.style.opacity = 1
  setTimeout(function(){
    overlay.style.opacity = 0
    overlay.style.visibility = 'hidden';
  }, 2000)
}

async function edit(){
  var kata = document.getElementById("kata").value
  var pilihan = document.getElementById("pilihan").value
  var output = document.getElementById("output")
  var loading = document.getElementById("loader")
  var word = document.getElementById("word")
  var definition = document.getElementById("definition")
  var deskripsi = document.getElementById("deskripsi").value
  if(kata && pilihan && deskripsi){
    if(pilihan == "definisi"){
      var pilih = 1
    }
    else if(pilihan == "contoh"){
      var pilih = 2
    }
    var hasil = await eel.edit(kata, pilih, deskripsi)()
    if(hasil == 1){
      word.innerHTML = "Hasil tidak ditemukan"
      definition.innerHTML = "Hasil tidak ditemukan"
    }
    else{
      var hasil = await eel.cari(kata)()
      kata = hasil[0]
      if(pilihan == "definisi"){
        word.innerHTML = hasil[0]
        definition.innerHTML = hasil[1]
      }
      else if(pilihan == "contoh"){
        word.innerHTML = hasil[0]
        definition.innerHTML = hasil[2]
      }
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
  }, 3000)
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
    }
    else{
      kata = hasil[0]
      if(pilihan == "definisi"){
        word.innerHTML = hasil[0]
        definition.innerHTML = hasil[1]
      }
      else if(pilihan == "contoh"){
        word.innerHTML = hasil[0]
        definition.innerHTML = hasil[2]
      }
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
  }, 3000)
  }
}

async function hapus(){
  var kata = document.getElementById("kata").value
  var pilihan = document.getElementById("pilihan").value
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
    }
    else{
      await eel.cari(kata, pilih, deskripsi)()
      word.innerHTML = "Hasil Dihapus"
      definition.innerHTML = "Hasil Dihapus"
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
  }, 3000)
  }
}


/*
window.addEventListener('contextmenu', function (e) {
  e.preventDefault();
}, false);

*/
