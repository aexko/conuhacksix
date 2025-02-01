import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/csv-reader',
      name: 'csv-reader',
      component: () => import('../views/CsvReader.vue'),
    },
  ],
})

export default router
