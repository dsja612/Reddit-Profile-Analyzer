<template>
    <!-- icon -->
    <!-- title -->
    <!-- info -->
    <!-- search bar -->

    <div class="headerContainer">
        <header>
            <img src="https://www.reshot.com/preview-assets/icons/4TX9GESJRZ/reddit-4TX9GESJRZ.svg" width="100" height="100">
            <h1>{{title}}</h1>
            <h4>{{info}}</h4>
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
}
h1 {
    margin-top: 20px;
    margin-bottom: 30px;
    text-shadow: 2px 4px 30px #14213D;
}
h4 {
    margin-bottom: 30px;
    text-shadow: 2px 4px 30px #14213D;
    color: #14213D;
}
</style>