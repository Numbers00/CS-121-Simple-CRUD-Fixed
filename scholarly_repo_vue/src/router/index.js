import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
    props: true
  },
  {
    path: '/authors',
    name: 'Authors',
    component: () => import('../views/Authors.vue'),
    props: true
  },
  {
    path: '/categories/:category_slug',
    name: 'Category',
    component: () => import('../views/Category.vue'),
    props: true
  },
  {
    path: '/:author_slug',
    name: 'AuthorDetails',
    component: () => import('../views/AuthorDetails.vue'),
    props: true
  },
  {
    path: '/search',
    name: 'Search',
    component: () => import('../views/Search.vue'),
    props: true
  },
  {
    path: '/changepage',
    name: 'ChangePage',
    component: () => import('../views/ChangePage.vue'),
    props: true
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
