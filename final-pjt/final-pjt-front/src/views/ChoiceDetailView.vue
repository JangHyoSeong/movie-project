<template>
  <div class="order-list">
    <div class="order-time">시간순</div>
    <div class="order-range">평점순</div>
  </div>

  <div class="poster">
    <p class="post"></p>
    <p class="post"></p>
    <p class="post"></p>
    <p class="post"></p>
    <p class="post"></p>
  </div>

  <div class="movie-content-list">
    <div class="movie-content">
      <p>제목 : 쇼생크 탈출</p>
      <p>방영일 : 24.05.10</p>
      <p>평점 : 5.0</p>
    </div>
    <div class="movie-content">
      <p>제목 : 쇼생크 탈출</p>
      <p>방영일 : 24.05.10</p>
      <p>평점 : 5.0</p>
    </div>
    <div class="movie-content">
      <p>제목 : 쇼생크 탈출</p>
      <p>방영일 : 24.05.10</p>
      <p>평점 : 5.0</p>
    </div>
    <div class="movie-content">
      <p>제목 : 쇼생크 탈출</p>
      <p>방영일 : 24.05.10</p>
      <p>평점 : 5.0</p>
    </div>
    <div class="movie-content">
      <p>제목 : 쇼생크 탈출</p>
      <p>방영일 : 24.05.10</p>
      <p>평점 : 5.0</p>
    </div>
  </div>
  <p class="go-to-select" @click="goToSelect">돌아가기</p>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goToSelect = function () {
  router.push({ name: 'choice' })
}
</script>

<style scoped>
.order-list {
  display: flex;
  padding: 2% 0% 0.5% 3.2%;
}

.order-time,
.order-range {
  width: 50px;
  border: 1px solid white;
  margin: 0.5%;
  padding: 0.5%;
  color: white;
}

.order-time:hover,
.order-range:hover,
.go-to-select:hover {
  background-color: #166AE8;
  border-style: none;
  color: white;
}

.poster,
.movie-content-list {
  display: flex;
  justify-content: space-evenly;
}

.post {
  margin: 0%;
  padding: 0%;
  width: 300px;
  height: 450px;
  background-color: rgb(200, 200, 200);
}

.movie-content {
  width: 300px;
  text-align: center;
  color: white;
}

.go-to-select {
  position: relative;
  left: 47.8%;
  width: 5%;
  color: white;
  padding: 0.5% 0%;
  text-align: center;
  border: 1px solid white;
}
</style>