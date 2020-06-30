<template>
    <div id="reg">
        <form>
            <h2 class="text-center">Registration</h2>



            <div class="form-group row">
              <div class="col-sm-7">
                <input v-model="username"  required="required" type="text" class="form-control" id="inputUsername" placeholder="Username">
              </div>
              <div v-if="error.username">
                  <small v-for="(err, index) in error.username" :key="index" class="text-danger">
                        {{err}}
                  </small>
              </div>
            </div>



            <div class="form-group row">
              <div class="col-sm-7">
                <input v-model="password"  required="required" type="password" class="form-control" id="inputPassword" placeholder="Password">
              </div>
              <div v-if="error.password">
                  <small v-for="(err, index) in error.password" :key="index" class="text-danger">
                        {{err}}
                  </small>
              </div>
            </div>

            <div class="form-group">
                <input type="email" class="form-control" placeholder="Email" v-model="email" required="required">
            </div>
            <div class="form-group">
                <button v-on:click="reg()" class="btn btn-primary btn-block">Create Account</button>
            </div>
        </form>

    </div>
</template>

<script>
import axios from 'axios'

    export default {
        name: 'Reg',
        data() {
            return {
              error: {
                  username: [],
                  password: []
              },
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
              },
            (error)=>{
              if (error.response){
                this.error.username = error.response.data.username
                this.error.password = error.response.data.password
              }
              console.log(error.response)
            });
            }
        }
    }
</script>

<style scoped>
    #reg {
        width: 500px;
        border: 1px solid #CCCCCC;
        background-color: #FFFFFF;
        margin: auto;
        margin-top: 200px;
        padding: 20px;
    }
</style>
