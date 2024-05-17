<template>
  <div class="background">
    <div class="background-filter">
      <img :src="backgroundImageSrc" alt="snapshot" />
      <div class="overlay"></div>
    </div>

    <div class="content-container">
      <article class="detail-container">
        <h1>{{ title }}</h1>
        <p>장르 : {{ genre.join(', ') }}</p>
        <p>국가 : {{ country }}</p>
        <p>개봉 상태 : {{ status }}</p>
        <p v-if="runningTime">러닝타임 : {{ runningTime }}분</p>
        <p v-if="openingDate">개봉 일자 : {{ openingDate }}</p>
      </article>
      <div class="youtube-container">
        <MovieDetailNav/>
      </div>
    </div>

    <div class="view-container">

    </div>


  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter, RouterView } from 'vue-router'
import axios from 'axios'
import MovieDetailNav from '@/components/MovieDetailNav.vue';

// 변수
const backgroundImageSrc = ref(null);
const title = ref('');
const overView = ref('');
const genre = ref([]);
const country = ref('');
const runningTime = ref('');
const status = ref('')
const openingDate = ref('')


const route = useRoute();

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/movie/${route.params.movie_id}/`,
  })
    .then((res) => {
      backgroundImageSrc.value = res.data.snapshots[0].snapshot
      title.value = res.data.title
      overView.value = res.data.overview
      genre.value = res.data.genre
      country.value = res.data.country
      runningTime.value = res.data.running_time
      if (res.data.status == 0) {
        status.value = '개봉'
      } else if (res.data.status == 1) {
        status.value = '개봉 예정'
      } else {
        status.value = '기타'
      }
      if (res.data.opening_date) {
        openingDate.value = res.data.opening_date
      }
      console.log(res.data)
    })
    .catch(err => console.log(err))
});
</script>

<style scoped>
/* .background {
  width: 100%;
  height: 180vh;
  background-color: #000;
  position: absolute;
  overflow: hidden;
} */

.background-filter {
  position: absolute;
  width: 100%;
  height: 40%;
}

.background-filter img {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(180deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 1) 90%), linear-gradient(270deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.75) 70%);
  pointer-events: none; /* 오버레이가 클릭 이벤트를 막지 않도록 */
}

.content-container{
  position: relative;
  top: 100px;
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border: 2px solid white;
  
}
.detail-container{
  color: white;
  text-align: center;
  /* border: 2px solid white; */
  padding: 1%;
  padding-bottom: 5%;
  margin-left: 10%;
}
.detail-container > p{
  font-size: 25px;
}
.detail-container > h1{
  font-size: 40px;
}
.youtube-container{
  width: 500px;
  height: 500px;
  border: 2px solid white;
}

.view-container{
  border: 2px solid white;
  top: 10%;
  color: white;
  position: relative;
}
</style>
