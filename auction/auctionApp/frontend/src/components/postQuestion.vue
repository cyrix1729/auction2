<script lang="ts">
import { defineComponent, ref } from 'vue';
    export default {
        props: ['itemId', 'userId'],
        data() {
            return {
                getResult: null,
            }
        },
        methods: {
            async postQuestion() {
                const postData = {
                    userId: this.userId,
                    question: (this.$refs.post_question as any).value,
                }
                try {
                    console.log(JSON.stringify(postData))
                    if (postData.question) {
                        console.warn("uwu");
                        const res = await fetch(`http://localhost:8000/postQuestion/${this.itemId}`, { 
                            method: "post", headers: {
                                "Content-Type": "application/json"
                            }, 
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

                        console.log(data)
                        console.log(result);

                        this.getResult = data;
                    }
                    else {console.warn("question is empty");}

                } catch (err) {
                    console.error(err);
                }
            },
        },
    }
</script>


<template>
  <header>
    <div class="">
        <b>please post your question</b>
        <form id="postQuestion" action="">
            <div class="form-group">
                <input class="form-control" type="text" name="name" ref="post_question" placeholder="put your question here" required/>
            </div>
            <div class="form-group">
                <button class="btn btn-primary" @click="postQuestion">SUBMIT</button>
            </div>
        </form>
      </div>
  </header>
</template>