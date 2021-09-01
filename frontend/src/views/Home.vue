<template>
    <div class="home">
        <Navbar />
        <div class="container">
            <div class="mt-5">
                <h3 class="d-inline">Data Schemas</h3>
                <router-link :to="{name: 'newSchema'}" class="btn btn-success d-inline float-end" role="button">New schema</router-link>
            </div>
            <SchemaTable />
        </div>
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import SchemaTable from '@/components/tables/SchemaTable.vue'


export default {
    name: 'Index',
    components: {
        Navbar,
        SchemaTable
    },
    data() {
        return {
            title: 'Home'
        }
    },
    created() {
        document.title = this.title
    }
}
</script>

<style scoped>
    .actionButton {
        width: 110px;
    }
</style>