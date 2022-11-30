import { initializeApp } from "firebase/app";
import { getDatabase, ref, child, get } from "firebase/database";
import { spawn } from "child_process";
import * as https from 'https';
import * as fs from "fs"
import * as cors from "cors"



// import  express  from 'express';
// const appExpress = express();
// import { createServer } from 'http';
// const serverExpress = createServer(appExpress);
// import { Server } from "socket.io";
// const io = new Server(serverExpress);

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAatvBlwakTQauxOkYIr509Q-kFt9FXda8",
  authDomain: "capstone-5857b.firebaseapp.com",
  databaseURL: "https://capstone-5857b-default-rtdb.firebaseio.com",
  projectId: "capstone-5857b",
  storageBucket: "capstone-5857b.appspot.com",
  messagingSenderId: "470841439165",
  appId: "1:470841439165:web:dbbf210810784a4a6718d4",
  measurementId: "G-PLXJSQJTGT"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const dbRef = ref(getDatabase());


const hostname = "127.0.0.1" 
const port = 3001 


// const result_01 = spawn('python',['track.py','--source','test.mp4','--max-id','16'],);
// result_01.stdout.on('data', function(data) {
//   console.log(data.toString());
// }); 

const options = {
  key: fs.readFileSync('rootca.key'),
  cert: fs.readFileSync('rootca.crt'),
};


// 서버를 만든다
const server = https.createServer(options,(req, res) => {
    
//   요청이 오면 실행되는 콜백 함수
    get(child(dbRef, `testf`)).then((snapshot) => {
        if (snapshot.exists()) {
        console.log(snapshot.val());
        var data = snapshot.toJSON()
        res.statusCode = 200 
        res.setHeader("Access-Control-Allow-Origin", "*");
        res.setHeader("Content-Type", "application/json") 
        let datalen = Object.keys(data).length
        console.log(Object.keys(data)[0].toString())
        console.log(data[Object.keys(data)[0].toString()]['id'])
        console,console.log('datalen : ',datalen);
        var cnt = 0
        for (var i=0;i<datalen;i++){
          console.log("test")
          var key = Object.keys(data)[cnt].toString()
          if (data[key]['id'] == 0){
            console.log("test2")
            delete data[key]
          }else {
            cnt += 1
          }
        }
        res.end(JSON.stringify(data,null,3)) 
        // fs.writeFileSync('/Users/kimgyujin/Desktop/Attendence_stu_3/template/static/data/data.json',stuData)
        } else {
        console.log("No data available");
        }
        }).catch((error) => {
        console.error(error);
    });
    
})


// //소켓 통신
// io.on('connection', (socket) => {
//   console.log("connected")

//   socket.on("ID", (arg) => {
//       console.log("id: " + arg); // arg: rfid에서 보낸 id
//       id = arg;
//   })
// });

// 서버를 요청 대기 상태로 만든다
server.listen(port, hostname, () => {
  // 요청 대기가 완료되면 실행되는 콜백 함수
  // 터미널에 로그를 기록한다
  console.log(`Server running at https://${hostname}:${port}/`)
})



