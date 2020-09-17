<template>
<div class="TweetList">
    <FilterBar v-on:filtrer="filtrerList" />
    <List :list="listeFiltree" />
</div>
</template>

<script>
import FilterBar from "./FilterBar.vue";
import List from "./List.vue";

export default {

    name: "TweetList",
    components: {
        FilterBar,
        List
    },
    props: {
        list: Array,
    },
    data() {
        return {
            listeFiltree: this.list
        }
    },
    methods: {
        filtrerList(filtre) {
            console.log(filtre);
        }
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style scoped>
.TweetList {
    max-height: ;
    height: auto;
    width: 40%;
    background-color: #424242;
}

.TweetList>div {
    margin: 0em 2em 1em 2em;
}

li:hover {
    cursor: pointer;
    background-color: #424242;
    color: ivory;
}
</style>
