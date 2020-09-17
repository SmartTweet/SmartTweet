<template>
<<<<<<< HEAD
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <Tweets msg="Hey" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
import Tweets from "./components/Tweets.vue"
// import HelloWorld from "./components/HelloWorld.vue"

export default {
  name: "App",
  components: {
    Tweets
  }
}
=======
<div>
    <!-- <img alt="Vue logo" src="./assets/logo.png" /> -->
    <TweetPanel />
</div>
</template>

<script>
import TweetPanel from "./components/TweetPanel.vue";

export default {
    name: "App",
    components: {
        TweetPanel,
    },
};
>>>>>>> master
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #131313;
}
</style>
