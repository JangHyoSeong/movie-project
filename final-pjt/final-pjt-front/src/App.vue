<template>
  <!-- 네비게이션 바 -->
  <div class="navbar">
    <!-- 네비게이션 바 배경 -->
    <div class="navbar-background"></div>
    <!-- 네비게이션 바 콘텐츠 -->
    <nav class="navbar-content">
      <!-- 사이트 로고 이미지 -->
      <img src="../public/Logo_img.png" alt="Logo" class="logo">
      <!-- 홈 링크 -->
      <RouterLink :to="{ name: 'home' }" class="nav">다각화</RouterLink>
      <!-- 검색 창 -->
      <input type="text" name="search" class="search-nav" placeholder=" ▷ 영화, 배우, 감독을 검색해보세요">
      <!-- 프로필 링크 -->
      <RouterLink :to="{ name: 'profile' }" class="profile-nav" v-show="store.isLogin">프로필</RouterLink>
    </nav>
  </div>
  <!-- 로그인 및 회원가입 컴포넌트 -->
  <Login />
  <Signup />
  <!-- 라우터 뷰 -->
  <RouterView @select-event="selectDataPass" :selectData="selectData" />

  <!-- 구글 폰트 -->
  <!-- <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link
    href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Jua&family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Nanum+Gothic&family=Nanum+Pen+Script&family=Noto+Sans+KR:wght@100..900&family=Open+Sans:ital,wght@0,300..800;1,300..800&family=Pacifico&family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Poetsen+One&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap"
    rel="stylesheet"> -->
</template>

<script setup>
import { ref } from 'vue'
import { useLoginStore } from './stores/login'
import Login from './components/Login.vue'
import Signup from './components/Signup.vue'

const store = useLoginStore()

const selectData = ref({})

// choice를 한 정보를 choicedetail로 넘겨줌
const selectDataPass = function (data) {
  console.log(data.value)
  selectData.value = data.value
}


</script>

<style>
* {
  font-family: "NEXONFootballGothicBA1", sans-serif;
  font-weight: 300;
  font-style: normal;
}

@font-face {
  font-family: 'NEXONFootballGothicBA1';
  src: url('https://gcore.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.1/NEXONFootballGothicBA1.woff') format('woff');
}

.search-nav {
  position: relative;
  left: 65%;
  width: 15%;
  height: 40%;
  border-style: none;
}

.profile-nav {
  position: absolute;
  right: 10%;
  color: white;
  text-decoration: none;
}

/* 네비게이션 바 배경 */
.navbar-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}

/* 네비게이션 바 콘텐츠 */
.navbar-content {
  height: 100%;
  display: flex;
  align-items: center;
  padding: 0 20px;
  /* 좌우 패딩 추가 */
}

/* 네비게이션 링크 */
.nav {
  color: white;
  text-decoration: none;
  margin-right: 20px;
  /* 링크 사이 간격 추가 */
}

/* 네비게이션 바 */
.navbar {
  width: 100%;
  height: 50px;
  position: relative;
  background-color: #111111;
  /* 배경 색상을 여기로 이동 */
}

/* 로고 이미지 */
.logo {
  width: 50px;
  height: 50px;
}

/* 전체 body */
body {
  margin: 0%;
  background-color: black;
}
</style>
