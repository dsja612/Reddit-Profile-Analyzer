<template>
    <Header title="Reddit User Analyser" info="just some info" @search="searchUser"></Header>
    <Overview v-if="showOverview"></Overview>
</template>

<script>
import Header from "./components/Header"
import Overview from "./components/Overview"

export default {
  name: 'App',
  components: {
    Header,
    Overview,
  },
  data() {
    return {
      data: {},
      showOverview: false,
      userExists: false,
    }
  },
  methods: {
    async fetchData(username) {

    },
    async searchUser(username) {
      const res = await fetch('http://localhost:5000/users/' + username)
      if (res.ok) {
        this.data = await res.json()
        this.showOverview = true
        this.userExists = true
      } else {
        alert('User does not exist!')
        this.showOverview = false
        this.userExists = false
      }
      // this.data.hasProperty('error') ? this.userExists = false : this.userExists = true
    }
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

