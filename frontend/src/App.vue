<script setup>
import { onMounted, ref } from 'vue'

onMounted( async()=>{  
  const response = await fetch('http://127.0.0.1:8000/get-csrf-token', {
        method: 'GET',
        credentials: 'include'  // This ensures cookies are sent with the request
    });
    console.log
    if (response.ok) {
        console.log("CSRF token set successfully.");
    } else {
        console.log("Failed to set CSRF token.");
    }    
})
</script>
<template>
  <router-view />
</template>
