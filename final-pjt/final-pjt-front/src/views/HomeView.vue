<template>
  <img src="../../public/background_img.png" alt="background_img" class="background_img">

  <div class="on-background">
    <div class="main_txt">
      <h5>어떤 영화를 찾으시나요?</h5>
      <h1>당신을 위한 영화 추천 사이트</h1>
      <h5>당신의 선택을 통하여 다양한 시각에서 영화를 추천해드립니다</h5>
    </div>

    <p class="recommend-btn" @click="recommend">추천 받기</p>

    <div class="movie_info_cnt">
      <div class="movie_cnt">
        <h2>{{ movieCount }}</h2>
        <h2>{{ genreCount }}</h2>
        <h2>{{ producerCount }}</h2>
        <h2>{{ actorCount }}</h2>
        <h2>{{ countryCount }}</h2>
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

    <div class="under-background-movie">
      <div class="new-entire-movie">
        <h1>[ 현재 개봉작 ]</h1>
        <div class="new-movie">
          <div @click="newMovieDetail(movie)" v-for="movie in moviesList">
            <img :src="movie.poster" class="post" alt="#">
          </div>
        </div>

        <h1>[ 개봉 예정작 ]</h1>
        <div class="new-movie">
          <div @click="newMovieDetail(movie)" v-for="movie in moviesList">
            <img :src="movie.poster" class="post" alt="#">
          </div>
        </div>
      </div>

    </div>

    <div class="footer">
      <div class="sns-logo">
        <a href="https://blog.naver.com/ehdgus3726"><img src="../../public/blog.png" alt="blog"></a>
        <a href="https://www.instagram.com/"><img src="../../public/instagram.png" alt="instagram"></a>
        <a href="https://www.youtube.com/"><img src="../../public/youtube.png" alt="youtube"></a>
      </div>
      <div class="copy">Copyright ⓒ 2024. SSAFY All Right Reserved</div>
    </div>
  </div>
  <Login />
  <Signup />
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Login from '@/components/Login.vue'
import Signup from '@/components/Signup.vue'

const router = useRouter()

// 추천 받기 클릭 시, Choice 페이지로 이동
const recommend = function () {
  router.push({ name: 'choice' })
}

// 포스터 클리 시, 영화 Detail 페이지로 이동하기
const newMovieDetail = function (movie) {
  router.push({ name: 'movieDetail', params: { movie_id: movie.movie_id } })
}

// 영화 정보 개수
const movieCount = ref(0)
const genreCount = ref(0)
const producerCount = ref(0)
const actorCount = ref(0)
const countryCount = ref(0)
const moviesList = ref([])

// 영화 정보 개수 받아오기
onMounted(() => {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/main/'
  })
    .then((res) => {
      movieCount.value = res.data.movie_count
      genreCount.value = res.data.genre_count
      producerCount.value = res.data.producer_count
      actorCount.value = res.data.actor_count
      countryCount.value = res.data.country_count
    })
    .catch(err => console.log(err))
})

//  영화 리스트 받아오기
onMounted(() => {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/movies/'
  })
    .then((res) => {
      moviesList.value = res.data
    })
    .catch(err => console.log(err))
})
</script>

<style scoped>
/* 사이트 크기 */
.on-background {
  height: 2000px;
}

/* 배경 이미지 */
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
  height: 10.5%;
}

.movie_cnt,
.movie_info {
  display: flex;
  justify-content: space-around;
  color: white;
}


/* 추천 받기 버튼 */
.recommend-btn {
  position: absolute;
  top: 50%;
  left: 45.3%;
  color: white;
  font-size: 200%;
  border: 1px solid white;
  padding: 1%;
}

.recommend-btn:hover {
  background-color: #166AE8;
  border-style: none;
}

.scroll {
  display: flex;
  justify-content: center;
  color: white;
  margin-top: 1.5%;
}

/* 상영 영화 목록 */
.under-background-movie {
  width: 100%;
  height: 55.5%;
}

.under-background-movie h1 {
  position: relative;
  top: 26%;
  text-align: center;
  color: white;
}

.new-entire-movie {
  position: relative;
  top: 27%;
  left: 8%;
  width: 85%;
}

.new-movie {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  color: white;
}

.post {
  width: 240px;
  height: 300px;
  background-color: rgb(200, 200, 200);
}

/* footer */
.footer {
  display: flex;
  width: 100%;
  height: 3%;
  background-color: black;
}

.sns-logo {
  display: flex;
  width: 15%;
}

.sns-logo a {
  padding-left: 10%;
}

.sns-logo img {
  height: 50%;
}

.copy {
  position: absolute;
  bottom: -124%;
  left: 8%;
  width: 85%;
  text-align: center;
  color: white;
}
</style>