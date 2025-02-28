

const decreaseBtn = document.getElementById("decreaseBtn");
const resetBtn = document.getElementById("resetBtn");
const increaseBtn = document.getElementById("increaseBtn");
const asd = document.getElementById("asd");
let count = 0;

 increaseBtn.onclick = function(){
    count++;
    asd.textContent = count;
 }


 decreaseBtn.onclick = function(){
    count--;
    asd.textContent = count;
 }


 resetBtn.onclick = function(){
    count = 0;
    asd.textContent = count;
 }


