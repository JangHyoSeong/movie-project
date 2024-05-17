<template>
  <p @click="SignVueOn" class="sign">회원가입</p>
  <div class="sign-popup" :class="isSign">
    <div class="sign-popup-detail">
      <div class="logo-title">
        <img src="../../public/Logo_img.png" alt="Logo" class="logo">
        <h1 style="color: #166AE8;">다각화</h1>
      </div>
      <div class="sign-popup-content">
        <h3 style="text-align: center">회원가입</h3>
        <form @submit.prevent="signUpRequest">
          <p><input type="text" class="input-txt" placeholder="이름" v-model="username"></p>
          <p><input type="text" class="input-txt" placeholder="이메일" v-model="email"></p>
          <p><input type="text" class="input-txt" placeholder="비밀번호" v-model="password1"></p>
          <p><input type="text" class="input-txt" placeholder="비밀번호 확인" v-model="password2"></p>
          <p><input type="text" class="input-txt" placeholder="닉네임" v-model="nickname"></p>
          <button class="sign-btn">회원가입</button>
        </form>
        <div class="sign-txt">
          <p>이미 가입하셨나요?</p>
          <p style="color: #166AE8; text-decoration:underline;">로그인</p>
        </div>
      </div>
      <button class="popup-close-btn" @click="SignVueOff">x</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const username = ref(null)
const email = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const isSign = ref(null)

const SignVueOn = function () {
  isSign.value = 'display-show'
}
const SignVueOff = function () {
  isSign.value = ''
}
const signUpRequest = function () {
  axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/dj-rest-auth/registration/',
    data: {
      username: username.value,
      email: email.value,
      password1: password1.value,
      password2: password2.value,
      nickname: nickname.value
    }
  })
    .then((res) => {
      console.log('회원가입 성공');
    })
    .catch((err) => {
      console.log(err);
    })
}
</script>

<style scoped>
.sign {
  position: absolute;
  top: 0%;
  right: 5%;
  color: white;
}

.sign-popup {
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

.sign-popup-detail {
  margin-top: 10%;
}

.logo-title {
  display: flex;
  justify-content: center;
  transform: translate(0%, -20%);
}

.logo {
  width: 20%;
  height: 20%;
}

.sign-txt {
  display: flex;
  justify-content: center;
}

.sign-popup-content {
  text-align: center;
  transform: translate(0%, -10%);
}

.sign-txt p {
  margin: 4% 2% 0% 0%;
}

.input-txt {
  padding: 2%;
  width: 50%;
}

.sign-btn {
  padding: 2%;
  color: white;
  border-style: none;
  border-radius: 10%;
  background-color: #166AE8;
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