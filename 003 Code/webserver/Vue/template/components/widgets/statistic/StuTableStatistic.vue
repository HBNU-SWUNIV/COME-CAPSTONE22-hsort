<template>
        <v-card height="550" class="rounded-lg pa-0" outlined>
            <v-row no-gutters>
                <v-col v-for="n in 20" :key="n">
                    <v-btn 
                        v-if = 'data[n] != null'
                        color="red"
                        @dblclick="changeStuInfo"
                    >{{dbclickState ? changeStuid : data[n]}}</v-btn>
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

<script>

import { getDatabase, ref, onValue} from "firebase/database";


export default{
    data : () => ({
        data : data,
        changeStuid : "1",
        dbclickState : false
    }),
    methods : {
        changeStuInfo () {
            var changeStuid = prompt("학생의 학번을 입력해주세요");
            this.changeStuid = changeStuid;
            this.dbclickState = true;
        }
    },
    computed : {
        recentData : function() {
            const db = getDatabase();
            const ref = ref(db,'test')
            onValue(ref,(snapshot) => {
                this.data = snapshot.val();
                console.log(snapshot.val());
            })
            
        }
    }
}
</script>


<style>

</style>


    