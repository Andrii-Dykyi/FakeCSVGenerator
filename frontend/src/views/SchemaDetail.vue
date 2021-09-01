<template>
    <div>
        <Navbar />
        <div class="container">
            <DataSetForm />
            <DataSetTable />
            <!-- <table class="table table-bordered text-center mt-5">
                <thead>
                    <tr>
                        <th scope="col" style="width: 10%">#</th>
                        <th scope="col" style="width: 25%">Created</th>
                        <th scope="col" style="width: 25%">Status</th>
                        <th scope="col" style="width: 40%">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="dataSet, index in schemaDataSets" :key="dataSet.id">
                        <th class="align-middle" scope="row">
                            {{ index + 1 }}
                        </th>
                        <td class="align-middle">
                            {{ dataSet.created }}
                        </td>
                        <td class="align-middle">
                            <div id="taskStatus" :class="dataSet.status == 'Processing' ?  'btn btn-danger' : 'btn btn-success'">
                                {{ dataSet.status }}
                            </div>
                        </td>
                        <td>
                            <form @submit.prevent="getDataSetFile(dataSet.id)" class="d-inline mx-2">
                                <button :class="dataSet.status == 'Processing' ?  'btn btn-outline-warning disabled actionButton' : 'btn btn-warning actionButton'" type="submit">
                                    Download
                                </button>
                            </form>
                            <form @submit.prevent="deleteDataSet(dataSet.id, index)" class="d-inline">
                                <button :class="dataSet.status == 'Processing' ? 'btn btn-danger disabled actionButton' : 'btn btn-danger actionButton'" type="submit">
                                    Delete
                                </button>
                            </form>
                        </td>
                    </tr>
                </tbody>
            </table> -->
        </div>
    </div>
</template>

<script>
// import { mapState } from 'vuex'
import Navbar from '@/components/Navbar.vue'
import DataSetForm from '@/components/forms/DataSetForm.vue'
import DataSetTable from '@/components/tables/DataSetTable.vue'
// import axiosApi from '../axios-api'
export default {
    name: "SchemaDetail",
    components: {
        Navbar,
        DataSetForm,
        DataSetTable
    },
    data() {
        return {
            schemaID: this.$route.params.id,
            numRows: null,
            creatingCSV: false
        }
    },
    created() {
        // this.getDataSets()
    },
    // computed: mapState(['schemaDataSets']),
    methods: {
        // async getDataSets() {
        //     console.log(`DETAIL ${this.$store.state.userToken}`)
        //     await axiosApi.get(`/api/my-schema/${this.schemaID}/`,
        //     {
        //         headers: {
        //             "Authorization": `Bearer ${this.$store.state.userToken}`
        //         }
        //     })
        //     .then(response => {
        //         this.$store.dispatch("setSchemaDataSets", response.data)
        //     })
        //     .catch(error => {
        //         console.log(error)
        //     })
        // },
        // async createDataSet() {
        //     await axiosApi.post(`/api/my-schema/${this.schemaID}/`, {
        //         num_row: this.numRows
        //     },
        //     {
        //         headers: {
        //             "Authorization": `Bearer ${this.$store.getters.getToken}`
        //         }
        //     })
        //     .then(response => {
        //         console.log(response)
        //         this.creatingCSV = true
        //         this.$store.dispatch("addSchemaDataSet", response.data.dataSet)
        //         this.getTaskStatus(response.data.taskID)
        //     })
        //     .catch(error => {
        //         console.log(error)
        //     })
        // },
        // async deleteDataSet(dataSetID, index) {
        //     await axiosApi.delete(`/api/my-schema/${dataSetID}/`,
        //     {
        //         headers: {
        //             "Authorization": `Bearer ${this.$store.getters.getToken}`
        //         }
        //     })
        //     .then(() => {
        //         this.$store.dispatch("removeSchemaDataSet", index)
        //     })
        //     .catch(error => {
        //         console.log(error)
        //     })
        // },
        // async getDataSetFile(dataSetID) {
        //     await axiosApi.get(`api/my-schema/get-file/${dataSetID}/`,
        //     {
        //         headers: {
        //             "Authorization": `Bearer ${this.$store.getters.getToken}`
        //         }
        //     })
        //     .then(response => {
        //         const fileURL = window.URL.createObjectURL(new Blob([response.data]));
        //         const fileLink = document.createElement('a');
        //         fileLink.href = fileURL;
        //         fileLink.setAttribute('download', `fakeSchema_${dataSetID}.csv`);
        //         document.body.appendChild(fileLink);
        //         fileLink.click();
        //     })
        //     .catch(error => {
        //         console.log(error)
        //     })
        // },
        // async getTaskStatus(taskID) {
        //     await axiosApi.get(`api/task-status/${taskID}/`,
        //     {
        //         headers: {
        //             "Authorization": `Bearer ${this.$store.getters.getToken}`
        //         }
        //     })
        //     .then(response => {
        //         const taskStatus = response.data.taskStatus
        //         if (taskStatus === "SUCCESS") {
        //             console.log('SUCC')
        //             this.creatingCSV = false
        //             this.numRows = ''
        //             this.$store.dispatch("changeDataSetStatus")
        //         } else if (taskStatus === "PENDING") {
        //             console.log('PEND')
        //             setTimeout(()=> {
        //                 this.getTaskStatus(taskID)
        //             }, 1000)
        //         }
        //     })
        // }
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