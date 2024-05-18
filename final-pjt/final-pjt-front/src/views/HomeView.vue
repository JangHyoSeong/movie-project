<template>
  <main>
    <img src="../../public/background_img.png" class="background-img" alt="background_img">

    <div class="main-txt" :class="fadeMode">
      <div class="main-explan-txt">
        <h5>어떤 영화를 찾으시나요?</h5>
        <h1>당신을 위한 영화 추천 사이트</h1>
        <h5>다양한 시각에서 영화를 추천해드립니다</h5>
      </div>

      <div class="recommend-btn" @click="recommend">
        <h2 class="recommend">추천 받기</h2>
      </div>

      <div class="movie-info-cnt">
        <div class="movie-animation">
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
        </div>
        <h3 class="scroll">Scroll ▽</h3>
      </div>
    </div>
  </main>

  <section>
    <div class="section-movie">
      <h1>[ 현재 개봉작 ]</h1>
      <div class="movies-poster">
        <div @click="newMovieDetail(movie)" v-for="movie in currentMovies1" :key="movie.movie_id">
          <img :src="movie.poster" class="poster" alt="#">
        </div>
        <h1 class="arrow arrow1-1" @click="showNextPoster1_1">
          < </h1>
            <h1 class="arrow arrow1-2" @click="showNextPoster1_2"> > </h1>
      </div>

      <h1>[ 개봉 예정작 ]</h1>
      <div class="movies-poster">
        <div @click="newMovieDetail(movie)" v-for="movie in currentMovies2" :key="movie.movie_id">
          <img :src="movie.poster" class="poster" alt="#">
        </div>
        <h1 class="arrow arrow2-1" @click="showNextPoster2_1">
          < </h1>
            <h1 class="arrow arrow2-2" @click="showNextPoster2_2"> > </h1>
      </div>
    </div>

    <div class="sns-logo">
      <a href="https://blog.naver.com/ehdgus3726"><img src="../../public/blog.png" alt="blog"></a>
      <a href="https://www.instagram.com/"><img src="../../public/instagram.png" alt="instagram"></a>
      <a href="https://www.youtube.com/"><img src="../../public/youtube.png" alt="youtube"></a>
    </div>

    <p class="copyright">Copyright ⓒ 2024. SSAFY All Right Reserved</p>

    <!-- 배경 화면만 보이기 -->
    <h5 @click="modeOn" class='mode-btn'>배경 ON</h5>

  </section>

  <Login />
  <Signup />
</template>

<script setup>
import 'animate.css'
import axios from 'axios'
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Login from '@/components/Login.vue'
import Signup from '@/components/Signup.vue'

const router = useRouter()

// 추천 받기 클릭 시, Choice 페이지로 이동
const recommend = function () {
  router.push({ name: 'choice' })
}

// 포스터 클릭 시, 영화 Detail 페이지로 이동하기
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

// 관리하는 인덱스
const startIndex1 = ref(0)
const endIndex1 = ref(6)
const startIndex2 = ref(0)
const endIndex2 = ref(6)

// 현재 영화 목록
const currentMovies1 = computed(() => {
  return moviesList.value.slice(startIndex1.value, endIndex1.value)
})
const currentMovies2 = computed(() => {
  return moviesList.value.slice(startIndex2.value, endIndex2.value)
})

// 현재 포스터 표시
const showNextPoster1_1 = () => {
  if (startIndex1.value !== 0) {
    startIndex1.value -= 1
    endIndex1.value -= 1
  }
}
const showNextPoster1_2 = () => {
  if (endIndex1.value !== moviesList.value.length) {
    startIndex1.value += 1
    endIndex1.value += 1
  } else {
    startIndex1.value = 0
    endIndex1.value = 6
  }
}
// 다음 포스터 표시
const showNextPoster2_1 = () => {
  if (startIndex2.value !== 0) {
    startIndex2.value -= 1
    endIndex2.value -= 1
  }
}

const showNextPoster2_2 = () => {
  if (endIndex2.value !== moviesList.value.length) {
    startIndex2.value += 1
    endIndex2.value += 1
  } else {
    startIndex2.value = 0
    endIndex2.value = 6
  }
}

// 클릭 시, 모드 전환 활성화 (메인 화면만 보이게 되기)
const fadeMode = ref()

const modeOn = function () {
  if (fadeMode.value === false || fadeMode.value === 'fade-out') {
    fadeMode.value = 'fade-in';
  } else {
    fadeMode.value = 'fade-out';
  }
}
</script>

<style scoped>
.mode-btn {
  position: absolute;
  top: 91%;
  right: 4%;
  padding: 0.5%;
  color: white;
  border: 1px solid white;
  border-radius: 100%;
}

.mode-btn:hover {
  background-color: #166AE8;
  border: none;
}

.fade-in {
  opacity: 1;
  animation: fadeIn 2s forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

.fade-out {
  opacity: 1;
  animation: fadeOut 2s forwards;
}

@keyframes fadeOut {
  from {
    opacity: 1;
  }

  to {
    opacity: 0;
  }
}

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
  position: relative;
  text-align: center;
  font-size: 200%;
  color: white;
  /* 움직이는 애니메이션 */
  animation: moveLeft 2s;
}

/* 애니메이션 위치 영역 */
@keyframes moveLeft {
  0% {
    left: -100%;
  }

  100% {
    left: 0%;
  }
}

/* 추천 받기 버튼 */
.recommend {
  position: relative;
  left: 44.5%;
  width: 9%;
  padding: 1%;
  color: white;
  text-align: center;
  border: 1px solid white;
  border-radius: 10%;
}

.recommend-btn {
  position: relative;
  /* 움직이는 애니메이션 */
  animation: moveRight 2s;
}

/* 애니메이션 위치 영역 */
@keyframes moveRight {
  0% {
    right: -100%;
  }

  100% {
    right: 0%;
  }
}

.recommend:hover {
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

/* 움직이는 애니메이션 */
.movie-animation {
  position: relative;
  animation: moveUp 2s;
}

/* 애니메이션 위치 영역 */
@keyframes moveUp {
  0% {
    top: -100vh;
  }

  100% {
    top: 0;
  }
}

/* 스크롤 글자 */
.scroll {
  position: relative;
  text-align: center;
  color: white;
  margin-top: 7vh;
  /* 움직이는 애니메이션 */
  animation: moveUpDown 2s infinite;
}

/* 애니메이션 위치 영역 */
@keyframes moveUpDown {
  0% {
    top: 0;
  }

  50% {
    top: 10px;
  }

  100% {
    top: 0;
  }
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
  /* 크기 커지는 애니메이션 */
  transform: scale(1.1);
}

.arrow {
  position: absolute;
  padding-bottom: 2.5%;
  font-size: 200%;
  width: 3.5%;
  height: 2%;
  border: 3px solid white;
  border-radius: 100%;
  color: gray;
  background-color: white;
  opacity: 0.75;
}

.arrow1-1 {
  left: 1%;
  bottom: 68%;
}

.arrow1-2 {
  right: 1%;
  bottom: 68%;
}

.arrow2-1 {
  left: 1%;
  bottom: 22.5%;
}

.arrow2-2 {
  right: 1%;
  bottom: 22.5%;
}

.arrow1-1:hover,
.arrow1-2:hover,
.arrow2-1:hover,
.arrow2-2:hover {
  opacity: 1;
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
  transform: scale(1.2);
  /* 크기 커지는 애니메이션 */
}

/* 저작권 글자 */
.copyright {
  text-align: center;
  color: white;
}
</style>