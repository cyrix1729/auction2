<script setup> // lang="ts"
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import HelloWorld from './components/HelloWorld.vue'
import AllQuestionsVue from './components/AllQuestions.vue';
</script>

<script> // lang="ts"
    export default {
        name: "App",
        data() {
            return {
                userId: 1,
                itemId: 1,
                questionId: 1,
            }
        },

        methods: {
            fortmatResponse(data) {
                var items = []
                for (let x in data){
                    for (let y in data[x]){
                        items.push(data[x][y]);
                    }
                }
                return items;
            },

            async getQuestion(){
                try {
                    const res = await fetch(`http://localhost:8000/auctionApp/getQuestion/${questionId}`, { method: "get"});
                    
                    if (!res.ok) {
                        const message = `An error has occured: ${res.status} - ${res.statusText}`;
                        throw new Error(message);
                    }

                    const data = await res.json();

                    this.getResult = this.fortmatResponse(data);

                } catch (err) {
                    this.getResult = err.message;
                }
            },

            async getItemQuestions(){
                try {
                    const res = await fetch(`http://localhost:8000/auctionApp/getItemQuestions/${itemId}`, { method: "get"});
                    
                    if (!res.ok) {
                        const message = `An error has occured: ${res.status} - ${res.statusText}`;
                        throw new Error(message);
                    }

                    const data = await res.json();

                    this.getResult = this.fortmatResponse(data);

                } catch (err) {
                    this.getResult = err.message;
                }
            },

            async postQuestion(){
                const postData = {
                    question: this.$refs.post_question.value,
                }

                try {
                    const res = await fetch(`http://localhost:8000/auctionApp/postQuestion/${itemId}/${userId}`, 
                        { method: "post", headers: {"Content-Type": "application/json"}, 
                        body : JSON.stringify(postData)
                    });
                    
                    if (!res.ok) {
                        const message = `An error has occured: ${res.status} - ${res.statusText}`;
                        throw new Error(message);
                    }

                    const data = await res.json();

                    const result = {
                        status: res.status + "-" + res.statusText,
                        headers: {
                            "Content-Type": res.headers.get("Content-Type"),
                            "Content-Length": res.headers.get("Content-Length"),
                        },
                        data: data,
                    };
                    this.getResult = this.fortmatResponse(result);

                } catch (err) {
                    this.getResult = err.message;
                }
            },

            async postAnswer(){
                const postData = {
                    answer: this.$refs.post_answer.value,
                }

                try {
                    const res = await fetch(`http://localhost:8000/auctionApp/postAnswer/${questionId}`, 
                        { method: "post", headers: {"Content-Type": "application/json"}, 
                        body : JSON.stringify(postData)
                    });
                    
                    if (!res.ok) {
                        const message = `An error has occured: ${res.status} - ${res.statusText}`;
                        throw new Error(message);
                    }

                    const data = await res.json();

                    const result = {
                        status: res.status + "-" + res.statusText,
                        headers: {
                            "Content-Type": res.headers.get("Content-Type"),
                            "Content-Length": res.headers.get("Content-Length"),
                        },
                        data: data,
                    };
                    this.getResult = this.fortmatResponse(result);

                } catch (err) {
                    this.getResult = err.message;
                }
            },
        }
    }
</script>

<template>
  <div>
    <AllQuestionsVue v-bind:userId="userId"/>
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
