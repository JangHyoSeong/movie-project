<template>
  <div class="profile-container">
    <h1>좋아요</h1>
    <div class="like-container">
      <div v-for="movie in userData.like_movies" class="like-post">
        <img :src="movie.poster" alt="#" width="200px">
      </div>
    </div>
  </div>

  <hr>

  <div class="profile-container">
    <h1>리뷰</h1>
    <div class="review-container">
      <p>{{ reviewMovie }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useLoginStore } from '@/stores/login'
import axios from 'axios'

const store = useLoginStore()

const props = defineProps({
  userData: Object,
})

// 유저가 리뷰를 작성한 영화들의 id 배열
const reviewMovie = computed(() => {
  console.log(props.userData)
  return props.userData.review_movies
})

// 유저가 작성한 리뷰 목록을 저장할 변수
const reviewList = ref([])

const loadReview = function () {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/profile/reviews/',
    data: {
      movie: reviewMovie.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      reviewList.value = res.data
    })
    .catch(err => console.log(err))
}

onMounted(() => {
  loadReview()
})
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
</style>