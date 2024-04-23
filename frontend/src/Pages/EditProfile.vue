<script setup>
import { ref, onMounted } from 'vue'
import Cookies from 'js-cookie';
import { useUserStore } from "../Stores/userStore";
import { RouterView,useRouter, useRoute } from 'vue-router'
import Sidebar from '../Components/Sidebar.vue';
import Header from '../Components/Header.vue'
import { CheckLogin } from '../authentication';

const user = useUserStore()
const showform = ref(false)
const first_name = ref('')
const last_name = ref('')
const email = ref('')
const spinner = ref(false)
const error = ref(false)

async function forgotPassword(){
  CheckLogin()
  const userStore = useUserStore()
  try {
          const response = await fetch(`http://127.0.0.1:8000/forgotPassword`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application-json',
          },
          });
          if (response.ok) {
              window.location.href = "http://127.0.0.1:8000/accounts/password_reset/";
          }
          else{
              console.error('Request failed!');
          }
      }
          catch(error) {
              console.log(error);
          }
}

async function EditProfile(e){
    e.preventDefault()
    CheckLogin()
    spinner.value = true
    const userStore = useUserStore()
    error.value = false
    console.log(userStore.getId)
    console.log(userStore.getFirst_name)
    console.log(userStore.getLast_name)


  try {
          const response = await fetch(`http://127.0.0.1:8000/editProfile`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application-json',
              'X-CSRFToken': Cookies.get('csrftoken'),
          },
          credentials: 'include',
          body: JSON.stringify({
            user_id: userStore.id,
            first_name: first_name.value,
            last_name: last_name.value,
            email: email.value
          })
          });
          if (response.ok) {
              const jsonResponse = await response.json();
              console.log(jsonResponse)
              console.log('ok') 
              if(jsonResponse.status != 200){
                error.value = true
              }
              else{
                showform.value = false
                userStore.setUser(jsonResponse.first_name,jsonResponse.last_name,jsonResponse.email,jsonResponse.id)
              }
         }
          else{
              console.error('Request failed!');
          }
      }
          catch(error) {
              console.log(error);
          }
          spinner.value = false
          first_name.value = ''
          last_name.value = ''
          email.value = ''
}

</script>
<template>
    <div>
      <Header />
      <div class="flex flex-row mt-4">
        <Sidebar class="basis-1/4 "/>
            <div class="basis-4/5 ml-8 items-center mt-6">       
                <div class=" flex justify-center items-center flex-col">
                    <div class="bg-white shadow-md rounded-lg p-8 w-1/2 max-w-md">
                        <h1 class="text-2xl font-bold mb-4">Profile Information</h1>
                        <div class="mb-4">
                            <label class="inputLabel">First Name:</label>
                            <p class="text-gray-800">{{ user.first_name }}</p>
                        </div>
                        <div class="mb-4">
                            <label class="inputLabel">Last Name:</label>
                            <p class="text-gray-800">{{ user.last_name }}</p>
                        </div>
                        <div class="mb-4">
                            <label class="inputLabel">Email:</label>
                            <p class="text-gray-800">{{ user.email }}</p>
                        </div>
                    </div>
                    <button v-if="!showform" @click="showform = true" class="buttonStyle mt-4 p-2">Edit Profile</button>
                    <p class="italic mt-2"> Change your password via this link <span class="underline text-blue-400" @click="forgotPassword">here.</span>You will be logged out</p>
                    <form v-if="showform" class="bg-white shadow-md rounded-lg p-8 max-w-md mt-4 w-1/2" :onsubmit="EditProfile">
                        <h1 class="text-2xl font-bold mb-4">Edit Profile</h1>
                        <div class="mb-4">
                            <label for="firstName" class="inputLabel">First Name:</label>
                            <input required id="firstName" type="text" v-model="first_name" class="inputStyle">
                        </div>
                        <div class="mb-4">
                            <label for="lastName" class="inputLabel">Last Name:</label>
                            <input required id="lastName" type="text" v-model="last_name" class="inputStyle">
                        </div>
                        <div class="mb-4">
                            <label for="email" class="inputLabel">Email:</label>
                            <input required id="email" type="email" v-model="email"  class="inputStyle">
                        </div>
                        <p v-if="error" class="error">Email Already Exists</p>
                        <div class="flex justify-between w-1/2 mx-auto">
                            <button type="submit" class="buttonStyle p-2">
                                <p>Save Changes</p>
                                <img v-if="spinner" src="../assets/spinner.png" width="20" height="20" class="animate-spin ml-2 mt-0.5">
                            </button>
                            <button @click="showform = false" type="submit" class="buttonStyle p-2">Close</button>
                        </div>
                    </form>
            </div>
        </div>
      </div>

    </div>
</template>