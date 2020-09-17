<template>
<div class="List">
    <ul class="list-group">
        <li class="list-group-item" @click="HashtagClick(tweet)" :key=tweet v-for="tweet in list">
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
    data() {
        return {
            selected: null,
        }
    },
    methods: {
        HashtagClick(tweet) {
            if (!tweet) {
                console.log("le tweet est null !");
                return;
            }
            console.log(tweet);
            this.selected = tweet;
        }
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style scoped>
.List {
    color: #131313;
}

li:hover {
    cursor: pointer;
    color: ivory;
    background-color: #666;
}
</style>
