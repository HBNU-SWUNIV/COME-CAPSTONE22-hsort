<template>
    <v-app id="setQrcode" class="primary">
        <v-content>
            <v-container fluid full-height>
                <v-layout align-center justify-center>
                    <v-flex xs12 sm8 md4 lg4>
                        <v-card class="elevation-1 pa-3">
                            <qr-code-vue :value="value"></qr-code-vue>
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
    
    components: {
        QrcodeVue,
    },
    value : "http://naver.com",
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
  #setQrcode {
    height: 50%;
    width: 100%;
    position: absolute;
    top: 0;
    left: 0;
    content: "";
    z-index: 0;
  }
</style>