<template>
  <div>
    <div class="order-list">
      <div @click="orderByNew" class="order-time">시간순</div>
      <div @click="orderByScore" class="order-range">평점순</div>
    </div>

    <div v-if="movies.length > 0">
      <div class="poster">
        <img :src="movies[0].poster" alt="#" class="post" @click="newMovieDetail(movies[0])">
      </div>

      <div v-if="movies.length > 0" class="movie-content-list">
        <div class="movie-content">
          <p>제목 : {{ movies[0].title }}</p>
          <p>방영일 : {{ movies[0].opening_date }}</p>
          <p>평점 : {{ movies[0].review_score }}</p>
        </div>
      </div>
    </div>
    <p class="go-to-select" @click="goToSelect">돌아가기</p>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 포스터 클릭 시, 영화 Detail 페이지로 이동하기
const newMovieDetail = function (movie) {
  router.push({ name: 'movieDetail', params: { movie_id: movie.movie_id } })
}

const props = defineProps({
  selectData: Object
})

// 돌아가기 클릭 시, 선택 페이지로 이동하기
const goToSelect = () => {
  router.push({ name: 'choice' })
}

// 필터링 된 영화 받아오기
const movies = ref([])

const genre = props.selectData.genre ? props.selectData.genre : null
const country = props.selectData.country ? props.selectData.country : null
const actor_code = props.selectData.actor ? props.selectData.actor.actor_code : null
const producer = props.selectData.producer ? props.selectData.producer.producer_id : null

onMounted(() => {
  console.log(props.selectData)
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/choice/result/',
    params: {
      genre: genre,
      country: country,
      actor: actor_code,
      producer: producer,
    }
  })
    .then((res) => {
      movies.value = res.data
      console.log(movies.value)
    })
    .catch(err => console.log(err))
})

// 리뷰 목록 가져오기
const reviews = ref([])

// 리뷰 최신순 정렬
const orderByNew = function () {
  reviews.value.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
}

// 리뷰 평점순 정렬
const orderByScore = function () {
  reviews.value.sort((a, b) => b.score - a.score)
}
</script>

<style scoped>
.order-list {
  display: flex;
  padding: 2% 0% 0.5% 3.2%;
}

.order-time,
.order-range {
  width: 40px;
  border: 1px solid white;
  margin: 0.5%;
  padding: 0.2% 0.5%;
  color: white;
  z-index: 1;
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
  width: 300px;
  height: 450px;
  z-index: 1;
  border-radius: 20px;
  cursor: pointer;
  padding: 3px;
  box-sizing: border-box;
  background-image: linear-gradient(145deg, transparent 35%, #e81cff, #40c9ff);
  background-size: 200% 100%;  /* background-size를 추가 */
  background-position: 0% 50%;  /* 초기 background-position을 설정 */
  animation: gradient 2.5s ease infinite;
}

@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}


.post:hover {
  opacity: 0.75;
  transform: scale(1.05);
  /* 크기 커지는 애니메이션 */
}

.movie-content {
  width: 290px;
  text-align: center;
  color: white;
}

.go-to-select {
  position: relative;
  left: 47.5%;
  width: 5%;
  color: white;
  padding: 0.5% 0%;
  text-align: center;
  border: 1px solid white;
}
</style>
