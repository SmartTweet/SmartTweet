<template>
    <form class="form-inline" v-on:submit.prevent="search" novalidate>
        <div class="form-group mb-3" v-bind:class="{'open':openSuggestion}">
            <div class="input-group-prepend">
                <span class="input-group-text">#</span>
            </div>
            <input placeholder="Search hashtag" type="text" class="form-control" v-model="hashtag">
            <button class="btn btn-primary"><i class="fa fa-search"></i></button>
        </div>
    </form>
</template>

<script>
export default {
  name: 'SearchBar',
  props: {
    hashtag: String
  },
  methods: {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
