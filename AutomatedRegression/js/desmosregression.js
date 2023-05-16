function getRSquaredValue(elements) {
    var find = null;
    for (var i = 0; i < elements.length; i++) {

        if (elements[i].innerHTML.search("\"R\"") >= 0) {
            find = elements[i];
            break;
        }

    }
    if (find == null) {
        return "Not found!";
    }
    else {
        var content = find.innerHTML;
        var index = content.search("equals");

        var rawstring = content.substring(index + 6);
        rawstring = rawstring.replaceAll(" ", "");
        if (rawstring.search("negative") != -1) {
            return rawstring.replace("negative", "-");
        }
        return rawstring;
    }
}

function getVariable(elements, variable) {
    var find = null;
    for (var i = 0; i < elements.length; i++) {
        if (elements[i].innerHTML.search("\"" + variable + "\"") >= 0) {
            find = elements[i];
            break;
        }
    }
    if (find == null) {
        return "Not found!";
    }
    else {
        var content = find.innerHTML;
        var index = content.search("equals");
        var rawstring = content.substring(index + 6);
        rawstring = rawstring.replaceAll(" ", "")
        if (rawstring.search("negative") != -1) {
            return rawstring.replace("negative", "-");
        }
        return rawstring;
    }
}
function rafAsync() {
    return new Promise(resolve => {
        requestAnimationFrame(resolve); //faster than set time out
    });
}

function checkElement(selector) {
    if (document.querySelector(selector) === null) {
        return rafAsync().then(() => checkElement(selector));
    } else {
        return Promise.resolve(true);
    }
}


function getRegressionValues(comp, rate) {
    var ret = "";
    checkElement(".dcg-regression-container").then
        ((element) => {
            console.log("In here");
            var elements = document.getElementsByClassName("dcg-mq-mathspeak");
            var r2 = getRSquaredValue(elements);
            var C = getVariable(elements, "C");
            if(C=="Not found!")
            {
                C="0";
            }
            var n = getVariable(elements, "n");
            var SP = getVariable(elements, "S");
            var L = getVariable(elements, "L");
            var reg = new RegFunction(r2, L, C, n, SP, comp, rate);
            ret = reg.toString();
            document.getElementById('stringy').value = ret;
            document.getElementById("CLICKME").click(); 
            return ret; 
        }
        );

}



