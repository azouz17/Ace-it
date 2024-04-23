<script setup>
const props = defineProps([ 'message', 'error'])
console.log(props.error)
</script>

<template>

<div class="animate-fade">
            <div v-if="!error" class="flex flex-col border border-gray rounded-b-lg mr-4 margin-right bg-green-200 self-end">
                <p class="mt-4 text-lg font-bold">{{ message }}</p>
                <img class="mx-auto" src="../assets/checkmark.png" width="30" height="30">
            </div> 
            <div v-if="error" class="flex flex-col border border-gray rounded-b-lg mr-4 margin-right bg-red-400 self-end">
                <p class="mt-4 text-lg font-bold">{{message}} </p>
                <p class="bg-white border border-gray rounded-2xl w-8 font-bold mx-auto">X</p>
            </div> 
</div>
</template>