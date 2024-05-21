<template>
  <div>
    <div class="profile-container">
      <h1>좋아요</h1>
      <div class="like-container">
        <div v-for="movie in userData.like_movies" class="like-post">
          <img :src="movie.poster" alt="#" width="200px" @click="goToMovie(movie.movie_id)">
        </div>
      </div>
    </div>

    <hr>

    <div class="profile-container">
      <h1>리뷰</h1>
      <div class="review-container">
        <div v-for="movie in reviewList" class="review-post">
          <img :src="movie.poster" alt="#" width="200px" @click="goToMovieReview(movie.movie_id)">
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useLoginStore } from '@/stores/login'
import axios from 'axios'

const store = useLoginStore()
const router = useRouter()

const props = defineProps({
  userData: Object,
})

// 리뷰 쓴 영화 목록
const reviewList = computed(() => {
  if (!props.userData || !props.userData.review_movies) {
    return []
  }
  const seenTitles = new Set()
  return props.userData.review_movies.filter(movie => {
    const isDuplicate = seenTitles.has(movie.title)
    seenTitles.add(movie.title)
    return !isDuplicate
  })
})

// 영화 상세정보로 이동
const goToMovie = function (movie_id) {
  router.push({name: "movieDetail", params: {movie_id: movie_id}})
}

const goToMovieReview = function (movie_id) {
  router.push({name: "movie-review", params: {movie_id: movie_id}})
}
</script>

<style scoped>

.profile-container {
  position: relative;
  left: 3%;
  width: 95%;
  color: white;
}
.like-container {
  display: flex;
}

hr {
  width: 95%;
}

.like-post {
  display: flex;
  padding-left: 1%;
}

.review-container {
  display: flex;
}

.review-post {
  display: flex;
  padding-left: 1%;
}
</style>