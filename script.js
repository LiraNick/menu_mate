let daily = document.getElementById("daily-sells-page")
let monthly = document.getElementById("monthly-sells-page")
let yearly = document.getElementById("yearly-sells-page")

function changeToDaily(){
    daily.style.display="block";
    monthly.style.display="none";
    yearly.style.display="none";
}

function changeToMonthly(){
    monthly.style.display="block";
    daily.style.display="none";
    yearly.style.display="none";

}

function changeToYearly(){
    yearly.style.display="block";
    daily.style.display="none";
    monthly.style.display="none";
}