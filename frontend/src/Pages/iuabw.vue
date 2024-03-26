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
                    <form>

                        
                    </form>
                <div v-if="showForm" class="items-center mx-auto border border-slate-300 rounded-lg p-2 mt-6">
                    <div class="flex flex-col items-center mt-2">
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
                        <input required @change="SetProfileImg" type="file" accept="image/png, image/jpeg" class=" ml-2 ">
                    </div>
                    <p v-if="error" class="text-red-500 p-2 font-bold italic"> Please ensure all fields are valid</p>
                    <button type="submit" class="bg-green-200 font-bold w-1/3 rounded p-2 mx-auto mt-8 hover:opacity-70">
                        <p>Send</p>
                        <img v-if="spinner" src="../assets/spinner.png" width="20" height="20" class="animate-spin ml-2 mt-0.5">
                    </button>
                    <button  @click="showForm = false , error = false" class="bg-green-200 font-bold w-1/3 rounded p-2 mx-auto mt-8 hover:opacity-70 ml-2"> Close</button>
                </div>
            </div>
        </div> 
    </div>
</div>
</template>