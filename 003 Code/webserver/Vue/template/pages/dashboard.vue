<template>
  <div id="pageDashboard">
    <v-container grid-list-xl fluid>
      <v-layout row wrap>
        <!-- mini statistic start -->
        <v-flex lg3 sm6 xs12>
          <mini-statistic
            v-bind:text="stuNum"
            title="총원"
            sub-title="Attendence"
            color="indigo"
          >
          </mini-statistic>
        </v-flex>
        <v-flex lg3 sm6 xs12>
          <mini-statistic
            v-bind:text="(Object.keys(data).length).toString()"
            title="출석"
            sub-title="Absence"
            color="red"
          >
          </mini-statistic>
        </v-flex> 
        <v-flex lg3 sm6 xs12>
          <mini-statistic
            v-bind:text="stuNum-Object.keys(data).length"
            title="지각"
            sub-title="late"
            color="light-blue"
          >
          </mini-statistic>
        </v-flex>
        <v-flex lg3 sm6 xs12>
          <mini-statistic
            text="1"
            title="지각"
            sub-title="Count"
            color="purple"
          >
          </mini-statistic>
        </v-flex>

    
      <!-- Attendancd stu  -->
      <!-- <v-btn
      @click="getStuInfo">
        Run
      </v-btn> -->
        
          <v-flex lg8 sm12 xs12>
            <template>
              <!-- <v-btn>{{inputTime}}</v-btn> -->
                    <v-card height="550" class="rounded-lg pa-0" outlined>
                        <v-row no-gutters>
                            <v-col v-for="n in 3" :key="n" >
                                <v-btn 
                                    v-if = "data['seat'+n] != null "
                                    color= 'light-blue lighten-4'
                                >
                                  <v-btn 
                                  rounded
                                  block
                                  x-large
                                  color="primary">
                                  {{data['seat'+ n]['id']}}
                                </v-btn>
                                
                              </v-btn>
                                <v-btn                         
                                    v-else color="light-blue lighten-4"
                                >
                                </v-btn>
                                <v-responsive
                                    v-if="n % 5 == 0"
                                    :key="`width-${n}`"
                                    width="100%"
                                ></v-responsive>
                            </v-col>
                        </v-row>
                    </v-card>
            </template>
          </v-flex>
<!-- 
              <v-flex lg4 sm12 xs12>
              <profile-card></profile-card>
              </v-flex> -->
      
            
          
        
      <!-- Attendancd stu  end -->
            

        <!-- mini statistic  end -->
        <!-- <v-flex lg8 sm12 xs12>
          <v-widget title="월별 통게" content-bg="white">
            <v-btn icon slot="widget-header-action">
              <v-icon class="text--secondary">refresh</v-icon>
            </v-btn>
            <div slot="widget-content">
              <e-chart
                :path-option="[
                  ['dataset.source', siteTrafficData],
                  ['color', [color.lightBlue.base, color.green.lighten1]],
                  ['legend.show', true],
                  ['xAxis.axisLabel.show', true],
                  ['yAxis.axisLabel.show', true],
                  ['grid.left', '2%'],
                  ['grid.bottom', '5%'],
                  ['grid.right', '3%'],
                  ['series[0].type', 'bar'],
                  ['series[0].areaStyle', {}],
                  ['series[0].smooth', true],
                  ['series[1].smooth', true],
                  ['series[1].type', 'bar'],
                  ['series[1].areaStyle', {}],
                ]"
                height="400px"
                width="85%"
              >
              </e-chart>
            </div>
          </v-widget>
        </v-flex>
        <v-flex lg4 sm12 xs12>
          <v-widget title="출결상황" content-bg="white">
            <div slot="widget-content">
              <e-chart
                :path-option="[
                  ['dataset.source', locationData],
                  ['legend.bottom', '0'],
                  ['color', [color.lightBlue.base, color.indigo.base, color.pink.base, color.green.base, color.cyan.base, color.teal.base]],
                  ['xAxis.show', false],
                  ['yAxis.show', false],
                  ['series[0].type', 'pie'],
                  ['series[0].avoidLabelOverlap', true],
                  ['series[0].radius', ['50%', '70%']],
                ]"
                height="400px"
                width="100%"
              >
              </e-chart>
            </div>
          </v-widget>
        </v-flex>
  -->
        
 

        <!-- Circle statistic -->
<!--         
        <v-flex lg4 sm12 xs12 v-for="(item,index) in trending" :key="'c-trending'+index">
          <circle-statistic
            :title="item.subheading"
            :sub-title="item.headline"
            :caption="item.caption"
            :icon="item.icon.label"
            :color="item.linear.color"
            :value="item.linear.value"
          >
          </circle-statistic>
        </v-flex> -->
        <!-- acitivity/chat widget -->
        
        <!-- <v-flex lg6 sm12 xs12>
          <chat-window height="308px"></chat-window>
        </v-flex>
        <v-flex lg6 sm12 xs12>
          <v-widget title="Activities" contentBg="white">
            <div slot="widget-content">
              <ol class="timeline timeline-activity timeline-point-sm timeline-content-right">
                <li class="timeline-block" v-for="(item, index) in activity" :key="index">
                  <div class="timeline-point">
                    <v-circle dot large :color="item.color"></v-circle>
                  </div>
                  <div class="timeline-content">
                    <time datetime="2018" class="subheading">{{item.timeString}}</time>
                    <div class="py-2 text--secondary" v-html="item.text"></div>
                  </div>
                </li>
              </ol>
            </div>
          </v-widget>
        </v-flex>
         -->
        
      </v-layout>
    </v-container>
  </div>
</template>






<script>
  import axios from 'axios';
  import Server from '@/api/app'
  import API from '@/api';
  import EChart from '@/components/chart/echart';
  import MiniStatistic from '@/components/widgets/statistic/MiniStatistic';
  import PostListCard from '@/components/widgets/card/PostListCard';
  import ProfileCard from '@/components/widgets/card/ProfileCard';
  import PostSingleCard from '@/components/widgets/card/PostSingleCard';
  import WeatherCard from '@/components/widgets/card/WeatherCard';
  import VWidget from '@/components/VWidget';
  import Material from 'vuetify/es5/util/colors';
  import VCircle from '@/components/circle/VCircle';
  import ChatWindow from '@/components/chat/ChatWindow';
  import CircleStatistic from '@/components/widgets/statistic/CircleStatistic';
  import LinearStatistic from '@/components/widgets/statistic/LinearStatistic';
  import data from '@/static/data/data.json'
  import StuTableStatistic from '@/components/widgets/statistic/StuTableStatistic'
import object from 'lodash/object';
  
  

  

  export default {
    layout: 'dashboard',
    components: {
      VWidget,
      MiniStatistic,
      ChatWindow,
      VCircle,
      WeatherCard,
      PostSingleCard,
      PostListCard,
      ProfileCard,
      EChart,
      CircleStatistic,
      LinearStatistic,
      StuTableStatistic,
    },
    data: () => ({
      absenceNum : '',
      stuNum: 3,
      color: Material,
      data : [],
      selectedTab: 'tab-1',
      inputTime : '',
      clickState : false,
      connectionCnt : '',
      cnt: '',
      attendanceNum: '',
      linearTrending: [
        {
          subheading: 'Sales',
          headline: '2,55',
          caption: 'increase',
          percent: 15,
          icon: {
            label: 'trending_up',
            color: 'success'
          },
          linear: {
            value: 15,
            color: 'success'
          }
        },
        {
          subheading: 'Revenue',
          headline: '6,553',
          caption: 'increase',
          percent: 10,
          icon: {
            label: 'trending_down',
            color: 'error'
          },
          linear: {
            value: 15,
            color: 'error'
          }
        },
        {
          subheading: 'Orders',
          headline: '5,00',
          caption: 'increase',
          percent: 50,
          icon: {
            label: 'arrow_upward',
            color: 'info'
          },
          linear: {
            value: 50,
            color: 'info'
          }
        }
      ],
      trending: [
        {
          subheading: 'Email',
          headline: '15+',
          caption: 'email opens',
          percent: 15,
          icon: {
            label: 'email',
            color: 'info'
          },
          linear: {
            value: 15,
            color: 'info'
          }
        },
        {
          subheading: 'Tasks',
          headline: '90%',
          caption: 'tasks completed.',
          percent: 90,
          icon: {
            label: 'list',
            color: 'primary'
          },
          linear: {
            value: 90,
            color: 'success'
          }
        },
        {
          subheading: 'Issues',
          headline: '100%',
          caption: 'issues fixed.',
          percent: 100,
          icon: {
            label: 'bug_report',
            color: 'primary'
          },
          linear: {
            value: 100,
            color: 'error'
          }
        },
      ]
    }),
    methods : {
      AttendanceNum() {
        var cnt = 0
        for(let i=1;i == Object.keys(this.data).length;i++){
          if(parseInt(this.data['seat'+i]['id']) > 0 ){
            cnt += 1
          }
        }
        return cnt
      },
      getStuInfo() {
        const axios = require("axios")
        this.inputTime = prompt("출석 시간을 입력해주세요")
        this.dbclickState = true;
        const currentTime = new Date()
        const CurrentHour = currentTime.getHours()
        const CurrentMin = currentTime.getMinutes()
        const CurrentSec = currentTime.getSeconds()
        this.connectionCnt = Math.floor((((3600 * this.inputTime) - (3600 * CurrentHour + 60 * CurrentMin + CurrentSec)) /5))
        // if (this.connectionCnt > 0 ){
        //   console.log(this.connectionCnt)
        //   timeRequest(this.connectionCnt)
        //   function timeRequest(num){
        //     for(let i = 0; i < num; i++){
        //       setTimeout(function() {
        //         this.getRes()
        //       }, 5000 * (i + 1))
        //     }
        //   }
        // }else{
        //   alert('현재시각보다 크게 입력해주세요')
        // }
      },
      getRes(){
            axios
              .get('https://127.0.0.1:3001').then(res=>
              {
                // let data = JSON.stringify(res.data,null,3)
                
                this.data = res.data

                // delete this.data['seat1']
                console.log(this.data)
              })

          },
      count(){
        this.cnt += 1
      },
      timeloop(){
        let interval = setInterval(this.getRes,5000)
        let cnt = setInterval(this.count,5000)
        console.log(this.data)
        // if (this.cnt == 5){
        //   clearInterval(interval)
        //   clearInterval(cnt)
        //   console.log(this.cnt)
        // }
      }
    },
    computed: {
      // activity () {
      //   return API.getActivity();
      // },
      // stuStatus(){
      //   return Server.getStudentStatus;
      // },
      posts () {
        return API.getPost(3);
      },
      siteTrafficData () {
        return API.getMonthVisit;
      },
      locationData () {
        return API.getLocation;
      },
      AttendanceData() {
        return Object.keys(data).length;
      },
    },
    mounted (){
        this.getStuInfo()
        this.timeloop()
        clearInterval(this.timeloop(),5000*3)
        
    }

  };
</script>

<style scroped>
@media (min-width: 1281px) {
  .theme--light.v-btn:not(.v-btn--icon):not(.v-btn--flat){
  width: 140px;
  height: 120px;
}
}

@media (orientation: portrait) {
	/* Portrait 모드일 때 적용할 CSS */
  @media (max-width: 767px) and (max-width: 1023px) {
  .theme--light.v-btn:not(.v-btn--icon):not(.v-btn--flat){
  width: 100px;
  height: 120px;
  }
} 
}

@media (orientation: landscape) {
  .theme--light.v-btn:not(.v-btn--icon):not(.v-btn--flat){
  width: 40px;
  height: 120px;
  }
}




</style>
