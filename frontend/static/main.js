const container = document.querySelector('.container')
const color = document.querySelector('.color')
const resetBtn = document.querySelector('.btnX')
const size=100

let draw = false

function populate(size) {
  container.style.setProperty('--size', size)
  for (let i = 0; i < size * size; i++) {
    const div = document.createElement('div')
    div.classList.add('pixel')

    div.addEventListener('mouseover', function(){
      if(!draw) return
      div.style.backgroundColor = color.value
    })
    div.addEventListener('mousedown', function(){
      div.style.backgroundColor = color.value
    })
    container.appendChild(div)
  }
}

  window.addEventListener("mousedown", function(){
    draw = true
    })
  window.addEventListener("mouseup", function(){
    draw = false
  })
   

  resetBtn.addEventListener('click', function(){
    container.innerHTML = ''
    populate(size)
  })

  

populate(size)