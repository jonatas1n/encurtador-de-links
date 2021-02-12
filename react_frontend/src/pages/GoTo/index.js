import { useParams, useHistory } from "react-router-dom"
import {useEffect} from 'react'

export default function GoTo() {
    let { short } = useParams()
    let history = useHistory()
    
    useEffect( () => fetch(`/redirect?link=${short}`, {'method': 'POST'})
    .then(res => res.json())
    .then(({ status, response }) => {
        if(status === 'success') {
            window.location = 'http://' + response
        } else {
            history.push('/not-found/')
        }
    }))

    return(
        <main>
            <h1>Aguarde</h1>
        </main>
    )
}