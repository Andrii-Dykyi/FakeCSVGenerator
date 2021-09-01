import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import SchemaCreate from '../views/SchemaCreate.vue'
import SchemaDetail from '../views/SchemaDetail.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/new-schema/',
    name: 'newSchema',
    component: SchemaCreate
  },
  {
    path: '/my-schema/:id/',
    name: 'mySchema',
    component: SchemaDetail
  },
  {
    path: '/login/',
    name: 'Login',
    component: Login
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
