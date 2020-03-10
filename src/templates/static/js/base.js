function shortenerGit() {
    window.location.replace("https://gitlab.com/pencillabs/encurtador-de-url");
}

function getRankOrShortener() {
    
    if (window.location == 'http://0.0.0.0:8000/') {
        window.location.replace('http://0.0.0.0:8000/rank/')
    }
    else {
        window.location.replace('http://0.0.0.0:8000/')
    }
}

var buttonRank = document.querySelector('#buttonRank')

if (window.location == 'http://0.0.0.0:8000/') {
    buttonRank.innerHTML = 'Rank dos mais acessados'
}
else if (window.location == 'http://0.0.0.0:8000/rank/') {
    buttonRank.innerHTML = 'Encurtar Links'
}