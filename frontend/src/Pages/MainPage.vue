<script setup>
import ApplicationTable from '../Components/ApplicationTable.vue'
import Sidebar from '../Components/Sidebar.vue';
import Header from '../Components/Header.vue'
import { ref } from 'vue'
import Cookies from 'js-cookie';
import { useUserStore } from "../Stores/userStore";
import Footer from '../Components/Footer.vue'

const userStore = useUserStore()
console.log(userStore.email,userStore.first_name, userStore.last_name, userStore.id)
</script>
<template>
    <div class="">
      <Header />
      <div class="flex flex-row mt-4">
        <Sidebar class="basis-1/4 "/>
        <div class="basis-4/5 ml-8 items-center">
          <ApplicationTable class=""/>
        </div>
      </div>
    </div>
</template>
