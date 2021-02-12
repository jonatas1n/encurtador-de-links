import React, { useState, useEffect } from 'react'
import { useParams } from "react-router-dom"
import podium from '../../assets/img/2x/podium.png';
import chevronLeft from '../../assets/img/SVG/chevron-left-solid.svg';
import './style.css';

//This page is responsible for show to user the shortened generated link 
export default function ShowLink() {
    const [rank, setRank] = useState([])
    
    let { link } = useParams();

    useEffect(() => {fetch(`/rank`, {'method': 'GET'})
        .then(res => res.json())
        .then(({ status, response }) => {
            if(status === 'success') {
                setRank(response)
            }
        })
    }, [])
    
    return(
        <main>
            <div className="side">
                <div id="back">
                    <a href="http://localhost:8880/">
                        <img id="back-btn" src={chevronLeft}/> Encurtar uma nova URL
                    </a>
                </div>
                <div className="card">
                    <h2>Este é o seu novo link:</h2>
                    <h2 id="link">
                        <a href={`/${link}`}>
                            {`petit.com/${link}`}
                        </a>
                    </h2>
                    <br/>
                    <h3>Menor tamanho,<br/> Maior Alcance.</h3>
                </div>
                <div id="ranking">
                    <h2>Links mais acessados</h2>
                    <table>
                        <thead>
                            <th></th>
                            <th>Endereço Original</th>
                            <th>Novo Link</th>
                            <th>Acessos</th>
                        </thead>
                        <tbody>
                            {rank.map((elem, it) => {
                                return (
                                    <tr>
                                        <td>{it+1})</td>
                                        <td>{(elem[0])}</td>
                                        <td><a href={'http://localhost:8880/' + elem[2]}>petit.com/{elem[2]}</a></td>
                                        <td>{elem[1]}</td>
                                    </tr>
                                )
                            })}
                        </tbody>
                    </table>
                </div>
            </div>
            <img src={podium} id="podium-img" alt="podium"/>
        </main>
    )
}