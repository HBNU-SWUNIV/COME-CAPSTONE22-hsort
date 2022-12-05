<template>
  <v-app id="selectRegister" class="primary">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4 lg4>
            <v-card class="elevation-1 pa-3">
              <v-card-actions>
                <v-row align="center">
                <v-btn x-large width="100" height="150" color="primary" @click="stuRegister" :loading="loading">학생</v-btn>
                <v-btn x-large width="100" height="150" color="primary" @click="proRegister" :loading="loading">교수</v-btn>
                </v-row>
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
  layout: 'defalut',
  data: () => ({
    loading: false,
  }),

  methods: {
    stuRegister() {
        this.loading = true;
        setTimeout(() => {
            this.$router.push('/stuRegister');
        }, 1000);
    },
    proRegister() {
        this.loading = true;
        setTimeout(() => {
            this.$router.push('/proRegister');
        }, 1000);
    }
  }
};
</script>


<style scoped lang="css">
  #selectRegister {
    height: 50%;
    width: 100%;
    position: absolute;
    top: 0;
    left: 0;
    content: "";
    z-index: 0;
  }
</style>
