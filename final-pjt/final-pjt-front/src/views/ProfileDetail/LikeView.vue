<template>
  <div class="like-container">
    <h1>좋아요</h1>
  </div>
</template>

<script setup>
defineProps({
  profile: Object,
})
</script>

<style scoped>
.like-container {
  position: absolute;
  top: 30%;
  left: 42%;
}
</style>