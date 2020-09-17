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
                "pomme",
                "pain",
                "raisin",
                "patate",
                "tomate",
                "pomme",
                "pain",
                "raisin",
                "patate",
                "tomate",
                "pomme",
                "pain",
                "raisin",
                "patate",
                "tomate",
                "pomme",
                "pain",
                "raisin",
                "patate",
                "tomate",
                "pomme",
                "pain",
                "raisin",
                "tofu"
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
}

.TweetPanel>div {
    margin: 1em;
    border-radius: 1em;
    padding: 1em;
}
</style>
