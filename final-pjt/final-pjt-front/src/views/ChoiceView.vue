<template>
  <div class="movie-select">
    <h2>[ 장르 선택 ]</h2>
    <div class="poster">
      <div v-for="genre in currentGenres" :key="genre.genre_id">
        <p class="post-txt">{{ genre.genre }}</p>
      </div>
      <h1 class="arrow arrow1" @click="showNextGenre">></h1>
    </div>

    <h2>[ 국가 선택 ]</h2>
    <div class="poster">
      <div v-for="country in currentCountries" :key="country.country_id">
        <p class="post-txt">{{ country.country }}</p>
      </div>
      <h1 class="arrow arrow2" @click="showNextCountry">></h1>
    </div>

    <h2>[ 배우 선택 ]</h2>
    <div class="poster">
      <div v-for="actor in currentActors" :key="actor.actor_id">
        <img :src="actor.profile_image" class="post-img" alt="#">
        <p class="actor-name">{{ actor.actor }}</p>
      </div>
      <h1 class="arrow arrow3" @click="showNextActor">></h1>
    </div>

    <h2>[ 감독 선택 ]</h2>
    <div class="poster">
      <div v-for="producer in currentProducers" :key="producer.producer_id">
        <img :src="producer.profile_image" class="post-img" alt="#">
        <p class="product-name">{{ producer.producer }}</p>
      </div>
      <h1 class="arrow arrow4" @click="showNextProducer">></h1>
    </div>

    <div class="btn">
      <h4 class="select-end-btn" @click="goToHome">홈으로</h4>
      <h4 class="select-end-btn" @click="goToDetail">최종 선택</h4>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 최종 선택 클릭 시, 선택 결과 페이지로 이동하기
const goToDetail = () => {
  router.push({ name: 'choice_detail' })
}

const goToHome = () => {
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
      genres.value = res.data.genres
      countries.value = res.data.countries
      actors.value = res.data.actors
      producers.value = res.data.producers
    })
    .catch((err) => console.log(err))
})

// 관리하는 인덱스
const startIndexGenre = ref(0)
const endIndexGenre = ref(6)
const startIndexCountry = ref(0)
const endIndexCountry = ref(6)
const startIndexActor = ref(0)
const endIndexActor = ref(6)
const startIndexProducer = ref(0)
const endIndexProducer = ref(6)

// 현재 항목 목록
const currentGenres = computed(() => {
  return genres.value.slice(startIndexGenre.value, endIndexGenre.value)
})

const currentCountries = computed(() => {
  return countries.value.slice(startIndexCountry.value, endIndexCountry.value)
})

const currentActors = computed(() => {
  return actors.value.slice(startIndexActor.value, endIndexActor.value)
})

const currentProducers = computed(() => {
  return producers.value.slice(startIndexProducer.value, endIndexProducer.value)
})

// 포스터 표시
const showNextGenre = () => {
  if (endIndexGenre.value < genres.value.length) {
    startIndexGenre.value += 1
    endIndexGenre.value += 1
  } else {
    startIndexGenre.value = 0
    endIndexGenre.value = 6
  }
}

const showNextCountry = () => {
  if (endIndexCountry.value < countries.value.length) {
    startIndexCountry.value += 1
    endIndexCountry.value += 1
  } else {
    startIndexCountry.value = 0
    endIndexCountry.value = 6
  }
}

const showNextActor = () => {
  if (endIndexActor.value < actors.value.length) {
    startIndexActor.value += 1
    endIndexActor.value += 1
  } else {
    startIndexActor.value = 0
    endIndexActor.value = 6
  }
}

const showNextProducer = () => {
  if (endIndexProducer.value < producers.value.length) {
    startIndexProducer.value += 1
    endIndexProducer.value += 1
  } else {
    startIndexProducer.value = 0
    endIndexProducer.value = 6
  }
}
</script>

<style scoped>
.arrow {
  position: absolute;
  padding-bottom: 2.5%;
  right: 0%;
  font-size: 200%;
  width: 3.5%;
  height: 2%;
  border: 3px solid white;
  border-radius: 100%;
  color: gray;
  background-color: white;
  opacity: 0.75;
}

.arrow1:hover,
.arrow2:hover,
.arrow3:hover,
.arrow4:hover {
  opacity: 1;
}

.arrow1 {
  bottom: 85%;
}

.arrow2 {
  bottom: 68%;
}

.arrow3 {
  bottom: 45%;
}

.arrow4 {
  bottom: 15%;
}

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
  transform: scale(1.1);
}

.post-img:hover {
  opacity: 0.5;
  transform: scale(1.1);
}

.post-img:hover+.actor-name {
  display: block !important;
}

.post-img:hover+.product-name {
  display: block !important;
}

.actor-name {
  position: absolute;
  top: 55%;
  font-size: 175%;
  font-weight: bold;
  display: none;
}

.product-name {
  position: absolute;
  top: 85%;
  font-size: 175%;
  font-weight: bold;
  display: none;
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
