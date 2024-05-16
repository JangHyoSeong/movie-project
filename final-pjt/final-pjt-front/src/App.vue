<template>
  <header class="navbar">
    <div class="navbar-background"></div>
    <nav class="navbar-content">
        <img src="../public/Logo_img.png" alt="Logo" class="logo">
        <RouterLink :to="{ name: 'home' }" class="nav">다각화</RouterLink>
      <div class="nav_sign">
        <RouterLink :to="{ name: 'login' }" class="nav login">로그인</RouterLink>
        <RouterLink :to="{ name: 'signup' }" class="nav signup">회원가입</RouterLink>
      </div>
    </nav>
  </header>

  <RouterView />
</template>

<style>
body {
  margin: 0;
}

/* 네비게이션 바 */
.navbar {
  position: relative;
  width: 100%;
  height: 50px;
}
.navbar-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #000000;
}
.navbar-content {
  position: relative;
  display: flex;
  align-items: center;
  height: 100%;
}
.nav {
  text-decoration: none;
  color: white;
}
.nav_sign {
  position: absolute;
  right: 0%;
  width: 12%;
}
.login, .signup {
  margin: 3%;
  padding: 3%;
  text-decoration: none;
  color: white;
  border: 1px solid white;
}
.login:hover, .signup:hover {
  background-color: #166AE8;
  border: none;
}
.logo {
  width: 50px;
  height: 50px;
}
</style>