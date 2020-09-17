const PieChart = Vue.component('pie-chart', {
    mixins: [VueChartJs.mixins.reactiveData],
    extends: VueChartJs.Pie
})

new Vue({
    el: '#app',
    data() {
        return {
            errors: [],
            hashtag: null,
            selectedSentiment: null, // 0: positive, 1: neutral, 2: negative, 3:mixed
            SENTIMENT: [
                'positive',
                'neutral',
                'negative',
                'mixed'
            ],
            tweets: null,
            // notFilteredTweets: null,
            hashtags: []
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
        toPercent: function (val) {
            if (!val) return ''
            return val * 100
        }
    },
    methods: {
        search: function (event) {
            if (this.checkForm())
                axios
                    .get('http://localhost:5000/api/tweet/' + this.hashtag)
                    .then(response => {
                        const responseData = response.data
                        this.notFilteredTweets = responseData
                        counts = _.countBy(responseData, 'sentiment')
                        this.$refs.chart.renderChart({
                            labels: ["Positive", "Neutral", "Negative", "Mixed"],
                            datasets: [{
                                label: 'Tweets sentiment',
                                backgroundColor: ['#89c402', '#0078d4', '#a51419', '#976C0E'],
                                data: [counts.positive, counts.neutral, counts.negative, counts.mixed]
                            }]
                        }, {
                            responsive: true,
                            maintainAspectRatio: false,
                            onClick: this.update,
                            title: { display: true, text: 'Number of tweet by sentiment for the hashtag #' + this.hashtag }
                        })
                    })
                    .catch(err => {
                        console.log(err)
                    })
        },
        checkForm: function () {
            if (!this.hashtag) {
                this.errors.push('Hashtag required.')
                return false
            }

            if (!this.hashtags.includes(this.hashtag)) {
                this.errors.push('Hashtag not in db. Try ' + this.hashtags.toString())
                return false
            }

            this.errors = []
            return true
        },
        update(point, event) {
            const item = event[0]
            this.selectedSentiment = item._index
            this.tweets = _.filter(this.notFilteredTweets, { 'sentiment': this.SENTIMENT[this.selectedSentiment] })
        }
    },
    mounted() {
        axios
            .get('http://localhost:5000/api/hashtags')
            .then(response => {
                this.hashtags = _.concat(response.data)
            })
            .catch(err => {
                console.log("err", err)
            })
    }
})