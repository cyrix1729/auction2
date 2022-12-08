<script> // lang="ts"
    export default {
        props: ['userId'],
        data() {
            return {
                getResult: null,
            }
        },
        methods: {
            async getUsersQuestions() {
                
                try {
                    const res = await fetch(`http://localhost:8000/getUsersQuestions/${this.userId}/`, { method: "get"});
                    console.log("uwu");
                    if (!res.ok) {
                        const message = `An error has occured: ${res.status} - ${res.statusText}`;
                        throw new Error(message);
                    }
                    
                    const data = await res.json();
                    
                    console.log(data)
                    for (let x in data){
                        
                        for (let y in data){
                            console.log(data[x][y]);
                        }
                    }

                    this.getResult = data;

                } catch (err) {
                    this.getResult = err.message;
                    console.error(err);
                }
            },
        },

        created() {
            this.getUsersQuestions();
        },
    }
</script>


<template>
  <header>
    <div class="">
        <h1>Questions</h1>
        <div v-if="getResult" class="alert alert-secondary mt-2" role="alert">
        <div class="row" v-for="item in getResult">
          <div class="col-sm-12 text-center">
            <b class = "w-25 p-3">{{ item.question }}</b>
          </div>
          <div class="col-sm-12 text-center">
            <b v-if="item.answer" class = "w-25 p-3">{{ item.answer}}</b>
            <b v-else>This Question has not yet recieved a response</b>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>