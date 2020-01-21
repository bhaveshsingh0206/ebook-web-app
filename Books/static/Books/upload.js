
var upload = document.querySelector("#upload");
upload.addEventListener('click',function(){
    console.log("Uplod clicked");
    var buttons = document.querySelectorAll(".off");
    buttons.forEach(function (i) {
        i.style.display = 'none'
    });
});


var close = document.querySelector(".close");
close.addEventListener('click',function(){
    console.log("Uplod clicked");
    var buttons = document.querySelectorAll(".off");
    buttons.forEach(function (i) {
        i.style.display = 'inline-block'
    });
});