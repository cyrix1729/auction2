<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import listings from './components/listings.vue'
import AllQuestionsVue from './components/AllQuestions.vue';
import QuestionVue from './components/Question.vue';
import PostItem from './components/postItem.vue';
import GetQuestionsOnItems from './components/GetQuestionsOnItems.vue';
</script>


<!--This is what I was using to test my parts. If you need to understand any of it just let me know. -Steph-->
<script lang="ts">
    export default {
    name: "App",
    data() {
      //place holder values for the functions I used. These will be changed once stuff is added to the main listings page.
        return {
            userId: 1,
            itemId: 1,
            questionId: 1,
        };
    }
}
</script>

<template>
  <listings/>
  <div>
    <AllQuestionsVue v-bind:userId="userId"/>
    <div>
        <QuestionVue v-bind:questionId="questionId"/>
        <PostItem v-bind:userId="userId"/>

        <GetQuestionsOnItems v-bind:userId="userId"/>
    </div>
  </div>
</template>
