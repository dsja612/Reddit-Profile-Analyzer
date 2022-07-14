<template>
    <Header title="Reddit User Analyser" info="just some info"></Header>
    <Overview></Overview>
</template>

<script>
import Header from "./components/Header"
import Overview from "./components/Overview"

export default {
  name: 'App',
  components: {
    Header,
    Overview,
  }
}
</script>

<style>

  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Poppins', sans-serif;
    background-color: #b8a4a0;
  }

  h1, h2, h3, h4, h5 {
    color: #0d0d0d;
  }

  .circle {   
    display: flex;
    height: 100px;
    width: 100px;
    background-color: #bbb;
    border-radius: 50%;
    justify-content: center;
    align-items: center;
  }

  hr {
    width: 80%;
    margin-left: auto;
    margin-right: auto;
  }
</style>

