<script setup>
import router from '../router';
import { useUserStore } from "../Stores/userStore";

    const userStore = useUserStore()

    function logout() {
      // Implement your logout logic here
      console.log("Logged out");
      router.push('/')
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
