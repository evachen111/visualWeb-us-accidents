<template>
  <div style="height: 90vh;width: 100%">
    <div id='myHourLinePlot' style="height: inherit"></div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "TimeHourPlot",
  data: () => ({
    LinePlotData: {x: [], y: []}
  }),
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      var reqUrl = 'http://127.0.0.1:5000/HourDataValues' //无参的例子
      console.log("ReqURL " + reqUrl)
      // await response and data
      const response = await fetch(reqUrl)
      const responseData = await response.json();
      // transform data to usable by lineplot
      // console.log(responseData)
      this.LinePlotData.x=responseData["x"]
      this.LinePlotData.y=responseData["y"]
      // draw the lineplot after the data is transformed
      this.drawLinePlot()
    },
    drawLinePlot() {
      var trace1 = {
        x: this.LinePlotData.x,
        y: this.LinePlotData.y,
        type: 'scatter'
      };
      var data = [trace1];
      var layout = {
        title: 'Count of Accidents by Hour',
        xaxis: {
          title: 'Hour'
        },
        yaxis: {
          title: 'Count of cases'
        }
      }
      var config = {responsive: true, displayModeBar: false}
      Plotly.newPlot('myHourLinePlot', data, layout, config);
    }
  }
}
</script>

<style scoped>

</style>