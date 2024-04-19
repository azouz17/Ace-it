<script setup>
import Sidebar from '../Components/Sidebar.vue';
import Header from '../Components/Header.vue'
import { ref as ref,onMounted } from 'vue'
import Cookies from 'js-cookie';
import { useUserStore } from "../Stores/userStore";
import { createRouter } from 'vue-router';
import $ from "jquery";
import Popup from '../Components/Popup.vue'
import { ref as Ref,getStorage,uploadBytes } from "firebase/storage";

const showForm = ref(false)
const fields = ref([])
const field = ref()
const experience = ref()
const rate = ref()
const about_me = ref('')
const name = ref('')
const spinner = ref(false)
const url = ref('https://jquery.com/download/')
const profileImg = ref()
const error = ref(false)
const message = ref('Request Submitted')
const showPopup = ref(false)

onMounted(async () => {
    try{
        const response = await fetch(`http://127.0.0.1:8000/getFields`,{
            method:'GET',
            headers:{
                'Content-Type': 'application-json',
                'X-CSRFToken': Cookies.get('csrftoken'),
            },
            credentails: 'include'
        })
        if(response.ok){
            const jsonResponse = await response.json();
             if(jsonResponse.status == 200){
                fields.value = jsonResponse.fields
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

async function CreateExpert(e){
        e.preventDefault()
        const userStore = useUserStore()
        const storage = getStorage();
        spinner.value  = true
    try{
        const response  = await fetch(`http://127.0.0.1:8000/createExpert`, {
            method:'POST',
            headers:{
                'Content-Type': 'application-json',
                'X-CSRFToken': Cookies.get('csrftoken'),
            },
            credentials:'include',
            body: JSON.stringify({
                name: name.value,
                rate:  rate.value,
                experience: experience.value,
                email: userStore.email,
                field: field.value,
                about_me: about_me.value,
                url: url.value,
                user_id: userStore.id,
                profile_picture: profileImg.value
            }),
        });
        if(response.ok) {
            const jsonResponse = await response.json();
            console.log(jsonResponse)
            if(jsonResponse.status != 200){
                error.value = true
                message.value = 'You have already submitted a request'
            } 
            else{
                const storage = getStorage();
                const file = profileImg.value
                const image = Ref(storage, profileImg.value.name);
                uploadBytes(image, file).then((snapshot) => {
                console.log('Uploaded a blob or file!');
});

            }
        }
    }
    catch(error){
        console.log(error);
    }
    spinner.value = false
    openPopup()
}

function openPopup(){
        let timeout
        showPopup.value = true
        timeout = setTimeout(closePopup,5000)
}
function closePopup(){
    showPopup.value = false
    error.value = false
}

function SetProfileImg(event){
    profileImg.value = event.target.files[0]
}
</script>

<template>
    <div>
        <Header />
        <div class="flex flex-row mt-4">
            <Sidebar class="basis-1/4" />
            <div class="basis-3/5 ml-8 mt-8 items-center self-center flex-col relative">
                <Popup v-if="showPopup" class=" w-3/6 -mt-12 float-right  absolute top-0 -right-40"  :error="error" :message="message" />
                <p class="text-3xl font-bold">Become An Expert</p>
                <p class="font-base mt-8 text-center">
                    Becoming an expert is a great oppurtunity for you to help aspiring individuals in their job hunt. The role would entail assisting them
                    with Interviews, Resume writing and many more. If you think you have the right credentials, sign up here now and we will get back to you
                    regarding your elegibility
                </p>
                <button v-if="!showForm" @click="showForm = true" class="bg-green-200 font-bold w-1/3 rounded p-2 mx-auto mt-8 hover:opacity-70">Sign Up</button>
                <div class=" rounded-lg p-2 mt-6 w-full mx-auto">
                    <div class="flex flex-col mt-2 bg-white shadow-md rounded-lg p-8 mt-4">
                        <form id="form" :onsubmit="CreateExpert">
                            <div class="flex flex-col">
                                <label class="inputLabel">Field: </label>
                                <select required v-model="field" class="inputStyle"> 
                                    <option disabled value="0">Please select one</option> 
                                    <option v-for="field in fields" :value="field.id">{{ field.name }}</option>
                                </select>
                            </div>
                            <div class="flex flex-col mt-2">
                                <label class="inputLabel">Rate / hour:</label>
                                <input required type="number" min="1" v-model="rate" class=" inputStyle">
                            </div>
                            <div class="flex flex-col mt-4">
                                <label class="inputLabel">Full name:</label>
                                <input required v-model="name" class=" inputStyle">
                            </div>
                            <div class="flex flex-col mt-4">
                                <label class="inputLabel">Experience:</label>
                                <input required type="number" min="0" v-model="experience" class=" inputStyle">
                            </div>
                            <div class="flex flex-col mt-4">
                                <label class="inputLabel">LinkedIn profile URL:</label>
                                <input required type="url" v-model="url" class=" inputStyle">
                            </div>
                            <div class="flex flex-col mt-4">
                                <label class="inputLabel">Biography:</label>
                                <textarea required placeholder="Write a short description about yourself and career and why you want to help others" v-model="about_me" rows="5" cols="70" class=" inputStyle " />
                            </div>
                            <div class="flex mt-4">
                                <label class="inputLabel">Profile Picture:</label>
                                <input  @change="SetProfileImg" type="file" accept="image/png, image/jpeg" class=" ml-2 ">
                            </div>
                            <div class="flex">
                                <button type="submit" class="bg-green-200 font-bold w-1/3 rounded p-2 mx-auto mt-8 hover:opacity-70">
                                    <p>Send</p>
                                    <img v-if="spinner" src="../assets/spinner.png" width="20" height="20" class="animate-spin ml-2 mt-0.5">
                                </button>
                                <button  @click="showForm = false , error = false" class="bg-green-200 font-bold w-1/3 rounded p-2 mx-auto mt-8 hover:opacity-70 ml-2"> Close</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>