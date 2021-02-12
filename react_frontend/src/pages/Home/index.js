import React, {useState} from 'react';

import './style.css';

import logo from '../../assets/img/SVG/Animacao.svg';

/*
 * Home component that returns the homepage of PetitLink
 */
export default function Home() {
    const [link, setLink] = useState('')
    const [short, setShort] = useState('')

    var pasteLink = ''

    /*
    * This function validates short-string
    */
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
                window.location = `/show/${response}`
            })
        } else {
            shortMessage.style.display = 'block'
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

    return(
        <main>
            <div className="side card">
                <img id="logo" src={logo} alt="logo"></img>
                <div id="slogan">Reduza o caminho, aumente os acessos!
                    <br/>
                    <h5><i>Insira uma URL longa e reduza com PetitLink</i></h5>
                </div>
                

                <div id="short-bar">
                    <div className="url-field">
                        <input
                            id="url-input"
                            placeholder="http://www.sitelongo.com.br/conteudo"
                            onChange={(el) => setLink(el.target.value)}
                            onSubmit={() => shortLinkRequest()}
                        />
                    </div>

                    <div className="url-field" id="short-field">
                        <input
                            placeholder="Apelido do link personalizado | petit.com/apelido"
                            onChange={(el) => setShort(el.target.value)}
                            onSubmit={() => shortLinkRequest()}
                        />
                    </div>
                    <p id="message-short">Digite outro apelido. O que você inseriu já existe</p>
                    <div className="left">
                        <input
                            id="short-check"
                            type="checkbox"
                            name="short-check"
                            onChange={() => showShortField()}
                        />
                        <label for="short-check">Personalizar Link</label>
                    </div>

                    <button id="short-btn" type="submit" onClick={() => shortLinkRequest()} >
                        Encolher!
                    </button>
                </div>
            </div>
        </main>
    )
}