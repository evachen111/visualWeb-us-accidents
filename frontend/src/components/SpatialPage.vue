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
            <li class="nav-item" role="presentation"><a class="nav-link" href="./PredictionPage.vue"><i
                class="fas fa-car-crash"
                style="width: 17px;"></i><span>Prediction</span></a><a
                class="nav-link" href="./TimePage.vue"><i class="fas fa-chart-line"></i><span>Time Analysis</span></a><a
                class="nav-link active"
                href="./SpatialPage.vue"><i class="fas fa-chart-area"></i><span>Spatial Analysis</span></a></li>
          </ul>
          <div class="text-center d-none d-md-inline">
            <button class="btn rounded-circle border-0" id="sidebarToggle" type="button"></button>
          </div>
        </div>
      </nav>
      <div class="d-flex flex-column" id="content-wrapper">
        <div id="content">
          <div class="container-fluid">
            <div class="d-sm-flex justify-content-between align-items-center mb-4">
              <h3 class="text-dark mb-0">Spatial Analysis</h3><span style="width: 600px;"><br>Where are the accident-prone areas (states/cities/counties/streets) in the U.S.?<br><br></span><a
                class="btn btn-primary btn-sm d-none d-sm-inline-block" role="button" href="#"><i
                class="fas fa-download fa-sm text-white-50"></i>&nbsp;Generate Report</a></div>
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
                    <div class="dropdown">
                      <button class="btn btn-primary btn-sm dropdown-toggle" data-toggle="dropdown"
                              aria-expanded="false" type="button" style="width: 100%;">All
                      </button>
                      <div class="dropdown-menu" role="menu"><a class="dropdown-item" role="presentation" href="#">First
                        Item</a><a class="dropdown-item" role="presentation" href="#">Second Item</a><a
                          class="dropdown-item" role="presentation" href="#">Third Item</a></div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col">
                <div class="row justify-content-center align-items-center">
                  <div class="col-auto col-xl-8 text-center"><span>Choose a city</span>
                    <div class="dropdown">
                      <button class="btn btn-success btn-sm dropdown-toggle" data-toggle="dropdown"
                              aria-expanded="false" type="button" style="width: 100%;">All
                      </button>
                      <div class="dropdown-menu" role="menu"><a class="dropdown-item" role="presentation" href="#">First
                        Item</a><a class="dropdown-item" role="presentation" href="#">Second Item</a><a
                          class="dropdown-item" role="presentation" href="#">Third Item</a></div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col">
                <div class="row justify-content-center align-items-center">
                  <div class="col-auto col-xl-9 text-center"><span>Choose a county</span>
                    <div class="dropdown">
                      <button class="btn btn-info btn-sm dropdown-toggle" data-toggle="dropdown" aria-expanded="false"
                              type="button" style="width: 100%;">All
                      </button>
                      <div class="dropdown-menu" role="menu"><a class="dropdown-item" role="presentation" href="#">First
                        Item</a><a class="dropdown-item" role="presentation" href="#">Second Item</a><a
                          class="dropdown-item" role="presentation" href="#">Third Item</a></div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col">
                <div class="row justify-content-center align-items-center">
                  <div class="col-auto col-xl-9 text-center"><span>Choose the street</span>
                    <div class="dropdown">
                      <button class="btn btn-warning btn-sm dropdown-toggle" data-toggle="dropdown" aria-expanded="false"
                              type="button" style="width: 100%;">All
                      </button>
                      <div class="dropdown-menu" role="menu"><a class="dropdown-item" role="presentation" href="#">First
                        Item</a><a class="dropdown-item" role="presentation" href="#">Second Item</a><a
                          class="dropdown-item" role="presentation" href="#">Third Item</a></div>
                    </div>
                  </div>
                </div>
              </div>
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
                    <SpatialMap/>
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
                    <SpatialRanking/>
                  </div>
                </div>
              </div>
              <div class="col-lg-6 col-xl-4">
                <div class="row" style="height: 50%;">
                  <div class="col" style="height: 100%;">
                    <div class="card text-white bg-primary shadow d-xl-flex" style="height: 80%;">
                      <div class="card-body">
                        <p class="m-0">Analysis</p>
                        <p class="text-white-50 small m-0">blablabla</p>
                      </div>
                    </div>
                  </div>
                  <div class="col" style="height: 100%;">
                    <div class="card text-white bg-success shadow" style="height: 80%;">
                      <div class="card-body">
                        <p class="m-0">Analysis</p>
                        <p class="text-white-50 small m-0">blablabla</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="row" style="height: 50%;">
                  <div class="col" style="height: 100%;">
                    <div class="card text-white bg-info shadow" style="height: 80%;">
                      <div class="card-body">
                        <p class="m-0">Analysis</p>
                        <p class="text-white-50 small m-0">blablabla</p>
                      </div>
                    </div>
                  </div>
                  <div class="col" style="height: 100%;">
                    <div class="card text-white bg-warning shadow" style="height: 80%;">
                      <div class="card-body">
                        <p class="m-0">Analysis</p>
                        <p class="text-white-50 small m-0">blablabla</p>
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
    <!--  <a class="border rounded d-inline scroll-to-top" href="#page-top"><i class="fas fa-angle-up"></i></a>-->
<!--  </div>-->
</template>

<!--<script src="../assets/js/jquery.min.js"></script>-->
<!--<script src="../assets/bootstrap/js/bootstrap.min.js"></script>-->
<!--<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.js"></script>-->
<!--<script src="../assets/js/script.min.js"></script>-->

<script>
import "../assets/js/jquery.min.js"
import "../assets/bootstrap/js/bootstrap.min.js"
import "../assets/js/script.min.js"
import SpatialMap from "@/components/SpatialMap";
import SpatialRanking from "@/components/SpatialRanking";
export default {
  name: "SpatialPage",
  components:{SpatialRanking,SpatialMap},
 data:()=>({
   statelist:[]
 })
}
</script>

<!--<style scoped>-->
<style >
@import "../assets/bootstrap/css/bootstrap.min.css";
/*@import "https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i";*/
@import "../assets/fonts/fontawesome-all.min.css";
@import "../assets/css/styles.min.css";
</style>