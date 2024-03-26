<script setup>
import { ref, onMounted } from 'vue'
let isModalOpen = ref(false)
function openModal(){
        isModalOpen.value = true;
      }
function closeModal() {
        isModalOpen.value = false;
      }
</script>

<template>
    <div>
      <button @click="openModal" class="border-white rounded bg-blue-500 p-1 w-24 text-white font-bold">Edit</button>
      <div v-if="isModalOpen" class="fixed inset-0 z-50 flex items-center justify-center">
        <div class="absolute inset-0 bg-black opacity-50 z-40"></div>
  
        <div class="bg-white p-8 rounded shadow-md w-1/2 z-50 relative">
          <button @click="closeModal" class="absolute top-4 right-4 text-gray-700 hover:text-gray-900">
            ✕
          </button>
  
          <h2 class="text-2xl font-bold mb-4">Edit Profile</h2>
              <div class="flex flex-col items-start">
                <div class="flex flex-row mt-2">
                    <label class="font-bold">Email: </label>
                    <input type="email" class="ml-2 border border-black rounded p-0.5 flex" id="Email" >
                </div>
                <div class="flex flex-row mt-2">
                    <label class="font-bold">Date of Birth: </label>
                    <input type="date" class="ml-2 border border-black rounded p-0.5 flex" id="username" >
                </div>
                <div class="flex flex-row mt-2">
                    <label class="font-bold">Image: </label>
                    <input  type="file" class="ml-2" id="Image">
                </div>
              </div>
      
              <div class="mt-6 flex justify-end">
                <button @click="closeModal" class="rounded bg-green-500 text-white mr-2 p-2 font-bold">Edit</button>
                <button @click="closeModal" class=" border-white bg-gray-300 text-gray-700 rounded p-2 font-bold">Close</button>
              </div>
        </div>
      </div>
    </div>
  </template>
  
  
  