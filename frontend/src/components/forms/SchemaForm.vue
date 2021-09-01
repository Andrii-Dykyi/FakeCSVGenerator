<template>
    <div class="mt-5">
        <h3 class="mb-5">New Schema</h3>
        <form @submit.prevent="submitSchema">
            <div class="mb-3 float-end">
                <button id="createSchemaButton" type="submit" class="btn btn-primary">Submit</button>
            </div>
            <div class="mb-3">
                <input v-model="schemaData.name" type="text" class="form-control w-25" placeholder="Name" required>
            </div>
            <div class="mb-3">
                <select v-model="schemaData.column_separator" class="form-select w-25">
                    <option value=",">Comma (,)</option>
                    <option value=".">Dot (.)</option>
                </select>
            </div>
            <div class="mb-3">
                <select v-model="schemaData.string_character" class="form-select w-25">
                    <option value='"'>Double-quote (")</option>
                    <option value="'">Single-quote (')</option>
                </select>
            </div>
        </form>
    </div>
</template>

<script>
import { mapState } from 'vuex'
import axiosApi from '@/axiosBase'

export default {
    name: "SchemaForm",
    data() {
        return {
            schemaData: {
                name: '',
                column_separator: ',',
                string_character: '"'
            }
        }
    },
    computed: mapState(['schemaColumns']),
    methods: {
        async submitSchema() {
            // Check if at least one column exists
            if (this.schemaColumns.length == 0) {
                return this.$toast.error('Please, add at least one column and push the button «Submit»', {
                    position: 'top'
                });
            }
            // Check every column
            for (const column of this.schemaColumns) {
                // Check all fields are filled
                if (!(column.name && column.order !== '')) {
                    return this.$toast.error('Please, fill in all fields and push the button «Submit»', {
                        position: 'top'
                    });
                }
                // Check on negative number in order field
                if (column.order < 0) {
                    return this.$toast.error("Please, correct the mistake! ORDER can't be negative number.", {
                        position: 'top'
                    });
                }
                // Special check of integer type
                if (column.typeof === 'integer') {
                    if (!(
                        column.range_from !== '' 
                        && column.range_from !== null 
                        && column.range_to !== '' 
                        && column.range_to !== null
                    )) {
                        return this.$toast.error('Please, fill in all fields and push the button «Submit»', {
                            position: 'top'
                        });
                    }
                    if (column.range_from > column.range_to) {
                        return this.$toast.error("Please, correct the mistake! FROM can't be more than TO", {
                            position: 'top'
                        });
                    }
                } else {
                    column.range_from = null
                    column.range_to = null
                }
            }

            await axiosApi.post('/my-schemas/', {
                name: this.schemaData.name,
                column_separator: this.schemaData.column_separator,
                string_character: this.schemaData.string_character,
                columns: this.schemaColumns
            })
            .then(() => {
                this.$store.dispatch('clearColumns')
                this.$router.push({ name: 'home' })
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>

<style scoped>
    .col-submit {
        margin-top: 32px;
    }
</style>