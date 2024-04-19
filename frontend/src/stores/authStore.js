// stores/auth.js
import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    logoutMessage: null,
  }),
  actions: {
    setLogoutMessage(message) {
      this.logoutMessage = message;
    },
    clearLogoutMessage() {
      this.logoutMessage = null;
    },
  },
});
