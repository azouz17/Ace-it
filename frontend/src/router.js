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
const routes = [
  { path: '/',name: 'Main Page', component: Login, props: true},
  { path: '/signup', component: SignUp, props: true },
  { path: '/Home', component: MainPage },
  { path: '/Interview', component: InterviewPage, props: true },
  { path: '/AboutMe',name: 'AboutMe', component: ExpertPage,},
  { path: '/ExpertEnrollment',name: 'Expert Enrollment', component: ExpertEnrollment,},
  { path: '/Resume',name: 'Resume', component: Resume,},
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
