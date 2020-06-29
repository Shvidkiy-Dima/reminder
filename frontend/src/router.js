import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginComponent from "./components/login.vue"
import RegComponent from "./components/reg.vue"
import Events from "./components/events.vue"

Vue.use(VueRouter)

export default new VueRouter({
    routes: [
        {
            path: '/',
            name: 'events',
            component: Events
        },
        {
            path: "/login",
            name: "login",
            component: LoginComponent
        },
        {
            path: "/registration",
            name: "reg",
            component: RegComponent
        },
    ]
})
