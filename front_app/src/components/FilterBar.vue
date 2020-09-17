<template>
<div>
    <div class="input-group mb-3">
        <div class="input-group-prepend">
            <span class="input-group-text">#</span>
        </div>
        <input placeholder="Search hashtag" type="text" class="form-control" v-model="filtre" v-on:keyup="filtrer">
    </div>

</div>
</template>

<script>
export default {
    name: 'FilterBar',
    props: {
        filter: String
    },
    data() {
        return {
            filtre: ""
        }
    },
    methods: {
        filtrer() {
            this.$emit('filtrer', this.filtre)
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style scoped>

</style>
