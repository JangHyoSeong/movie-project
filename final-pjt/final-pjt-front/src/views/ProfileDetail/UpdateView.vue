<template>
  <div class="profile-container">
    <div class="password-update">
      <h2>비밀번호 변경</h2>
      현재 비밀번호 <input type="text" name="password" id="password" placeholder="Password">
      새 비밀번호 <input type="text" name="password" id="password" placeholder="New Password">
      새 비밀번호 확인 <input type="text" name="password" id="password" placeholder="Password Check">
    </div>
  </div>

  <hr>

  <div class="profile-container">
    <p class="user-delete" @click="userDelete">회원정보 탈퇴</p>
  </div>
</template>

<script setup>
defineProps({
  profile: Object,
})

const userDelete = function () {
  confirm('회원탈퇴를 하시겠습니까?')
  confirm('다시 한번 생각해보시죠')
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

#password {
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
</style>