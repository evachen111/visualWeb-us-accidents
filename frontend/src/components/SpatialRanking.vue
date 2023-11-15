<template>
  <div style="height: 90vh;width: 100%">
    <div id='myRankingPlot' style="height: inherit"></div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "SpatialRanking",
  props:["selectedState","selectedCounty"],
  data: () => ({
    BarPlotData: {x: [], y: []},
  }),
  mounted() {
    this.fetchData()
    // this.drawBarPlot()
  },
  methods: {
    async fetchData() {
      var reqUrl = 'http://127.0.0.1:5000/GetSpatialDataBar?state='+ this.$props.selectedState
          +'&county=' + this.$props.selectedCounty
      console.log("ReqURL " + reqUrl)
      // await response and data
      const response = await fetch(reqUrl)
      const responseData = await response.json();
      // transform data to usable by lineplot
      // console.log(responseData)
      this.BarPlotData.x=responseData["region"]
      this.BarPlotData.y=responseData["count"]
      // this.$data.beplot after the data is transformed
      this.drawBarPlot()
    },

    drawBarPlot() {
      // plotly code comes later here
      // var data = [
      //   {
      //     x: ['CA', 'FL', 'TX', 'OR', 'VA', 'NY', 'PA', 'MN', 'NC', 'SC'],
      //     y: [795868, 401388, 149037, 126341, 113535, 108049, 99975, 97185, 91362, 89216],
      //     marker:{
      //       color: ['rgb(180,10,10)', 'rgb(222,128, 0)', 'rgb(255,204,151)', 'rgb(255,204,151)', 'rgb(250,204,151)', 'rgb(245,204,151)'
      //         , 'rgb(235,204,151)', 'rgb(222,200,180)', 'rgb(220,200,180)', 'rgb(210,204,184)']
      //     },
      //     type: 'bar'
      //   }
      // ];
      //
      // var layout = {
      //   title: 'Top 10 states with the most traffic accidents'
      // };
      var trace1 = {
        x: this.BarPlotData.x,
        y: this.BarPlotData.y,
        type: 'bar'
      };
      var data = [trace1];
      var layout = {
        title: 'Ranking areas inside the Specified Region',
        xaxis: {
          title: 'Region'
        },
        yaxis: {
          title: 'Count'
        }
      }
      var config = {responsive: true, displayModeBar: false}
      Plotly.newPlot('myRankingPlot', data,layout,config);

    }
  }
}
</script>

<style scoped>

</style>