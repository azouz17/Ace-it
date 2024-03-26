<script setup>
import Header from '../Components/Header.vue';
import { ref,onMounted } from 'vue';
import Cookies from 'js-cookie';
import Sidebar from '../Components/Sidebar.vue'
import { RouterView,useRouter, useRoute } from 'vue-router'
import { useExpertStore } from "../Stores/ExpertStore";
import ExpertModal from '../Components/ExpertModal.vue'

const ExpertStore = useExpertStore()
const rating = parseInt(ExpertStore.rating)
const showModal = ref(false)
const error = ref(false)
const showpopup = ref(false)
const Expert = {
    name: ExpertStore.name,
    email: ExpertStore.ExpertEmail
}

function closeModal(error,closed){
    showModal.value = false
    if(!closed){
        openPopup(error,closed)
    }
}
function openPopup(status,closed){
        let timeout
        error.value = status
        showpopup.value = true
        timeout = setTimeout(closePopup,5000)
}
function closePopup(){
    showpopup.value = false
    error.value = false
}

</script>

<template>
    <div>
        <Header />
        <div class="w-full justify-end flex h-24">
        <div v-if="showpopup" class="animate-fade w-2/6 ">
            <div v-if="!error" class="flex flex-col border border-gray rounded-b-lg mr-4 margin-right bg-green-200 self-end">
                <p class="mt-4 text-lg font-bold">Message Sent</p>
                <img class="mx-auto" src="../assets/checkmark.png" width="30" height="30">
            </div> 
            <div v-if="error" class="flex flex-col border border-gray rounded-b-lg mr-4 margin-right bg-red-400 self-end">
                <p class="mt-4 text-lg font-bold">Something went wrong </p>
                <p class="bg-white border border-gray rounded-2xl w-8 font-bold mx-auto">X</p>
            </div> 
        </div>
      </div>
        <div class="flex flex-row -mt-10">
            <Sidebar class="basis-1/4 mt-4"/>
            <div class="basis-3/5 ml-8 flex flex-col  mt-10">
                <router-link class="font-bold text-blue-600 underline hover:text-blue-300 text-left w-12" to="/Interview">Back</router-link>
                <p class="font-bold text-3xl">{{ExpertStore.name}}</p>
                <img v-bind:src=" ExpertStore.profile_picture" width="200" height="100" class="border border-gray-300 rounded mx-auto mt-10">
                <div class="flex w-2/5 flex-wrap mx-auto">
                    <div v-for="x in rating" class="mx-auto mt-2">
                        <img width="20" height="15" src="../assets/star.png">
                    </div>
                </div>
                <div class="mt-4 flex text-left">{{ ExpertStore.about_me }}</div>
                <div class="text-left mt-8">
                    <p>- <span class="font-bold"> {{ ExpertStore.Experience }}</span> years of experience in the Field of <span class="font-bold">{{ ExpertStore.field.name }}</span></p>
                    <p class="mt-2">- Charges <span class="font-bold">{{ ExpertStore.rate }}£</span>/hour for scheduled meetings </p>
                </div>
                <button @click="showModal = true" class="bg-green-200 font-bold w-1/3 rounded p-2 mx-auto mt-4 hover:opacity-70">Contact</button>
            </div>
        </div>
        <ExpertModal v-if="showModal"  :Expert="Expert" @closeModal="closeModal" />
    </div>
    <router-view />
</template>