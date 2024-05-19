<template>
  <div class="review-container">
    <div class="review-score-container">
      <!-- 총 평점 및 리뷰 작성 버튼 -->
      <div class="total-score">
        <p>총 평점 : 4.5</p>
        <button @click="showReviewModal">리뷰 작성</button>
      </div>
      <!-- 리뷰 개수 -->
      <p>1234개의 평점이 등록되었습니다</p>
    </div>
    <div class="review-list-container">
      <!-- 최신 순, 평점 순 버튼 -->
      <div class="sort-buttons">
        <button>최신 순</button>
        <button>평점 순</button>
      </div>
      <!-- 리뷰 목록 -->
      <div class="review-list">
        <div v-for="review in reviews" class="review-item">
          <div class="review-content">
            <p>{{ review.user.nickname }}</p>
            <p>{{ review.score }} 점</p>
            <p>{{ format(review.created_at, 'yyyy-MM-dd HH:mm:ss') }}</p>
            <p>{{ review.content }}</p>
          </div>
          <button class="delete-button" @click="deleteReview(review.id)">✖</button>
        </div>
      </div>
    </div>
  </div>

  <!-- 리뷰 작성 모달 -->
  <MovieReviewForm v-if="reviewModalVisible" @closeModal="hideModal"/>
</template>

<script setup>
defineProps({
  movie: Object,
})
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { format } from 'date-fns'
import { useLoginStore } from '@/stores/login'
import axios from 'axios'
import MovieReviewForm from '@/components/MovieReviewForm.vue'

const route = useRoute()
const store = useLoginStore()

// 모달 관련 변수
const reviewModalVisible = ref(false)

// 모달 나타내기, 숨기기
const showReviewModal = function () {
  reviewModalVisible.value = true
}

const hideModal = function () {
  reviewModalVisible.value = false
}

// 리뷰 목록 가져오기
const reviews = ref([])

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/${route.params.movie_id}/reviews/`
  })
    .then((res) => {
      reviews.value = res.data
      console.log(reviews.value)
    })
    .catch(err => {
      console.log(err)
    })
})

// 리뷰 삭제 기능
// 현재는 아무나 리뷰 삭제 가능. 고쳐야함
const deleteReview = function (review_id) {
  axios({
    method: 'delete',
    url: `http://127.0.0.1:8000/api/v1/${route.params.movie_id}/reviews/`,
    data: {
      review_id
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      alert('리뷰가 정상적으로 삭제되었습니다.')
    })
    .catch((err) => {
      alert('오류 발생')
    })
}
</script>

<style scoped>
.review-container {
  display: flex;
  padding: 20px;
}

.review-score-container {
  flex: 1;
  margin-right: 20px;
}

.review-list-container {
  flex: 2;
  display: flex;
  flex-direction: column;
}

.total-score {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 30px;
}

.sort-buttons {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 10px;
}

.review-list {
  border: 1px solid #ccc;
  padding: 10px;
  background-color: #1f1f1f;
}

.review-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid #444;
  padding: 10px 0;
}

.review-item:first-child {
  border-top: none;
}

.review-content p {
  margin: 5px 0;
}

.delete-button {
  background-color: transparent;
  border: none;
  color: white;
  font-size: 20px;
  cursor: pointer;
  padding: 5px;
}

.delete-button:hover {
  color: red;
}
</style>