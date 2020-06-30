<template>
    <div id="login">
    <form>
        <h2 class="text-center">Log in</h2>
        <div class="form-group">
            <input type="text" class="form-control" placeholder="Username" v-model="username"  required="required">
        </div>
        <div class="form-group">
            <input type="password" class="form-control" placeholder="Password" v-model="password" required="required">
        </div>
        <div class="form-group">
            <button @click="login()" class="btn btn-primary btn-block">Log in</button>
        </div>
    </form>
      <div v-if="error.status">
          <small id="passwordHelp" class="text-danger">
                {{error.msg}}
          </small>
      </div>
    <p class="text-center"><router-link to='/registration'>Create an Account</router-link></p>


    </div>

</template>

<script>
import axios from 'axios'

    export default {
        name: 'Login',
        data() {
            return {
                    error: {
                        status: false,
                        msg: ''
                    },
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
              },
            (error)=>{
              this.error.status = true
              if (error.response) {
                    this.error.msg = error.response.data.detail
                    }
             else {
                  this.error.msg = error.message
                  }
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
