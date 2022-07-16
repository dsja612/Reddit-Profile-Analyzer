<template>
    <pulse-loader :loading=store.showLoading size="20px"></pulse-loader>
</template>
 
<script>
    import { store } from '../main.js'
    import PulseLoader from 'vue-spinner/src/PulseLoader.vue'
    export default {
        name: "Loading",
        components: {
            PulseLoader
        },
        data() {
            return {
                store,
            }
        },
    }
</script>

<style scoped>

</style>