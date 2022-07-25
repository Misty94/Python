function apiResponse(response){
    return response.json();
}

function loadImage(data){
    const data = await response.json();
    const resultsDiv = document.querySelector(".results");
    resultsDiv.innerHTML = "";

    for(const image of data.message){
        resultsDiv.innerHTML += `
        <div class="dogImageContainer">
            <img src="${image}" alt="Dog Image" class="dogImage"/>
        </div>
        `;
    }
}

function alternativeFetch(){
    fetch(URL, settings)
        .then(apiResponse)
        .then(loadImage)
}

// OR

function alternativeFetch(){
    fetch(URL, settings)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            const resultsDiv = document.querySelector(".results");
            resultsDiv.innerHTML = "";
        
            for(const image of data.message){
                resultsDiv.innerHTML += `
                <div class="dogImageContainer">
                    <img src="${image}" alt="Dog Image" class="dogImage"/>
                </div>
                `;
            }
        })
}