<template>
  <div class="profile-content">
    <h1>{{ userData.username }}님의 프로필 페이지</h1>
    <hr>
  </div>
  <ProfileDetailNav :userData="userData" />
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
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
.profile-content {
  color: white;
}

.profile-content > h1 {
  padding:  1% 0% 0% 3%;
}

hr {
  width: 95%;
}
</style>