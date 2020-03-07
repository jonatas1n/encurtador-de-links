
function encurtadorGit() {
    window.location.replace("https://gitlab.com/pencillabs/encurtador-de-url");
}


/*function formValidate() {
    let form = document.querySelector("#urlForm")
    if (!form.checkValidity()){
        let errorMessage    = document.querySelector("#messageError")
        
        errorMessage.style.display = "block"
        errorMessage.innerHTML = `<p> Não é possível encurtar. Verifique se está no formato certo <b>(http://...)</b> <p>`
        
        setTimeout(erroAppear, 1000*5)
        function erroAppear() {
            errorMessage.style.display = "none"
        }
    } else {
    }
}*/


$(document).ready( () =>{
    $("#urlForm").submit( e => {
        
        alert("LeoLindo")
        
        $.ajax({
            type:'POST',
            url: '',
            data: {
                url:$('#id_url').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(){
                alert('leo')
            }
        })
        
        e.preventDefault()
    })
})

