<template>
<table class="table table-bordered text-center mt-5">
    <thead>
        <tr>
            <th scope="col" style="width: 10%">#</th>
            <th scope="col" style="width: 30%">Created</th>
            <th scope="col" style="width: 30%">Status</th>
            <th scope="col" style="width: 30%">Actions</th>
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
                    <button 
                        :class="dataSet.status == 'Processing' ?  'btn btn-outline-warning disabled actionButton' : 'btn btn-warning actionButton'" 
                        type="submit"
                    >
                        Download
                    </button>
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
    name: 'DataSetTable',
    computed: mapState(['schemaDataSets']),
    methods: {
        async getSchemaDataSets() {
            await axiosApi.get(`/schema/${this.$route.params.id}/data-sets/`)
            .then(response => {
                console.log(response.data)
                this.$store.dispatch('setSchemaDataSets', response.data)
            })
            .catch(error => {
                console.log(error)
            })
        },
        async getDataSetFile(dataSetID) {
            await axiosApi.get(`/dataset/${dataSetID}/file/`)
            .then(response => {
                const fileURL = window.URL.createObjectURL(new Blob([response.data]));
                const fileLink = document.createElement('a');

                fileLink.href = fileURL;
                fileLink.setAttribute('download', `fakeSchema_${dataSetID}.csv`);
                document.body.appendChild(fileLink);

                fileLink.click();
            })
        }
    },
    created() {
        this.getSchemaDataSets()
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