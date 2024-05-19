<template>
  <div class="profile-page">
    <h1 style="color: white;">프로필 페이지</h1>

    <div class="profile-img"></div>
    <div class="profile-content"></div>
  </div>
  <ProfileDetailNav />
</template>

<script setup>
import ProfileDetailNav from '@/components/ProfileDetailNav.vue'
</script>

<style scoped>
.profile-page {
  text-align: center;
}

.profile-img {
  position: absolute;
  top: 20%;
  left: 10%;
  width: 400px;
  height: 400px;
  border-radius: 10%; 
  background-color: rgb(200, 200, 200);
}

.profile-content {
  position: absolute;
  top: 20%;
  left: 40%;
  width: 800px;
  height: 600px;
  border-radius: 5%; 
  background-color: rgb(200, 200, 200);
}
</style>