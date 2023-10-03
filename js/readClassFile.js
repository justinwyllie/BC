const fs = require('fs');
let filename = "D:\\Data\\clients\\screen4\\tutorials\\python\\Class4B.txt";

//this just slurps it in
fs.readFile(filename, 'utf8', function(err, data) {
if (err) throw err;
    console.log(data);
});
    


    

   