<template>
  <div>
    <div v-for="movie in recommendedMovies">
      <img :src="movie.poster" alt="">
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()

defineProps({
  movie: Object,
})

const recommendedMovies = ref([])

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/${route.params.movie_id}/associate/`,
  })
    .then((res) => {
      recommendedMovies.value = res.data
    })
    .catch(err => console.log(err))
})
</script>

<style scoped>

</style>