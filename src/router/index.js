
import Home from '@/components/Home.vue'
import About from '@/components/cctv.vue'
import Alert from '@/components/alert.vue'
import Ctr from '@/components/ctr.vue'

import { createWebHistory, createRouter } from "vue-router";


const routes = [
  {
    path: "/Home",
    name: "home",
    component: Home,
  },
  {
    path: "/cctv",
    name: "lab1",
    component: About,
  },
  {
    path: "/alert",
    name: "alert",
    component: Alert,
  },
  {
    path: "/ctr",
    name: "ctr",
    component: Ctr,
  },
  
];

const router = createRouter({
  history: createWebHistory(),routes
});

export default router;

  
