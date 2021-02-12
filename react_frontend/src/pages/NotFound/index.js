import React from 'react';
import Logo from '../../assets/img/2x/Logotipo@2x.png';

export default function NotFound() {
    return(
        <div className="card">
            <img src={Logo}></img>
            <h2>Essa página não foi encontrada. Tente novamente...</h2>
            <a href="http://localhost:8880/">Ir para o PetitLink</a>
        </div>
    )
}