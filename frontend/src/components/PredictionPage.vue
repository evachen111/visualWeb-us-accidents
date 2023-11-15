<template>
  <!--  <div id="app">-->
  <body id="page-top">
  <div id="wrapper">
    <nav class="navbar navbar-dark align-items-start sidebar sidebar-dark accordion bg-gradient-primary p-0">
      <div class="container-fluid d-flex flex-column p-0">
        <a class="navbar-brand d-flex justify-content-center align-items-center sidebar-brand m-0" href="#">
          <div class="sidebar-brand-icon rotate-n-15"><i class="fas fa-laugh-wink"></i></div>
          <div class="sidebar-brand-text mx-3"><span>Team_IMPACT<br>US accidents<br></span></div>
        </a>
        <hr class="sidebar-divider my-0">
        <ul class="nav navbar-nav text-light" id="accordionSidebar">
          <li class="nav-item" role="presentation">
            <a class="nav-link active" href="./PredictionPage.vue"><i
                class="fas fa-car-crash" style="width: 17px;"></i><span>Prediction</span></a>
            <a class="nav-link" href="./TimePage.vue"><i
                class="fas fa-chart-line"></i><span>Time Analysis</span></a>
            <a class="nav-link" href="./SpatialPage.vue"><i
                class="fas fa-chart-area"></i><span>Spatial Analysis</span></a></li>
        </ul>
        <div class="text-center d-none d-md-inline">
          <button class="btn rounded-circle border-0" id="sidebarToggle" type="button"></button>
        </div>
      </div>
    </nav>
    <div class="d-flex flex-column" id="content-wrapper">
      <div id="content">
        <div class="container-fluid">
          <div class="row">
            <div class="col">
              <div class="d-sm-flex justify-content-between align-items-center mb-4">
                <h3 class="text-dark mb-0">Prediction</h3><span><br>Wondering how&nbsp;enviromental factors affect the severities of traffic accidents, give it a try!<br><br></span><a
                  class="btn btn-primary btn-sm d-none d-sm-inline-block" role="button" href="#"><i
                  class="fas fa-download fa-sm text-white-50"></i>&nbsp;Generate Report</a></div>
            </div>
          </div>
          <div class="row">
            <div class="col-xl-5">
              <div class="row">
                <div class="col-md-6 col-xl-12 mb-4">
                  <div class="card shadow border-left-primary py-2">
                    <div class="card-body">
                      <div class="row align-items-center no-gutters">
                        <div class="col mr-2">
                          <div class="text-uppercase text-primary font-weight-bold text-xs mb-1"><span>Weather</span>
                          </div>
                        </div>
                      </div>
                      <div><span>Is it raining? Snowing?Windy?……</span></div>
                      <ul class="list-group">
                        <li class="list-group-item">
                          <div>
                            <div class="row">
                              <div class="col text-right d-xl-flex justify-content-xl-end align-items-xl-center"><span
                                  class="text-right">Specify the weather</span></div>
                              <div class="col-xl-6">
<!--                                <div class="dropdown"  style="width: 100%;">-->
<!--                                  <button class="btn btn-primary btn-sm dropdown-toggle" data-toggle="dropdown"-->
<!--                                          aria-expanded="false" type="button" style="width: 100%;">Default-->
<!--                                  </button>-->
<!--                                  <div class="dropdown-menu" role="menu"><a class="dropdown-item" role="presentation"-->
<!--                                                                            href="#">First Item</a><a-->
<!--                                      class="dropdown-item" role="presentation" href="#">Second Item</a><a-->
<!--                                      class="dropdown-item" role="presentation" href="#">Third Item</a></div>-->
<!--                                </div>-->
<!--                                <v-select-->
<!--                                    :items="weathers.values"-->
<!--                                    dense-->
<!--                                    v-model="weathers.selectedValue"-->
<!--                                    @change="changeWeather"-->
<!--                                ></v-select>-->
                              </div>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-xl-12 mb-4">
                  <div class="card shadow border-left-success py-2">
                    <div class="card-body">
                      <div class="row align-items-center no-gutters">
                        <div class="col mr-2">
                          <div class="text-uppercase text-success font-weight-bold text-xs mb-1"><span>POI</span></div>
                          <div><span>Point-Of-Interest annotations</span>
                            <div class="row">
                              <div class="col">
                                <div class="card shadow mb-4">
                                  <ul class="list-group list-group-flush">
                                    <li class="list-group-item">
                                      <div class="row align-items-center no-gutters">
                                        <div class="col mr-2">
                                          <h6 class="mb-0"><strong>Junction</strong></h6><span class="text-xs">indicates presence of junction in a nearby location<br></span>
                                        </div>
                                        <div class="col-auto">
                                          <div class="custom-control custom-checkbox" id="jc">
<!--                                            <input-->
<!--                                              class="custom-control-input" type="checkbox" value="0" id="formCheck-1"-->
<!--                                              v-model="junction" @change = "handleChange1(event)"-->
<!--                                              >-->
                                            <input
                                                class="custom-control-input" type="checkbox" id="formCheck-1"
                                                v-model="junction"
                                            >
                                            <label
                                              class="custom-control-label" for="formCheck-1"></label>
                                          </div>
                                        </div>
                                      </div>
                                    </li>
                                    <li class="list-group-item">
                                      <div class="row align-items-center no-gutters">
                                        <div class="col mr-2">
                                          <h6 class="mb-0"><strong>Traffic Signal</strong></h6><span class="text-xs">indicates presence of traffic signals in a nearby location<br></span>
                                        </div>
                                        <div class="col-auto">
                                          <div class="custom-control custom-checkbox" id="sg"><input
                                              class="custom-control-input" type="checkbox" id="formCheck-2" v-model="signal"><label
                                              class="custom-control-label" for="formCheck-2"></label></div>
                                        </div>
                                      </div>
                                    </li>
                                    <li class="list-group-item">
                                      <div class="row align-items-center no-gutters">
                                        <div class="col mr-2">
                                          <h6 class="mb-0"><strong>Crossing</strong></h6><span class="text-xs">indicates presence of crossing in a nearby location<br></span>
                                        </div>
                                        <div class="col-auto">
                                          <div class="custom-control custom-checkbox" id="cs"><input
                                              class="custom-control-input" type="checkbox" id="formCheck-3" v-model="crossing"><label
                                              class="custom-control-label" for="formCheck-3"></label></div>
                                        </div>
                                      </div>
                                    </li>
                                  </ul>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 col-xl-12 mb-4">
                  <div class="card shadow border-left-info py-2">
                    <div class="card-body">
                      <div class="row align-items-center no-gutters">
                        <div class="col mr-2">
                          <div class="text-uppercase text-warning font-weight-bold text-xs mb-1"><span
                              style="color: rgb(54,185,204);">Period</span></div>
                          <div><span>Is it daytime or night?</span></div>
                          <div class="row">
                            <div class="col">
                              <ul class="list-group">
                                <li class="list-group-item">
                                  <div>
                                    <div class="row">
                                      <div
                                          class="col text-right d-xl-flex justify-content-xl-end align-items-xl-center">
                                        <span class="text-right">Specify the period</span></div>
                                      <div class="col-xl-6">

<!--                                        <div class="dropdown" style="width: 100%;">-->
<!--                                          <button class="btn btn-info btn-sm dropdown-toggle" data-toggle="dropdown"-->
<!--                                                  aria-expanded="false" type="button" style="width: 100%;">{{period}}}-->
<!--                                          </button>-->
<!--                                          <div class="dropdown-menu"-->
<!--                                               role="menu">-->
<!--                                            <a class="dropdown-item" role="presentation" >Day</a>-->
<!--                                            <a class="dropdown-item" role="presentation" >Night</a>-->
<!--&lt;!&ndash;                                            <a class="dropdown-item" role="presentation"&ndash;&gt;-->
<!--&lt;!&ndash;                                               >Third Item</a>&ndash;&gt;-->
<!--                                          </div>-->
<!--                                        </div>-->


<!--                                        <v-select-->
<!--                                            :items="periods.values"-->
<!--                                            dense-->
<!--                                            v-model="periods.selectedValue"-->
<!--                                            @change="changePeriod"-->
<!--                                        ></v-select>-->
<!--                                        <select v-model="periods" multiple>-->
<!--                                          <option value="1">Day</option>-->
<!--                                          <option value="0">Night</option>-->
<!--                                        </select>-->

                                      </div>
                                    </div>
                                  </div>
                                </li>
                              </ul>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xl-7">
              <div class="row">
                <div class="col">
                  <div class="card">
                    <div class="card-body">
                      <h4 class="card-title">Severity Prediction</h4>
                      <h6 class="text-muted card-subtitle mb-2">In case of data from US accidents</h6>
                      <p class="text-danger card-text">According to the factors you choose, we predict that if an
                        accident were going to happen, the severity(1 lowest-4highest) would
                        be:<br><br><strong>???????</strong><br><br>No matter what the severity, for the
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
                      <PredictionBarPlot/>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row sr-only">
            <div class="col-md-6 col-xl-4 mb-4">
              <div class="card shadow border-left-primary py-2">
                <div class="card-body">
                  <div class="row align-items-center no-gutters">
                    <div class="col mr-2">
                      <div class="text-uppercase text-primary font-weight-bold text-xs mb-1"><span>Weather</span></div>
                    </div>
                  </div>
                  <div><span>Is it raining? Snowing?Windy?……</span></div>
                  <ul class="list-group">
                    <li class="list-group-item">
                      <div>
                        <div class="row">
                          <div class="col text-right d-xl-flex justify-content-xl-end align-items-xl-center"><span
                              class="text-right">Specify the weather</span></div>
                          <div class="col-xl-6">
                            <div class="dropdown" style="width: 100%;">
                              <button class="btn btn-primary btn-sm dropdown-toggle" data-toggle="dropdown"
                                      aria-expanded="false" type="button" style="width: 100%;">Weather
                              </button>
                              <div class="dropdown-menu" role="menu"><a class="dropdown-item" role="presentation"
                                                                        href="#">First Item</a><a class="dropdown-item"
                                                                                                  role="presentation"
                                                                                                  href="#">Second
                                Item</a><a class="dropdown-item" role="presentation" href="#">Third Item</a></div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-xl-4 mb-4">
              <div class="card shadow border-left-success py-2">
                <div class="card-body">
                  <div class="row align-items-center no-gutters">
                    <div class="col mr-2">
                      <div class="text-uppercase text-success font-weight-bold text-xs mb-1"><span>POI</span></div>
                      <div><span>Point-Of-Interest annotations</span>
                        <div class="row">
                          <div class="col">
                            <div class="card shadow mb-4">
                              <ul class="list-group list-group-flush">
                                <li class="list-group-item">
                                  <div class="row align-items-center no-gutters">
                                    <div class="col mr-2">
                                      <h6 class="mb-0"><strong>Junction</strong></h6><span class="text-xs">indicates presence of junction in a nearby location<br></span>
                                    </div>
                                    <div class="col-auto">
                                      <div class="custom-control custom-checkbox"><input class="custom-control-input"
                                                                                         type="checkbox"
                                                                                         id="formCheck-1"><label
                                          class="custom-control-label" for="formCheck-1"></label></div>
                                    </div>
                                  </div>
                                </li>
                                <li class="list-group-item">
                                  <div class="row align-items-center no-gutters">
                                    <div class="col mr-2">
                                      <h6 class="mb-0"><strong>Traffic Signal</strong></h6><span class="text-xs">indicates presence of traffic signals in a nearby location<br></span>
                                    </div>
                                    <div class="col-auto">
                                      <div class="custom-control custom-checkbox"><input class="custom-control-input"
                                                                                         type="checkbox"
                                                                                         id="formCheck-2"><label
                                          class="custom-control-label" for="formCheck-2"></label></div>
                                    </div>
                                  </div>
                                </li>
                                <li class="list-group-item">
                                  <div class="row align-items-center no-gutters">
                                    <div class="col mr-2">
                                      <h6 class="mb-0"><strong>Crossing</strong></h6><span class="text-xs">indicates presence of crossing in a nearby location<br></span>
                                    </div>
                                    <div class="col-auto">
                                      <div class="custom-control custom-checkbox"><input class="custom-control-input"
                                                                                         type="checkbox"
                                                                                         id="formCheck-3"><label
                                          class="custom-control-label" for="formCheck-3"></label></div>
                                    </div>
                                  </div>
                                </li>
                              </ul>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-xl-4 mb-4">
              <div class="card shadow border-left-info py-2">
                <div class="card-body">
                  <div class="row align-items-center no-gutters">
                    <div class="col mr-2">
                      <div class="text-uppercase text-warning font-weight-bold text-xs mb-1"><span
                          style="color: rgb(54,185,204);">Period</span></div>
                      <div><span>Is it daytime or night?</span></div>
                      <div class="row">
                        <div class="col">
                          <ul class="list-group">
                            <li class="list-group-item">
                              <div>
                                <div class="row">
                                  <div class="col text-right d-xl-flex justify-content-xl-end align-items-xl-center">
                                    <span class="text-right">Specify the period</span></div>
                                  <div class="col-xl-6">
                                    <div class="dropdown" style="width: 100%;">
                                      <button class="btn btn-info btn-sm dropdown-toggle" data-toggle="dropdown"
                                              aria-expanded="false" type="button" style="width: 100%;">Period
                                      </button>
                                      <div class="dropdown-menu" role="menu"><a class="dropdown-item"
                                                                                role="presentation" href="#">First
                                        Item</a><a class="dropdown-item" role="presentation" href="#">Second Item</a><a
                                          class="dropdown-item" role="presentation"
                                          href="#">Third Item</a></div>
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </li>
                          </ul>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col">
              <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Correlation Heatmap</h4>
                  <p class="card-text">
                    Some words
                  </p>
                  <div class="row">
                    <div class="col-xl-6">
                      <div class="card shadow mb-4">
                        <div class="card-header d-flex justify-content-between align-items-center">
                          <h6 class="text-primary font-weight-bold m-0">Weather Condition vs. Severity</h6>
                          <div class="dropdown no-arrow">
                            <button class="btn btn-link btn-sm dropdown-toggle" data-toggle="dropdown"
                                    aria-expanded="false" type="button"><i class="fas fa-ellipsis-v text-gray-400"></i>
                            </button>
                            <div class="dropdown-menu shadow dropdown-menu-right animated--fade-in"
                                 role="menu">
                              <p class="text-center dropdown-header">dropdown header:</p><a class="dropdown-item"
                                                                                            role="presentation"
                                                                                            href="#">&nbsp;Action</a><a
                                class="dropdown-item" role="presentation" href="#">&nbsp;Another action</a>
                              <div class="dropdown-divider"></div>
                              <a class="dropdown-item" role="presentation" href="#">&nbsp;Something else here</a></div>
                          </div>
                        </div>
                        <div class="card-body d-xl-flex justify-content-xl-center align-items-xl-center">
                          <!--                          <img-->
                          <!--                            src="../assets/img/heatmap1.png" width="90%" height="90%">-->
                          <PredictionHeatmapWeather/>
                        </div>
                      </div>
                    </div>
                    <div class="col-xl-6">
                      <div class="card shadow mb-4">
                        <div class="card-header d-flex justify-content-between align-items-center">
                          <h6 class="text-primary font-weight-bold m-0">Road Condition vs. Severity</h6>
                          <div class="dropdown no-arrow">
                            <button class="btn btn-link btn-sm dropdown-toggle" data-toggle="dropdown"
                                    aria-expanded="false" type="button"><i class="fas fa-ellipsis-v text-gray-400"></i>
                            </button>
                            <div class="dropdown-menu shadow dropdown-menu-right animated--fade-in"
                                 role="menu">
                              <p class="text-center dropdown-header">dropdown header:</p><a class="dropdown-item"
                                                                                            role="presentation"
                                                                                            href="#">&nbsp;Action</a><a
                                class="dropdown-item" role="presentation" href="#">&nbsp;Another action</a>
                              <div class="dropdown-divider"></div>
                              <a class="dropdown-item" role="presentation" href="#">&nbsp;Something else here</a></div>
                          </div>
                        </div>
                        <div class="card-body d-xl-flex justify-content-xl-center align-items-xl-center">
                          <!--                          <img-->
                          <!--                            src="../assets/img/heatmap2.png" width="90%" height="90%">-->
                          <PredictionHeatmapRoad/>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <footer class="bg-white sticky-footer">
        <div class="container my-auto">
          <div class="text-center my-auto copyright"><span>Copyright © Team Impact &nbsp;IVDA 2022</span></div>
        </div>
      </footer>
    </div>
    <a class="border rounded d-inline scroll-to-top" href="#page-top"><i class="fas fa-angle-up"></i></a></div>
  </body>

  <!--  </div>-->

</template>

<script>
import "../assets/js/jquery.min.js"
import "../assets/bootstrap/js/bootstrap.min.js"
import "../assets/js/script.min.js"

import PredictionHeatmapRoad from "@/components/PredictionHeatmapRoad";
import PredictionBarPlot from "@/components/PredictionBarPlot";
import PredictionHeatmapWeather from "@/components/PredictionHeatmapWeather";
// import Vue from "vue";
// var cb1=new Vue({
//   el:"#jc",
//   data:{
//     checkedStatus:"0"
//   },
//   methods:{
//     handleChange1:function (event){
//       console.log("现在的junction checkbox值为：",event.target.checked)
//     },
//   }
// })
export default {
  name: "PredictionPage",
  components: {PredictionHeatmapWeather, PredictionHeatmapRoad, PredictionBarPlot},
  data: () => ({
    periods: {
      values: ["Day","Night"],
      selectedValue: "Day"
    },

    weathers: {
      values: ["weather_list"],
      selectedValue: "weather_list"
    },

    signal:{
      checked:false
    },

    crossing:{
      checked:false
    },

    junction:{
      checked:false
    }
  }),
  method:{
    // changePeriod(){
    //   // this.scatterPlotId+=1
    //   // code
    // },
    // changeWeather() {
    //   this.linePlotId += 1
    // },
    // handleChange1:function (event){
    //   console.log("现在的junction checkbox值为：",event.target.checked)
    // },
    // handleChange2:function (event){
    //   console.log("现在的signal checkbox值为：",event.target.checked)
    // },
    // handleChange3:function (event){
    //   console.log("crossing checkbox值为：",event.target.checked)
    // }
  }
}
</script>

<!--<style scoped>-->
<style>
@import "../assets/bootstrap/css/bootstrap.min.css";

/*@import "https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i";*/
@import "../assets/fonts/fontawesome-all.min.css";
@import "../assets/css/styles.min.css";
</style>