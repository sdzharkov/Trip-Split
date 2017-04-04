import Vue from 'vue'
import Vuex from 'vuex'
import * as getters from './getters'
import * as actions from './actions'
import * as mutations from './mutations'

Vue.use(Vuex)

const state = {
  vehicle: '',
  route: null,
  src: '',
  gasPrice: null,
  passengers: 1,
  finalCalc: null
}

export default new Vuex.Store({
  state,
  mutations,
  getters,
  actions
})
