/**
 * Created by A35863 on 2015-09-08.
 */
var count=60;
var counter = setInterval(timer, 1000);
function timer()
{
    count=count-1;
    if (count<=0){
        clearInterval(counter);
        window.setTimeout('window.location.reload()');
        return;
    }
    document.getElementById("timer").innerHTML=count + " secs";
}
