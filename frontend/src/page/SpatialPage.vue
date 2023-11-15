<template>
  <body id="app" >
  <div>
    <div class="d-flex flex-column" id="content-wrapper">
      <div id="content">
        <div class="container-fluid">
          <div class="row">
            <div class="col">
              <div class="d-sm-flex justify-content-between align-items-center mb-4">
                <h3 class="text-dark mb-0">Spatial Analysis</h3>
                <br>Where are the accident-prone areas (states/cities/counties/streets) in the U.S.?<br><br>
                <a
                  class="btn btn-primary btn-sm d-none d-sm-inline-block" role="button" href="#"><i
                  class="fas fa-download fa-sm text-white-50"></i>&nbsp;Generate Report</a></div>
            </div>
          </div>

          <div
              class="row sr-only visible">
            <div class="col-md-6 col-xl-3 mb-4">
              <div class="card shadow border-left-primary py-2">
                <div class="card-body">
                  <div class="row align-items-center no-gutters">
                    <div class="col mr-2">
                      <div class="text-uppercase text-primary font-weight-bold text-xs mb-1"><span>State</span></div>
                      <div class="text-dark font-weight-bold h5 mb-0"><span>Some conclusion or analysis</span>
                        <div></div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-xl-3 mb-4">
              <div class="card shadow border-left-success py-2">
                <div class="card-body">
                  <div class="row align-items-center no-gutters">
                    <div class="col mr-2">
                      <div class="text-uppercase text-success font-weight-bold text-xs mb-1"><span>City</span></div>
                      <div class="text-dark font-weight-bold h5 mb-0"><span>Some conclusion or analysis</span></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-xl-3 mb-4">
              <div class="card shadow border-left-info py-2">
                <div class="card-body">
                  <div class="row align-items-center no-gutters">
                    <div class="col mr-2">
                      <div class="text-uppercase text-warning font-weight-bold text-xs mb-1"><span
                          style="color: rgb(54,185,204);">County</span></div>
                      <div class="text-dark font-weight-bold h5 mb-0"><span>Some conclusion or analysis</span></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-xl-3 mb-4">
              <div class="card shadow border-left-warning py-2">
                <div class="card-body">
                  <div class="row align-items-center no-gutters">
                    <div class="col mr-2">
                      <div class="text-uppercase text-warning font-weight-bold text-xs mb-1"><span>Street</span></div>
                      <div class="text-dark font-weight-bold h5 mb-0"><span>Some conclusion or analysis</span></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col">
              <div class="row justify-content-center align-items-center">
                <div class="col-auto col-xl-8 text-center"><span>Choose a state</span>
<!--                  <div class="dropdown">-->
<!--                    <button class="btn btn-primary btn-sm dropdown-toggle" data-toggle="dropdown"-->
<!--                            aria-expanded="false" type="button" style="width: 100%;">All-->
<!--                    </button>-->
<!--                    <div class="dropdown-menu" role="menu"><a class="dropdown-item" role="presentation" href="#">First-->
<!--                      Item</a><a class="dropdown-item" role="presentation" href="#">Second Item</a><a-->
<!--                        class="dropdown-item" role="presentation" href="#">Third Item</a></div>-->
<!--                  </div>-->
<!--                  {{this.states.selectedValue}}-->
                  <v-container fluid data-app="true">
                    <v-select
                        :items="states.values"
                        dense
                        v-model="states.selectedValue"
                        @change="changeState"
                    ></v-select>
                  </v-container>

                </div>
              </div>
            </div>
            <div class="col">
              <div class="row justify-content-center align-items-center">
                <div class="col-auto col-xl-8 text-center"><span>Choose a county</span>
<!--                  <div class="dropdown">-->
<!--                    <button class="btn btn-success btn-sm dropdown-toggle" data-toggle="dropdown"-->
<!--                            aria-expanded="false" type="button" style="width: 100%;">All-->
<!--                    </button>-->
<!--                    <div class="dropdown-menu" role="menu"><a class="dropdown-item" role="presentation" href="#">First-->
<!--                      Item</a><a class="dropdown-item" role="presentation" href="#">Second Item</a><a-->
<!--                        class="dropdown-item" role="presentation" href="#">Third Item</a></div>-->
<!--                  </div>-->
                  <v-container fluid data-app="true">
                    <v-select
                        :items="counties.values"
                        dense
                        v-model="counties.selectedValue"
                        @change="changeCounty"
                    ></v-select>
                  </v-container>

                </div>
              </div>
            </div>
<!--            <div class="col">-->
<!--              <div class="row justify-content-center align-items-center">-->
<!--                <div class="col-auto col-xl-9 text-center"><span>Choose a county</span>-->
<!--                  <div class="dropdown">-->
<!--                    <button class="btn btn-info btn-sm dropdown-toggle" data-toggle="dropdown" aria-expanded="false"-->
<!--                            type="button" style="width: 100%;">All-->
<!--                    </button>-->
<!--                    <div class="dropdown-menu" role="menu"><a class="dropdown-item" role="presentation" href="#">First-->
<!--                      Item</a><a class="dropdown-item" role="presentation" href="#">Second Item</a><a-->
<!--                        class="dropdown-item" role="presentation" href="#">Third Item</a></div>-->
<!--                  </div>-->
<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
<!--            <div class="col">-->
<!--              <div class="row justify-content-center align-items-center">-->
<!--                <div class="col-auto col-xl-9 text-center"><span>Choose the street</span>-->
<!--                  <div class="dropdown">-->
<!--                    <button class="btn btn-warning btn-sm dropdown-toggle" data-toggle="dropdown" aria-expanded="false"-->
<!--                            type="button" style="width: 100%;">All-->
<!--                    </button>-->
<!--                    <div class="dropdown-menu" role="menu"><a class="dropdown-item" role="presentation" href="#">First-->
<!--                      Item</a><a class="dropdown-item" role="presentation" href="#">Second Item</a><a-->
<!--                        class="dropdown-item" role="presentation" href="#">Third Item</a></div>-->
<!--                  </div>-->
<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
            <!--              <div class="col">-->
            <!--                <div class="row justify-content-center align-items-center">-->
            <!--                  <div class="col-auto col-xl-9 text-center">-->
            <!--                    <div class="row">-->
            <!--                      <div class="col"><span>Choose the street</span></div>-->
            <!--                    </div>-->
            <!--                    <div class="row">-->
            <!--                      <div class="col">-->
            <!--                        <div class="dropdown">-->
            <!--                          <button class="btn btn-warning btn-sm dropdown-toggle" data-toggle="dropdown"-->
            <!--                                  aria-expanded="false" type="button" style="width: 100%;">All-->
            <!--                          </button>-->
            <!--                          <div class="dropdown-menu" role="menu"><a class="dropdown-item" role="presentation" href="#">First-->
            <!--                            Item</a><a class="dropdown-item" role="presentation" href="#">Second Item</a><a-->
            <!--                              class="dropdown-item" role="presentation" href="#">Third Item</a>-->
            <!--&lt;!&ndash;                            <h6&ndash;&gt;-->
            <!--&lt;!&ndash;                                class="dropdown-header" role="presentation">Header</h6>&ndash;&gt;-->
            <!--                          </div>-->
            <!--                        </div>-->
            <!--                      </div>-->
            <!--                    </div>-->
            <!--                  </div>-->
            <!--                </div>-->
            <!--              </div>-->
          </div>
          <div class="row">
            <div class="col-lg-6 col-xl-12">
              <div class="card shadow mb-4" style="width: 100%;">
                <div class="card-header d-flex justify-content-between align-items-center">
                  <h6 class="text-primary font-weight-bold m-0">Map Visualization</h6>
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
                  <!--                    <img-->
                  <!--                      src="../assets/img/spatial_map.png" width="80%" height="80%">-->
                  <SpatialMap :key="mapPlotID"
                              :selectedState="states.selectedValue"
                              :selectedCounty="counties.selectedValue"
                  />

                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-lg-6 col-xl-8">
              <div class="card shadow mb-4" style="width: 100%;">
                <div class="card-header d-flex justify-content-between align-items-center">
                  <h6 class="text-primary font-weight-bold m-0">Ranking</h6>
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
                <div class="card-body">
                  <!--                    <img class="img-fluid" src="../assets/img/spatial_summary.png">-->
                  <SpatialRanking :key="barPlotID"
                                  :selectedState="states.selectedValue"
                                  :selectedCounty="counties.selectedValue"
                  />
                </div>
              </div>
            </div>
            <div class="col-lg-6 col-xl-4">
              <div class="row" style="height: 50%;">
                <div class="col" style="height: 100%;">
                  <div class="card text-white bg-primary shadow d-xl-flex" style="height: 80%;">
                    <div class="card-body">
                      <p class="m-0">Analysis</p>
                      <p class="text-white-50 small m-0">1</p>
                    </div>
                  </div>
                </div>
                <div class="col" style="height: 100%;">
                  <div class="card text-white bg-success shadow" style="height: 80%;">
                    <div class="card-body">
                      <p class="m-0">Analysis</p>
                      <p class="text-white-50 small m-0">2</p>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row" style="height: 50%;">
                <div class="col" style="height: 100%;">
                  <div class="card text-white bg-info shadow" style="height: 80%;">
                    <div class="card-body">
                      <p class="m-0">Analysis</p>
                      <p class="text-white-50 small m-0">3</p>
                    </div>
                  </div>
                </div>
                <div class="col" style="height: 100%;">
                  <div class="card text-white bg-warning shadow" style="height: 80%;">
                    <div class="card-body">
                      <p class="m-0">Analysis</p>
                      <p class="text-white-50 small m-0">4</p>
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
    <a class="border rounded d-inline scroll-to-top" href="#app"><i class="fas fa-angle-up"></i></a>
  </div>
  </body>
</template>

<!--<script src="../assets/js/jquery.min.js"></script>-->
<!--<script src="../assets/bootstrap/js/bootstrap.min.js"></script>-->
<!--<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.js"></script>-->
<!--<script src="../assets/js/script.min.js"></script>-->

<script>
import "../assets/js/jquery.min.js"
import "../assets/bootstrap/js/bootstrap.min.js"
import "../assets/js/script.min.js"
import SpatialMap from "@/components/SpatialMap.vue";
import SpatialRanking from "@/components/SpatialRanking.vue";
export default {
  name: "SpatialPage",
  components:{SpatialRanking,SpatialMap},
  // props:["selectedState"],

  data: () => ({
    // periodId:0,
    // weatherId:0,
    mapPlotID:0,
    barPlotID:0,
    // statelist:["All","Else"],

    states: {

      values: ['All','Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',

        'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',

        'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',

        'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',

        'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming',

        'District of Columbia'],

      selectedValue: "All"

    },

    // states: {
    //   values: ["All","Else"],
    //   // values: this.statelist,
    //   selectedValue: "All"
    // },
// coountylist:["All","Else"],
    counties: {
      values: ["All","Else"],
      selectedValue: "All"
    }
  }),
  mounted() {
    this.fetchData()
  },

    methods: {
      async fetchData(){
        var reqUrl = 'http://127.0.0.1:5000/GetCountyList?state='+ this.states.selectedValue
        console.log("ReqURL " + reqUrl)
        // await response and data
        const response = await fetch(reqUrl)
        const responseData = await response.json();
        console.log("counties:", responseData["countylist"])
        // this.counties=responseData["countylist"]
        this.counties.values=responseData["countylist"]

      },
      changeState() {
        this.fetchData()
        // this.periods.selectedValue = periodId
        // this.states.selectedValue=stateId
        this.barPlotID += 1
        this.mapPlotID+=1
        // this.best=PredictionBarPlot.methods.getBest()
        // console.log("best:",this.best)
        //code
      },
      changeCounty() {
        // this.weathers.selectedValue = weatherID
        this.barPlotID += 1
        this.mapPlotID+=1
        // this.best=PredictionBarPlot.methods.getBest()
        // console.log("best:",this.best)
      }

    }
}
</script>

<!--<style scoped>-->
<style >
@import "../assets/bootstrap/css/bootstrap.min.css";
/*@import "https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i";*/
@import "../assets/fonts/fontawesome-all.min.css";
@import "../assets/css/styles.min.css";
</style>