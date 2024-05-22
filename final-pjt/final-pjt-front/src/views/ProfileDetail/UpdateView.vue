<template>
  <div class="profile-container">
    <form class="password-update" @submit.prevent="passwordUpdate">
      <h2>비밀번호 변경</h2>
      
      <label for="password1">새 비밀번호</label>
      <input type="text" name="password1" class="password" v-model="password1" placeholder="New Password">

      <label for="password2">새 비밀번호 확인</label>
      <input type="text" name="password2" class="password" v-model="password2" placeholder="Password Check">

      <!-- 제출 버튼 -->
      <input type="submit" class="password-btn" value="변경">
    </form>
  </div>

  <hr>

  <div class="profile-container">
    <p class="user-delete" @click="userDelete">회원정보 탈퇴</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useLoginStore } from '@/stores/login'
import { useRouter } from 'vue-router'
import axios from 'axios'

defineProps({
  profile: Object,
})

const store = useLoginStore()
const router = useRouter()

const userDelete = function () {
  confirm('회원탈퇴를 하시겠습니까?')

  axios({
    method: 'delete',
    url: 'http://127.0.0.1:8000/api/v1/profile/member_leave/',
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      alert('회원 탈퇴가 실행되었습니다.')
      store.logout()
      router.push({name: 'home'})
    })
    .catch(err => console.log(err))
}


const password1 = ref('')
const password2 = ref('')

const passwordUpdate = function () {

  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/dj-rest-auth/password/change/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data:{
      new_password1: password1.value,
      new_password2: password2.value
    }
  })
    .then((res) => {
      alert('비밀번호 변경이 완료되었습니다')
      router.push({name: 'profile-like'})
    })
    .catch(err => console.log(err))
}
</script>

<style scoped>
.profile-container {
  position: relative;
  left: 3%;
  width: 95%;
  color: white;
}

hr {
  width: 95%;
}

.password-update {
  display: flex;
  width: 15%;
  flex-direction: column;
}

.password {
  margin: 3%;
  padding: 3%;
}

.user-delete {
  position: relative;
  left: 95%;
  font-size: 50%;
  text-align: center;
  width: 4%;
  border: 1px solid;
  padding: 0.2% 0%;
}

.user-delete:hover {
  background-color: red;
  border-style: none;
}

.password-btn {
  margin-left: 3%;
  width: 94%;
  border: 1px solid white;
  border-radius: 5px;
  background-color: black;
  color: white;
  margin-top: 3%;
  padding: 1%;
}

.password-btn:hover {
  background-color: #166AE8;
  color: white;
  border-style: none;
}
</style>