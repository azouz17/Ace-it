<script setup>
import { ref, onMounted } from 'vue'
import Cookies from 'js-cookie';
import { useUserStore } from "../Stores/userStore";
import { RouterView,useRouter, useRoute } from 'vue-router'

const props = defineProps(['column'])
const emit = defineEmits(['closeModal'])
const isModalOpen = ref(false)
const text = ref('')
const router = useRouter()

onMounted( () => {
    isModalOpen.value = true
    console.log(props.column)
})

function closeModal(){
    isModalOpen.value = false
    emit('closeModal')
}
async function ModifyColumn(){
    const userStore = useUserStore()
    try{
        const response  = await fetch(`http://127.0.0.1:8000/EditColumn`, {
            method:'POST',
            headers:{
                'Content-Type': 'application-json',
                'X-CSRFToken': Cookies.get('csrftoken'),
            },
            credentials:'include',
            body: JSON.stringify({
                column_id: props.column.column_id,
                text: text.value,
            }),
        });
        if(response.ok) {
            const jsonResponse = await response.json();
            console.log(jsonResponse)
            if(!jsonResponse.status == 200){
                window.alert('something went wrong')
            } 
        }
    }
    catch(error){
        console.log(error);
    }
    closeModal()
    router.go()
}
</script>
<template>
    <div>
      <div v-if="isModalOpen" class="fixed inset-0 z-50 flex items-center justify-center">
        <div class="absolute inset-0 bg-black opacity-50 z-40"></div>
  
        <div class="bg-white p-8 rounded shadow-md w-1/2 z-50 relative">
          <button @click="closeModal" class="absolute top-4 right-4 text-gray-700 hover:text-gray-900">
            ✕
          </button>
              <div class="flex flex-col items-center">
                <div class="flex flex-col mt-4">
                    <label class="font-bold mb-2">{{ column.text }} : </label>
                    <input type="text" class="ml-2 border border-black rounded p-1 flex" v-model="text">
                </div>
              </div>
      
              <div class="mt-6 flex justify-end">
                <button @click="ModifyColumn" class="rounded bg-green-300 mr-2 p-2 font-bold">Edit</button>
                <button @click="closeModal" class=" border-white bg-gray-300 text-gray-700 rounded p-2 font-bold">Close</button>
              </div>
        </div>
      </div>
    </div>
  </template>