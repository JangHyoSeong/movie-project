<template>
  <h5 class="select-end-btn" @click="goToHome">홈으로</h5>
  
  <div class="background">
    <!-- 배경 이미지 -->
    <div class="background-filter">
      <img :src="backgroundImageSrc" alt="snapshot" />
      <!-- 그라데이션 오버레이 -->
      <div class="overlay"></div>
    </div>

    <!-- 내용 컨테이너 -->
    <div class="content-container">
      <!-- 영화 상세 정보 -->
      <article class="detail-container">
        <h1>{{ title }}</h1>
        <p>장르 : {{ genre.join(', ') }}</p>
        <p>국가 : {{ country }}</p>
        <p>개봉 상태 : {{ status }}</p>
        <p v-if="runningTime">러닝타임 : {{ runningTime }}분</p>
        <p v-if="openingDate">개봉 일자 : {{ openingDate }}</p>
      </article>
      <!-- 유튜브 플레이어 -->
      <div class="youtube-container">
        <iframe width="576" height="324" :src="videoUrl" frameborder="0"
          allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
        </iframe>
      </div>
    </div>

    <!-- 영화 선택 네비게이션 -->
    <div class="view-container">
      <MovieDetailNav :movie="movie" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import MovieDetailNav from '@/components/MovieDetailNav.vue'

const router = useRouter()

// 홈으로 클릭 시, 메인 페이지로 이동하기
const goToHome = () => {
  router.push({ name: 'home' })
  window.scrollTo(0, 0) // 이동 시 가장 최상단 고정
}

// 변수
const backgroundImageSrc = ref(null);
const title = ref('')
const overView = ref('');
const genre = ref([]);
const country = ref('');
const runningTime = ref('');
const status = ref('')
const openingDate = ref('')
const movie = ref('')

const route = useRoute();
const videoUrl = ref(null)

onMounted(() => {
  // 영화 정보 로드
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/movie/${route.params.movie_id}/`,
  })
    .then((res) => {
      movie.value = res.data
      backgroundImageSrc.value = res.data.snapshots[0].snapshot
      title.value = res.data.title
      overView.value = res.data.overview
      genre.value = res.data.genre
      country.value = res.data.country
      runningTime.value = res.data.running_time
      if (res.data.show_status == 0) {
        status.value = '개봉'
      } else if (res.data.show_status == 1) {
        status.value = '개봉 예정'
      } else {
        status.value = '기타'
      }
      if (res.data.opening_date) {
        openingDate.value = res.data.opening_date
      }
    })
    .catch(err => console.log(err))
    .then((res) => {
      // 유튜브 트레일러 로드
      // const API_KEY = import.meta.env.VITE_YT_API_KEY

      axios({
        method: 'get',
        url: `https://www.googleapis.com/youtube/v3/search?key=${API_KEY}`,
        params: {
          part: 'snippet',
          q: `${title.value} 트레일러`,
          maxResults: 1,
          type: 'video',
        }
      })
        .then((res) => {
          videoUrl.value = `https://www.youtube.com/embed/${res.data.items[0].id.videoId}?autoplay=1&mute=1`
        })
        .catch(err => console.log(err))
    })
})
</script>

<style scoped>
/* 배경 스냅샷 스타일 */
.background-filter {
  position: absolute;
  width: 100%;
  height: 66%;
}

.background-filter img {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* 그라데이션 오버레이 스타일 */
.overlay {
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(190deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 1) 85%), linear-gradient(270deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.75) 70%);
  pointer-events: none;
  /* 오버레이가 클릭 이벤트를 막지 않도록 */
}

/* 내용 컨테이너 스타일 */
.content-container {
  position: relative;
  top: 3vh;
  left: 3%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* 영화 상세 정보 컨테이너 스타일 */
.detail-container {
  color: white;
  text-align: center;
  padding-bottom: 5%;
  margin-left: 10%;
}

/* 영화 상세 정보 스타일 */
.detail-container>p {
  font-size: 25px;
}

.detail-container>h1 {
  font-size: 40px;
}

/* 유튜브 플레이어 컨테이너 스타일 */
.youtube-container {
  position: absolute;
  top: 14%;
  right: 10%;
}

/* 영화 선택 네비게이션 컨테이너 스타일 */
.view-container {
  top: 10%;
  color: white;
  position: relative;
}

/* 선택 종료 버튼 스타일 */
.select-end-btn {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: 5%;
  left: 2%;
  width: 4%;
  height: 4%;
  border: 1px solid white;
  color: white;
  z-index: 1;
}

/* 선택 종료 버튼 호버 효과 스타일 */
.select-end-btn:hover {
  color: white;
  border-style: none;
  background-color: #166AE8;
}
</style>