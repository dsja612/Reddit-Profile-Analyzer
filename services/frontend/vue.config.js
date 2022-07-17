const { defineConfig } = require('@vue/cli-service')
module.exports = {
  devServer: {
    allowedHosts: "all",
    proxy: "https://reddit-crawler-backend.herokuapp.com/",
  },
}