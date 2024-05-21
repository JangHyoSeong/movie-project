<template>
  <div class="chat-container">
    <div class="chat-list">
      <div v-for="chat in chatList" class="chat">
        <p>채팅 유저 : {{ chat.user.nickname }}</p>
        <p>채팅 : {{ chat.content }}</p>
      </div>
    </div>
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
</style>