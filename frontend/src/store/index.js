import { createStore } from 'vuex'


export default createStore({
    state: {
        username: localStorage.getItem('username') || '',
        userSchemas: [],
        schemaColumns: [],
        schemaDataSets: []
    },
    mutations: {
        directloginUser(state, username) {
            state.username = username
            localStorage.setItem("username", username)
        },
        directLogoutUser(state) {
            state.username = ''
            localStorage.removeItem("username")
        },
        directSetSchemas(state, schemas) {
            state.userSchemas = schemas
        },
        directRemoveSchema(state, index) {
            state.userSchemas.splice(index, 1)
        },
        directAddColumn(state, column) {
            state.schemaColumns.push(column)
        },
        directRemoveColumn(state, index) {
            state.schemaColumns.splice(index, 1)
        },
        directClearColumns(state) {
            state.schemaColumns.splice(0, state.schemaColumns.length)
        },
        directSetSchemaDataSets(state, dataSets) {
            state.schemaDataSets = dataSets
        },
        directAddSchemaDataSet(state, dataSet) {
            state.schemaDataSets.push(dataSet)
        },
        directChangeDataSetStatus(state) {
            state.schemaDataSets[state.schemaDataSets.length-1].status = "Ready"
        }
    },
    actions: {
        loginUser(context, username) {
            context.commit("directloginUser", username)
        },
        logoutUser(context) {
            context.commit("directLogoutUser")
        },
        setSchemas(context, schemas) {
            context.commit("directSetSchemas", schemas)
        },
        removeSchema(context, index) {
            context.commit("directRemoveSchema", index)
        },
        addColumn(context, column) {
            context.commit("directAddColumn", column)
        },
        removeColumn(context, index) {
            context.commit("directRemoveColumn", index)
        },
        clearColumns(context) {
            context.commit("directClearColumns")
        },
        setSchemaDataSets(context, dataSets) {
            context.commit("directSetSchemaDataSets", dataSets)
        },
        addSchemaDataSet(context, dataSet) {
            context.commit("directAddSchemaDataSet", dataSet)
        },
        changeDataSetStatus(context) {
            context.commit("directChangeDataSetStatus")
        }
    }
})
