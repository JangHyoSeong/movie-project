import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ChoiceDetailView from '@/views/ChoiceDetailView.vue'
import ChoiceView from '@/views/ChoiceView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/choice',
      name: 'choice',
      component: ChoiceView
    },
    {
      path: '/choice_detail',
      name: 'choice_detail',
      component: ChoiceDetailView
    },
    {
      path: '/movie/:movie_id',
      name: 'movieDetail',
      component: MovieDetailView
    },
  ]
})

export default router
