<template>
    <div id="login">
        <h1>Login</h1>
        <input type="text" name="username" v-model="username" placeholder="Username" />
        <input type="password" name="password" v-model="password" placeholder="Password" />
        <button type="button" v-on:click="login()">Login</button>
        <router-link to='/registration'>Registration</router-link>
    </div>
</template>

<script>
import axios from 'axios'

    export default {
        name: 'Login',
        data() {
            return {
                    username: "",
                    password: ""

            }
        },
        methods: {
            login() {
                axios.post('http://localhost:8000/auth/jwt/create/',
              {
              username: this.username,
              password: this.password
            }).then(res => {
                sessionStorage.setItem('access', res.data.access)
                sessionStorage.setItem('refresh', res.data.refresh)
                this.$router.replace({ name: "events" });
              });
            }
        }
    }
</script>

<style scoped>
    #login {
        width: 500px;
        border: 1px solid #CCCCCC;
        background-color: #FFFFFF;
        margin: auto;
        margin-top: 200px;
        padding: 20px;
    }
</style>
