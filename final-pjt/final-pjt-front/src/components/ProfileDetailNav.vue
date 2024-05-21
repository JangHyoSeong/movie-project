<template>
  <RouterLink :to="{ name: 'profile-update' }" 
    class="navbar-link">회원정보수정</RouterLink>

  <RouterView :userData="userData"/>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

defineProps({
  userData: Object
})
</script>

<style scoped>
.navbar-link {
  position: absolute;
  top: 8%;
  right: 10%;
  text-decoration: none;
}
</style>