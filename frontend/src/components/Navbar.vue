<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <router-link to="/" class="navbar-brand">Fake CSV Generator</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link to="/" class="nav-link">Schemas</router-link>
                    </li>
                </ul>
                <span class="navbar-text">
                    Hello, <b>{{ getUsername() }}</b>
                </span>
                <a class="nav-link" href="#" @click="logout">Logout</a>
            </div>
        </div>
    </nav>
</template>

<script>
import axiosApi from '../axiosBase'

export default {
    name: 'navbar',
    methods: {
        getUsername() {
            return this.$store.state.username
        },
        async logout() {
            await axiosApi.post('/logout/', {})
            .then(() => {
                this.$store.dispatch("logoutUser")
            })
            .then(() => {
                this.$router.push({ name: "Login" })
            })
        }
    }
}
</script>

<style scoped>
    .nav-link {
        color: red;
    }
</style>