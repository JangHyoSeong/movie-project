<template>
  <div class="profile-page">
    <h1 style="color: white;">프로필 페이지</h1>

    <div class="profile-img"></div>
    <div class="profile-content"></div>
  </div>
  <ProfileDetailNav :userData="userData"/>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useLoginStore } from '@/stores/login'
import axios from 'axios'
import ProfileDetailNav from '@/components/ProfileDetailNav.vue'


const store = useLoginStore()

// 유저 데이터를 저장할 변수
const userData = ref([])

// 유저 데이터를 받아오는 함수
const loadUserData = function () {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/profile/',
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      userData.value = res.data
      console.log(userData.value)
    })
    .catch(err => console.log(err))
}

// 페이지가 로드되었을 때 바로 유저 데이터를 가져올 수 있게 함
onMounted(() => {
  loadUserData()
})

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