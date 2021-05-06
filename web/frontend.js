function search_words(){
  var data = document.getElementById("input").value
  if(data){
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

function add_words(){
  var kata = document.getElementById("kata").value
  var definisi = document.getElementById("definisi").value
  var contoh = document.getElementById("contoh").value
  var overlay = document.getElementById("overlay")
  overlay.style.visibility = 'visible';
  overlay.style.opacity = 1
  setTimeout(function(){
    overlay.style.visibility = 'hidden';
    overlay.style.opacity = 0
  }, 3000)
}
