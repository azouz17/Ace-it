import { defineStore } from 'pinia'
import { useLocalStorage } from "@vueuse/core"

export const useExpertStore = defineStore('Expert', {
    state: () => {
      return {
       name: useLocalStorage('name'),
       about_me: useLocalStorage('about_me'),
       ExpertEmail: useLocalStorage('ExpertEmail'),
       Experience: useLocalStorage('Experience'),
       field: useLocalStorage('field'),
       profile_picture: useLocalStorage('profile_picture'),
       rate: useLocalStorage('rate'),
       rating: useLocalStorage('rating'),
      };
    }, 
    getters: {
      getName: (state) => state.name ,
      getAboutMe: (state) => state.about_me ,
      getExpertEmail: (state) => state.ExpertEmail ,
      getExperience: (state) => state.Experience ,
      getField: (state) => state.field,
      getProfile_picture: (state) => state.profile_picture,
      getRate: (state) => state.rate ,
      getRating: (state) => state.rating ,

    },
    actions: {
      setExpert(name,about_me, email,Experience,field, profile_picture,rate,rating) {
        this.name = name
        this.about_me = about_me
        this.ExpertEmail = email
        this.Experience  = Experience
        this.field = field
        this.profile_picture = profile_picture
        this.rate = rate
        this.rating = rating
      },
      ClearExpert(){
        this.name = ''
        this.about_me = ''
        this.ExpertEmail = ''
        this.Experience  = 0
        this.field = ''
        this.profile_picture = null
        this.rate = 0
        this.rating = 0
      }
    },
  });