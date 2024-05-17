<template>
  <p @click="LoginVueOn" class="login">로그인</p>
  <div class="login-popup" :class="isLogin">
    <div class="login-popup-detail">
      <div class="logo-title">
        <img src="../../public/Logo_img.png" alt="Logo" class="logo">
        <h1 style="color: #166AE8;">다각화</h1>
      </div>

      <div class="login-popup-content">
        <h3>로그인</h3>
        <form @submit.prevent="login">
          <p><input type="text" class="input-txt" placeholder="아이디" v-model.trim="username"></p>
          <p><input type="text" class="input-txt" placeholder="비밀번호" v-model.trim="password"></p>
          <input class="login-btn" type="submit" value="로그인">
        </form>
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
import { ref } from 'vue'
import { useLoginStore } from '@/stores/login'

const store = useLoginStore()

const username = ref('')
const password = ref('')

const login = function () {
  const payload = {
    username: username.value,
    password: password.value,
  }
  store.login(payload)
}

const isLogin = ref(null)

const LoginVueOn = function () {
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
  display: none;
  border-radius: 3%;
  border: 1px solid black;
  background-color: white;
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
  text-align: center;
  transform: translate(0%, 0%);
}

.login-txt {
  text-align: center;
}

.input-txt {
  width: 50%;
  padding: 3%;
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
  color: white;
  border-style: none;
  border-radius: 10%;
  background-color: #166AE8;
}

.popup-close-btn {
  top: 2%;
  left: 92%;
  position: absolute;
}

.display-show {
  display: block;
}
</style>