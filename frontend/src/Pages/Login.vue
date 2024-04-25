<script setup>
import { RouterView,useRouter, useRoute } from 'vue-router'
import { onMounted, ref } from 'vue'
import Cookies from 'js-cookie';
import { useUserStore } from "../Stores/userStore";
import { useAuthStore } from '../stores/authStore';
import { logout } from '../authentication.js'

const username = ref('')
const password = ref('')
const error = ref(false)
const router = useRouter()
const route = useRoute()
const spinner = ref(false)
const AuthStore = useAuthStore()

onMounted( async()=>{  
    Cookies.remove('session') 
    logout(AuthStore.logoutMessage)    
})

async function forgotPassword(){
  try {
          const response = await fetch(`http://127.0.0.1:8000/forgotPassword`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application-json',
          },
          });
          if (response.ok) {
              window.location.href = "http://127.0.0.1:8000/accounts/password_reset/";
              console.log(jsonResponse)
          }
          else{
              console.error('Request failed!');
          }
      }
          catch(error) {
              console.log(error);
          }
}

async function login(){

  const userStore = useUserStore()
  spinner.value  = true
  try {
          const response = await fetch(`http://127.0.0.1:8000/`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application-json',
              'X-CSRFToken': Cookies.get('csrftoken'),
          },
          credentials: 'include',
          body: JSON.stringify({
            username: username.value.toLowerCase(),
            password: password.value,
          }),
          });
          if (response.ok) {
              const jsonResponse = await response.json();
              if(jsonResponse.status == 200){
                userStore.setUser(jsonResponse.first_name,jsonResponse.last_name,jsonResponse.email,jsonResponse.id)
                error.value = false
                const expirationTime = new Date(Date.now() + jsonResponse.timeout*1000); 
                const expirationUTCString = expirationTime.toUTCString();
                document.cookie = `session=active; expires=${expirationUTCString}; path=/;`
                AuthStore.clearLogoutMessage()
                router.push('/Home')
              }
              else{
                error.value = true
              }
              console.log(jsonResponse)
          }
          else{
              console.error('Request failed!');
          }
      }
          catch(error) {
              console.log(error);
          }
          spinner.value  = false
}
</script>

<template>
  <div class="w-64 mt-24">
    <span class="text-lg text-red-500">{{ AuthStore.logoutMessage }}</span>
    <p class="text-3xl mb-4">Login</p>
    <p v-if="error" class="error">Please ensure login credentials are valid</p>
    <div class="flex flex-col bg-white p-4 rounded border border-grey text-left">
      <p class="mb-2">Email:</p>
      <input type="text" class="border border-black rounded p-1" v-model="username">
      <p class="mb-2">Password:</p>
      <input type="password" class="border border-black rounded p-1" v-model="password">
    </div>
    <button @click="forgotPassword()" class="underline text-blue-400 italic mt-2">Forgot Password</button>
    <button class="bg-[#99C8C2] w-1/2 rounded p-2 mx-auto mt-4 hover:opacity-70 items-center flex justify-center" @click="login">
        <p>Login</p>
        <img v-if="spinner" src="../assets/spinner.png" width="20" height="20" class="animate-spin ml-2 mt-0.5">
    </button>
    <p> Dont have an Account ?</p>
    <router-link class="underline" to="/signup">
          Sign Up
    </router-link>
  </div>
</template>

<style scoped>

</style>
