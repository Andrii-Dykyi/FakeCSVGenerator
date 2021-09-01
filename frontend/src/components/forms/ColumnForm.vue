<template>
    <div class="mt-5 mb-5">
        <div class="border p-4 rounded-3">
            <form @submit.prevent="addColumn" class="form-inline">
                <div class="row">
                    <div class="col">
                        <label class="form-label">Column name</label>
                        <input v-model="newColumn.name" class="form-control" type="text" required>
                    </div>
                    <div class="col">
                        <label class="form-label">Column type</label>
                        <select v-model="newColumn.typeof" @click="displayIntegerField" class="form-select" required>
                            <option 
                                v-for="column_type in columnTypes" 
                                :key="column_type.type" 
                                :value="column_type.type"
                            >
                                {{ column_type.display }}
                            </option>
                        </select>
                    </div>
                    <div v-if="displayInteger" class="col">
                        <label class="form-label">From</label>
                        <input v-model="newColumn.range_from" class="form-control" type="number" min="0">
                    </div>
                    <div v-if="displayInteger" class="col">
                        <label class="form-label">To</label>
                        <input v-model="newColumn.range_to" class="form-control" type="number" min="0">
                    </div>
                    <div class="col">
                        <label class="form-label">Order</label>
                        <input v-model="newColumn.order" type="number" class="form-control" min="0">
                    </div>
                </div>
                <div class="mt-3">
                    <button type="submit" class="btn btn-primary">Add column</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
// import axiosApi from '../axios-api'


export default {
    name: "columnForm",
    data() {
        return {
            displayInteger: false,
            columnTypes: [
                {display: 'Full name', type: 'name'},
                {display: 'Company name', type: 'company'}, 
                {display: 'Job', type: 'job'}, 
                {display: 'Integer', type: 'integer'},
                {display: 'Phone number', type: 'phone_number'},
                {display: 'Address', type: 'address'},
                {display: 'Email', type: 'email'},
                {display: 'Domain name', type: 'domain_name'}
            ],
            newColumn: {
                name: '',
                typeof: '',
                range_from: "0",
                range_to: "1",
                order: "0"
            }
        }
    },
    methods: {
        addColumn() {
            this.$store.dispatch("addColumn", this.newColumn)
            this.newColumn = {
                name: '',
                typeof: '',
                range_from: "0",
                range_to: "1",
                order: "0"
            }
        },
        displayIntegerField() {
            if (this.newColumn.typeof == 'integer') {
                this.displayInteger = true
            } else {
                this.displayInteger = false
            }
        },
    }
}
</script>

<style scoped>
</style>