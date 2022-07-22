<template>
    <!-- icon -->
    <!-- title -->
    <!-- info -->
    <!-- search bar -->

    <div class="headerContainer">
        <header>
            <img src="https://www.reshot.com/preview-assets/icons/4TX9GESJRZ/reddit-4TX9GESJRZ.svg" width="100" height="100">
            <h1>{{title}}</h1>
            <!-- <h1>{{info}}</h1> -->
            <SearchBar prefix="/u/"/>
        </header>
        <Loading></Loading>
    </div>
</template>

<script>
import SearchBar from "../Interactive/SearchBar"
import Loading from "../Loading/Loading"

export default {
    name: 'Header',
    props: {
        title: String,
        info: String,
    },
    components: {
        SearchBar,
        Loading,
    },
}
</script>

<style scoped>
    .headerContainer {
        padding: 15px;
        padding-bottom: 25px;
        border-radius: 5px;
        text-align: center;
        margin-bottom: 50px;
        background-color: #FEF9F8;
    }

    h1 {
        margin-bottom: 15px;
    }
</style>