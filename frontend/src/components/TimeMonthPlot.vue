<template>
  <div style="height: 90vh;width: 100%">
    <div id='myMonthLinePlot' style="height: inherit"></div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "TimeMonthPlot",
  data: () => ({
    LinePlotData: {x: [], y: []}
  }),
  mounted() {
    this.fetchData()
  },
  methods: {
    // drawLinePlot() {
    //   // plotly code comes later here
    //   var trace1 = {
    //     x: [1, 2, 3, 4],
    //     y: [10, 15, 13, 17],
    //     type: 'scatter'
    //   };
    //
    //   var trace2 = {
    //     x: [1, 2, 3, 4],
    //     y: [16, 5, 11, 9],
    //     type: 'scatter'
    //   };
    //
    //   var data = [trace1, trace2];
    //
    //   Plotly.newPlot('myMonthLinePlot', data);

      async fetchData() {
        var reqUrl = 'http://127.0.0.1:5000/MonthDataValues' //无参的例子
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
          title: 'Count of Accidents by Month',
          xaxis: {
            title: 'Month'
          },
          yaxis: {
            title: 'Count of cases',
            // tick0:0,
            // tickmode : 'linear',
            //
            // dtick : 0.25
            // tickmode:"linear"
          }
        }
        var config = {responsive: true, displayModeBar: false}
        Plotly.newPlot('myMonthLinePlot', data, layout, config);

    }
  }
}
</script>

<style scoped>

</style>