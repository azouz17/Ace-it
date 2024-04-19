<script setup>
import router from '../router';
import { useUserStore } from "../Stores/userStore";
import { useChatStore } from '../stores/ChatStore';
import { useExpertStore } from '../Stores/ExpertStore'
import { logout } from '../authentication.js'
import Cookies from 'js-cookie';

const userStore = useUserStore()
const ChatStore = useChatStore()
const ExpertStore  = useExpertStore()

async function Logout (){        
  logout('Successfully logged out')
}
</script>
<template>
  <div class="w-screen max-w-full  items-center">
    <div class="bg-[#111010]  p-4 flex items-center w-full rounded-lg">
      <button @click="Logout" class="bg-white rounded font-bold p-2 hover:opacity-70">Logout</button>
      <div class="text-white text-2xl font-bold mx-auto">Ace-It!</div>
      <div class="flex items-baseline space-x-4">
        <button @click="router.push('/Edit')" class="bg-white rounded font-bold p-2 hover:opacity-70">Edit</button>
        <div class="text-white">Welcome, {{ userStore.first_name }}</div>
      </div>
    </div>
</div>
</template>



<style scoped>
</style>
