import { defineStore } from 'pinia'
import { useLocalStorage } from "@vueuse/core"

export const useChatStore = defineStore('Chat', {
    state: () => {
      return {
        chat: useLocalStorage('Chat', []), 
      };
    }, 
    getters: {
      getChat: (state) => state.chat ,
    },
    actions: {
      addToChat(text) {
        this.chat.push(text)
      }, 
      clearChat() {
        this.chat = []
      }, 
    },
  });