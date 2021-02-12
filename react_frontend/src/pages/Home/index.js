import React, {useState} from 'react';

import './style.css';

import logo from '../../assets/img/SVG/Animacao.svg';
import paste from '../../assets/img/SVG/paste-solid.svg';

/*
 * Home component that returns the homepage of PetitLink
 */
export default function Home() {
    const [link, setLink] = useState('')
    const [short, setShort] = useState('')

    var pasteLink = ''

    function shortValidate(){
        if(short == '') return true

        fetch(`/check?short=${short}`, {
            'method': 'POST',
        }).then(res => res.json()).then(({status, response}) => {
            if(status === 'sucess'){
                return false
            }
            return true
        })
    }

    /*
    * This function makes the request to the API for a shortened link from a URL
    */
    function shortLinkRequest() {
        var shortMessage = document.getElementById('message-short')

        shortMessage.style.display = 'none'

        if(shortValidate()){
            fetch(`/add?url=${link}&short=${short}`, {
                'method': 'POST',
            }).then(res => res.json()).then(({status, response}) => {
                if(status === 'error'){
                    window.location = `/show/${response}/exist`
                } else {
                    window.location = `/show/${response}`
                }
            })
        } else {
            shortMessage.style.display = 'block'
        }
    }

    /*
    * This function validates an url
    * @param {String} url - url to validate
    */
    function validURL(url) {
        var pattern = new RegExp('^(https?:\\/\\/)?'+ 
            '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ 
            '((\\d{1,3}\\.){3}\\d{1,3}))'+ 
            '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ 
            '(\\?[;&a-z\\d%_.~+=-]*)?'+ 
            '(\\#[-a-z\\d_]*)?$','i'); 
        return !!pattern.test(url);
    }

    /*
    * This function check URL validation and shows Shrink Button to user
    */
    function showShrinkBtn(){
        var element = document.querySelector('.url-field input')
        var button = document.getElementById('short-btn')

        if(validURL(element.value)){
            button.style.display = 'block'
        } else {
            button.style.display = 'none'
        }
    }

    /*
    * Function that shows short-string field when checkbox is checked
    */
    function showShortField(){
        var elem = document.getElementById('short-check')
        var shortElem = document.getElementById('short-field')

        if(elem.checked){
            shortElem.style.display = 'block'
        } else {
            shortElem.style.display = 'none'
        }
    }

    navigator.clipboard.readText()
    .then(text => {
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
                <div id="slogan">Reduza o caminho, aumente os acessos!
                    <br/>
                    <h5><i>Insira uma URL muito longa e reduza com PetitLink</i></h5>
                </div>
                

                <div id="short-bar">
                    <div class="url-field">
                        <input
                            id="url-input"
                            placeholder="http://www.sitelongo.com.br/conteudo"
                            onChange={(el) => {setLink(el.target.value); showShrinkBtn()}}
                            onSubmit={() => shortLinkRequest()}
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
                            onChange={(el) => setShort(el.target.value)}
                            onSubmit={() => shortLinkRequest()}
                        />
                    </div>
                    <p id="message-short">Digite outro apelido. O que você inseriu já existe</p>
                    <div class="left">
                        <input
                            id="short-check"
                            type="checkbox"
                            name="short-check"
                            onChange={() => showShortField()}
                        />
                        <label for="short-check">Personalizar Link</label>
                    </div>

                    <button id="short-btn" onClick={() => shortLinkRequest()} >
                        Encolher Link
                    </button>
                </div>
            </div>
        </main>
    )
}