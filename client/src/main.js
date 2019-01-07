import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import VueToastr2 from "vue-toastr-2";
import paper from "paper";
import VTooltip from "v-tooltip";
import Vue2TouchEvents from 'vue2-touch-events'

import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "vue-toastr-2/dist/vue-toastr-2.min.css";

Vue.config.productionTip = false;

paper.install(window);

window.toastr = require("toastr");
Vue.use(VueToastr2);
Vue.use(VTooltip);
Vue.use(Vue2TouchEvents);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
