import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/csv-reader',
      name: 'csv-reader',
      component: () => import('../views/CsvReader.vue'),
    },

    {
      path: '/dashboard',
      name: 'Dashboard',
      component: () => import('../views/Dashboard.vue'),
    }
  ],
})

export default router
