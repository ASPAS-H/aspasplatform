let url = {
    url: "https://viacep.com.br/ws/",
    filled: false
}

function validateZIP() {
    let zip = document.getElementById("zipCode").value;
    console.log(zip)
    if (zip.length == 8) {
        if (url.filled == false) {
            url.url += zip + "/json";
            url.filled = true;
            updateAddress();
        }
    } else {
        url.url = "https://viacep.com.br/ws/",
            url.filled = false;
    }
}

function updateAddress() {
    fetch(url.url)
        .then(function (response) {
            response.json().then(function (data) {
                if (data) {
                    updateFields(data)
                }
            });
        })
        .catch(function (err) {
            console.error('Failed retrieving information', err);
        });
}

function updateFields(data) {
    document.querySelector('#address').value = data.logradouro;
    document.querySelector('#city').value = data.localidade;
    document.querySelector('#uf').value = data.uf
    document.querySelector('#vile').value = data.bairro;
}