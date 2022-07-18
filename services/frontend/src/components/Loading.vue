<template>
    <PulseLoader :loading=store.showLoading size="20px"></PulseLoader>
</template>
 
<script>
    import { store } from '../main.js'
    import PulseLoader from './PulseLoader'
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