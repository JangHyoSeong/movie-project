<template>
  <div>
    <div class="poster-container" v-for="movie in searchResult" :key="movie.movie_id">
      <img class="poster" :src="movie.poster" alt="" width="300px">
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  searchResult: Array
})
</script>

<style scoped>
.poster-container {
  display: inline;
}
.poster {
  margin: 30px;
}

</style>