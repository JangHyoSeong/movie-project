<template>
  <div class="like-container">
    <h1>좋아요</h1>
    <div v-for="movie in userData.like_movies">
      <img :src="movie.poster" alt="" width="100px">
    </div>
  </div>
</template>

<script setup>
defineProps({
  userData: Object,
})
</script>

<style scoped>
.like-container {
  position: absolute;
  top: 30%;
  left: 42%;
}
</style>