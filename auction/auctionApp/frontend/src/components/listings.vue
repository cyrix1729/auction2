<template>
      <div class="modal-body row">
        <ul v-if="active" class="col-sm">
            <h1>Listings</h1> 
            <p v-for = "element in items.item">
                Description: {{ element.desc }}<br>
                Start Time: {{ element.start_time }}<br>
                End Time: {{ element.end_time }}<br>
                Starting Price: {{ element.start_price }}<br>
                Current Price: {{ element.cur_price }} <br>
                <button v-on:click="displayItem(element.id, element.seller[0].id)">
                    SHOW ITEM
                </button>
            </p>
            <div v-if="items.item.length <= 0">
                <b>There is no listing related to {{searchData}}</b>
            </div>
        </ul> 
        <div v-if="showItem" class="col-sm-5">
            <GetItem v-bind:itemId="itemToDisplay" :key="componentKey"/>
            <Question v-bind:itemId="itemToDisplay" :key="componentKey"/>
            <Bid v-bind:itemId="itemToDisplay" :key="componentKey"/>
        </div>
      </div>
</template>
  
<script lang="ts">
import Vue from 'vue';
import Bid from './Bid.vue';
import GetItem from './getItem.vue';
import PostQuestion from './postQuestion.vue';
import Question from './Question.vue';
export default {
    props: ['searchData'],
    data() {
        return {
            items: [],
            active: false,
            showItem: false,
            itemToDisplay: 0,
            componentKey: 0,
        };
    },
    created() {
        this.fetchListings();
    },
    methods: {
        async fetchListings() {
            try {
                let response = await fetch(`http://localhost:8000/api/listings/${this.searchData}`, {
                    "credentials": "include",
                });
                let data = await response.json();
                this.items = data;
                this.active = true;
                console.log(data);
            }
            catch (error) {
                console.log(error);
            }
        },
        displayItem (item_id : number, seller_id : number){
            this.itemToDisplay = item_id;
            if (this.showItem == false){
                this.showItem = !this.showItem;
            }
            else{
                console.log("forcing reload")
                this.forceRerender();
            }
        },
        forceRerender() {
            this.componentKey += 1;
        },
    },
    components: { PostQuestion, GetItem, Question, Bid }
}
  
  </script>