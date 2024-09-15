import { createRouter, createWebHistory } from 'vue-router';
import Home from './pages/Home.vue';
import ITTeamList from './pages/ITTeamList.vue';
import RequestServiceList from './pages/RequestServiceList.vue';
import UserRequests from './pages/UserRequests.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/it-team-list',
    name: 'ITTeamList',
    component: ITTeamList,
  },
  {
    path: '/request-service-list',
    name: 'RequestServiceList',
    component: RequestServiceList,
  },
  {
    path: '/user-request',
    name: 'UserRequests',
    component: UserRequests,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;