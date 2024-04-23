import Cookies from 'js-cookie';
import { RouterView,useRouter, useRoute } from 'vue-router'
import router from './router'
import { useUserStore } from "./Stores/userStore";
import { useChatStore } from './stores/ChatStore';
import { useExpertStore } from './Stores/ExpertStore'
import {useAuthStore} from './stores/authStore'


export async function logout (message){
    const userStore = useUserStore()
    const ChatStore = useChatStore()
    const ExpertStore  = useExpertStore() 
    const authStore = useAuthStore()       
    try{
        const response = await fetch('http://127.0.0.1:8000/logout', {
            method:'POST',
            headers:{
                'Content-Type': 'application-json',
                'X-CSRFToken': Cookies.get('csrftoken'), 
            } ,
            credentials: 'include',
        })
        if(response.ok){
          if(response.status == 200)
            userStore.emptyUser()
            ChatStore.clearChat()
            ExpertStore.ClearExpert()
            authStore.setLogoutMessage(message)
            router.push('/')
        }
    }
    catch(error){
        console.log(error)
    }
}
export function CheckLogin(){
    const router = useRouter()
    let session 
    session = Cookies.get('session')
    if (!session){
        logout()
        router.push('/')
    }
}
