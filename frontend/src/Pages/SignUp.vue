<script setup>
import { RouterView,useRouter, useRoute } from 'vue-router'
import { ref } from 'vue'
import Cookies from 'js-cookie';
import { useUserStore } from "../Stores/userStore";

const error = ref('Please ensure login credentials are valid')
const Firstname = ref('')
const Lastname = ref('')
const password = ref('')
const email = ref('')
const displayerror = ref(false)
const spinner = ref(false)
const router = useRouter()
const route = useRoute()

function validatefields(){
  return (Firstname.value && Lastname.value && password.value && email.value)
}


async function Signup(){
 if(validatefields())
{
  spinner.value  = true
try {
  const userStore = useUserStore()
         const response = await fetch(`http://127.0.0.1:8000/signup`, {
         method: 'POST',
         headers: {
             'Content-Type': 'application-json',
             'X-CSRFToken': Cookies.get('csrftoken'),
         },
         credentials: 'include',
         body: JSON.stringify({
           first_name: Firstname.value,
           last_name: Lastname.value,
           email: email.value.toLowerCase(),
           password: password.value,
         }),
         });
         if (response.ok) {
             const jsonResponse = await response.json();
             if(jsonResponse.status == 200){
               userStore.setUser(jsonResponse.first_name,jsonResponse.last_name,jsonResponse.email,jsonResponse.id)
               displayerror.value = false
               const expirationTime = new Date(Date.now() + jsonResponse.timeout*1000); 
               const expirationUTCString = expirationTime.toUTCString();
               document.cookie = `session=active; expires=${expirationUTCString}; path=/;`
               router.push('/Home')
             }
             else{
               error.value = 'Email Already Exists'
               displayerror.value = true
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
else{
  displayerror.value = true
  error.value = 'please ensure all fields not empty'
}
}

</script>

<template>
  <div class="w-64 mt-24">
    <p class="text-3xl mb-4">Sign Up</p>
    <p v-if="displayerror" class="text-red-500 p-2 mt-4 font-bold italic">{{ error }}</p>
    <div class="flex flex-col bg-white p-4 rounded border border-grey text-left">
      <p class="mb-2">First Name:</p>
      <input v-model="Firstname" type="text" class="border border-black rounded p-1">
      <p class="mb-2">Last Name:</p>
      <input v-model="Lastname" type="text" class="border border-black rounded p-1">
      <p class="mb-2">Password:</p>
      <input v-model="password" type="password" class="border border-black rounded p-1">
      <p class="mb-2">Email:</p>
      <input v-model="email" type="email" class="border border-black rounded p-1">
    </div>
    <button class="bg-[#99C8C2] w-1/2 rounded p-2 mx-auto mt-4 hover:opacity-70 items-center flex justify-center" @click="Signup">
        <p>Sign up</p>
        <img v-if="spinner" src="../assets/spinner.png" width="20" height="20" class="animate-spin ml-2 mt-0.5">
    </button>
    <router-view></router-view>
  </div>
</template>

<style scoped>

</style>
