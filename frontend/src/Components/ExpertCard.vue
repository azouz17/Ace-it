<script setup>
import { ref as ref, onMounted } from 'vue'
import ExpertModal from './ExpertModal.vue'
import Cookies from 'js-cookie';
import { useUserStore } from "../Stores/userStore";
import { RouterView,useRouter, useRoute } from 'vue-router'
import { useExpertStore } from "../Stores/ExpertStore";
import { getStorage, ref as Ref, getDownloadURL } from "firebase/storage";

const props = defineProps(['Expert'])
const emit = defineEmits(['openPopup'])
const router = useRouter()
const showModal = ref(false)
const ImgUrl = ref('https://via.placeholder.com/140x100')

// onMounted(async () => {
//     const storage = getStorage();
//     const ImgRef = Ref(storage, props.Expert.profile_picture);
//     await getDownloadURL(ImgRef)
//   .then((url) => {
//     // Or inserted into an <img> element
//     console.log(url)
//     const img = document.getElementById('myimg');
//     img.setAttribute('src', url);
//   })
//   .catch((error) => {
//     // Handle any errors
//   });  

// })

function closeModal(error,closed){
    showModal.value = false
    emit('openPopup',error,closed)
}
async function AboutMe(){
    const ExpertStore = useExpertStore()
    console.log(ExpertStore.Experience)
    ExpertStore.setExpert(props.Expert.name,props.Expert.about_me,props.Expert.email,props.Expert.experience,props.Expert.field.name,props.Expert.profile_picture,props.Expert.rate,props.Expert.rating)
    router.push('/AboutMe')
}
</script>

<template>
    <div class="flex flex-col bg-white w-80 mt-2 shadow-md" >
        <div class="basis-1/3 rounded-lg p-6 items-center ">
            <p class="font-bold mb-2">{{ Expert.name }}</p>
            <img id="myimg" class="mx-auto rounded w-28 h-28" v-bind:src="props.Expert.profile_picture" alt="Loading.....">
            <hr class="text-black mt-2">
            <div class="flex flex-row mt-2">
                <p class="font-bold">Field:</p>
                <p class="ml-2">{{ Expert.field.name }}</p>  
            </div>
            <div class="flex flex-row">
                <p class="font-bold">Experience:</p>
                <p class="ml-1">{{ Expert.experience }} years</p>  
            </div>
            <div class="flex flex-row">
                <p class="font-bold">Rate:</p>
                <p class="ml-1">{{ Expert.rate }}£ / hour</p>  
            </div>
            <div class="flex flex-row">
                <button @click="showModal = true" class="bg-green-200 font-bold w-1/3 rounded p-2 mx-auto mt-4 hover:opacity-70">Contact</button>
                <button @click="AboutMe" class="bg-green-200 font-bold w-1/3 rounded p-2 mx-auto mt-4 hover:opacity-70">About</button>
            </div>

        </div>
    </div>
    <ExpertModal v-if="showModal"  :Expert="Expert" @closeModal="closeModal" />
    <router-view />
</template>