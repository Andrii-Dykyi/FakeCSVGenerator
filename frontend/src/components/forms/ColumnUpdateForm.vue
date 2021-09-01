<template>
<div>
    <form @submit.prevent>
        <div class="row mb-3">
            <div class="col">
                <label class="form-label">Column name</label>
                <input 
                    type="text" 
                    class="form-control" 
                    :value="column.name" 
                    @input="onNameChange(column, $event.target.value)"
                >
            </div>
            <div class="col">
                <label class="form-label">Column type</label>
                <select 
                    :value="column.typeof" 
                    @click="displayIntegerField" 
                    class="form-select" 
                    @change="onTypeChange(column, $event.target.value)"
                    required
                >
                    <option 
                        v-for="column_type in columnTypes" 
                        :key="column_type.type" 
                        :value="column_type.type" 
                    >
                        {{ column_type.display }}
                    </option>
                </select>
            </div>
            <div :class="column.typeof != 'integer' ? 'col d-none' : 'col'">
                <label class="form-label">From</label>
                <input 
                    type="text" 
                    class="form-control" 
                    :value="column.range_from" 
                    @input="onFromChange(column, $event.target.value)"
                    min="0"
                >
            </div>
            <div :class="column.typeof != 'integer' ? 'col d-none' : 'col'">
                <label class="form-label">To</label>
                <input 
                    type="text" 
                    class="form-control" 
                    :value="column.range_to" 
                    @input="onToChange(column, $event.target.value)"
                    min="0"
                >
            </div>
            <div class="col">
                <label class="form-label">Order</label>
                <input 
                    type="number" 
                    class="form-control" 
                    :value="column.order" 
                    @input="onOrderChange(column, $event.target.value)" 
                    min="0"
                >
            </div>
            <div class="col-1">
                <button 
                    type="button" 
                    class="btn btn-danger col-submit float-end"
                    @click="removeColumn(index)"
                >
                Delete
                </button>
            </div>
        </div>
    </form>
</div>
</template>

<script>
export default {
    name: "ColumnUpdateForm",
    props: ['column', 'index'],
    data() {
        return {
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
        } 
    },
    methods: {
        removeColumn(index) {
            this.$store.dispatch('removeColumn', index)
        },
        onNameChange(column, value) {
            column.name = value
        },
        onTypeChange(column, value) {
            column.typeof = value
        },
        onFromChange(column, value) {
            column.range_from = value
        },
        onToChange(column, value) {
            column.range_to = value
        },
        onOrderChange(column, value) {
            column.order = value
        }
    }
}
</script>

<style scoped>
    .col-submit {
        margin-top: 32px;
    }
</style>