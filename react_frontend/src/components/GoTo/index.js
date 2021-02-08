import { useParams, useHistory } from "react-router-dom"

export default function GoTo() {
    let { short } = useParams()
    let history = useHistory()
    
    fetch(`/redirect?link=${short}`, {'method': 'POST'})
    .then(res => res.json())
    .then(({ status, response }) => {
        if(status === 'success') {
            window.location = 'http://' + response
        } else {
            history.push('/not-found/')
        }
    })

    return(
        <h1>Aguarde</h1>
    )
}