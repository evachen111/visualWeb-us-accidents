<template>
  <body id="app" >
  <div>
    <div class="d-flex flex-column" id="content-wrapper">
      <div id="content">
        <div class="container-fluid">
          <div class="row">
            <div class="column">
          <div class="d-sm-flex justify-content-between align-items-center mb-4">
            <h3 class="text-dark mb-0">Time Analysis</h3><span><br>Which season, which month, &nbsp;which weekday, and at which time of a day&nbsp;are accidents most likely to occur in the U.S?&nbsp;<br><br></span><a
              class="btn btn-primary btn-sm d-none d-sm-inline-block"
              role="button" href="#"><i class="fas fa-download fa-sm text-white-50"></i>&nbsp;Generate Report</a>
          </div>
            </div>
          </div>

          <div class="row">
            <div class="col-lg-4 col-xl-4">
              <div class="button">
                <div class="row" @click="show(1)" :class="index===1? 'active':''">
                  <div class="card shadow border-left-primary py-2" data-toggle="tooltip" data-bs-tooltip=""
                       style="width: 100%;" title="Click to see the visualization!">
                    <div class="card-body" data-bs-hover-animate="bounce">
                      <div class="row align-items-center no-gutters">
                        <div class="col mr-2">
                          <div class="text-uppercase text-primary font-weight-bold text-xs mb-1">
                            <div class="row">
                              <div class="col"><span>Year</span></div>
                            </div>
                          </div>
                          <div class="text-dark font-weight-bold h5 mb-0"><span>
                            It seems that the number of traffic accidents is increasing every year, especially after the year 2019, there is a huge increase!
                          </span></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="row" @click="show(2)" :class="index===2? 'active':''">
                  <div class="card shadow border-left-success py-2" data-toggle="tooltip" data-bs-tooltip=""
                       style="width: 100%;" title="Click to see the visualization!">
                    <div class="card-body" data-bs-hover-animate="bounce">
                      <div class="row align-items-center no-gutters">
                        <div class="col mr-2">
                          <div class="text-uppercase text-success font-weight-bold text-xs mb-1"><span>Month</span>
                          </div>
                          <div class="text-dark font-weight-bold h5 mb-0"><span>
                            The most accidents occurred in December and, relatively fewest in July. Almost more than half of the accidents occurred in the last three months
                          </span></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="row" @click="show(3)" :class="index===3? 'active':''">
                  <div class="card shadow border-left-info py-2" data-toggle="tooltip" data-bs-tooltip=""
                       style="width: 100%;" title="Click to see the visualization!">
                    <div class="card-body" data-bs-hover-animate="bounce">
                      <div class="row align-items-center no-gutters">
                        <div class="col mr-2">
                          <div class="text-uppercase text-warning font-weight-bold text-xs mb-1"><span
                              style="color: rgb(54,185,204);">Weekday</span></div>
                          <div class="text-dark font-weight-bold h5 mb-0"><span>
                            There are twice as many accidents on weekdays as on weekends, and Fridays are the most likely to be involved in crashes. The least number of traffic accidents occur on Sundays
                          </span></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="row" @click="show(4)" :class="index===4? 'active':''">
                  <div class="card shadow border-left-warning py-2" data-toggle="tooltip" data-bs-tooltip=""
                       style="width: 100%;" title="Click to see the visualization!">
                    <div class="card-body" data-bs-hover-animate="bounce">
                      <div class="row align-items-center no-gutters">
                        <div class="col mr-2">
                          <div class="text-uppercase text-warning font-weight-bold text-xs mb-1"><span>Period</span>
                          </div>
                          <div class="text-dark font-weight-bold h5 mb-0"><span>
                            More traffic accidents occur during the day than at night
                          </span></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="row" @click="show(5)" :class="index===5? 'active':''">
                  <div class="card shadow border-left-pink py-2" data-toggle="tooltip" data-bs-tooltip=""
                       style="width: 100%;" title="Click to see the visualization!">
                    <div class="card-body" data-bs-hover-animate="bounce">
                      <div class="row align-items-center no-gutters">
                        <div class="col mr-2">
                          <div class="text-uppercase text-warning font-weight-bold text-xs mb-1"><span
                              style="color: #f968d9;">Hour</span></div>
                          <div class="text-dark font-weight-bold h5 mb-0"><span>The most deadliest accident hour is 17:00pm, implying the event office-returning hours. The second most deadliest accident hour is 7am, implying the morning office-going hours.</span></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-8 col-xl-8">
              <div class="card shadow mb-4" style="width: 100%;height: 100%;">
                <div class="card-header d-flex justify-content-between align-items-center">
                  <!--                  <h6 class="text-primary font-weight-bold m-0">Year</h6>-->
                  <h6 class="text-primary font-weight-bold m-0">
                    {{ titletext }}
                  </h6>

                  <!--                    <div class="one" v-show="index===1 && isShow"></div>-->
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
                  <!--                      src="../assets/img/by_year.png" width="100%" height="100%">-->
                  <!--                    <TimeYearPlot/>-->
                  <keep-alive>
                    <component :is="comp"
                               v-show="isShow"></component>
                  </keep-alive>

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
import TimeYearPlot from "@/components/TimeYearPlot.vue";
import TimeMonthPlot from "@/components/TimeMonthPlot.vue";
import TimeHourPlot from "@/components/TimeHourPlot.vue";
import TimeWeekdayPlot from "@/components/TimeWeekdayPlot.vue";
import TimePeriodPlot from "@/components/TimePeriodPlot.vue";
// import { Line } from 'vue-chartjs/legacy'
export default {
  name: "TimePage",
  components: {TimeYearPlot, TimeWeekdayPlot, TimePeriodPlot, TimeHourPlot, TimeMonthPlot},
  // data: () => ({
  //
  // }),
  data() {
    return {
      // 控制切换按钮后按钮改变样式
      index: 1,
      // 控制子组件显示
      comp: 'TimeYearPlot',
      titletext: 'Year',
      // 控制点击按钮后子组件显示，再次点击隐藏
      isShow: true
    }
  },
  methods: {
    show(value) {
      if (this.index === value) {
        this.index = 0
        this.isShow = !this.isShow
      } else {
        this.index = value
        this.isShow = true
      }
      if (value === 1) {
        this.comp = 'TimeYearPlot'
        this.titletext = "Year"
      }
      if (value === 2) {
        this.comp = 'TimeMonthPlot'
        this.titletext = "Month"
      }
      if (value === 3) {
        this.comp = 'TimeWeekdayPlot'
        this.titletext = "Weekday"
      }
      if (value === 4) {
        this.comp = 'TimePeriodPlot'
        this.titletext = "Period"
      }
      if (value === 5) {
        this.comp = 'TimeHourPlot'
        this.titletext = "Hour"
      }

    }
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