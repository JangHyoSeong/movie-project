<template>
  <div>
    <div class="order-list">
      <div class="order-time">시간순</div>
      <div class="order-range">평점순</div>
    </div>

    <div v-if="movies.length > 0">
    <div class="poster">
      <img :src="movies[0].poster" alt="" class="post">
    </div>

    <div class="movie-content-list">
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

const props = defineProps({
  selectData: Object
})
const router = useRouter()

// 돌아가기 클릭 시, 선택 페이지로 이동하기
const goToSelect = function () {
  router.push({ name: 'choice' })
}

// 필터링 된 영화 받아오기

const movies = ref([])
onMounted(() => {
  console.log(props.selectData)
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/choice/result/',
    params: {
      genre: props.selectData.genre,
      country: props.selectData.country,
      actor: props.selectData.actor,
      producer: props.selectData.producer
    }
  })
    .then((res) => {
      movies.value = res.data
      console.log(movies.value)
    })
    .catch(err => console.log(err))
})
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
  margin: 0%;
  padding: 0%;
  width: 300px;
  height: 450px;
  background-color: rgb(200, 200, 200);
  z-index: 1;
}

.post:hover {
  opacity: 0.75;
  transform: scale(1.05); /* 크기 커지는 애니메이션 */
}

.movie-content {
  width: 300px;
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