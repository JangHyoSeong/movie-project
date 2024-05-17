<template>
  <img src="../../public/background_img.png" alt="background_img" class="background_img">
  
  <div class="background">
    <div class="main_txt">
      <h5>어떤 영화를 찾으시나요?</h5>
      <h1>당신을 위한 영화 추천 사이트</h1>
      <h5>당신의 선택을 통하여 다양한 각도에서 영화를 추천해드립니다</h5>
    </div>

    <p class="recommend-btn" @click="recommend">추천 받기</p>

    <div class="movie_info_cnt">
      <div class="movie_cnt">
        <h2>999</h2>
        <h2>100</h2>
        <h2>100</h2>
        <h2>100</h2>
        <h2>100</h2>
      </div>
      <div class="movie_info">
        <h2>영화 수</h2>
        <h2>장르 수</h2>
        <h2>감독 수</h2>
        <h2>배우 수</h2>
        <h2>국가 수</h2>
      </div>
      <h3 class="scroll">Scroll ▽</h3>
    </div>

    <div class="new_movie">
      <h1>[ 현재 개봉작 ]</h1>
        <div class="poster">
          <p class="post"></p>
          <p class="post"></p>
          <p class="post"></p>
          <p class="post"></p>
          <p class="post"></p>
          <p class="post"></p>
        </div>
      <h1>[ 개봉 예정작 ]</h1>
      <div class="poster">
          <p class="post"></p>
          <p class="post"></p>
          <p class="post"></p>
          <p class="post"></p>
          <p class="post"></p>
          <p class="post"></p>
        </div>
    </div>
  </div>
  <Login />
  <Signup />
</template>

<script setup>
import { useRouter } from 'vue-router'
import Login from '@/components/Login.vue'
import Signup from '@/components/Signup.vue'

const router = useRouter()

const recommend = function () {
  router.push({name: 'choice'})
  console.log('fdsfds')
}
</script>

<style scoped>
/* 배경 사이즈 */
.background {
  height: 2000px;
}
.background_img {
  position: absolute;
  width: 100%;
  height: 100%;
  z-index: -1;
}

/* 메인화면 텍스트 */
.main_txt {
  position: relative;
  top: 5%;
  text-align: center;
  width: 100%;
  height: 30%;
  font-size: 200%;
  color: white;
  z-index: -1;
}

/* 영화 정보 개수 */
.movie_info_cnt {
  width: 100%;
  height: 13.5%;
}
.movie_cnt, .movie_info {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  color: white;
}
.scroll {
  display: flex;
  justify-content: center;
  color: white;
}

/* 추천 받기 버튼 */
.recommend-btn {
  position: absolute;
  top: 50%;
  left: 46%;
  color: white;
  font-size: 200%;
  border: 1px solid white;
  padding: 1%;
}
.recommend-btn:hover {
  background-color: #166AE8;
  border-style: none;
}

/* 상영 영화 목록 */
.new_movie {
  width: 100%;
  height: 55%;
  background-color: rgb(255, 132, 132);
  text-align: center;
}
.poster {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}
.post {
  width: 200px;
  height: 250px;
  background-color: gray;
}
</style>