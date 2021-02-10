import React from 'react';
import './style.css';

export default function Home() {
    // const [url, setUrl] = useState('')

    function shrinkUrl() {
        var link = document.getElementById('url-field').value
        // var short = document.getElementById('short-field').value
        var short = ''

        fetch(`/add?url=${link}&short=${short}`, {
            'method': 'POST',
        }).then(res => res.json()).then(data => window.location = `/show/${data.response}`)
    }

    return(
        <main>
            
            <div id="short-bar">
                <input id="url-field"/>
                <button id="short-btn" onClick={() => shrinkUrl()} >
                    Encolher
                </button>
            </div>
        </main>
    )
}