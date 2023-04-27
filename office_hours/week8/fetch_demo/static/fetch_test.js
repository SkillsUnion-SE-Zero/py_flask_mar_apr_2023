console.log("Testing....");

function fetchFromFlask(e) {
    console.log("Button clicked");
    fetch("http://localhost:5000/fetch", {method: "GET"})
        .then(response => response.json()) // => is an arrow function
        .then(json_data => {
            console.log(json_data);
            let containerDiv = document.getElementById("fetch-container");
            containerDiv.replaceChildren(); // Clear out everything inside the div
            // Create new HTML elements
            let nameTag = document.createElement("p");
            nameTag.innerText = "Name: " + json_data["name"];
            let messageTag = document.createElement("p");
            messageTag.innerText = "Message: " + json_data["message"];
            containerDiv.appendChild(nameTag);
            containerDiv.appendChild(messageTag);
        })
        .catch(err => console.log(err));
}