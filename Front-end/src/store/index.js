import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'
// import lodash from 'lodash'
import api from '../../api/api.js'
// var _ = lodash

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    vehicle: '',
    route: null,
    src: '',
    avgGas: null,
    lists: {
      passengers: []
    }
    // activeType: null,
    // itemsPerPage: 20,
    // items: {/* [id: number]: Item */},
    // users: { [id: string]: User },
    // lists: {
    //   top: [/* number */],
    //   new: [],
    //   show: [],
    //   ask: [],
    //   job: []
    // }
  },

    //   lookupnewCar: _.debounce(function () {
    //   var inst = this
    //   axios.get('http://localhost:8000/carAPI/cars/?car_make=' + this.car_make + '&car_year=' + this.car_year + '&car_model=' + this.car_model)
    //     .then(function (response) {
    //       console.log(response.data)
    //       inst.$set(inst, 'cars', response.data)
    //     })
    //     .catch(function (error) {
    //       if (error) {
    //         console.log(error)
    //       }
    //     })
    // }, 500)
        // .then((response) => commit('SET_GAS', response))
  actions: {
    // FETCH_GAS_DATA: ({ commit }) => {
    //   _.debounce(function () {
    //     axios.get('http://localhost:8000/carAPI/gas')
    //       .then(function (response) {
    //         console.log('response')
    //         commit('SET_GAS', response)
    //       })
    //       .catch(function (error) {
    //         if (error) {
    //           console.log(error)
    //         }
    //       })
    //   }, 500)
    // }

    FETCH_GAS_DATA: ({ commit }) => {
      return api.get('http://localhost:8000/carAPI/gas')
        .then((response) => commit('SET_GAS', response))
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
    SET_AVG_GAS: (state, avgGas) => {
      state.avg_gas = avgGas
    },
    SET_PASSENGERS: (state, { passengers }) => {
      passengers.forEach(passenger => {
        if (passenger) {
          Vue.set(state.passengers, passenger)
        }
      })
    }
    // SET_ACTIVE_TYPE: (state, { type }) => {
    //   state.activeType = type
    // },

    // SET_LIST: (state, { type, ids }) => {
    //   state.lists[type] = ids
    // },

    // SET_ITEMS: (state, { items }) => {
    //   items.forEach(item => {
    //     if (item) {
    //       Vue.set(state.items, item.id, item)
    //     }
    //   })
    // },

    // SET_USER: (state, { user }) => {
    //   Vue.set(state.users, user.id, user)
    // }
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
        var to = state.route.legs[0].start_address
        return to
      }
    }
    // ids of the items that should be currently displayed based on
    // current list type and current pagination
    // activeIds (state) {
    //   const { activeType, itemsPerPage, lists } = state
    //   const page = Number(state.route.params.page) || 1
    //   if (activeType) {
    //     const start = (page - 1) * itemsPerPage
    //     const end = page * itemsPerPage
    //     return lists[activeType].slice(start, end)
    //   } else {
    //     return []
    //   }
    // },

    // // items that should be currently displayed.
    // // this Array may not be fully fetched.
    // activeItems (state, getters) {
    //   return getters.activeIds.map(id => state.items[id]).filter(_ => _)
    // }
  }
})

export default store
