<template>
    <div class="mt-5">
        <h3 class="d-inline">Data Sets</h3>
        <form @submit.prevent="createDataSet" class="row float-end">
            <div class="col-auto">
                <label class="col-form-label"></label>
            </div>
            <div class="col-auto">
                <input 
                    v-model="dataSet.num_row" 
                    type="number" 
                    class="form-control" 
                    placeholder="Number of Rows" 
                    min="1"
                    required
                >
            </div>
            <div class="col-auto">
                <button :disabled="creatingCSV" id="dataSetSubmit" type="submit" class="btn btn-success">Generate data</button>
            </div>
        </form>
    </div>
</template>

<script>
import axiosApi from '@/axiosBase'


export default {
    name: "dataSetForm",
    data() {
        return {
            dataSet: {
                num_row: "1"
            },
            creatingCSV: false
        }
    },
    methods: {
        async createDataSet() {
            await axiosApi.post(`/schema/${this.$route.params.id}/data-sets/`, this.dataSet)
            .then(response => {
                this.creatingCSV = true
                this.$store.dispatch("addSchemaDataSet", response.data.dataSet)
                this.getDataSetStatus(response.data.taskID)
                this.$toast.success("Please wait. Your data is generating!", {
                    position: 'top'
                })
            })
        },
        async getDataSetStatus(taskID) {
            await axiosApi.get(`/schema/status/${taskID}/`)
            .then(response => {
                const taskStatus = response.data.taskStatus

                if (taskStatus === "SUCCESS") {
                    this.dataSet.num_row = "1"
                    this.creatingCSV = false
                    this.$store.dispatch("changeDataSetStatus")
                    this.$toast.info("Your data is ready. Push the button «Download»", {
                        position: 'top'
                    })
                } else if (taskStatus === "PENDING") {
                    setTimeout(() => {
                        this.getDataSetStatus(taskID)
                    }, 2000)
                }
            })
        }
    }
}
</script>

<style scoped>
</style>