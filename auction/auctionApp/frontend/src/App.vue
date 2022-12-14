<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import listings from './components/listings.vue'
import AllQuestionsVue from './components/AllQuestions.vue';
import postQuestion from './components/postQuestion.vue';
import AnswerVue from './components/Answer.vue';
import QuestionVue from './components/Question.vue';
import PostItem from './components/postItem.vue';
import GetItem from './components/getItem.vue';
import GetQuestionsOnItems from './components/GetQuestionsOnItems.vue';
</script>

<template>
  <div>
    <listings/>
 

  </div>

</template>-



<!--
This is what I was using to test my parts. If you need to understand any of it just let me know. -Steph


<script lang="ts">
    export default {
    name: "App",
    data() {
        return {
            userId: 1,
            itemId: 1,
            questionId: 1,
            AnswerActive: false,
            QuestionActive: false,
            PostQuestionActive: false,
        };
    },
    methods: {
        showQuestion() {
            this.QuestionActive = !this.QuestionActive;
        },
        showAnswer() {
            this.AnswerActive = !this.AnswerActive;
        },
        showPostQuestion() {
            this.PostQuestionActive = !this.PostQuestionActive;
        },
    },
    components: { PostItem, GetQuestionsOnItems }
}
</script>

<template>
  <div>
    <AllQuestionsVue v-bind:userId="userId"/>
    <div>
        <button @click="showQuestion">show question</button>
        <button @click="showPostQuestion">show question response</button>
    </div>
    <div>
        <QuestionVue v-bind:questionId="questionId" v-if="QuestionActive"/>
        <postQuestion v-bind:itemId="itemId" v-bind:userId="userId" v-if="PostQuestionActive"/>
        <PostItem v-bind:userId="userId"/>

        <GetQuestionsOnItems v-bind:userId="userId"/>
    </div>
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
</style>-->