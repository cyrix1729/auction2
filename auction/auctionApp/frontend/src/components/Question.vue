<script lang="ts">
    export default {
        props: ['questionId'],
        data() {
            return {
                getResult: null,
            }
        },
        methods: {
            async getQuestion() {
                
                try {
                    const res = await fetch(`http://localhost:8000/getQuestion/${this.questionId}`, { method: "get"});
                    if (!res.ok) {
                        const message = `An error has occured: ${res.status} - ${res.statusText}`;
                        throw new Error(message);
                    }
                    
                    const data = await res.json();

                    this.getResult = data;

                } catch (err) {
                    console.error(err);
                }
            },
        },

        created() {
            this.getQuestion();
        },
    }
</script>


<template>
  <header>
    <div class="">
        <div v-if="getResult" class="alert alert-secondary mt-2" role="alert">
            <div class="col-sm-12 text-center">
                <b class = "w-25 p-3">{{ getResult }}</b>
            </div>
        </div>
    </div>
  </header>
</template>