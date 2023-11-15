<template>
  <div class="col-xl-7">
    <div class="row">
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Severity Prediction</h4>
            <h6 class="text-muted card-subtitle mb-2">In case of data from US accidents</h6>
            <p class="text-danger card-text">According to the factors you choose, we predict that if an
              accident were going to happen, the severity(1 for the lowest and 4 for the highest) would
              be:
              <!--                        <br><br><strong>2</strong><br><br>-->
            <h1><strong>
            <p style="color: red ">{{best}}</p>
            </strong></h1><p>
            No matter what the severity, for the
            safety of your life, please drive with caution😀</p>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <div class="card shadow mb-4">
          <div class="card-header d-flex justify-content-between align-items-center">
            <h6 class="text-primary font-weight-bold m-0">Prediction</h6>
            <div class="dropdown no-arrow">
              <button class="btn btn-link btn-sm dropdown-toggle" data-toggle="dropdown" aria-expanded="false"
                      type="button"><i class="fas fa-ellipsis-v text-gray-400"></i></button>
              <div class="dropdown-menu shadow dropdown-menu-right animated--fade-in"
                   role="menu">
                <p class="text-center dropdown-header">dropdown header:</p><a class="dropdown-item"
                                                                              role="presentation" href="#">&nbsp;Action</a><a
                  class="dropdown-item" role="presentation" href="#">&nbsp;Another action</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" role="presentation" href="#">&nbsp;Something else here</a></div>
            </div>
          </div>
          <div class="card-body d-xl-flex justify-content-xl-center align-items-xl-center">
            <!--                      <img-->
            <!--                        src="../assets/img/prediction.png" width="100%" height="100%">-->
            <div style="height: 90vh; width: 100%" >
              <!--    <h3>Profit View of: {{ $props.selectedWeather }} & {{ $props.selectedPeriod }}</h3>-->
              <div id='myPredictionPlot' style="height: inherit"></div>



            <!--                      <ScatterPlot :key="scatterPlotId"-->
            <!--                                   :selectedCategory="categories.selectedValue"-->
            <!--                                   @changeCurrentlySelectedCompany="changeCurrentlySelectedCompany"-->
            <!--                      />-->

          </div>
        </div>
      </div>
    </div>
  </div>


  </div>
</template>

<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "PredictionBarPlot",
  props: ["selectedWeather", "selectedPeriod","ifCrossing","ifJunction","ifSignal"],

  data: () => ({
    BarPlotData: {x: [], y: []},
    best:"?"
  }),
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      var reqUrl = 'http://127.0.0.1:5000/PredictionBar?weather='+ this.$props.selectedWeather
          +'&period=' + this.$props.selectedPeriod
          +'&crossing=' + this.$props.ifCrossing
          +'&junction=' + this.$props.ifJunction
          +'&signal=' + this.$props.ifSignal
      console.log("ReqURL " + reqUrl)
      // await response and data
      const response = await fetch(reqUrl)
      const responseData = await response.json();
      // transform data to usable by lineplot
      // console.log(responseData)
      this.BarPlotData.x=responseData["x"]
      this.BarPlotData.y=responseData["y"]
      this.best=responseData["best"]
      // this.$data.best=responseData["best"]
      // console.log("Most possible severity: " + this.best)
      // draw the lineplot after the data is transformed
      this.drawBarPlot()
    },
    drawBarPlot() {
      var trace1 = {
        x: this.BarPlotData.x,
        y: this.BarPlotData.y,
        type: 'bar'
      };
      var data = [trace1];
      var layout = {
        title: 'Prediction Result with Probabilities',
        xaxis: {
          title: 'Severity'
        },
        yaxis: {
          title: 'Probability'
        }
      }
      var config = {responsive: true, displayModeBar: false}
      Plotly.newPlot('myPredictionPlot',data,layout,config);
    },
    // getBest(){
    //   console.log("get best:",this.best)
    //   return this.best
    // }

    }

}
</script>

<style scoped>

</style>