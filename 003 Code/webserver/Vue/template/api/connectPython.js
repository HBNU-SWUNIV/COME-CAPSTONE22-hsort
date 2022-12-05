const  spawn  = require('child_process').spawn; 
const result_01 = spawn('python3',['test.py'],);
var output = [];
var outputs = [];

result_01.stdout.on('data', function(data) {
     console.log(data.toString());
}); 

result_01.stdout.on('exit',function() {
     console.log('exit');
});

module.exports = result_01