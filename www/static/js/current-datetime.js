function currentDate() {
    var date = new Date();
    var seperator1 = "-";
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    var strDate = date.getDate();
    if (month >= 1 && month <= 9) {
        month = "0" + month;
    }
    if (strDate >= 0 && strDate <= 9) {
        strDate = "0" + strDate;
    }
    var currentdate = year + seperator1 + month + seperator1 + strDate;
    return currentdate;
}

function expectedTime(offSetMinute) {
    var date = new Date();
    var seperator2 = ":";
    var hour = date.getHours()
    var minute = date.getMinutes()
    var totalMinute = hour * 60 + minute + offSetMinute;
    if (totalMinute < 0) {
        totalMinute = 0;
    }

    var expectedHour = Math.floor(totalMinute / 60);
    if (expectedHour >= 0 && expectedHour <= 9) {
        expectedHour = "0" + expectedHour;
    }

    var expectedMinute = totalMinute % 60;
    if (expectedMinute >= 0 && expectedMinute <= 9) {
        expectedMinute = "0" + expectedMinute;
    }
    
    return expectedHour+":"+expectedMinute;
}

document.getElementById("today").value = currentDate();
document.getElementById("anhourago").value = expectedTime(-60);
document.getElementById("rightnow").value = expectedTime(0);