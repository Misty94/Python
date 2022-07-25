// console.log("Hello There!"); <- It works!

// function apiResponse(response){
//     console.log(response);
// }

async function handleDogFormRequest(event){ // this event param will stop the page from reloading when you submit the form
    event.preventDefault();

    // console.log("Submitted the form!");
    
    const numberOfDogs = document.querySelector("#numberOfDogs").value; // the name of the id (if it was a class it would be .numberofDogs)
    // console.log(numberOfDogs);
    const URL = `https://dog.ceo/api/breeds/image/random/${numberOfDogs}`; // the backticks are like a f string in python
                //"https://dog.ceo/api/breeds/image/random/" + numberOfDogs = this is the same thing

                // console.log(URL)
    // const settings = {
    //     method : "GET",
    //     headers : {
    //         "Authorization" : ToKEN_GOES_HERE
    //     },
    //     body: JSON.stringify(data)
    // }
    const settings = {
        method : "GET"
    };

    // fetch(URL, settings)
    //     .then(apiResponse);   <- another way to do it with function apiResponse at the top
    
    // fetch(URL, settings)
    //     .then(function(response){
    //         console.log(response);
    //     });
        // .then()
        // .catch()
    const response = await fetch(URL, settings);
    const data = await response.json();
    console.log(data);

    const resultsDiv = document.querySelector(".results");
    resultsDiv.innerHTML = "";
    for(const image of data.message ){ // message is the array or list / from this list, grab the first element and do something with it (we're calling the element image)
        resultsDiv.innerHTML += `
        <div class="dogImageContainer">
            <img src="${image}" alt="Dog Image" class="dogImage"/>
        </div>
        `;
    }
}