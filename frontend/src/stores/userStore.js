import { defineStore } from 'pinia'
import { useLocalStorage } from "@vueuse/core"

export const useUserStore = defineStore('user', {
    state: () => {
      return {
       first_name: useLocalStorage('first_name'),
       last_name: useLocalStorage('last_name'),
       email:  useLocalStorage('email'),
       id: useLocalStorage('id')
      };
    }, 
    getters: {
      getId: (state) => state.id ,
      getFirst_name: (state) => state.first_name ,
      getLast_name: (state) => state.last_name ,
      getEmail: (state) => state.email
    },
    actions: {
      setUser(first_name, last_name, email,id) {
        this.first_name = first_name; 
        this.last_name = last_name
        this.email = email
        this.id = id
      },
      emptyUser(){
        this.first_name = ''; 
        this.last_name = ''
        this.email = ''
        this.id = ''
      }  
    },
  });