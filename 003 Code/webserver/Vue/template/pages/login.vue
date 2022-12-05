<template>
  <v-app id="login" class="primary">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4 lg4>
            <v-card class="elevation-1 pa-3">
              <v-card-text>
                <div class="layout column align-center">
                  <img src="../static/m.png" alt="Vue Material Admin" width="120" height="120">
                  <h1 class="flex my-4 primary--text">출결관리시스템</h1>
                </div>

                <v-form>
                  <v-text-field append-icon="person" name="login" label="Login" type="text"
                                v-model="model.username"></v-text-field>
                  <v-text-field append-icon="lock" name="password" label="Password" id="password" type="password"
                                v-model="model.password"></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer> 
                <v-btn block color="primary" @click="userRegister" :loading="loading">회원가입</v-btn>
                <v-btn block color="primary" @click="login" :loading="loading">로그인</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";



  export default {
    layout: 'default',
    data: () => ({
      loading: false,
      radios : 'selectStu',
      model: {
        username: '',
        password: '',
      }
    }),

    methods: {

      login() {
        const auth = getAuth();

        //hash
        // const crypto = require('crypto');
        // const password = crypto.createHash('sha256').update(this.password).digest('base64');

        signInWithEmailAndPassword(auth,this.model.username, this.model.password)
        .then((userCredential) => {
        // Signed in 
        const user = userCredential.user;
        setTimeout(() => {
          this.$router.push('/dashboard');
        }, 1000);
        // ...
        })
        .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        });

        console.log(this.radios)
        
      },
      
      userRegister() {
        this.loading = true;
        setTimeout(() => {
          this.$router.push('/UserRegister');
        }, 1000);
      },
    }

  };
</script>



<style scoped lang="css">
  #login {
    height: 50%;
    width: 100%;
    position: absolute;
    top: 0;
    left: 0;
    content: "";
    z-index: 0;
  }
</style>
