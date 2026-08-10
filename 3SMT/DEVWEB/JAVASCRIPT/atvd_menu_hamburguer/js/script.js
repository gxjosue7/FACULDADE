const button = document.querySelector("header button")
const home = document.querySelector("header nav ul")

button.addEventListener("click", function() {
    if (home.style.height == home.scrollHeight + "px") {
        home.style.height = "0px"
    } else {
        home.style.height = home.scrollHeight + "px"
    }
})