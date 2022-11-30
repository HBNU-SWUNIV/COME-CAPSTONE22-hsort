<template>
    <v-app id="stuRegister" class="primary">
        <v-content>
            <v-container fluid full-height>
                <v-layout align-center justify-center>
                    <v-flex xs12 sm8 md4 lg4>
                        <v-card class="elevation-1 pa-3">
                            <v-card-text>
                                <v-text-field append-icon="person" name="stuNumber" label="학번 입력" type="text"
                                v-model="model.stuNumber"></v-text-field>
                                <v-text-field append-icon="person" name="stuName" label="이름 입력" type="text"
                                v-model="model.stuName"></v-text-field>
                                <v-text-field append-icon="person" name="username" label="아이디 입력" type="text"
                                v-model="model.username"></v-text-field>
                                <v-text-field append-icon="lock" name="password" label="비밀번호 입력" id="password" type="password"
                                v-model="model.password"></v-text-field>
                                <v-text-field append-icon="lock" name="stuPhone" label="전화번호 입력" type="text"
                                v-model="model.stuPhone"></v-text-field>
                                <v-text-field append-icon="lock" name="stuEmail" label="이메일 입력" type="text"
                                v-model="model.stuEmail"></v-text-field>
                                <input @change="upload" type="file" id="file" class="inputfile" /> 
                                <!-- <label for="file" class="input-plus">+</label> -->
                                <v-img :src="model.imageUrl" ></v-img>
                            </v-card-text>          
                            <v-card-actions>
                            <v-spacer></v-spacer> 
                                <v-btn block color="primary" @click="login" :loading="loading">뒤로</v-btn>
                                <v-btn block color="primary" @click="signUp" >다음</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
  import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
  import { getDatabase, ref, set } from "firebase/database";

  

  export default {
    layout: '/default',
    data: () => ({
      loading: false,
      model: {
        imageUrl: '',
        stuImage: '',
        stuNumber: '',
        stuName: '',
        stuPhone: '',
        stuEmail: '',
        username: '',
        password: '',
      }
    }),
    methods: {
      login() {
        this.loading = true;
        setTimeout(() => {
          this.$router.push('/login');
        }, 1000);
      },
       signUp() {
          const db = getDatabase();
          set(ref(db,'users/Student/' + this.model.username.split('@')[0]) , {
            Name : this.model.stuName,
            stuNumber : this.model.stuNumber,
            Phone : this.model.stuPhone,
            profile_image : this.model.imageUrl
          })

          //hash
          // const crypto = require('crypto');
          // const password = crypto.createHash('sha256').update(this.password).digest('base64');

          //Auth setting
          const auth = getAuth();
          createUserWithEmailAndPassword(auth, this.model.username, this.model.password)
          .then((userCredential) => {
          // Signed in
            const user = userCredential.user;
            console.log(user)
          // ...
          })
          .catch((error) => {
            const errorCode = error.code;
            console.log(errorCode)
            const errorMessage = error.message;
            console.log(errorMessage)
          // ..


          this.loading=true;
          setTimeout(() => {
          this.$router.push('/SuccessRegister');
          }, 1000);
          
          })


       },
        
        upload(e) { 
            let imageFile = e.target.files // 업로드한 파일의 데이터가 여기있음.
            console.log(imageFile[0])
            let url = URL.createObjectURL(imageFile[0]) // 파일의 필요한 데이터만을 url 변수에 넣음
            console.log(url) // 확인
            this.model.imageUrl = url // 미리 작성해둔 imageUrl : ' ' 변수에 가지고있는 경로데이터를 쳐넣음
        } 
    }
  };
  
</script>


<style scoped lang="css">
  #stuRegister {
    height: 50%;
    width: 100%;
    position: absolute;
    top: 0;
    left: 0;
    content: "";
    z-index: 0;
  }
</style>