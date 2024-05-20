<template>
  <h4 class="select-end-btn" @click="goToHome">Home</h4>

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

        <!-- 좋아요 기능 -->
        <label class="like-container" @click="likeMovie">
          <input type="checkbox">
          <div class="like-checkmark">
            <svg viewBox="0 0 256 256">
              <rect fill="none" height="256" width="256"></rect>
              <path
                d="M224.6,51.9a59.5,59.5,0,0,0-43-19.9,60.5,60.5,0,0,0-44,17.6L128,59.1l-7.5-7.4C97.2,28.3,59.2,26.3,35.9,47.4a59.9,59.9,0,0,0-2.3,87l83.1,83.1a15.9,15.9,0,0,0,22.6,0l81-81C243.7,113.2,245.6,75.2,224.6,51.9Z"
                stroke-width="20px" stroke="#FFF" fill="none"></path>
            </svg>
          </div>
        </label>

      </article>
      <!-- 유튜브 플레이어 -->
      <div class="youtube-container">
        <iframe width="600" height="350" :src="videoUrl" frameborder="0"
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
import { useLoginStore } from '@/stores/login'
import axios from 'axios'
import MovieDetailNav from '@/components/MovieDetailNav.vue'

const router = useRouter()
const store = useLoginStore()

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
      const API_KEY = import.meta.env.VITE_YT_API_KEY

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

// 영화 좋아요 기능
const likeMovie = function () {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/api/v1/${route.params.movie_id}/like/`,
    data: {
      movie_id: route.params.movie_id,
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      // 이 부분은 나중에 좋아요 버튼 색깔이 바뀌는 것으로 수정 바람
      alert('좋아요 성공')
    })
    .catch(err => console.log(err))
}
</script>

<style scoped>
.like-container input {
  position: absolute;
  cursor: pointer;
  opacity: 0;
}

.like-container {
  position: absolute;
  top: 4.5vh;
  left: 15.5vh;
  font-size: 20px;
  user-select: none;
  transition: 100ms;
}

.like-checkmark {
  top: 0;
  left: 0;
  height: 2em;
  width: 2em;
  transition: 100ms;
  animation: dislike_effect 400ms ease;
}

.like-container input:checked~.like-checkmark path {
  fill: #FF5353;
  stroke-width: 0;
}

.like-container input:checked~.like-checkmark {
  animation: like_effect 400ms ease;
}

@keyframes like_effect {
  0% {
    transform: scale(0);
  }

  50% {
    transform: scale(1.2);
  }

  100% {
    transform: scale(1);
  }
}

@keyframes dislike_effect {
  0% {
    transform: scale(0);
  }

  50% {
    transform: scale(1.2);
  }

  100% {
    transform: scale(1);
  }
}

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
  left: 2%;
  display: flex;
  align-items: center;
}

/* 영화 상세 정보 컨테이너 스타일 */
.detail-container {
  color: white;
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
  top: 6%;
  right: 12%;
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