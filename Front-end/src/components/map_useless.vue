  <script>
  var googleMapsClient = require('@google/maps').createClient({
    key: 'AIzaSyDWqkSWcyfLuSqhWaVGVexdWmIQvDCQQAs'
  })

  // googleMapsClient.geocode({
  //   address: '1600 Amphitheatre Parkway, Mountain View, CA'
  // }, function (err, response) {
  //   if (!err) {
  //     console.log(response.json.results)
  //   }
  // })

  googleMapsClient.distanceMatrix({
    origins: 'San Francisco',
    destinations: 'Sacramento'
  }, function (err, response) {
    if (!err) {
      console.log(response.jsonp.results)
    }
  })
  </script>



  <template>
  <gmap-map 
    :center="center"
    :zoom="7"
    :style="{ width: '500px', height: '500px'}"
    >
    <gmap-marker 
      v-for="m in markers"
      :position="m.position"
      :clickable="true"
      :draggable="true"
      @click="center=m.position"
    ></gmap-marker>
  </gmap-map>
</template>

<script>
// New in 0.4.0
// import * as VueGoogleMaps from '../../node_modules/vue2-google-maps'
// var Vue = require('vue')
var VueGoogleMaps = require('vue2-google-maps')

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBMSi1KFmkp-dto-D_21QPPkDvfaeE7l0w'
    // libraries: 'directions'
  }
})

// var directionsDisplay = google.maps.DirectionsRenderer()
// console.log(directionsDisplay)

export default {
  props: {
    data1: String,
    data2: String
  },
  data () {
    return {
      center: {lat: 37.7749, lng: -122.4194},
      markers: [{
        position: {lat: 10.0, lng: 10.0}
      }, {
        position: {lat: 11.0, lng: 11.0}
      }]
    }
  }
}
</script>

