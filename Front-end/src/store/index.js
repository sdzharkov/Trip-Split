import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'
// import lodash from 'lodash'
import api from './api.js'
// var _ = lodash

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    vehicle: '',
    route: null,
    src: '',
    gasPrice: 3.0,
    passengers: 1,
    finalCalc: null
  },
  actions: {
    FETCH_GAS_DATA: ({ commit, state }) => {
      return api.get('http://localhost:8000/carAPI/gas')
        .then((response) => commit('SET_GAS', response))
    },
    FETCH_FINAL_DATA: ({ commit, state }) => {
      var distance = 0
      for (var i = 0; i < state.route.legs.length; i++) {
        distance += parseFloat(state.route.legs[i].distance.text.split(' ')[0])
      }

      var final = (distance * (1 / state.vehicle.car_comb_mpg) * state.gasPrice) / state.passengers

      commit('SET_FINAL_VAL', final)
    }

    // // ensure data for rendering given list type
    // FETCH_LIST_DATA: ({ commit, dispatch, state }, { type }) => {
    //   commit('SET_ACTIVE_TYPE', { type })
    //   return fetchIdsByType(type)
    //     .then(ids => commit('SET_LIST', { type, ids }))
    //     .then(() => dispatch('ENSURE_ACTIVE_ITEMS'))
    // },

    // // ensure all active items are fetched
    // ENSURE_ACTIVE_ITEMS: ({ dispatch, getters }) => {
    //   return dispatch('FETCH_ITEMS', {
    //     ids: getters.activeIds
    //   })
    // },

    // FETCH_ITEMS: ({ commit, state }, { ids }) => {
    //   // only fetch items that we don't already have.
    //   ids = ids.filter(id => !state.items[id])
    //   if (ids.length) {
    //     return fetchItems(ids).then(items => commit('SET_ITEMS', { items }))
    //   } else {
    //     return Promise.resolve()
    //   }
    // },

    // FETCH_USER: ({ commit, state }, { id }) => {
    //   return state.users[id]
    //     ? Promise.resolve(state.users[id])
    //     : fetchUser(id).then(user => commit('SET_USER', { user }))
    // }
  },
  mutations: {
    SET_GAS: (state, gas) => {
      state.gas = gas
    },
    SET_VEHICLE: (state, vehicle) => {
      state.vehicle = vehicle
      // Vue.set(state, vehicle, vehicle)
    },
    SET_ROUTE: (state, route) => {
      state.route = route
    },
    SET_SRC: (state, src) => {
      state.src = src
    },
    SET_GAS_PRICE: (state, gasPrice) => {
      state.gasPrice = gasPrice
    },
    SET_PASSENGERS: (state, passengers) => {
      state.passengers = passengers
    },
    SET_FINAL_VAL: (state, finalCalc) => {
      state.finalCalc = finalCalc
    }
  },

  getters: {
    getCar: state => {
      if (state.vehicle === '') {
        return 'Your Car'
      }
      var s = ''
      s += state.vehicle['car_make']
      s += ' '
      s += state.vehicle['car_model']
      return s
    },
    getRoute: state => {
      return state.route
    },
    getStartDest: state => {
      if (state.route === null) {
        return 'Destination'
      } else {
        return state.route.legs[0].start_address
      }
    },
    getFinalValue: state => {
      return state.finalCalc
    },
    getPassengers: state => {
      return state.passengers
    }
  }
})

export default store
