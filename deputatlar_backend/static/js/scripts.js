let com = document.getElementById("comment")
let btn = document.getElementById("tkbtn")
let exit = document.getElementById("tkexit")


btn.addEventListener("click", function show() {
    com.style.display = "block";
});

exit.addEventListener("click", function hide() {
    com.style.display = "none";
})