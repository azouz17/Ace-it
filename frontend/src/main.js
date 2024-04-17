import { createApp } from 'vue'
import './assets/style.css'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import { initializeApp } from "firebase/app";
const firebaseConfig = {
    apiKey: "AIzaSyCdTwA_Wv72oJHsnjaTbEyRqO-PIZQtQ_Q",
    authDomain: "aceit-dcd72.firebaseapp.com",
    projectId: "aceit-dcd72",
    storageBucket: "aceit-dcd72.appspot.com",
    messagingSenderId: "48122325567",
    appId: "1:48122325567:web:fd542e27b811ffe711a68a"
  };


const app = createApp(App)
app.use(initializeApp(firebaseConfig))
app.use(createPinia())
app.use(router);
app.mount('#app');
