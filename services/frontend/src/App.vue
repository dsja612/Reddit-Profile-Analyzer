<template>
    <Header title="Reddit Profile Analyser" 
      info="get insights on your reddit profile, activity and favourite subreddits" 
      @search="searchUser">
    </Header>
    <Overview v-if="store.showOverview"></Overview>
</template>

<script>
import { store } from './main.js'
import Header from "./components/Containers/Header"
import Overview from "./components/Containers/Overview"

export default {
  name: 'App',
  components: {
    Header,
    Overview,
  },
  data() {
    return {
      data: {},
      store,
    }
  },
  methods: {
    async searchUser(username) {
      store.showOverview = false
      store.showLoading = true

      const res = await fetch('https://reddit-crawler-backend.herokuapp.com/users/' + username)
      if (res.ok) {
        this.data = await res.json()
        this.storeData()
        store.showOverview = true
      } else {
        this.$swal.fire({ 
          icon: 'error',
          title: 'Error!',
          text: 'This user does not exist!'
        })
        store.showOverview = false
      }
      store.showLoading = false
    },

    storeData() {
      store.username = this.data.basic_data.data.name
      store.userDateJoined = new Date(this.data.basic_data.data.created_utc * 1000)
      store.numComments = this.data.num_comments
      store.numSubmissions = this.data.num_submissions
      store.commentKarma = this.data.basic_data.data.comment_karma
      store.submissionKarma = this.data.basic_data.data.link_karma
      store.topSubreddits = this.data.top_subreddits
      store.topWords = this.data.top_words
      store.commentPolarity = this.data.comment_polarity_summary
      store.commentSentiment = this.data.comment_sentiment
      store.commentFreqHrs = this.data.comment_freq.hrs
      store.commentFreqDays = this.data.comment_freq.days
      console.log(this.data)
    }
  },
  
}

</script>

<style>

  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  /* body {
    font-family: 'Poppins', sans-serif;
    background-color: #b8a4a0;
  }

  h1, h2, h3, h4, h5 {
    color: #0d0d0d;
  }

  .circle {   
    display: flex;
    height: 150px;
    width: 150px;
    background-color: #bbb;
    border-radius: 50%;
    justify-content: center;
    align-items: center;
  }

  hr {
    width: 80%;
    margin-left: auto;
    margin-right: auto;
  } */

#app {
  /* font-family: 'Avenir', Helvetica, Arial, sans-serif; */
  font-family:"Roboto",sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #022B3A;
  /* margin-top: 60px; */
  background-color: #E5E5E5;
}
.app-container {
  text-align: center;
}
body #app .p-button {
  margin-left: .2em;
}
form {
  margin-top: 2em;
}
</style>

