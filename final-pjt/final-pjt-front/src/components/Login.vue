<template>
  <p @click="LoginVue" class="login">로그인</p>
  <div class="login-popup" :class="isLogin">
    <div class="login-popup-detail">
      <div class="logo-title">
        <img src="../../public/Logo_img.png" alt="Logo" class="logo">
        <h1 style="color: #166AE8;">다각화</h1>
      </div>

      <div class="login-popup-content">
        <h3>로그인</h3>
        <p><input type="text" class="input-txt" placeholder="이메일"></p>
        <p><input type="text" class="input-txt" placeholder="비밀번호"></p>
        <button class="login-btn">로그인</button>
        <div class="sign-login">
          <p>계정이 없으신가요?</p>
          <p style="color: #166AE8; text-decoration:underline;">회원가입</p>
        </div>
      </div>

      <button class="popup-close-btn" @click="LoginVueOff">x</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const isLogin = ref(null)

const LoginVue = function () {
  isLogin.value = 'display-show'
}
const LoginVueOff = function () {
  isLogin.value = ''
}
</script>

<style scoped>
.login {
  position: absolute;
  top: 0%;
  right: 10%;
  color: white;
}

.login-popup {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 400px;
  height: 500px;
  background-color: white;
  border: 1px solid black;
  border-radius: 3%;
  display: none;
}

.login-popup-detail {
  margin-top: 15%;
}

.logo-title {
  display: flex;
  justify-content: center;
  transform: translate(0%, 0%);
}

.logo {
  width: 20%;
  height: 20%;
}

.login-popup-content {
  transform: translate(0%, 0%);
  text-align: center;
}

.login-txt {
  text-align: center;
}

.input-txt {
  padding: 3%;
  width: 50%;
}

.sign-login {
  margin: 1%;
  display: flex;
  justify-content: center;
}

.sign-login p {
  padding: 1%
}

.login-btn {
  padding: 2%;
  border-radius: 10%;
  border-style: none;
  background-color: #166AE8;
  color: white;
}

.popup-close-btn {
  position: absolute;
  left: 92%;
  top: 2%;
}

.display-show {
  display: block;
}
</style>