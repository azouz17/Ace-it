<script setup>
import EditRecord from './EditRecord.vue';
import RowModal from '../Components/RowModal.vue'
import ColumnModal from '../Components/ColumnModal.vue'
import { ref, onMounted } from 'vue'
import Cookies from 'js-cookie';
import { useUserStore } from "../stores/userStore";
import { RouterView,useRouter, useRoute } from 'vue-router'
import { CheckLogin } from '../authentication';

const showRowModal = ref(false)
const showColumnModal = ref(false)
const temp = ref('')
const row_id = ref()
const row_count = ref()
const column_id = ref()
const columns = ref([])
const rows = ref()
const showAddcolumnInput = ref(false)
const columnText = ref('')
const table_id = ref(0)
const router = useRouter()


onMounted(async () => {
  CheckLogin()
  const userStore = useUserStore()
  try{
         const response = await fetch(`http://127.0.0.1:8000/getTable`, {
         method: 'POST',
         headers: {
             'Content-Type': 'application-json',
             'X-CSRFToken': Cookies.get('csrftoken'),
         },
         credentials: 'include',
         body: JSON.stringify({
           id: userStore.getId,
         }),
         });
         if (response.ok) {
             const jsonResponse = await response.json();
             if(jsonResponse.status == 200){
              row_count.value = jsonResponse.row_count
              columns.value = jsonResponse.columns
              console.log(columns.value)
              console.log(columns.value.length)
              rows.value = jsonResponse.rows
              table_id.value = jsonResponse.table_id
             }
             else{
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
})
async function CreateTable(){
  CheckLogin()
  const userStore = useUserStore()
  try{
         const response = await fetch(`http://127.0.0.1:8000/createTable`, {
         method: 'POST',
         headers: {
             'Content-Type': 'application-json',
             'X-CSRFToken': Cookies.get('csrftoken'),
         },
         credentials: 'include',
         body: JSON.stringify({
           id: userStore.getId,
         }),
         });
         if (response.ok) {
             const jsonResponse = await response.json();
             if(jsonResponse.status == 200){
              row_count.value = jsonResponse.row_count
              columns.value = jsonResponse.columns
              console.log(columns.value)
              console.log(columns.value.length)
              rows.value = jsonResponse.rows
              table_id.value = jsonResponse.table_id
             }
             else{
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
}

function setupRowModal(row_num,text){
  showRowModal.value  = true
  temp.value = text
  row_id.value = row_num 
}
function setupColumnModal(col){
  showColumnModal.value = true
  column_id.value = col
}
function closeModal(){
  showRowModal.value  = false
  showColumnModal.value = false
}
function columnInput(){
  showAddcolumnInput.value = !showAddcolumnInput.value
  columnText.value = ''
}
async function AddColumn(){
  CheckLogin()
  const userStore = useUserStore()
    try{
        const response  = await fetch(`http://127.0.0.1:8000/addColumn`, {
            method:'POST',
            headers:{
                'Content-Type': 'application-json',
                'X-CSRFToken': Cookies.get('csrftoken'),
            },
            credentials:'include',
            body: JSON.stringify({
              column: columnText.value,
              table_id: table_id.value
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
    router.go()
}

async function DeleteColumn(col_id){
  CheckLogin()
  try{
        const response  = await fetch(`http://127.0.0.1:8000/deleteColumn`, {
            method:'POST',
            headers:{
                'Content-Type': 'application-json',
                'X-CSRFToken': Cookies.get('csrftoken'),
            },
            credentials:'include',
            body: JSON.stringify({
              column_id: col_id
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
    router.go()
}

async function DeleteRow(row_id){
  CheckLogin()
    try{
        const response  = await fetch(`http://127.0.0.1:8000/deleteRow`, {
            method:'POST',
            headers:{
                'Content-Type': 'application-json',
                'X-CSRFToken': Cookies.get('csrftoken'),
            },
            credentials:'include',
            body: JSON.stringify({
              row_id: row_id
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
    router.go()
}
</script>

<template>
    <div v-if="table_id" class="overflow-x-auto rounded-lg border border-gray-200">
  <table class="table-auto min-w-full divide-y divide-gray-200 overflow-x-scroll scrollbar">
    <thead class="bg-gray-50">
      <tr class="">
        <th v-for="col in columns" scope="col" class="thdata align-baseline min-w-16 text-center text-lg">{{col.text}}
          <div class="flex flex-row w-6 justify-center w-full">
            <button @click="DeleteColumn(col.column_id)" class="text-center  text-black px-0.5 text-sm"><img src="../assets/Delete.png" width="12" height="12"></button>
            <button @click="setupColumnModal(col)" class="text-center text-black px-0.5 tex-sm"><img src="../assets/edit.png" width="12" height="12"></button>
          </div>
        </th>
        <th scope="col" class="thdata font-semibold">
          <div class="flex justify-center w-full">
            <div  v-if="!showAddcolumnInput" @click="columnInput()" class="flex flex-row bg-green-200 p-2 rounded border border-gray text-black text-sm justify-between w-3/4 mb-2 max-w-32" >
              <button>Add Column</button>
              <img src="../assets/PLus.png" width="25" height="15">
            </div>
          </div>
          <div v-if="showAddcolumnInput" class="flex flex-row">
            <input type="text" class="bg-white border border-black rounded p-1 text-base text-black w-24" v-model="columnText">
            <button class="border border-black rounded p-1 text-black mx-1 " @click="columnInput()">Back</button>
            <button class="border border-black rounded p-1 text-black mx-1" @click="AddColumn()">Add Column</button>
          </div>

        </th>
      </tr>
    </thead>
    <tbody class="bg-white divide-y divide-gray-200">
      <tr v-for="row in row_count" class="odd:bg-white even:bg-slate-100 overflow-x-scroll">
        <td class="text-center" v-for="cell in rows[row.row_id]">{{ cell.text}}</td>
        <td class="p-2 text-center"><button @click="DeleteRow(row.row_id)" class="bg-slate-400 px-2 rounded border border-black font-semibold mx-1">Delete</button><button class="bg-slate-200 px-2 rounded border border-black font-semibold mx-1" @click="setupRowModal(row.row_id,'Edit')">Edit</button></td>
      </tr>
    </tbody>
  </table>
</div>
<div v-if="columns.length" class="flex flex-row bg-green-200 font-semibold p-2 rounded border border-gray-100  justify-between w-1/5 mt-4" @click="setupRowModal(-1,'Add')">
      <button  class="">Add Row</button>
      <img src="../assets/PLus.png" width="25" height="15">
</div>
<RowModal v-if="showRowModal" @closeModal="closeModal" :columns="columns" :row="rows[row_id]" :text="temp"/>
<ColumnModal v-if="showColumnModal" @closeModal="closeModal" :column="column_id"/>
<div v-if="!table_id" class="mt-4">
  <p class="text-base text-left">Start tracking your job Applications by creating your table below.<br>
    Your table can be structured however you want be dynamically adding and deleting columns<br>
  Happy Tracking!</p>
  <div class="flex flex-row bg-green-200 font-semibold p-2 rounded border border-gray  w-1/4 justify-between mt-4">
    <button @click="CreateTable" v-if="!table_id ">CREATE TABLE</button>
    <img src="../assets/PLus.png" width="25" height="15">
</div>
</div>
</template>