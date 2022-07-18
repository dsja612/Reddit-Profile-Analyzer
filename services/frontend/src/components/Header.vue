<template>
    <!-- icon -->
    <!-- title -->
    <!-- info -->
    <!-- search bar -->

    <div class="headerContainer">
        <header>
            <i class="fa-brands fa-reddit fa-6x"></i>
            <h1>{{title}}</h1>
            <!-- <h1>{{info}}</h1> -->
            <SearchBar prefix="/u/"/>
        </header>
        <Loading></Loading>
    </div>
</template>

<script>
import SearchBar from "./SearchBar"
import Loading from "./Loading"

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
        max-width: 100%;
        margin: auto;
        overflow: auto;
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