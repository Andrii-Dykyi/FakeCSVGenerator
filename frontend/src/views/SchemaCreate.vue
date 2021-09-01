<template>
    <div>
        <Navbar />
        <div class="container">
            <!-- SCHEMA CREATE FORM -->
            <SchemaForm />
            <!-- SCHEMA COLUMNS -->
            <div class="mt-5">
                <h3 class="mb-3">Schema Columns</h3>
                <ColumnUpdateForm
                    v-for="column, index in orderedColumns"
                    :key="index"
                    :column="column"
                />
            </div>
            <!-- COLUMN CREATE FORM -->
            <ColumnForm />
        </div>
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import SchemaForm from '@/components/forms/SchemaForm.vue'
import ColumnForm from '@/components/forms/ColumnForm.vue'
import ColumnUpdateForm from '@/components/forms/ColumnUpdateForm.vue'
import { mapState } from 'vuex'
// import axiosApi from '../axiosBase'


export default {
    name: "SchemaCreate",
    components: {
        Navbar,
        SchemaForm,
        ColumnForm,
        ColumnUpdateForm
    },
    data() {
        return {
            title: 'New Schema',
            noColumns: false
        }
    },
    created() {
        document.title = this.title
    },
    computed: {
        ...mapState(['schemaColumns']),
        orderedColumns() {
            const sorted = [...this.schemaColumns]
            return sorted.sort((a, b) => a.order - b.order)
        }
    },
    methods: {

    }
}
</script>

<style scoped>
    .col-submit {
        margin-top: 32px;
    }
</style>