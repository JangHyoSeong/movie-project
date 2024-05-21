<template>
  <div class="profile-page">
    <div class="profile-content">
      <h1>{{ userData.username }}님의 프로필 페이지</h1>
      <hr>

      <!-- 유저 좋아요 목록 -->
      <div class="like-container">
        <h1>좋아요</h1>
        <div v-for="movie in userData.like_movies">
          <img :src="movie.poster" alt="" width="100px">
        </div>
      </div>

      <!-- 유저 리뷰 목록 -->
      <div class="comment-container">
        <h1>리뷰</h1>
        <p>{{ reviewMovie }}</p>
      </div>

    </div>
  </div>
  <ProfileDetailNav :userData="userData" />
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useLoginStore } from '@/stores/login'
import axios from 'axios'
import ProfileDetailNav from '@/components/ProfileDetailNav.vue'

const store = useLoginStore()

// 유저 데이터를 저장할 변수
const userData = ref([])

// 유저 데이터를 받아오는 함수
const loadUserData = function () {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/profile/',
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      userData.value = res.data
      console.log(userData.value)
    })
    .catch(err => console.log(err))
}

// 페이지가 로드되었을 때 바로 유저 데이터를 가져올 수 있게 함
onMounted(() => {
  loadUserData()
  loadReview()
})

// //  유저 리뷰 목록 데이터 Script
// const props = defineProps({
//   userData: Object,
// })

// // 유저가 리뷰를 작성한 영화들의 id 배열
const reviewMovie = computed(() => {
  return userData.review_movies
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
</script>

<style scoped>
* {
  margin: 0%;
  padding: 0%;
}

.profile-content {
  width: 100%;
  height: 100vh;
  background-color: rgb(200, 200, 200);
}

.profile-content>h1 {
  padding: 1%;
}

.comment-container {
  position: absolute;
  top: 30%;
  left: 42%;
}
</style>