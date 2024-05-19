<template>
  <!-- 모달 전체 창 -->
  <div class="modal-overlay">
    <!-- 모달 내부 컨텐츠 -->
    <div class="modal-content">
      <button class="close-button" @click="closeModal">X</button>
      <h3>리뷰 작성</h3>

      <!-- 작성 form -->
      <form @submit.prevent="submitReview">
        <div>
          <label for="score">평점</label>
          <input type="number" id="score" v-model="reviewScore" min="0" max="5" step="0.1" required>
        </div>
        <div>
          <label for="review">리뷰</label>
          <textarea id="review" v-model="reviewContent" required></textarea>
        </div>
        <button type="submit">작성</button>
      </form>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useLoginStore } from '@/stores/login'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const store = useLoginStore()

const emit = defineEmits(['close'])

const closeModal = function () {
  emit('closeModal')
}

const reviewScore = ref(0)
const reviewContent = ref('')

// 리뷰 작성 요청
const submitReview = function () {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/api/v1/${route.params.movie_id}/reviews/`,
    data: {
      score: reviewScore.value,
      content: reviewContent.value,
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      alert('리뷰 작성 완료')
      reviewScore.value = 0
      reviewContent.value = ''
      closeModal()
      router.push({name: 'movie-review', params:{movie_id: route.params.movie_id}})
    })
    .catch(err => {
      alert('리뷰 작성 권한이 없습니다')
    })
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  color: black;
  padding: 20px;
  border-radius: 8px;
  width: 300px;
  position: relative;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
}
</style>