<template>
    <v-app id="SuccessRegister" class="primary">
        <v-content>
            <v-container fluid full-height>
                <v-layout align-center justify-center>
                    <v-flex xs12 sm8 md4 lg4>
                        <v-card class="elevation-1 pa-3">
                            <div class="layout column align-center">
                            <img src="../static/m.png" alt="Vue Material Admin" width="120" height="120">
                            <h1 class="flex my-4 primary--text">출결관리시스템</h1>
                            <h2 class="flex my-4">회원가입이 완료되었습니다</h2>
                            </div>       
                            <v-card-actions>
                            <v-spacer></v-spacer> 
                                <v-btn block color="primary" @click="login" :loading="loading">홈으로</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
  

  

  export default {
    layout: '/default',
    data: () => ({
      loading: false,
    }),
    methods: {
      login() {
        this.loading = true;
        setTimeout(() => {
          this.$router.push('/login');
        }, 1000);
      },
    }
  };
  
</script>


<style scoped lang="css">
  #SuccessRegister {
    height: 50%;
    width: 100%;
    position: absolute;
    top: 0;
    left: 0;
    content: "";
    z-index: 0;
  }
</style>