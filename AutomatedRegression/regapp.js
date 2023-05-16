var express = require('express');
var fs = require('fs');
const { dirname } = require('path');
var app = express();

function writeToFile(filepath, content) {
    fs.appendFile(filepath, content+"\n", function (err) {
        if (err) {
            console.log(err);
        }
    });
}

console.log("Got here!");
app.get('/',function(req,res) {
    res.sendFile(__dirname +"/html/"+ 'regression.html');
  });
app.use(express.urlencoded({extended: true}));
app.use("/js", express.static('./js/'));
app.post('/sendparams',function(req, res) {
writeToFile("data/regressionresults/model6.csv",req.body.name);
  });


app.listen(8080, function() {
    console.log('Server running at http://127.0.0.1:8080/');
  });