var form = document.getElementById("form");
var btns = document.getElementsByClassName("run");
var displayError = document.getElementById("error-message");

form.addEventListener("submit", function (e) {
    e.preventDefault();
})

for (var btn of btns) {
    btn.addEventListener("click", function () {
        var action = this.dataset.action;
        const file = form.filename.value;
        const extension = file.split(".")[1];

        // if (action === "play") {
        //     if (extension == "txt" || extension == "pdf") {
        //         readFile(file)
        //     } else {
        //         displayError.textContent = "Invalid file format";
        //     };
        // }
        if (action === "save") {
            if (extension == "txt" || extension == "pdf") {
                saveAudio(file)
            } else {
                displayError.textContent = "Invalid file format";
            };
        }
    })
}

// function readFile (file) {
//     fetch (read_file_url, {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//             "X-CSRFToken": csrftoken
//         },
//         body: JSON.stringify({"file": file})
//     })
//     .then(resp => resp.json())
//     .then(data => {
//         console.log(data);
//         form.filename.value = "";
//     })
//     .catch(error => {
//         alert(error);
//     })
// }

function saveAudio (file) {
    fetch (save_audio_url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify({"file": file})
    })
    .then(resp => resp.json())
    .then(data => {
        form.filename.value = "";
        alert(data);
    })
    .catch(error => {
        alert("An error occured");
    })
}
