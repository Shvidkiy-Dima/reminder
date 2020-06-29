<template>
    <div id="login">
        <h1>Login</h1>
        <input type="text" name="username" v-model="username" placeholder="Username" />
        <input type="password" name="password" v-model="password" placeholder="Password" />
        <input type="email" name="email" v-model="email" placeholder="Email" />
        <button type="button" v-on:click="reg()">Registration</button>
    </div>
</template>

<script>
import axios from 'axios'

    export default {
        name: 'Login',
        data() {
            return {
                    username: "",
                    password: "",
                    email: ""

            }
        },
        methods: {
            reg() {
                axios.post('http://localhost:8000/auth/users/',
              {
              username: this.username,
              password: this.password,
              email: this.email
            }).then(() => {
                this.$router.replace({ name: "login" });
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
