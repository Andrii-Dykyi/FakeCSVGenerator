<template>
    <div class="login-wrapper text-center d-flex justify-content-center align-items-center">
        <div class="border border-dark p-5">
            <form @submit.prevent="loginUser" class="m-5">
                <h1 class="mb-5">Login</h1>
                <div v-if="incorrectAuth" class="border my-2">
                    <div class="p-4 bg-danger">Please enter correct credentials</div>
                </div>
                <input
                    v-model="userData.username" 
                    class="form-control mb-2" 
                    type="text" 
                    name="username" 
                    required 
                    placeholder="Username"
                >
                <input
                    v-model="userData.password" 
                    class="form-control mb-2" 
                    type="password" 
                    name="password" 
                    required
                    autocomplete=""
                    placeholder="Password"
                >
                <button class="w-100 btn btn-primary mt-2" type="submit">Submit</button>
            </form>
        </div>
    </div>
</template>

<script>
import axiosApi from '../axiosBase.js'

export default {
    name: 'Login',
    data() {
        return {
            title: 'Login',
            userData: {
                username: '',
                password: '',
            },
            incorrectAuth: false
        }
    },
    created() {
        document.title = this.title
    },
    methods: {
        async loginUser() {
            await axiosApi.post('/login/', this.userData)
            .then((response) => {
                this.$store.dispatch("loginUser", response.data.username)
                this.$router.push({ name: 'home' })
            })
            .catch(() => {
                this.userData.username = ''
                this.userData.password = ''
                this.incorrectAuth = true
            })
        }
    }  
}
</script>

<style scoped>
    .login-wrapper {
        height: 100vh;
    }
</style>