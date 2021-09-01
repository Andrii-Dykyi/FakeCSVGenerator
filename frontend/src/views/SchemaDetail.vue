<template>
    <div>
        <Navbar />
        <div class="container">
            <DataSetForm />
            <DataSetTable />
        </div>
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import DataSetForm from '@/components/forms/DataSetForm.vue'
import DataSetTable from '@/components/tables/DataSetTable.vue'

export default {
    name: "SchemaDetail",
    components: {
        Navbar,
        DataSetForm,
        DataSetTable
    }
}
</script>

<style scoped>
    #taskStatus {
        width: 110px;
    }
    .actionButton {
      width: 110px;
    }
</style>