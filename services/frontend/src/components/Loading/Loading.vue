<template>
    <div v-if="store.showLoading" class="overlay"></div>
    <PulseLoader :loading=store.showLoading size="20px" 
        :style="{'margin-top': '10px', 'margin-bottom': '-45px'}"></PulseLoader>
</template>
 
<script>
    import { store } from '../../main.js'
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
    .overlay {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        height: 100%;
        width: 100%;
        opacity: 0.8;
        background-color: #7b7b7b;
    }
</style>