<template>
  <div class="profile-navbar-container">
    <div class="navbar-content">
      <RouterLink :to="{ name: 'profile-like' }" class="navbar-link">좋아요</RouterLink>
      <RouterLink :to="{ name: 'profile-comment' }" class="navbar-link">리뷰</RouterLink>
      <RouterLink :to="{ name: 'profile-update' }" class="navbar-link">회원정보수정</RouterLink>
    </div>
  </div>
  <hr class="hr">
  <RouterView />
</template>

<script setup>

</script>

<style scoped>
.navbar-content {
  position: absolute;
  top: -25%;
  left: 40%;
}

.navbar-link {
  display: flex;
  justify-content: space-around;
  width: 250px;
  text-decoration: none;
  font-size: 150%;
}

.hr {
  position: absolute;
  top: 29%;
  left: 42%;
  width: 48%;
  z-index: 1;
  border: none;
  border-top: 1px solid black; /* 또는 원하는 색상으로 변경 */
}
</style>