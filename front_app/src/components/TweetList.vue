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
            console.log(filtre)
            // mecanique de filtre
            this.listeFiltree = this.list.filter(function () {
                    $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
                }
            }
        }
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style scoped>
.TweetList {
    height: 20em;
    width: 60%;
    background-color: #424242;
    margin: 3em;
    padding: 1em;
}

li:hover {
    cursor: pointer;
    background-color: #424242;
    color: ivory;
}
</style>
