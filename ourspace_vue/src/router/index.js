import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PostView from '../views/PostView.vue'
// import CategoryView from '../views/CategoryView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  // Lazy loading the category site.
  {
    path: '/category',
    name: 'category',
    component: () => import(/* webpackChunkName: "about" */ '../views/CategoryView.vue')
  },
  // Lazy loading the post site.
  // {
  //   path: '/post/:postId',
  //   name: 'post',
  //   component: () => import(/* webpackChunkName: "about" */ '../views/PostView.vue')
  // },
  {
    path: '/post/:postId',
    name: 'post',
    component: PostView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
