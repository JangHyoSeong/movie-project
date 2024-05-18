<template>
  <div class="navbar">
    <div class="navbar-background"></div>
    <nav class="navbar-content">
      <!-- 사이트 로고 이미지 -->
      <img src="../public/Logo_img.png" alt="Logo" class="logo">
      <RouterLink :to="{ name: 'home' }" class="nav">다각화</RouterLink>
      <RouterLink :to="{ name: 'profile' }">프로필</RouterLink>
    </nav>
  </div>

  <RouterView />
</template>

<style>
/* 네비게이션 바 */
.navbar {
  width: 100%;
  height: 50px;
  position: relative;
}

.navbar-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #111111;
  opacity: 0.75;
}

.navbar-content {
  height: 100%;
  display: flex;
  position: relative;
  align-items: center;
}

.nav {
  color: white;
  text-decoration: none;
}

.logo {
  width: 50px;
  height: 50px;
}

body {
  margin: 0%;
  background-color: black;
}
</style>