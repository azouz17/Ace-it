<script setup>
import router from '../router';
import { useUserStore } from "../Stores/userStore";
import Cookies from 'js-cookie';

    const userStore = useUserStore()
async function logout (){        
    try{
        const response = await fetch('http://127.0.0.1:8000/logout', {
            method:'POST',
            headers:{
                'Content-Type': 'application-json',
                'X-CSRFToken': Cookies.get('csrftoken'), 
            } ,
            credentials: 'include',
        })
        if(response.ok){
          if(response.status == 200)
            console.log("logged out")
            //userStore.emptyUser()
            router.push('/')
        }
    }
    catch(error){
        console.log(error)
    }
}
</script>
<template>
  <div class="w-screen max-w-full  items-center">
    <div class="bg-[#111010]  p-4 flex items-center w-full rounded-lg">
      <div class="text-white text-2xl font-bold mx-auto">Ace-It!</div>
      <div class="flex items-baseline space-x-4">
        <button @click="logout" class="bg-white rounded font-bold p-2 hover:opacity-70">Logout</button>
        <div class="text-white">Welcome, {{ userStore.first_name }}</div>
      </div>
    </div>
</div>
</template>



<style scoped>
</style>
