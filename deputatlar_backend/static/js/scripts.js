let com = document.getElementById("comment")
let btn = document.getElementById("tkbtn")
let exit = document.getElementById("tkexit")


btn.addEventListener("click", function show() {
    com.style.display = "block";
});

exit.addEventListener("click", function hide() {
    com.style.display = "none";
})

//function click

function click(map, nav){
    map.style.visibility = "visible";
    nav.classList.add("active");
}

// Navigate ids
let nav1, nav2, nav3, nav4

nav1 = document.getElementById("nav1")
nav2 = document.getElementById("nav2")
nav3 = document.getElementById("nav3")
nav4 = document.getElementById("nav4")

// Maps ids

let map1, map2, map3, map4, map5

map1 = document.getElementById("map1")
map2 = document.getElementById("map2")
map3 = document.getElementById("map3")
map4 = document.getElementById("map4")
map5 = document.getElementById("map5")

function addClass(nav){
    nav.classList.add("active");
}

function removeClass(nav){
    nav.classList.remove("active");
}

nav1.addEventListener("click", function(){
    nav1.classList.add("active")
    nav2.classList.remove("active")
    nav3.classList.remove("active")
    nav4.classList.remove("active")
    map1.style.display = "block";
})

nav2.addEventListener("click", function(){
    nav2.classList.add("active")
    nav1.classList.remove("active")
    nav3.classList.remove("active")
    nav4.classList.remove("active")
    map1.style.display = "none";
    map2.style.display = "block";
})
nav3.addEventListener("click", function(){
    nav3.classList.add("active")
    nav2.classList.remove("active")
    nav1.classList.remove("active")
    nav4.classList.remove("active")
    map1.style.display = "none";
    map2.style.display = "none";
    map3.style.display = "block";
})

nav4.addEventListener("click", function(){
    nav4.classList.add("active")
    nav1.classList.remove("active")
    nav3.classList.remove("active")
    nav2.classList.remove("active")
    map1.style.display = "none";
    map2.style.display = "none";
    map3.style.display = "none";
    map4.style.display = "block";
})