import api from './api.js'

export const FETCH_GAS_DATA = ({ commit, state }) => {
  return api.get('http://localhost:8000/carAPI/gas')
    .then((response) => commit('SET_GAS', response))
}

export const FETCH_FINAL_DATA = ({ commit, state }) => {
  if (state.route === null || state.vehicle === '' || state.gasPrice === null) {
    return -1
  }
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
