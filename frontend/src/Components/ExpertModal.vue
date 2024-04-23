<script setup>
import { ref, onMounted } from 'vue'
import Cookies from 'js-cookie';
import { useUserStore } from "../Stores/userStore";
import { RouterView,useRouter, useRoute } from 'vue-router'
import { CheckLogin } from '../authentication';

const emit = defineEmits(['closeModal'])
const props = defineProps(['Expert'])
const isModalOpen = ref(true)
const subject = ref('')
const message = ref('')
const error =  ref(false)
const spinner = ref(false)

function isEmptyOrWhitespace(str) {
    return !str || /^\s*$/.test(str);
}
function closeModal(error,closed){
    spinner.value = false
    isModalOpen.value = false
    emit('closeModal',error,closed)
}
function validatefields(){
    
    if(isEmptyOrWhitespace(subject.value) || isEmptyOrWhitespace(message.value)){
        return false
    }
    return true
 
}
 async function sendMessage(){
    CheckLogin()
    if(validatefields()){
        const userStore = useUserStore()
        spinner.value  = true
    try{
        const response  = await fetch(`http://127.0.0.1:8000/sendemail`, {
            method:'POST',
            headers:{
                'Content-Type': 'application-json',
                'X-CSRFToken': Cookies.get('csrftoken'),
            },
            credentials:'include',
            body: JSON.stringify({
                subject: subject.value,
                message: 'from '+userStore.email +'\n'+'\n'+ message.value,
                user_email: userStore.email,
                expert_email: props.Expert.email
            }),
        });
        if(response.ok) {
            const jsonResponse = await response.json();
            console.log(jsonResponse)
            if(!jsonResponse.status == 200){
                error.value = true
            } 
        }
    }
    catch(error){
        console.log(error);
    }
        message.value = ''
        subject.value = ''
        closeModal(error.value,false)
    }
    else{
        error.value  = true
    }
    spinner.value  = false
}
</script>
<template>
    <div>
      <div v-if="isModalOpen" class="fixed inset-0 z-50 flex items-center justify-center">
        <div class="absolute inset-0 bg-black opacity-50 z-40"></div>
  
        <div class="bg-white p-8 rounded shadow-md w-1/2 z-50 relative">
          <button @click="closeModal(false,true)" class="absolute top-4 right-4 text-gray-700 hover:text-gray-900">
            ✕
          </button>
          <p v-if="error" class="text-red-500 p-2 font-bold italic">Please ensure all fields are not empty</p>
          <div class="text-left mt-4 flex">Message<p class="ml-1 font-semibold">{{ Expert.name }}</p></div>
              <div class="flex flex-col items-start w-full">
                <div class="flex flex-col mt-4 items-start ml-2">
                    <label class=" mb-2"> Subject: </label>
                    <input type="text" class=" border border-black rounded p-1 flex" v-model="subject">
                </div>
                <div class="flex flex-col mt-4 items-start ml-2 w-full">
                    <label class=" mb-2"> Message: </label>
                    <div class="w-full">
                        <textarea type="text"  rows="5"  class=" border border-black rounded p-1 w-4/5 flex" v-model="message"/>
                    </div>
                </div>
              </div>
      
              <div class="mt-6 flex justify-end">
                <button @click="sendMessage" class="rounded bg-green-300 mr-2 p-2 font-bold flex align-baseline">Send
                    <img v-if="spinner" src="../assets/spinner.png" width="20" height="20" class="animate-spin ml-2 mt-0.5">
                </button>
                <button @click="closeModal(false,true)" class=" border-white bg-gray-300 text-gray-700 rounded p-2 font-bold">Close</button>
              </div>
        </div>
      </div>
    </div>
  </template>