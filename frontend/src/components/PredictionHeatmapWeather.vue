<template>
  <div style="height: 90vh;width: 100%">
    <div id='myHeatmap2' style="height: inherit"></div>
  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "PredictionHeatmapWeather",
  data: () => ({
  }),
  mounted() {
    this.drawHeatmap()
  },
  methods: {
    drawHeatmap() {
      // plotly code comes later here
      var data = [
        {
          z: [[ 1.        ,  0.99385692, -0.36652699,  0.13775622,  0.21113381,
            0.07878798, -0.00442492, -0.04533516],
            [ 0.99385692,  1.        , -0.34602841,  0.13431233,  0.21757311,
              0.01301063, -0.00828863, -0.09745912],
            [-0.36652699, -0.34602841,  1.        ,  0.13881561, -0.36330464,
              -0.17409964,  0.07766306,  0.03780223],
            [ 0.13775622,  0.13431233,  0.13881561,  1.        ,  0.03638196,
              -0.03430467,  0.01368817,  0.04388288],
            [ 0.21113381,  0.21757311, -0.36330464,  0.03638196,  1.        ,
              0.03617689, -0.12162406,  0.00737141],
            [ 0.07878798,  0.01301063, -0.17409964, -0.03430467,  0.03617689,
              1.        ,  0.02716694,  0.04838158],
            [-0.00442492, -0.00828863,  0.07766306,  0.01368817, -0.12162406,
              0.02716694,  1.        ,  0.01384491],
            [-0.04533516, -0.09745912,  0.03780223,  0.04388288,  0.00737141,
              0.04838158,  0.01384491,  1.        ]],
          x: ['Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)',
            'Pressure(in)', 'Visibility(mi)', 'Wind_Direction', 'Wind_Speed(mph)',
            'Precipitation(in)','Severity'],
          y: ['Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)',
            'Pressure(in)', 'Visibility(mi)', 'Wind_Direction', 'Wind_Speed(mph)',
            'Precipitation(in)','Severity'],
          type: 'heatmap',
          hoverongaps: false
        }
      ];
      Plotly.newPlot('myHeatmap2', data);

    }
  }
}
</script>

<style scoped>

</style>