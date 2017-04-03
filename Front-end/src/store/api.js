import Vue from 'Vue'
Vue.use(require('vue-resource'))

export default {
  get (url) {
    return Vue.http.get(url)
      .then((response) => Promise.resolve(response.body))
      .catch((error) => Promise.reject(error))
  }
  // post (url, request) {
  //   return Vue.http.post(url, request)
  //     .then((response) => Promise.resolve(response))
  //     .catch((error) => Promise.reject(error))
  // },
  // patch (url, request) {
  //   return Vue.http.patch(url, request)
  //     .then((response) => Promise.resolve(response))
  //     .catch((error) => Promise.reject(error))
  // },
  // delete (url, request) {
  //   return Vue.http.delete(url, request)
  //     .then((response) => Promise.resolve(response))
  //     .catch((error) => Promise.reject(error))
  // }
}
