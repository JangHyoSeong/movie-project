<template>
  <div class="movie-select">
    <h2>[ 장르 선택 ]</h2>
    <div div class="poster">
      <div v-for="genre in genres">
        <p class="post-txt">{{ genre.genre }}</p>

      </div>
    </div>

    <h2>[ 국가 선택 ]</h2>
    <div div class="poster">
      <div v-for="count in countries">
        <p class="post-txt">{{ count.country }}</p>
      </div>
    </div>

    <h2>[ 배우 선택 ]</h2>
    <div div class="poster">
      <div v-for="act in actors">
        <img :src="act.profile_image" class="post-img" alt="#">
      </div>
    </div>

    <h2>[ 감독 선택 ]</h2>
    <div div class="poster">
      <div v-for="product in producers">
        <img :src="product.profile_image" class="post-img" alt="#">
      </div>
    </div>

    <div class="btn">
      <h4 class="select-end-btn" @click="goToHome">홈으로</h4>
      <h4 class="select-end-btn" @click="goToDetail">최종 선택</h4>
    </div>
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

const goToHome = function () {
  router.push({ name: 'home' })
}

const genres = ref([])
const countries = ref([])
const actors = ref([])
const producers = ref([])

// 영화 상세 정보 받아오기
onMounted(() => {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/choice/'
  })
    .then((res) => {
      console.log(res.data);
      genres.value = res.data.genres
      countries.value = res.data.countries
      actors.value = res.data.actors
      producers.value = res.data.producers
    })
    .catch((err) => console.log(err))
})
</script>

<style scoped>
.movie-select {
  position: relative;
  left: 8%;
  width: 85%;
  color: white;
  text-align: center;
}

.poster {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}

.post-txt {
  margin: 0%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 150%;
  color: black;
  width: 180px;
  height: 90px;
  background-color: rgb(200, 200, 200);
}

.post-img {
  width: 180px;
  height: 210px;
}

.post-txt:hover {
  font-weight: bold;
  color: white;
  background-color: darkgray;
  transform: scale(1.1); /* 크기 커지는 애니메이션 */
}

.post-img:hover {
  opacity: 0.75;
  transform: scale(1.1); /* 크기 커지는 애니메이션 */
}

.btn {
  display: flex;
}

.select-end-btn {
  margin: 1% 0% 1% 1%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  left: 40.5%;
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