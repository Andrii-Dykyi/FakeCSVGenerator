import axios from 'axios'
import Cookies from 'universal-cookie'
import router from './router'


const cookies = new Cookies().get("csrftoken")

const axiosApi = axios.create({
    baseURL: "/api",
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": cookies,
    },
    withCredentials: true
})

axiosApi.defaults.xsrfCookieName = "csrftoken";
axiosApi.defaults.xsrfHeaderName = "X-CSRFToken";

axiosApi.interceptors.response.use(response => {
    if (response.status === 403) {
        router.push({ name: "login" })
    }
    return response
})

export default axiosApi