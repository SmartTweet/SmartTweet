<template>
  <div class="tweets">
    <h1>{{ msg }}</h1>
    <table v-if="tweets" class="table table-striped">
                <thead class="thead-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Date</th>
                        <th scope="col">Content</th>
                        <th scope="col">Confident level</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="tweet in tweets" :key="tweet.id_tweet">
                        <th scope="row">{{ tweet.id_tweet }}</th>
                        <td>{{ tweet.date }}</td>
                        <td>{{ tweet.content }}</td>
                        <td>{{ tweet.confident_level | toPercent }}%</td>
                    </tr>
                </tbody>
            </table>
  </div>
</template>

<script>
export default {
  name: 'Tweets',
  props: {
    msg: String,
    tweets: Array
  },
  created: function() {
      axios
                    .get('http://localhost:5000/api/tweets/')
                    .then(response => {
                        const responseData = response.data
                        this.tweets = responseData
                    })
                    .catch(err => {
                        console.log(err)
                    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
