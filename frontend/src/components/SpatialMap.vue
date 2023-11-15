<template>
  <div style="height: 90vh;width: 100%">
    <div id='myMapPlot' style="height: inherit"></div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "SpatialMap",
  props:["selectedState","selectedCounty"],
  data: () => ({
    mapPlotJson:"",
    BarPlotData: {x: [], y: []}
  }),
  mounted() {
    this.fetchData()
    // this.drawMapPlot()
  },
  methods: {
    // 使用json数据
    // async fetchData() {
    //   var reqUrl = 'http://127.0.0.1:5000/YearData' //无参的例子
    //   console.log("ReqURL " + reqUrl)
    //   // await response and data
    //   const response = await fetch(reqUrl)
    //   const responseData = await response.json();
    //   // transform data to usable by lineplot
    //   responseData.data.forEach((data) => {
    //     this.LinePlotData.x.push(data[0])
    //     this.LinePlotData.y.push(data[1])
    //   })
    async fetchData() {
      var reqUrl = 'http://127.0.0.1:5000/GetSpatialDataMap?state='+ this.$props.selectedState
          +'&county=' + this.$props.selectedCounty
      console.log("ReqURL " + reqUrl)
      // await response and data
      const response = await fetch(reqUrl)
      const responseData = await response.json();
      // transform data to usable by lineplot
      console.log("responseData:",responseData)
      this.mapPlotJson=responseData["geojson"]
      this.BarPlotData.x=responseData["region"]
      this.BarPlotData.y=responseData["count"]
      // this.BarPlotData.x=responseData["region"]
      // this.BarPlotData.y=responseData["count"]
      // this.$data.beplot after the data is transformed
      this.drawMapPlot()
    },


    drawMapPlot() {

      var data = [{
        type: 'choropleth',
        // locationmode: 'USA-states',
        geojson: "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json",
        // this.mapPlotJson,
        featureidkey:"id",
        locations: ['OH',
          'IN', 'KY', 'WV', 'MI', 'PA', 'CA', 'NV', 'MN',
          'TX', 'MO', 'CO', 'OK', 'LA', 'KS', 'WI', 'IA',
          'MS', 'NE', 'ND', 'WY', 'SD', 'MT', 'NM', 'AR',
          'IL', 'NJ', 'GA', 'FL', 'NY', 'CT', 'RI', 'SC',
          'NC', 'MD', 'MA', 'TN', 'VA', 'DE', 'DC', 'ME',
          'AL', 'NH', 'VT', 'AZ', 'UT', 'ID', 'OR', 'WA'],
        // locations:this.BarPlotData.x,
        // z:this.BarPlotData.y,
        z: [24409, 20850, 6638, 7632, 43843, 99975, 795868, 6197, 97185, 149037, 29633, 25340, 8806,
          47232, 9033, 7896, 9607, 5320, 3320, 2258, 990, 201, 15964, 2370, 10935, 47105, 52902,
          40086, 401388, 108049, 29762, 4451, 89216, 91362, 65085, 6392, 52613, 113535, 4842,
          9133, 2193, 19322, 3866, 365, 56504, 49193, 8544, 126341, 32554],
        // text:this.BarPlotData.x,
        text: ['OH',
          'IN', 'KY', 'WV', 'MI', 'PA', 'CA', 'NV', 'MN',
          'TX', 'MO', 'CO', 'OK', 'LA', 'KS', 'WI', 'IA',
          'MS', 'NE', 'ND', 'WY', 'SD', 'MT', 'NM', 'AR',
          'IL', 'NJ', 'GA', 'FL', 'NY', 'CT', 'RI', 'SC',
          'NC', 'MD', 'MA', 'TN', 'VA', 'DE', 'DC', 'ME',
          'AL', 'NH', 'VT', 'AZ', 'UT', 'ID', 'OR', 'WA'],
        autocolorscale: true
      }];

      var layout = {
        title: 'Number of Traffic Accidents by State',
        geo:{
          scope: 'usa',
          countrycolor: 'rgb(255, 255, 255)',
          showland: true,
          landcolor: 'rgb(217, 217, 217)',
          showlakes: true,
          lakecolor: 'rgb(255, 255, 255)',
          subunitcolor: 'rgb(255, 255, 255)',
          lonaxis: {},
          lataxis: {}
        }
      };
      Plotly.newPlot("myMapPlot", data, layout, {showLink: false});


    }
  }
}
</script>

<style scoped>

</style>