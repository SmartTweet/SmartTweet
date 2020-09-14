const PieChart = Vue.component('pie-chart', {
    mixins: [VueChartJs.mixins.reactiveData],
    extends: VueChartJs.Pie
})

new Vue({
    el: '#app',
    data() {
        return {
            hashtag: '',
            selectedSentiment: null, // 0: positive, 1: neutral, 2: negative, 3:mixed
            SENTIMENT: [
                'positif',
                'neutral',
                'negative',
                'mixed'
            ],
            tweets: null,
            notFilteredTweets: null
        }
    },
    components: {
        'pie-chart': PieChart
    },
    filters: {
        toUpperCase: function (val) {
            if (!val) return ''
            val = val.toString()
            return val.toUpperCase()
        },
        toPercent: function(val) {
            if (!val) return ''
            return val * 100
        }
    },
    methods: {
        search: function (event) {
            axios
                .get('http://localhost:5000/api/tweet/' + this.hashtag)
                .then(response => {
                    const responseData = response.data
                    this.notFilteredTweets = responseData
                    counts = _.countBy(responseData, 'sentiment')
                    console.log(responseData)
                    console.log(counts)

                    this.$refs.chart.renderChart({
                        labels: ["Positive", "Neutral", "Negative", "Mixed"],
                        datasets: [{
                            label: 'Tweets sentiment',
                            backgroundColor: ['#89c402', '#0078d4', '#a51419', '#976C0E'],
                            data: [counts.positif, counts.neutral, counts.negative, counts.mixed]
                        }]
                    }, { responsive: true, maintainAspectRatio: false, onClick: this.update })
                    console.log(counts)
                })
                .catch(err => {
                    console.log(err)
                })
        },
        update(point, event) {
            const item = event[0]
            console.log(item)
            this.selectedSentiment = item._index
            this.tweets = _.filter(this.notFilteredTweets, { 'sentiment': this.SENTIMENT[this.selectedSentiment] })
        }
    }
})