<template>
  <div class="movie-select">
    <h1>[ 장르 선택 ]</h1>
    <div class="poster">
      <p class="post"></p>
    </div>
    <h1>[ 국가 선택 ]</h1>
    <div class="poster">
      <p class="post"></p>
    </div>
    <h1>[ 배우 선택 ]</h1>
    <div class="poster">
      <p class="post2"></p>
    </div>
    <h1>[ 감독 선택 ]</h1>
    <div class="poster">
      <p class="post2"></p>
    </div>

    <h4 class="select-end-btn" @click="goToDetail">최종 선택</h4>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 최종 선택 클릭 시, 선택 결과 페이지로 이동하기
const goToDetail = function () {
  router.push({ name: 'choice_detail' })
}

// 영화 상세 정보 받아오기
onMounted(() => {
  axios({
    method: 'get',
    url: ''
  })
    .then((res) => { })
    .catch((err) => console.log(err))
})
</script>

<style scoped>
.movie-select {
  color: white;
  text-align: center;
}

.movie-select h1 {
  margin: 0;
}

.poster {
  display: flex;
  justify-content: space-evenly;
}

.post {
  width: 150px;
  height: 100px;
  background-color: rgb(200, 200, 200);
}

.post:hover,
.post2:hover {
  color: white;
  opacity: 0.75;
}

.post2 {
  width: 150px;
  height: 180px;
  background-color: rgb(200, 200, 200);
}

.select-end-btn {
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  left: 47.3%;
  width: 100px;
  height: 50px;
  border: 1px solid white;
  color: white;
}

.select-end-btn:hover {
  color: white;
  border-style: none;
  background-color: #166AE8;
}
</style>