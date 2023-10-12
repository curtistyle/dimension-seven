var input = document.getElementById("inputSearch");

input.addEventListener("keypress", function(event) {
    alert("asd")
    if (event.key === "Enter") {
        event.preventDefault();
        alert("asdasd")
    }
    });

