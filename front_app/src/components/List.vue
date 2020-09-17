<template>
<div>
    <ul class="list-group">
        <li class="list-group-item" @click="HashtagClick" :key=tweet v-for="tweet in list">
            {{tweet}}
        </li>
    </ul>
</div>
</template>

<script>
export default {
    name: "List",
    props: {
        list: Array,
    },
    methods: {
        HashtagClick() {
            console.log(' WAZA');
        }
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style scoped>
.TweetList {
    height: 90%;
    width: 40%;
    background-color: #424242;
    margin: 3em;
    padding: 1em;
    background-color: ivory;
}

li:hover {
    cursor: pointer;
    background-color: red;
}
</style>
