<template>
    <div>
        <h1>
            Edit Profile
        </h1>
        <form @submit = 'postData' method="post">
            Username: 
            <input required v-model= user.username  />
            <br>
            Email: 
            <input type = 'email' required v-model= user.email  />
            <br>
            Date of Birth: 
            <input type = 'Date' required v-model= user.DOB  />
            <br>
            <button @click="editData">Save</button>
        </form>



    </div>
    

</template>

<script lang="ts">
import Vue from 'vue'  
import axios from 'axios'
import VueAxios from 'vue-axios'

    export default {
        data(){
            return {
                user: [],
            }
        },
        created(){
            this.fetchUser()
        },

        methods: {
            async editData(e){
            e.preventDefault()   
            let payload = 
            console.log(payload)
            let response = await fetch(`http://127.0.0.1:8000/api/`, {
                method: 'PUT',
                headers: {
                'Content-Type': 'application/json', },
                body: JSON.stringify(payload)})
            },



            async fetchUser(){
                try{
                    let response = await fetch('http://127.0.0.1:8000/api/user',{
                    'credentials': "include",})
                    let data = await response.json()
                    this.user = data.cur_user_data
                    
                }
                    catch(error){
                        console.log(error)
                    }
                
            },

            async editTask(){
                try{
                   
                }
                catch(error){
                        console.log(error)
                    }
               
             },  
        }
    }

        

</script>