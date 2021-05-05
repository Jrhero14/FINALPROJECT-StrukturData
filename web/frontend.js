function search_words(){
  var output = document.getElementById("output")
  var loading = document.getElementById("loader")
  output.style.visibility = 'hidden'
  loading.style.visibility = 'visible'
  output.style.opacity = 0
  loading.style.opacity = 1
  var data = document.getElementById("input").value
  setTimeout(function(){
    output.style.visibility = 'visible'
    loading.style.visibility = 'hidden';
    output.style.opacity = 1
    loading.style.opacity = 0
}, 3000)
  console.log(data)
}
