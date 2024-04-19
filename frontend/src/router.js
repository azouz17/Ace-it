import { createRouter, createWebHistory, createWebHashHistory } from 'vue-router';
import App from './App.vue';
import SignUp from './Pages/SignUp.vue'
import Header from './Components/Header.vue'
import Login from './Pages/Login.vue'
import MainPage from './Pages/MainPage.vue'
import InterviewPage from './Pages/InterviewPage.vue'
import ExpertCard from './Components/ExpertCard.vue'
import ExpertPage from './Pages/ExpertPage.vue';
import ExpertEnrollment from './Pages/ExpertEnrollment.vue'
import Resume from './Pages/Resume.vue'
import EditProfile from './Pages/EditProfile.vue'
import Cookies from 'js-cookie';
import NotFound from './Pages/NotFound.vue'
import {logout} from './authentication'
const routes = [
  { path: '/',name: 'Login', component: Login, props: true},
  { path: '/Edit',name: 'Edit Profile', component: EditProfile, props: true},
  { path: '/signup', name: "Signup", component: SignUp, props: true },
  { path: '/Home', component: MainPage },
  { path: '/Interview', component: InterviewPage, props: true },
  { path: '/AboutMe',name: 'AboutMe', component: ExpertPage,},
  { path: '/ExpertEnrollment',name: 'Expert Enrollment', component: ExpertEnrollment,},
  { path: '/Resume',name: 'Resume', component: Resume,},
  { path: '/:catchAll(.*)',redirect: '/error'}, // Redirect any unmatched URL to the error page
  { path: '/error', name: 'Error', component: NotFound, },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});


router.beforeEach(async (to, from) => {
  let session 
  session = Cookies.get('session')
  if (to.name == 'Login' ||  to.name == 'Signup') {
    // redirect the user to the login page
    return true
  }
  else{
    if(from.name == 'Login' ||  from.name == 'Signup'){
      return true
    }
    if(!session){
      logout('Session Expired, Please login again')
      return { name: 'Login' }
    }
    return true
  }
})

export default router;
