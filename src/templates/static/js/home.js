

function formValidate() {
    let form = document.querySelector("#urlForm")
    if (!form.checkValidity()){
        let errorMessage    = document.querySelector("#messageError")
        
        errorMessage.style.display = "block"
        errorMessage.innerHTML = `<p> Não é possível encurtar. Verifique se está no formato certo <b>(http://...)</b> <p>`
        
        setTimeout(erroAppear, 1000*5)
        function erroAppear() {
            errorMessage.style.display = "none"
        }
    }
}


$(document).ready( () =>{
    
    let forms       = document.querySelector("#contentForms")
    let result      = document.querySelector("#contentResult")
    let urlInput    = document.querySelector("#id_url")

    $("#urlForm").submit( e => {
        
        $.ajax({
            type:'POST',
            url: '/',
            data: {
                url:$('#id_url').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(json){
                let html_link = document.querySelector('#link-base')
                let html_short_url = document.querySelector('#link-result')

                forms.className     = 'animation-forms' 
                result.className    = 'normal-result'
                urlInput.className  = 'animation-input'
                
                html_link.innerHTML = json.link
                html_short_url.innerHTML = json.short_url
                html_short_url.href = json.short_code
            },
        })
        
        e.preventDefault()
    })

    $("#id_url").focus( () => {
        if(forms.className == 'animation-forms'){
            forms.className    = 'back-forms' 
        }
        if(result.className == 'normal-result'){
            result.className   = 'without-result'
        }
        if(urlInput.className == 'animation-input'){
            document.querySelector("#id_url").className  = 'back-input'
        }
    })

})
