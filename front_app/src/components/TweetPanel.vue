<template>
<div class="TweetPanel">
    <TweetList :list=tweet_list />
</div>
</template>

<script>
import TweetList from "./TweetList.vue";

export default {
    name: "TweetPanel",
    data() {
        return {
            tweet_list: [
                "patate",
                "tomate",
                "pomme"
            ]
        }
    },
    components: {
        TweetList,
    },
    methods: {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style scoped>
.TweetPanel {
    width: 100%;
    background-color: grey;
}
</style>
