//디지털 시계
setInterval(myWatch, 1000)      //1초 간격으로 시간설정

function myWatch(){
    var date = new Date();
    var now = date.toLocaleTimeString();
    document.getElementById('display').innerHTML = now;
}