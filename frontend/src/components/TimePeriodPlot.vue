<template>
  <div style="height: 90vh;width: 100%">
    <div id='myPeriodBarPlot' style="height: inherit"></div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "TimePeriodPlot",
  data: () => ({
    LinePlotData: {x: [], y: []}
  }),
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      var reqUrl = 'http://127.0.0.1:5000/PeriodDataValues' //无参的例子
      console.log("ReqURL " + reqUrl)
      // await response and data
      const response = await fetch(reqUrl)
      const responseData = await response.json();
      // transform data to usable by lineplot
      // console.log(responseData)
      this.LinePlotData.x=responseData["x"]
      this.LinePlotData.y=responseData["y"]
      // draw the lineplot after the data is transformed
      this.drawBarPlot()
    },
    // drawLinePlot() {
    //   var trace1 = {
    //     x: this.LinePlotData.x,
    //     y: this.LinePlotData.y,
    //     type: 'scatter'
    //   };
    //   var data = [trace1];
    //   var layout = {}
    //   var config = {responsive: true, displayModeBar: false}
    //   Plotly.newPlot('myPeriodLinePlot', data, layout, config);
    // },

    drawBarPlot() {
      // plotly code comes later here
      var data = [
        {
          x: this.LinePlotData.x,
          y: this.LinePlotData.y,
          type: 'bar'
        }
      ];
      var layout = {
        title: 'Count of Accidents by Day/Night',
        xaxis: {
          title: 'Day Period'
        },
        yaxis: {
          title: 'Count of cases'
        }
      }
      Plotly.newPlot('myPeriodBarPlot', data,layout);

    }
  }
}
</script>

<style scoped>

</style>