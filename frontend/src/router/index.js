import Vue from 'vue';
import Router from 'vue-router'
import Layout from '../components/Layout.vue';
import PredictionPage from '../page/PredictionPage.vue';
import TimePage from '../page/TimePage.vue';
import SpatialPage from '../page/SpatialPage.vue';




Vue.use(Router);

export default new Router({
    mode: "history",
    //base: process.env.BASE_URL,
    routes: [
        {
            path: "/",
            component: Layout,

            children: [
                {
                    path: "",
                    name: "Prediction",
                    component: PredictionPage
                },
                {
                    path: "TimePage",
                    name: "TimePage",
                    component: TimePage
                },
                {
                    path: "SpatialPage",
                    name: "SpatialPage",
                    component: SpatialPage
                }
            ]
        }
    ]
});



