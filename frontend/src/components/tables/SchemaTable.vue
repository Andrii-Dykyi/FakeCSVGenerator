<template>
<table class="table table-bordered text-center mt-5">
    <thead>
        <tr>
            <th scope="col" style="width: 10%">#</th>
            <th scope="col" style="width: 25%">Title</th>
            <th scope="col" style="width: 25%">Modified</th>
            <th scope="col" style="width: 40%">Actions</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="schema, index in userSchemas" :key="schema.id">
            <th class="align-middle" scope="row">{{ index+1 }}</th>
            <td class="align-middle">{{ schema.name }}</td>
            <td class="align-middle">{{ schema.modified }}</td>
            <td>
                <router-link 
                    :to="`/my-schema/${schema.id}/`" 
                    class="btn btn-primary mx-2 actionButton" 
                    role="button"
                >
                Edit
                </router-link>
                <form @submit.prevent="deleteSchema(schema.id, index)" class="d-inline">
                    <button class="btn btn-danger actionButton" type="submit">Delete</button>
                </form>
            </td>
        </tr>
    </tbody>
</table>
</template>

<script>
import { mapState } from 'vuex'
import axiosApi from '@/axiosBase'

export default {
    name: 'SchemaTable',
    created() {
        this.getUserSchemas()
    },
    computed: mapState(['userSchemas']),
    methods: {
        async getUserSchemas() {
            await axiosApi.get('/my-schemas/')
            .then(response => {
                this.$store.dispatch('setSchemas', response.data)
            })
            .catch(error => {
                console.log(error)
            })
        },
        async deleteSchema(schema_id, index) {
            axiosApi.delete(`/delete-schema/${schema_id}/`)
            .then(() => {
                this.$store.dispatch("removeSchema", index)
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>

<style scoped>
    .actionButton {
        width: 110px;
    }
</style>