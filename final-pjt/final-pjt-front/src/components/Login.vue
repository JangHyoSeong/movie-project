<template>
  <!-- 로그인 버튼 -->
  <p @click="LoginVueOn" class="login">로그인</p>
  <!-- 로그인 팝업 -->
  <div class="login-popup" :class="isLogin">
    <div class="login-popup-detail">
      <!-- 로고 및 제목 -->
      <div class="logo-title">
        <img src="../../public/Logo_img.png" alt="Logo" class="logo">
        <h1 style="color: #166AE8;">다각화</h1>
      </div>
      <!-- 로그인 컨텐츠 -->
      <div class="login-popup-content">
        <h3>로그인</h3>
        <form @submit.prevent="login">
          <!-- 아이디 입력창 -->
          <p><input type="text" class="input-txt" placeholder="아이디" v-model.trim="username"></p>
          <!-- 비밀번호 입력창 -->
          <p><input type="password" class="input-txt" placeholder="비밀번호" v-model.trim="password"></p>
          <!-- 로그인 버튼 -->
          <input class="login-btn" type="submit" value="로그인">
        </form>
        <!-- 회원가입 링크 -->
        <div class="sign-login">
          <p>계정이 없으신가요?</p>
          <p style="color: #166AE8; text-decoration:underline;">회원가입</p>
        </div>
      </div>
      <!-- 팝업 닫기 버튼 -->
      <button class="popup-close-btn" @click="LoginVueOff">x</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useLoginStore } from '@/stores/login'

const store = useLoginStore()

const username = ref('')
const password = ref('')

// 로그인 함수
const login = function () {
  const payload = {
    username: username.value,
    password: password.value,
  }
  store.login(payload)
}

// 로그인 팝업 상태
const isLogin = ref(null)

// 로그인 팝업 활성화 함수
const LoginVueOn = function () {
  isLogin.value = 'display-show'
}

// 로그인 팝업 비활성화 함수
const LoginVueOff = function () {
  isLogin.value = ''
}
</script>

<style scoped>
/* 로그인 버튼 스타일 */
.login {
  position: absolute;
  top: 0%;
  right: 10%;
  color: white;
}

/* 로그인 팝업 스타일 */
.login-popup {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 350px;
  height: 500px;
  display: none;
  border-radius: 3%;
  border: 1px solid black;
  background-color: white;
}

/* 로그인 팝업 디테일 스타일 */
.login-popup-detail {
  margin-top: 15%;
}

/* 로고 및 제목 스타일 */
.logo-title {
  display: flex;
  justify-content: center;
  transform: translate(0%, -20%);
}

/* 제목 스타일 */
.logo-title h1 {
  transform: translate(0%, -20%);
}

/* 로고 이미지 스타일 */
.logo {
  width: 20%;
  height: 20%;
}

/* 로그인 컨텐츠 스타일 */
.login-popup-content {
  text-align: center;
  transform: translate(0%, 0%);
}

/* 로그인 입력창 스타일 */
.input-txt {
  width: 50%;
  padding: 3%;
  margin: 1%;
}

/* 회원가입 링크 스타일 */
.sign-login {
  margin: 1%;
  display: flex;
  justify-content: center;
}

.sign-login p {
  padding: 1%
}

/* 로그인 버튼 스타일 */
.login-btn {
  margin-top: 1%;
  padding: 2% 4%;
  color: white;
  border-style: none;
  border-radius: 10%;
  background-color: #166AE8;
}

/* 팝업 닫기 버튼 스타일 */
.popup-close-btn {
  top: 2%;
  left: 92%;
  position: absolute;
}

/* 활성화된 팝업 표시 스타일 */
.display-show {
  display: block;
}
</style>
