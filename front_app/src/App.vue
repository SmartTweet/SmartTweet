<template>
<div id="app">
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
