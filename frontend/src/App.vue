<template>
    <div id="app">
        <router-view></router-view>
  </div>
</template>

<script>

export default {
        name: 'App',
        created() {
            this.check_auth()
        },
        methods: {
            check_auth() {
              let access_token = sessionStorage.getItem('access')
              if(!access_token) {
                  this.$router.replace({ name: "login" });
              }
            },
            logout() {
                console.log('IN PROGRESS')
            }
        }
    }
</script>
