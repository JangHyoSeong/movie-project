<template>

  <main>
    <img src="../../public/background_img.png" class="background-img" alt="background_img">

    <div class="main-txt">
      <div class="main-explan-txt">
        <h5>어떤 영화를 찾으시나요?</h5>
        <h1>당신을 위한 영화 추천 사이트</h1>
        <h5>다양한 시각에서 영화를 추천해드립니다</h5>
      </div>

      <h1 class="recommend-btn" @click="recommend">추천 받기</h1>

      <div class="movie-info-cnt">
        <div class="movie-cnt">
          <h2>{{ movieCount }}</h2>
          <h2>{{ genreCount }}</h2>
          <h2>{{ producerCount }}</h2>
          <h2>{{ actorCount }}</h2>
          <h2>{{ countryCount }}</h2>
        </div>
        <div class="movie-cnt">
          <h2>영화 수</h2>
          <h2>장르 수</h2>
          <h2>감독 수</h2>
          <h2>배우 수</h2>
          <h2>국가 수</h2>
        </div>
        <h3 class="scroll">Scroll ▽</h3>
      </div>
    </div>
  </main>

  <section>
    <div class="section-movie">
      <h1>[ 현재 개봉작 ]</h1>
      <div class="movies-poster">
        <div @click="newMovieDetail(movie)" v-for="movie in moviesList">
          <img :src="movie.poster" class="poster" alt="#">
        </div>
      </div>

      <h1>[ 개봉 예정작 ]</h1>
      <div class="movies-poster">
        <div @click="newMovieDetail(movie)" v-for="movie in moviesList">
          <img :src="movie.poster" class="poster" alt="#">
        </div>
      </div>
    </div>

    <div class="sns-logo">
      <a href="https://blog.naver.com/ehdgus3726"><img src="../../public/blog.png" alt="blog"></a>
      <a href="https://www.instagram.com/"><img src="../../public/instagram.png" alt="instagram"></a>
      <a href="https://www.youtube.com/"><img src="../../public/youtube.png" alt="youtube"></a>
    </div>

    <p class="copyright">Copyright ⓒ 2024. SSAFY All Right Reserved</p>
  </section>

  <Login />
  <Signup />
</template>

<script setup>
import 'animate.css'
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
/* 상단 화면 비율 */
main {
  width: 100%;
  height: 88vh;
}

/* 배경 이미지 */
.background-img {
  position: absolute;
  top: 0%;
  width: 100%;
  height: 100%;
  z-index: -1;
}

/* 메인화면 전체 텍스트 */
.main-txt {
  position: relative;
  top: 7vh;
}

/* 메인화면 텍스트 */
.main-explan-txt {
  text-align: center;
  font-size: 200%;
  color: white;
  z-index: -1;
}

/* 추천 받기 버튼 */
.recommend-btn {
  position: relative;
  left: 44%;
  width: 9.2%;
  padding: 1%;
  color: white;
  text-align: center;
  border: 1px solid white;
}

.recommend-btn:hover {
  border-style: none;
  background-color: #166AE8;
}

/* 영화 정보 영역 */
.movie-info-cnt {
  position: relative;
  top: 5vh;
}

/* 영화 정보 갯수 */
.movie-cnt {
  display: flex;
  justify-content: space-around;
  color: white;
}

/* 스크롤 글자 */
.scroll {
  position: relative;
  text-align: center;
  color: white;
  margin-top: 7vh;
  animation: moveUpDown 2s infinite; /* 움직이는 애니메이션 */
}

/* 애니메이션 위치 영역 */
@keyframes moveUpDown {
    0% { top: 0; }
    50% { top: 10px; }
    100% { top: 0; }
}

/* 하단 화면 비율 */
section {
  width: 100%;
  height: 90vh;
}

/* 상영 영화 목록 */
.section-movie {
  height: 90vh;
  position: relative;
  top: 5vh;
  text-align: center;
  color: white;
}

/* 영화 포스터 위치 */
.movies-poster {
  display: flex;
  justify-content: space-evenly;
}

/* 영화 포스터 크기 */
.poster {
  width: 24vh;
  height: 32vh;
}

.poster:hover {
  opacity: 0.75;
  transform: scale(1.1); /* 크기 커지는 애니메이션 */
}

/* SNS 로고 영역 */
.sns-logo {
  position: absolute;
  display: flex;
  height: 8vh;
}


/* SNS 로고 이미지 */
.sns-logo img {
  padding: 1vh 0vh 0vh 3vh;
  height: 4vh;
}

.sns-logo img:hover {
  transform: scale(1.2); /* 크기 커지는 애니메이션 */
}

/* 저작권 글자 */
.copyright {
  text-align: center;
  color: white;
}
</style>