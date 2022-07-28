<template>
    <div class="footerContainer" :style="{ position: changeFooterPosition }" :key="footerKey">
        <a :href="githubLink" target="_blank"><i class="pi pi-github" style="font-size: 2rem"></i></a>
    </div>
</template>

<script>
    import { store } from "../../main.js"

    export default {
        name: 'Footer',
        props: {
            githubLink: String,
        },
        data() {
            return {
                store,
                footerKey: 0,
            }
        },
        computed: {
            changeFooterPosition() {
                this.forceRender()
                
                if (!store.showOverview) {
                    return "absolute"
                }
                else { 
                    return "none"
                }
            }
        },
        methods: {
            forceRender() {
                this.footerKey += 1
            }
        }
    }
</script>

<style scoped>
.footerContainer {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100px;
    bottom: 0;
    left: 0;
    margin: 0;
}
</style>