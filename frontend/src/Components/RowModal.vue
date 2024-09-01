<script setup>
import { ref, onMounted } from 'vue'
import Cookies from 'js-cookie';
import { useUserStore } from "../Stores/userStore";
import { RouterView,useRouter, useRoute } from 'vue-router'
import { CheckLogin } from '../authentication';

const props = defineProps(['columns','row','text'])
const emit = defineEmits(['closeModal'])
const isModalOpen = ref(false)
const row_id = ref(-1)
const new_row = ref([])
const router = useRouter()

onMounted( () => {
    let text
    isModalOpen.value = true
    new_row.value.length = props.columns.length
    if(props.row){
        row_id.value = props.row[0].row_id.row_id
        for(let i = 0; i < props.columns.length; i++){
            text = props.row.find(cell => cell.column_id.column_id === props.columns[i].column_id).text
            new_row.value[i] = text
        }
    }
})

function closeModal(){
    isModalOpen.value = false
    new_row.value = []
    emit('closeModal')

}
async function ModifyRow(){
    CheckLogin()
    const userStore = useUserStore()
    try{
        const response  = await fetch(`http://127.0.0.1:8000/modifyrow`, {
            method:'POST',
            headers:{
                'Content-Type': 'application-json',
                'X-CSRFToken': Cookies.get('csrftoken'),
            },
            credentials:'include',
            body: JSON.stringify({
                new_row: new_row.value,
                row_id: row_id.value,
                columns: props.columns,
                user_id: userStore.id
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
              <div class="flex flex-col items-start">
                <div class="flex flex-row mt-4 w-1/2 justify-between" v-for="(col,index) in columns">
                    <label class="font-bold">{{ col.text }} </label>
                    <input type="email" v-model="new_row[index]" class="ml-2 border border-black rounded p-0.5 flex " :id="col.text" >
                </div>
              </div>
      
              <div class="mt-6 flex justify-end">
                <button @click="ModifyRow" class="rounded bg-green-300 mr-2 p-2 font-bold">{{text}}</button>
                <button @click="closeModal" class=" border-white bg-gray-300 text-gray-700 rounded p-2 font-bold">Close</button>
              </div>
        </div>
      </div>
    </div>
  </template>