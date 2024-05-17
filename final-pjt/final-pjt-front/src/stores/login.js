import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useLoginStore = defineStore('login', () => {
  const token = ref(null)
  const router = useRouter()

  const login = function (payload) {
    const username = payload.username
    const password = payload.password
    
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/dj-rest-auth/login/',
      data: {
        username, password
      }
    })
      .then((res) => {
        token.value = res.data.key
        router.push({name: 'home'})
        console.log(token.value)
      })
      .catch(err => console.log(err))
  }

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  return { token, login, isLogin }
}, { persist: true})
