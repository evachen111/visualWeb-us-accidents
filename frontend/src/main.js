import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from "./router/index";

import "./assets/js/jquery.min.js"
import "./assets/bootstrap/js/bootstrap.min.js"
import "./assets/js/script.min.js"


// 新增的
window.$=window.jQuery=require('jquery');
require("./assets/js/jquery.min.js");
require("./assets/bootstrap/js/bootstrap.min.js");
require("./assets/js/script.min.js")



Vue.config.productionTip = false

new Vue({
  el: "#app",
  vuetify,
  router,
  render: h => h(App),
  components: {App}
}).$mount('#app');

