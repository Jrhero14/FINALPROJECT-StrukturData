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
    let hasil = await eel.cari(word)
    console.log(kata)
    if(hasil == "nyaa"){
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

function edit_words(){
  var kata = document.getElementById("kata").value
  var pilihan = document.getElementById("pilihan").value
  var deskripsi = document.getElementById("deskripsi").value
  if(kata && pilihan != 0 && deskripsi){
    var output = document.getElementById("output")
    var loading = document.getElementById("loader")
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
    console.log(data)
  }
}

function preview(){
  var kata = document.getElementById("kata").value
  var pilihan = document.getElementById("pilihan").value
  if(kata && pilihan != 0){
    var output = document.getElementById("output")
    var loading = document.getElementById("loader")
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
    console.log(data)
  }
}

/*
window.addEventListener('contextmenu', function (e) {
  e.preventDefault();
}, false);

*/
