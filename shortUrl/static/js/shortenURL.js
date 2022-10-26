const original_URL = document.getElementById('original_URL')
var full_URL = document.getElementById('full_URL')
const URLForm = document.getElementById('URLForm')
const btn = document.getElementById('btn')

URLForm.addEventListener('submit', shortenURL)

function shortenURL (e) {
    // e.preventDefault()
    console.log(original_URL.value)
    full_URL.textContent = original_URL.value
}

// e.preventDefault()
