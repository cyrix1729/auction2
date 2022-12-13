<template>
    <div><button @click="fetchListings">Fetch Listings</button>
      <div>
        <ul v-if="active">
            <p v-for="i in 4" :key="i">
            Description: {{ items.item[i].desc }}
            Start Time: {{ items.item[i].start_time }}
            End Time: {{ items.item[i].end_time }}
            Starting Price: {{ items.item[i].start_price }}
            Current Price: {{ items.item[i].cur_price }}
            
            
            </p>
            
           
        </ul> 
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import Vue from 'vue';
    export default {
        data(){
            return {
                items: [] ,
                active: false,
            }
        },
  
        methods: {
            // numberOfItems(itemsX){
            //     return itemsX.length
            // },

            async fetchListings(){
                try{
                    let response = await fetch('http://localhost:8000/api/listings/')
                    let data = await response.json()
                    this.items = data
                    console.log(this.items)
                    this.active = true;
                }
                    catch(error){
                        console.log(error)
                    }
  
            }
  
        }
      }
  
  </script>