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
    computed: {
        //Filtering the suggestion based on the input
        matches() {
            return this.hashtags.filter((str) => {
                console.log("this hash", str.indexOf(this.hashtag))
                return str.indexOf(this.hashtag) >= 0;
            })
        },
        //The flag
        openSuggestion() {
            return this.hashtag !== "" &&
                this.matches.length != 0 &&
                this.open === true
        }
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
                        console.log(counts)
                        this.$refs.chart.renderChart({
                            labels: ["Positive", "Neutral", "Negative", "Mixed"],
                            datasets: [{
                                label: 'Tweets sentiment',
                                backgroundColor: ['#89c402', '#0078d4', '#a51419', '#976C0E'],
                                data: [counts.positive, counts.neutral, counts.negative, counts.mixed]
                            }]
                        }, { responsive: true, maintainAspectRatio: false, onClick: this.update })
                    })
                    .catch(err => {
                        console.log(err)
                    })
        },
        checkForm: function () {
            if (this.hashtag)
                return true

            if (!this.hashtag)
                this.errors.push('Hashtag required.')
        },
        update(point, event) {
            const item = event[0]
            this.selectedSentiment = item._index
            this.tweets = _.filter(this.notFilteredTweets, { 'sentiment': this.SENTIMENT[this.selectedSentiment] })
        },

        // Autocomplete
        //When enter pressed on the input
        enter() {
            this.selection = this.matches[this.current];
            this.open = false;
        },

        //When up pressed while suggestions are open
        up() {
            if (this.current > 0)
                this.current--;
        },

        //When up pressed while suggestions are open
        down() {
            if (this.current < this.suggestions.length - 1)
                this.current++;
        },

        //For highlighting element
        isActive(index) {
            return index === this.current;
        },

        //When the user changes input
        change() {
            if (this.open == false) {
                this.open = true;
                this.current = 0;
            }
        },

        //When one of the suggestion is clicked
        suggestionClick(index) {
            this.selection = this.matches[index];
            this.open = false;
        },
    },
    mounted() {
        axios
            .get('http://localhost:5000/api/hashtags')
            .then(response => {
                this.hashtags = _.concat(response.data)
                // this.hashtags = response.data
                console.log("#", this.hashtags)
            })
            .catch(err => {
                console.log("err", err)
            })
    }
})