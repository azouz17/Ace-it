<script setup>
import Header from '../Components/Header.vue';
import { ref,onMounted } from 'vue';
import Cookies from 'js-cookie';
import Sidebar from '../Components/Sidebar.vue'
import { RouterView,useRouter, useRoute } from 'vue-router'
import { useExpertStore } from "../Stores/ExpertStore";
import ExpertModal from '../Components/ExpertModal.vue'
import Popup from '../Components/Popup.vue'

const ExpertStore = useExpertStore()
const rating = parseInt(ExpertStore.rating)
const showModal = ref(false)
const error = ref(false)
const showpopup = ref(false)
const Expert = {
    name: ExpertStore.name,
    email: ExpertStore.ExpertEmail
}
const message = ref('Message Sent')

function closeModal(error,closed){
    showModal.value = false
    if(!closed){
        openPopup(error,closed)
    }
}
function openPopup(status,closed){
    if(!closed){
        let timeout
        error.value = status
        if(error.value == true){
            message.value = "Something went wrong"
        }
        showpopup.value = true
        timeout = setTimeout(closePopup,5000)
    }
}
function closePopup(){
    showpopup.value = false
    error.value = false
    message.value = 'Message Sent'
}

</script>

<template>
    <div>
        <Header />
        <div class="flex flex-row ">
            <Sidebar class="basis-1/4 mt-4"/>
            <div class="basis-3/5 ml-8 flex flex-col relative mt-10">
                <Popup v-if="showpopup" class=" w-3/6 float-right absolute top-0 -mt-10 -right-40"  :error="error" :message="message" />
                <router-link class="font-bold text-blue-600 underline hover:text-blue-300 text-left w-12" to="/ExpertHelp">Back</router-link>
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