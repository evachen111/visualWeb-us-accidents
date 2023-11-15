<!--<template>-->
<!--  <div class="Layout">-->
<!--    this is the page layout-->
<!--    <ul class="menu">-->
<!--      <li><router-link :to="{ name: 'PredictionPage' }" exact>Prediction</router-link></li>-->
<!--      <li><router-link :to="{ name: 'TimePage'}">Time Analysis</router-link></li>-->
<!--      <li><router-link :to="{ name: 'SpatialPage' }">Spatial Analysis</router-link></li>-->
<!--    </ul>-->
<!--    <router-view></router-view>-->
<!--  </div>-->
<!--</template>-->

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
<!--                      <a class="nav-link active" href="../page/PredictionPage.vue">-->
<!--                        <i class="fas fa-car-crash" style="width: 17px;"></i>-->
<!--                        <span>Prediction</span>-->
<!--                      </a>-->

<!--                      <a class="nav-link">-->
<!--                        <i class="fas fa-chart-line"></i>-->
<!--                        <span>Time Analysis</span>-->
<!--                      </a>-->

<!--                      <a class="nav-link" href="../page/pageSpatialPage">-->
<!--                        <i class="fas fa-chart-area"></i>-->
<!--                        <span>Spatial Analysis</span>-->
<!--                      </a>-->

            <router-link :to="{ name: 'Prediction' }"  class = "nav-link active">
              <i class="fas fa-car-crash" style="width: 17px;"></i>
              <span>Prediction</span>
            </router-link>

            <router-link :to="{ name: 'TimePage' }"  class = "nav-link active">
              <i class="fas fa-chart-line"></i>
              <span>Time Analysis</span>
            </router-link>

            <router-link :to="{ name: 'SpatialPage' }"  class = "nav-link active">
              <i class="fas fa-chart-area"></i>
              <span>Spatial Analysis</span>
            </router-link>

          </li>
        </ul>
        <div class="text-center d-none d-md-inline">
          <button class="btn rounded-circle border-0" id="sidebarToggle" type="button"></button>
        </div>
      </div>
    </nav>
    <router-view></router-view>
    <a class="border rounded d-inline scroll-to-top" href="#page-top"><i class="fas fa-angle-up"></i></a></div>
  </body>
  <!--  <a class="border rounded d-inline scroll-to-top" href="#page-top"><i class="fas fa-angle-up"></i></a>-->
  <!--  </div>-->
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Layout"
}
</script>

<style scoped>

</style>