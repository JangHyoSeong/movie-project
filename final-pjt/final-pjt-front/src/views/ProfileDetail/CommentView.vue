<template>
  <div class="comment-container">
    <h1>리뷰</h1>
  </div>
</template>

<script setup>
defineProps({
  profile: Object,
})
</script>

<style scoped>
.comment-container {
  position: absolute;
  top: 30%;
  left: 42%;
}
</style>