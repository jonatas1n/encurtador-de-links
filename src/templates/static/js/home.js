
function encurtadorGit() {
    window.location.replace("https://gitlab.com/pencillabs/encurtador-de-url");
}

var buttonForm = document.querySelector("#formButton")
buttonForm.addEventListener('click', formValidate)

function formValidate() {
    let form = document.querySelector("#urlForm")
    if (!form.checkValidity()){
        let errorMessage = document.querySelector("#messageError")
        
        errorMessage.style.display = "block"
        errorMessage.innerHTML = `<p> Não é possível encurtar. Verifique se está no formato certo <b>(http://...)</b> <p>`
        
        setTimeout(erroAppear, 1000*5)
        function erroAppear() {
            errorMessage.style.display = "none"
        }
    }
    
    let urlAlreadyExist = document.getElementsByClassName("errorlist")
    if(urlAlreadyExist){
        console.log("Leolindo")
    }
}

