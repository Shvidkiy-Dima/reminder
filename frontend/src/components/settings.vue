<template>
    <div id="settings">
        <form>
            <h2 class="text-center">Settings {{ username }}</h2>
            <div class="form-group">
                <input type="email" class="form-control" placeholder="Email" v-model="email" required="required">
            </div>
            <div class="form-group">
                <input type="password" class="form-control" placeholder="Please enter current password" v-model="current_password" required="required">
            </div>
            <div class="form-group">
                <button v-on:click="change()" class="btn btn-primary btn-block">Change</button>
            </div>
        </form>

    </div>
</template>

<script>
import Request from '../utils/request'

export default {
        name: 'Settings',
        data() {
            return {
                    username: "",
                    email: "",
                    current_password: ''
            }
        },
        watch: {
              '$route'() {
                  this.set_user_info()
              }
            },
        created(){
            this.set_user_info()
        },
        methods: {
            set_user_info(){
              Request({
                method: 'get',
                url: 'http://localhost:8000/auth/users/me/'
              },(res)=>{
                  this.email = res.data.email
                  this.username = res.data.username
              })
            },
            change() {
                Request({
                  method: 'patch',
                  url: 'http://localhost:8000/auth/users/me/',
                  data: {
                      email: this.email,
                  }
                }, ()=>{
                  this.$router.replace({ name: "events" });
                })
        }
    }
  }
</script>

<style scoped>
    #settings {
        width: 500px;
        border: 1px solid #CCCCCC;
        background-color: #FFFFFF;
        margin: auto;
        margin-top: 200px;
        padding: 20px;
    }
</style>
