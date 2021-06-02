
function mostra(id){

    if (id == 'pix'){
        document.getElementById(id).style.display = 'block';
        document.getElementById('ted').style.display = 'none';
    }
    else if (id == 'ted'){
        document.getElementById(id).style.display = 'block';
        document.getElementById('pix').style.display = 'none';
    }

    else{
        document.getElementById('pix').style.display = 'none';
        document.getElementById('ted').style.display = 'none';
    }
                
}