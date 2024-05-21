<template>
  <!-- 채팅창 전체를 감싸는 div -->
  <div class="chat-container">

    <!-- 지금까지의 채팅이 들어가는 영역 -->
    <div class="chat-list">
      <!-- 채팅 -->
      <div v-for="chat in chatList" class="chat" :class="{ 'my-chat': currentUser.id === chat.user.id }">
        <p>채팅 유저 : {{ chat.user.nickname }}</p>
        <p>채팅 : {{ chat.content }}</p>
      </div>
    </div>

    <!-- 채팅 입력구간 -->
    <form @submit.prevent="chatSubmit">
      <input class="chat-input" type="text" placeholder="NewComment" v-model="chatMessage">
      <input type="submit" value="submit">
    </form>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useLoginStore } from '@/stores/login'
import axios from 'axios'

const store = useLoginStore()
const route = useRoute()

defineProps({
  movie: Object,
})

const chatList = ref([])

const loadMessage = function () {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/${route.params.movie_id}/chat/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      chatList.value = res.data
      console.log(chatList.value)
    })
    .catch(err => console.log(err))
}

onMounted(() => {
  loadMessage()
})

// 현재 입력창의 메시지와 쌍방향 연결
const chatMessage = ref('')

// 채팅을 DB에 보내서 저장
const chatSubmit = function () {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/api/v1/${route.params.movie_id}/chat/`,
    data: {
      content: chatMessage.value,
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      loadMessage()
      chatMessage.value = ''
    })
    .catch(err => console.log(err))
}

// 1초마다 채팅을 새로불러옴
const repeat = setInterval(loadMessage, 1000)

// 현재 로그인된 유저 정보 가져오기
const currentUser = ref(null)
onMounted(() => {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/current_user/',
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      currentUser.value = res.data
    })
    .catch(err => console.log(err))
})

// 현재 유저가 리뷰 작성자인지 확인
const isCurrentUser = function (user) {
  return currentUser.value && user.id === currentUser.value.id
}
</script>

<style scoped>
.chat-container{
  border: 2px solid white;
  position: relative;
}

.chat-list{
  height: 300px;
  width: 60%;
}

.chat-input{
  background-color: white;
  height: 30px;
  width: 100%;
  bottom: 0;
}

/* 내 채팅 */
.my-chat{
  text-align: right;
  color: red;
}
</style>