<template>
  <div class="movie-navbar-container">
    <div class="navbar-content">
      <RouterLink :to="{name: 'movie-overview'}" :movie="movie" class="navbar-link">소개 | </RouterLink>
      <RouterLink :to="{name: 'movie-review'}" class="navbar-link">리뷰 | </RouterLink>
      <RouterLink :to="{name: 'movie-recommend'}" class="navbar-link">추천 영화 | </RouterLink>
      <RouterLink :to="{name: 'movie-chat'}" class="navbar-link">채팅방 | </RouterLink>
    </div>
  </div>
  <hr>
  <RouterView :movie="movie"/>
</template>

<script setup>
defineProps({
  movie: Object,
})
</script>

<style scoped>
.movie-navbar-container{
  color: white;
  display: flex;
  justify-content: center;
}
.navbar-content{
  font-size: 30px;
  margin: 3px solid white;
}
.navbar-link{
  text-decoration: none;
  color: white;
}
</style>