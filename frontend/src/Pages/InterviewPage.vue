<script setup>
import Sidebar from '../Components/Sidebar.vue';
import Header from '../Components/Header.vue'
import ExpertCard from '../Components/ExpertCard.vue';
import { ref as ref,onMounted } from 'vue';
import Cookies from 'js-cookie';
import Popup from '../Components/Popup.vue'
import { getStorage, ref as Ref, getDownloadURL } from "firebase/storage";
import { CheckLogin } from '../authentication';

const Experts = ref([])
const showpopup = ref(false)
const error = ref(false)
const rate = ref(0)
const field = ref(0)
const experience = ref(0)
const filteredExperts = ref([])
const Fields = ref([])
const message = ref('Message Sent')


onMounted(async () => {
    CheckLogin()
    try{
        const response = await fetch(`http://127.0.0.1:8000/getExperts`, {
         method: 'GET',
         headers: {
             'Content-Type': 'application-json',
             'X-CSRFToken': Cookies.get('csrftoken'),
         },
         credentials: 'include',
         });
         if (response.ok){
            const jsonResponse = await response.json();
             if(jsonResponse.status == 200){
              Experts.value = jsonResponse.experts
              Fields.value = jsonResponse.fields
              filteredExperts.value = Experts.value
              let i = 0
              for(i; i<Experts.value.length;i++)
              {
                SetUrl(Experts.value[i])
              }
             }
             console.log(jsonResponse)
         }
    }
    catch(error){
        console.log(error)
    }
})
 async function SetUrl(expert){
    const storage = getStorage()
    const ImgRef = Ref(storage, expert.profile_picture)
    await getDownloadURL(ImgRef)
  .then((url) => {
    expert.profile_picture = url
  })
  .catch((error) => {
    // Handle any errors
  }); 
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
function resetFilters(){
    experience.value = 0
    field.value = 0
    rate.value = 0
}
function FilterExperts(){
    if(experience.value == 0 && rate.value == 0 && field.value == 0){
        filteredExperts.value = Experts.value
    }
    else{
        filteredExperts.value = Experts.value.filter((expert) => expert.experience >= experience.value && expert.rate >= rate.value ) 
        if(field.value != 0 ){
            filteredExperts.value = filteredExperts.value.filter((expert)=> expert.field.id == field.value)
        }
    }
}
</script>

<template>
    <div>
      <Header />
      <div class="w-full justify-end flex h-24">
        <Popup class="w-2/6 " v-if="showpopup" :error="error" :message="message"/>
      </div>
        <div class="flex flex-row -mt-16">
            <Sidebar class="basis-1/4 "/>
            <div class="basis-3/5 ml-8 items-center">
                <p class="text-3xl font-bold">Choose Your Expert</p>
                <p class="text-lg mt-2">We have a wide of experts in a variety of fields that will be able to assist you in your job hunt. Take your pick and send them a message to talk about what to do next</p>
                <div class="justify-start flex align-baseline mt-4">
                    <div class="flex ml-6">
                        <label class="font-semibold" >Rate:</label>
                        <select v-model="rate" class="w-12 ml-2 border border-black rounded h-6">
                            <option value = "0">all</option>
                            <option value = "5">5£+</option>
                            <option value = "10">10£+</option>
                            <option value = "15">15£+</option>
                        </select>
                    </div>
                    <div class="flex ml-6">
                        <label class="font-semibold" >Field:</label>
                        <select  v-model="field" class="w-12 ml-2 border border-black rounded h-6"> 
                          <option value="0">all</option> 
                          <option v-for="field in Fields" :value="field.id">{{ field.name }}</option>
                        </select>
                    </div>
                    <div class="flex ml-6">
                        <label class="font-semibold" >Experience:</label>
                        <select class="w-12 ml-2 border border-black rounded h-6" v-model="experience">
                            <option value="0" selected>all</option>
                            <option value="3">3+</option>
                            <option value = "5">5+</option>
                            <option value = "10">10+</option>
                            <option value = "15">15+</option>
                        </select>
                    </div>
                    <div class="ml-8">
                        <button @click="FilterExperts" class="font-semibold mr-2 bg-slate-200 border border-white rounded px-3 py-1 hover:opacity-70 ml-2 h-8">Filter </Button>
                        <button @click="resetFilters" class="font-semibold mr-2 bg-slate-200 border border-white rounded px-3 py-1 hover:opacity-70 ml-2">Clear</Button>
                    </div>
                </div>
                <div class="flex flex-wrap justify-between mt-4">
                    <div :key="expert.email" v-for="expert in filteredExperts"> 
                        <ExpertCard @openPopup="openPopup" :Expert="expert" class=""/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>