<script setup>
import Sidebar from '../Components/Sidebar.vue';
import Header from '../Components/Header.vue'
import { ref as ref,onMounted, nextTick } from 'vue'
import Cookies from 'js-cookie';
import axios from "axios";
import { useChatStore } from '../stores/ChatStore'
import { CheckLogin } from '../authentication';

const ChatStore = useChatStore()
const chat = ref([])
chat.value = ChatStore.getChat
const prompt = ref('')
const loading = ref(false)
const reply = ref('')

async function SendPrompt(e){
    let timeout
    e.preventDefault()
    CheckLogin()
    chat.value.push(prompt.value)
    loading.value = true
    await nextTick()
    scrollToBottom();

    const options = {
    method: "POST",
    url: "https://api.edenai.run/v2/text/generation",
    headers: {
        authorization: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMWIwMTUxNzctMjUyNC00MjJlLWJmMGQtOTlhZGNlNWVlOWEwIiwidHlwZSI6ImFwaV90b2tlbiJ9.j0vGhh2tLgnRF8Rh-8UTazXlaghBCOvc2vpqxcmc7NQ",
    },
    data: {
        providers: "cohere",
        text: prompt.value,
        temperature: 0.2,
        max_tokens: 250,
        fallback_providers: "amazon",
    },
    };

    axios
    .request(options)
    .then((response) => {
        console.log(response)
        reply.value = response.data.cohere.generated_text
    })
    .catch((error) => {
        console.error(error);
    });
    prompt.value=''
    timeout = setTimeout(AddText,10000)
}

function scrollToBottom() {
      var scroll = document.getElementById("scrollableDiv");
      scroll.scrollTop = scroll.scrollHeight;
}
function AddText(){
    loading.value = false
    chat.value.push(reply.value)

}

</script>
<template>
    <div>
        <Header />
        <div class="flex flex-row mt-4">
            <Sidebar class="basis-1/4"/>
            <div class="basis-4/5 ml-8 mt-4 items-center flex-col relative">
                <p class="text-3xl font-bold">Ask Away!</p>
                <p class="text-lg mt-2">Ask our dedicated AI assistant questions about your resume. You can ask for general advice or tailored advice regarding your own resume</p>
                <div id="scrollableDiv" class="mt-6 overflow-y-scroll h-3/6 border border-gray rounded-lg p-2 scrollbar max-h-96 bg-white">
                    <div v-for="messages in chat" class="mt-6 w-2/5 p-4 rounded-2xl even:bg-blue-200 odd:bg-green-200 text-left">
                        <p class="">{{ messages }}</p>
                    </div>
                    <div v-if="loading" class="mt-6 w-2/5 p-4 rounded-2xl bg-blue-200 text-left animate-pulse">
                        <p class="">. . . . . . . . . . . .</p>
                    </div>
                </div>
                <div class="flex flex-col mt-10">
                    <form id="form" :onsubmit="SendPrompt">
                        <div class=" flex flex-row justify-between">
                            <input required v-model="prompt" type="text" class="w-full border border-gray-400 rounded-lg p-1 h-12 w-4/5 mr-6" placeholder="Message...">
                            <button type="submit" class="bg-green-200 font-bold w-1/5 rounded p-2 hover:opacity-70">
                                        <p>Send</p>
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>