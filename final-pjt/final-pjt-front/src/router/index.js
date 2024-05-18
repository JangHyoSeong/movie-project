import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ChoiceDetailView from '@/views/ChoiceDetailView.vue'
import ChoiceView from '@/views/ChoiceView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import OverviewView from '@/views/MovieDetail/OverviewView.vue'
import ReviewView from '@/views/MovieDetail/ReviewView.vue'
import RecommendView from '@/views/MovieDetail/RecommendView.vue'
import ChatView from '@/views/MovieDetail/ChatView.vue'
import ProfileView from '@/views/ProfileView.vue'

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
      component: MovieDetailView,
      children: [
        {path: '', name: 'movie-overview', component: OverviewView, props: true},
        {path: 'review', name: 'movie-review', component: ReviewView, props: true},
        {path: 'recommend', name: 'movie-recommend', component: RecommendView, props: true},
        {path: 'chat', name: 'movie-chat', component: ChatView, props: true},
      ]
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    }
  ]
})

export default router
