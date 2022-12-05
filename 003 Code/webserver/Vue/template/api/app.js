
// var createError = require('http-errors');
// var express = require('express');
// var path = require('path');
// var cookieParser = require('cookie-parser');
// var logger = require('morgan');
//var indexRouter = require('../api/index');
// var usersRouter = require('../api/users');

//connect express
// var app = express();

// view engine setup
/*
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'dist')));

app.use('/', indexRouter);
app.use('/users', usersRouter);
*/



const https = require("https")

const cors = require("cors")({
  origin : true
})


const options = {
  hostname: '127.0.0.1',
  port: 3000,
};


// const req = https.get(options, res => {
//   cors(res,req,() => {
//     var body = ""
//     console.log(res.data);
//     console.log(`statusCode: ${res.statusCode}`);
//     res.on('data', d => {
//       body += d;
//     });
//     res.on('end',function() {
//       try{
//         let json = JSON.parse(body)
//         console.log(json)   
//       }catch(error){
//         console.error(error.massage)
//       }
//     });
//   })
  

// });

// req.on('error', error => {
//   console.error(error);
// });

// req.end();


const axios = require('axios');





  axios
    .get('34.64.215.205')
    .then(res => {
      console.log(`statusCode: ${res.status}`);
      console.log(res.data);
      var stuStatus = JSON.stringify(res.data);
      const data = JSON.parse(stuStatus)
      console.log(data)
    })
    .catch(error => {
      console.error(error);
    });


    // async sequentialRequest(num) {
    //   const arr = ['첫번째','두번째','세번째','네번째']
    //   for (let i = 0; i < arr.length; i++) {
    //     try {
    //       // (3)
    //       await this.getRes(arr[i])
    //     } catch (err) {
    //       // (4)
    //       console.log(err)
    //     }
    //   }
    // }
    
    // getRes(num) {
    //   return new Promise((resolve, reject) => {
    //     this.axios.post("api주소",{ num })  // api주소, body에 보낼 값 위에서 받은 num[i]값
    //       .then(() => {
    //         // (1) 정상적인 응답이 왔을때 
    //         resolve("compleate")
    //       })
    //       .catch(() => {
    //         // (2) 정상적인 응답을 받지 못했을때 
    //         reject("network err")
    //       })
    //   })
    // }

/*
var io = require("socket.io")

io.on('connection', (socket) => {
  console.log("connected")

  socket.on("data", (arg) => {
      id = arg;
      console.log("id: " + arg); // arg: 자바(안드로이드)에서 보낸 데이터
  });
});
*/

/*
app.post('/test',function(req, res, next) {
  return res.send(id);
})
*/

/*
const result_0 = require('./connectPython');

result_01.stdout.on('data', function(data) {
  console.log(data.toString());
});

result_01.stdout.on('exit', function(data) {
  console.log('exit');
  res.send('exit')
  result_01.kill();
}); 
*/

/*
var spawn =require('child_process').spawn
ls = spawn('ls',['-a']);
ls.stdout.on('data', function(data) { 
  console.log('stdout:'+ data);
})
*/


// catch 404 and forward to error handler
/*
app.use(function(req, res, next) {
  next(createError(404));
});
*/

console.log("아라라라라라라ㅏㄹ릴요");
console.log("아라라라라라라ㅏㄹ릴요");
console.log("아라라라라라라ㅏㄹ릴요");









// error handler

/*
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});
*/



export default{
  // getStudentStatus : getHeaders('http://127.0.0.1:3001').then(res => {JSON.stringify(res.data)})
}

// module.exports = app;
