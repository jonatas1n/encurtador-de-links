import React, {useState} from 'react';
import './style.css';
import logo from '../../assets/img/SVG/Animacao.svg';
import paste from '../../assets/img/SVG/paste-solid.svg';

export default function Home() {
    const [link, setLink] = useState('')
    const [short, setShort] = useState('')

    var pasteLink = ''

    function shrinkUrl() {
        fetch(`/add?url=${link}&short=${short}`, {
            'method': 'POST',
        }).then(res => res.json()).then(({status, response}) => {
            if(status == 'error'){
                window.location = `/show/${response}/exist`
            } else {
                window.location = `/show/${response}`
            }
        })
    }

    function validURL(str) {
        var pattern = new RegExp('^(https?:\\/\\/)?'+ 
            '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ 
            '((\\d{1,3}\\.){3}\\d{1,3}))'+ 
            '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ 
            '(\\?[;&a-z\\d%_.~+=-]*)?'+ 
            '(\\#[-a-z\\d_]*)?$','i'); 
        return !!pattern.test(str);
    } 

    function showButton(){
        var element = document.querySelector('.url-field input')
        var button = document.getElementById('short-btn')

        if(validURL(element.value)){
            button.style.display = 'block'
        } else {
            button.style.display = 'none'
        }
    }

    function showShort(){
        var elem = document.getElementById('short-check')
        var shortElem = document.getElementById('short-field')

        if(elem.checked){
            shortElem.style.display = 'block'
        } else {
            shortElem.style.display = 'none'
        }
    }

    navigator.clipboard.readText().then(text => {
        var pasteBtn = document.getElementById('paste-btn')

        if(validURL(text)){
            pasteBtn.style.display = 'block'
            pasteLink = text
        }
    })

    return(
        <main>
            <div class="side card">
                <img id="logo" src={logo} alt="logo"></img>
                <div id="subtitle">Reduza o caminho, aumente os acessos!</div>
                <div id="short-bar">
                    <div class="url-field">
                        <input
                            id="url-input"
                            placeholder="http://www.sitelongo.com.br/conteudo"
                            onChange={(e) => {setLink(e.target.value); showButton()}}
                            onSubmit={() => shrinkUrl()}
                        />
                        <button id="paste-btn">
                            <img id="paste-icon"
                                src={paste}
                                onClick={() => {
                                    var urlInput = document.getElementById('url-input');
                                    urlInput.value = pasteLink
                                }}
                                alt="paste-icon"
                            />
                        </button>
                    </div>

                    <div class="url-field" id="short-field">
                        <input
                            placeholder="Apelido do link personalizado | petit.com/apelido"
                            onChange={(e) => setShort(e.target.value)}
                            onSubmit={() => shrinkUrl()}
                        />
                    </div>
                    <div>
                        <input id="short-check" type="checkbox" name="short-check" onChange={() => showShort()}/>
                        <label for="short-check">Personalizar Link</label>
                    </div>

                    <button id="short-btn" onClick={() => shrinkUrl()} >
                        Encolher Link
                    </button>
                </div>
            </div>
        </main>
    )
}