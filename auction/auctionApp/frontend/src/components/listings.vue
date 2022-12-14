<template>
      <div>
        <ul v-if="active">
            <h1>Listings</h1> 
            <button> Profile </button>
            <input required placeholder= 'search' />
            <p v-for = "element in items.item">
            Description: {{ element.desc }}<br>
            Start Time: {{ element.start_time }}<br>
            End Time: {{ element.end_time }}<br>
            Starting Price: {{ element.start_price }}<br>
            Current Price: {{ element.cur_price }} <br>
            <div v-if="element.seller[0].id == this.userId">
                <PostQuestion v-bind:itemId="element.id" v-bind:userId="element.id"/>
            </div>
            
        </p>
        </ul> 
      </div>
  </template>
  
  <script lang="ts">
  import Vue from 'vue';
import PostQuestion from './postQuestion.vue';
    export default {
    data() {
        return {
            userId: null,
            items: [],
            active: false,
        };
    },
    created() {
        this.fetchListings();
    },
    methods: {
        async fetchListings() {
            try {
                let response = await fetch("http://localhost:8000/api/listings/", {
                    "credentials": "include",
                });
                let data = await response.json();
                this.items = data;
                console.log(data);
                this.active = true;
            }
            catch (error) {
                console.log(error);
            }
        }
    },
    components: { PostQuestion }
}
  
  </script>