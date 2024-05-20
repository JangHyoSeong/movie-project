<template>
  <div v-if="isLoading" class="loading-screen">
    <div class="loaderBar">
      <h1>Loding</h1>
    </div>
  </div>

  <!-- 3초 후 Loding이 끝나면 실행되는 화면 -->
  <div v-else>
    <!-- 장르 선택 섹션 -->
    <div class="movie-select">
      <h2>[ 장르 선택 ]</h2>
      <div class="poster">
        <!-- 장르 목록 -->
        <div v-for="genre in currentGenres" :key="genre.genre_id">
          <p class="post-txt" @click="genreSelect(genre.genre)"
          :class="{'is-selected' : selectedParams.genre === genre.genre}">{{ genre.genre }}</p>
        </div>
        <!-- 이전/다음 장르 화살표 -->
        <h1 class="arrow arrow5" @click="showPrevGenre">
          &lt; </h1>
        <h1 class="arrow arrow1" @click="showNextGenre"> &gt; </h1>
      </div>

      <!-- 국가 선택 섹션 -->
      <h2>[ 국가 선택 ]</h2>
      <div class="poster">
        <!-- 국가 목록 -->
        <div v-for="country in currentCountries" :key="country.country_id">
          <p 
            class="post-txt" 
            @click="countrySelect(country.country)"
            :class="{'is-selected' : selectedParams.country === country.country}"
          >{{ country.country }}</p>
        </div>
        <!-- 이전/다음 국가 화살표 -->
        <h1 class="arrow arrow6" @click="showPrevCountry">
          &lt; </h1>
        <h1 class="arrow arrow2" @click="showNextCountry"> &gt; </h1>
      </div>

      <!-- 배우 선택 섹션 -->
      <h2>[ 배우 선택 ]</h2>
      <div class="poster">
        <!-- 배우 목록 -->
        <div v-for="actor in currentActors" :key="actor.actor_id" class="actor-poster">
          <img 
            :src="actor.profile_image ? actor.profile_image : '../public/default_img.jpg'"
            class="post-img" alt="#"
            @click="actorSelect(actor.actor)"
            :class="{'is-selected' : selectedParams.actor === actor.actor}"
          >
          <p class="actor-name">{{ actor.actor }}</p>
        </div>
        <!-- 이전/다음 배우 화살표 -->
        <h1 class="arrow arrow7" @click="showPrevActor">
          < </h1>
            <h1 class="arrow arrow3" @click="showNextActor"> > </h1>
      </div>

      <!-- 감독 선택 섹션 -->
      <h2>[ 감독 선택 ]</h2>
      <div class="poster">
        <!-- 감독 목록 -->
        <div v-for="producer in currentProducers" :key="producer.producer_id" class="producer-poster">
          <img 
            :src="producer.profile_image ?  producer.profile_image : '../public/default_img.'" 
            class="post-img" 
            :class="{'is-selected' : selectedParams.producer === producer.producer}"
            alt="#"
            @click="producerSelect(producer.producer)">
          <p class="product-name">{{ producer.producer }}</p>
        </div>
        <!-- 이전/다음 감독 화살표 -->
        <h1 class="arrow arrow8" @click="showPrevProducer">
          < </h1>
            <h1 class="arrow arrow4" @click="showNextProducer"> > </h1>
      </div>

      <!-- 홈으로/최종 선택 버튼 -->
      <div class="btn">
        <h4 class="select-end-btn" @click="goToHome">홈으로</h4>
        <h4 class="select-end-btn" @click="goToDetail" :selectedParams="selectedParams">최종 선택</h4>
      </div>
    </div>

  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, computed, onMounted, watch } from 'vue'
import { useRouter, RouterLink } from 'vue-router'

const isLoading = ref(true);

onMounted(() => {
  setTimeout(() => {
    isLoading.value = false;
  }, 3000); // 3초 후에 로딩 상태를 false로 변경
});


const router = useRouter()

// 부모 컴포넌트로 emit
const emit = defineEmits(['selectEvent'])

// 최종 선택 클릭 시, 선택 결과 페이지로 이동하기
const goToDetail = () => {
  emit('selectEvent', selectedParams)
  router.push({ name: 'choice_detail', props: { selectedParams: selectedParams.value } })
}

// 홈으로 클릭 시, 메인 페이지로 이동하기
const goToHome = () => {
  router.push({ name: 'home' })
  window.scrollTo(0, 0) // 이동 시 가장 최상단 고정
}

// 영화 정보 관련 데이터
const genres = ref([])
const countries = ref([])
const actors = ref([])
const producers = ref([])
const movies = ref([])

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
      movies.value = res.data.movies
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

// 슬라이더를 반대로 이동하는 로직 추가
const showPrevGenre = () => {
  if (startIndexGenre.value !== 0) {
    startIndexGenre.value -= 1
    endIndexGenre.value -= 1
  }
}

const showPrevCountry = () => {
  if (startIndexCountry.value !== 0) {
    startIndexCountry.value -= 1
    endIndexCountry.value -= 1
  }
}

const showPrevActor = () => {
  if (startIndexActor.value !== 0) {
    startIndexActor.value -= 1
    endIndexActor.value -= 1
  }
}

const showPrevProducer = () => {
  if (startIndexProducer.value !== 0) {
    startIndexProducer.value -= 1
    endIndexProducer.value -= 1
  }
}

// 어떤 장르, 국가, 배우, 감독을 선택헀는지 저장할 변수
const selectedParams = ref({
  genre: null,
  country: null,
  actor: null,
  producer: null
})

const genreSelect = function (genre) {
  selectedParams.value.genre = genre
  console.log(selectedParams.value)
}

const countrySelect = function (country) {
  selectedParams.value.country = country
}

const actorSelect = function (actor) {
  selectedParams.value.actor = actor
}

const producerSelect = function (producer) {
  selectedParams.value.producer = producer
}

// 현재 선택된 요소에 따라 영화를 필터링
const filteredMovies = computed(() => {
  return movies.value.filter(movie => {
    return (
      (selectedParams.value.genre === null || selectedParams.value.genre.includes(movie.genre)) &&
      (selectedParams.value.country === null || movie.country === selectedParams.value.country) &&
      (selectedParams.value.actor === null || selectedParams.value.actor.includes(movie.actor)) &&
      (selectedParams.value.producer === null || selectedParams.value.producer.includes(movie.producer))
    )
  })
})

watch(selectedParams, () => {
  console.log('Filtered Movies:', filteredMovies.value)
}, { deep: true })

</script>

<style scoped>
/* 3초동안 Loding 화면 */
.loaderBar {
  width: 30%;
  height: 75px;
  background: #cccccc;
  border-radius: 10px;
  position: absolute;
  top: 50%;
  left: 35%;
  overflow: hidden;
  z-index: -1;
}

.loaderBar h1 {
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1;
  color: white;
}

.loaderBar::before {
  content: "";
  position: absolute;
  height: 100%;
  animation: fillProgress 3s ease-in-out infinite, lightEffect 1s infinite linear;
  animation-fill-mode: forwards;
  z-index: -1;
}



@keyframes fillProgress {
  0% {
    width: 0;
  }

  50% {
    width: 50%;
  }

  100% {
    width: 100%;
  }
}

@keyframes lightEffect {

  0%,
  20%,
  40%,
  60%,
  80%,
  100% {
    background: linear-gradient(137deg, #ffdb3b 10%, #FE53BB 45%, #8F51EA 67%, #0044ff 87%);
  }
}

/* 슬라이더 화살표 스타일 */
.arrow {
  position: absolute;
  padding-bottom: 2.5%;
  font-size: 200%;
  width: 3%;
  height: 1%;
  border: 3px solid white;
  border-radius: 100%;
  color: gray;
  background-color: white;
  opacity: 0.75;
}

/* 화살표에 호버 효과 적용 */
.arrow1:hover,
.arrow2:hover,
.arrow3:hover,
.arrow4:hover,
.arrow5:hover,
.arrow6:hover,
.arrow7:hover,
.arrow8:hover {
  opacity: 1;
}

/* 화살표 위치 및 스타일 조정 */
.arrow1,
.arrow2,
.arrow3,
.arrow4 {
  right: 2.2%;
}

.arrow1,
.arrow5 {
  bottom: 85%;
}

.arrow2,
.arrow6 {
  bottom: 68%;
}

.arrow3,
.arrow7 {
  bottom: 45%;
}

.arrow4,
.arrow8 {
  bottom: 15%;
}

.arrow5,
.arrow6,
.arrow7,
.arrow8 {
  left: 2.2%;
}

/* 영화 선택 영역 스타일 */
.movie-select {
  position: relative;
  left: 8%;
  width: 85%;
  color: white;
  text-align: center;
}

/* 포스터 그룹 스타일 */
.poster {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}

/* 포스터 텍스트 스타일 */
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

/* 포스터 이미지 스타일 */
.post-img {
  width: 180px;
  height: 210px;
  transition: opacity 0.3s, transform 0.3s;
}

/* 포스터 텍스트 호버 효과 스타일 */
.post-txt:hover {
  font-weight: bold;
  color: white;
  background-color: darkgray;
  transform: scale(1.1);
}

/* 포스터 이미지 호버 효과 스타일 */
.post-img:hover {
  opacity: 0.5;
  transform: scale(1.1);
}

/* 배우/감독 이름 스타일 */
.actor-name,
.product-name {
  position: absolute;
  font-size: 150%;
  font-weight: bold;
  display: none;
  color: white;
}

.actor-name {
  top: 55%;
}

.product-name {
  top: 85%;
}

/* 배우 포스터 호버 시 이름 표시 */
.actor-poster:hover .actor-name {
  display: block;
}

/* 감독 포스터 호버 시 이름 표시 */
.producer-poster:hover .product-name {
  display: block;
}

/* 버튼 그룹 스타일 */
.btn {
  display: flex;
}

/* 선택 종료 버튼 스타일 */
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

/* 선택 종료 버튼 호버 효과 스타일 */
.select-end-btn:hover {
  color: white;
  border-style: none;
  background-color: #166AE8;
}

/* 선택된 이미지 */
.is-selected {
  border: rgb(134, 27, 235) 3px solid;
}
</style>