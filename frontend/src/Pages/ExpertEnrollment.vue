<script setup>
import Sidebar from '../Components/Sidebar.vue';
import Header from '../Components/Header.vue'
import { ref,onMounted } from 'vue'
import Cookies from 'js-cookie';
import { useUserStore } from "../Stores/userStore";
import { createRouter } from 'vue-router';
import $ from "jquery";

const showForm = ref(false)
const fields = ref([])
const field = ref(2)
const experience = ref(3)
const rate = ref(4)
const about_me = ref('iuerohaibvjhpwfei')
const name = ref('qgu3ig4')
const spinner = ref(false)
const url = ref('https://jquery.com/download/')
const profileImg = ref()
const error = ref(false)

function isEmptyOrWhitespace(str) {
    return !str || /^\s*$/.test(str);
}
function validatefields(){
    if(isEmptyOrWhitespace(rate.value) || fields.value == 0 || isEmptyOrWhitespace(about_me.value) || isEmptyOrWhitespace(name.value) || isEmptyOrWhitespace(experience.value) || isEmptyOrWhitespace(url.value) || isEmptyOrWhitespace(profileImg.value)){
        console.log('empty')
        return false
    }
    else{
        console.log('malyaneen')
        return true
    }
}

async function CreateExpert(){
    if(validatefields()){
        console.log('tmam')

        const userStore = useUserStore()
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
                url: url.value
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
    spinner.value = false
    }
    else{
        error.value = true
    }
}
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

function SetProfileImg(event){
    console.log(event)
    console.log(profileImg.value = event.target.files[0])
}
function temp(){
    console.log('gowa el mathod')
    $("form").on("submit", function (e) {
            e.preventDefault();
        });
}
</script>

<template>
    <div>
        <Header />
        <div class="flex flex-row mt-4">
            <Sidebar class="basis-1/4" />
            <div class="basis-3/5 ml-8 mt-4 items-center">
                <p class="text-3xl font-bold">Become An Expert</p>
                <p class="font-base mt-8 text-center">
                    Becoming an expert is a great oppurtunity for you to help aspiring individuals in their job hunt. The role would entail assisting them
                    with Interviews, Resume writing and many more. If you think you have the right credentials, sign up here now and we will get back to you
                    regarding your elegibility
                </p>
                <button v-if="!showForm" @click="showForm = true" class="bg-green-200 font-bold w-1/3 rounded p-2 mx-auto mt-8 hover:opacity-70">Sign Up</button>
                <div v-if="showForm" class="items-center mx-auto border border-slate-300 rounded-lg p-2 mt-6">
                    <div class="flex flex-col mt-2">
                        <form id="form" :onsubmit="temp">
                            <div class="flex flex-col">
                                <label class="font-semibold">Field: </label>
                                <select required v-model="field" class="w-15 ml-2 border border-black rounded h-6"> 
                                    <option disabled value="0">Please select one</option> 
                                    <option v-for="field in fields" :value="field.id">{{ field.name }}</option>
                                </select>
                            </div>
                            <div class="flex flex-col mt-2">
                                <label class="font-semibold">Rate / hour:</label>
                                <input required type="number" min="0" v-model="rate" class=" ml-2 border border-black rounded h-6 p-1">
                            </div>
                            <div class="flex flex-col mt-4">
                                <label class="font-semibold">Full name:</label>
                                <input required v-model="name" class=" ml-2 border border-black rounded h-6 p-1">
                            </div>
                            <div class="flex flex-col mt-4">
                                <label class="font-semibold">Experience:</label>
                                <input required type="number" min="0" v-model="experience" class=" ml-2 border border-black rounded h-6 p-1">
                            </div>
                            <div class="flex flex-col mt-4">
                                <label class="font-semibold">LinkedIn profile URL:</label>
                                <input required type="url" v-model="url" class=" ml-2 border border-black rounded h-6 p-1">
                            </div>
                            <div class="flex flex-col mt-4">
                                <label class="font-semibold">Biography:</label>
                                <textarea required placeholder="Write a short description about yourself and career and why you want to help others" v-model="about_me" rows="5" cols="70" class=" ml-2 p-1 border border-black rounded " />
                            </div>
                            <div class="flex mt-4">
                                <label class="font-semibold">Profile Picture:</label>
                                <input  @change="SetProfileImg" type="file" accept="image/png, image/jpeg" class=" ml-2 ">
                            </div>
                            <p v-if="error" class="text-red-500 p-2 font-bold italic"> Please ensure all fields are valid</p>
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