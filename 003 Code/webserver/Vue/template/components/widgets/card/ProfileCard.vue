<template>
  <v-card>
    <v-img :src="require('../../../static/people/man/'+imgName)" height="400">
      <v-layout column class="media ma-0">
        <v-card-title>
          <v-btn dark icon>
            <v-icon>chevron_left</v-icon>
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn dark icon>
            <v-icon>more_vert</v-icon>
          </v-btn>
        </v-card-title>
        <v-spacer></v-spacer>
      </v-layout>
    </v-img>
    <v-list two-line class="pa-0">
      <v-list-tile href="#">
        <v-list-tile-action>
          <v-icon color="indigo">phone</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>{{Phone}}</v-list-tile-title>
          <v-list-tile-sub-title>Mobile</v-list-tile-sub-title>
        </v-list-tile-content>
        <v-list-tile-action>
          <v-icon>chat</v-icon>
        </v-list-tile-action>
      </v-list-tile>
      
      <v-divider inset></v-divider>
      <v-list-tile href="#">
        <v-list-tile-action>
          <v-icon color="indigo">person</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>{{stuName}}</v-list-tile-title>
          <v-list-tile-sub-title>Personal</v-list-tile-sub-title>
        </v-list-tile-content>
      </v-list-tile>
      <v-divider inset></v-divider>
    </v-list>
  </v-card>   
</template>

<script>
import VWidget from '../../VWidget.vue';
export default {
  data : () => ({
    imgName: "m1.jpg",
    stuName : "김규진",
    Phone : "010-2234-0289",
  }),
  components: { VWidget },

  
};
</script>
