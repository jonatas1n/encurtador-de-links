import React, { useState, useEffect } from 'react'
import { useParams } from "react-router-dom"

export default function ShowLink() {
    const [rank, setRank] = useState([])
    
    let { link } = useParams();

    useEffect(() =>{
        fetch(`/rank`, {'method': 'GET'})
        .then(res => res.json())
        .then(({ status, response }) => {
            if(status === 'success') {
                setRank(response)
            }
        })
    })

    
    return(
        <main>
            <h2>
                Este é o seu novo link:
                <a href={`http://localhost:3000/${link}`}>
                    <br/>
                    {`http://localhost:3000/${link}`}
                </a>
            </h2>

            <h2>Ranking:</h2>
            <ol>
                {console.log(rank)}
                {rank.map((elem) => {
                    return <li>{elem[0]} -> <a href={'localhost:3000/' + elem[2]}>localhost:3000/{elem[2]}</a> | {elem[1]} acessos</li>
                })}
            </ol>
        </main>
    )
}