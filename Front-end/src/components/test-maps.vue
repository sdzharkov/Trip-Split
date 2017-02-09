<template>
<!--   <div id="map"></div>
    <div id="right-panel">
    <p>Total Distance: <span id="total"></span></p>
  </div> -->
</template>

<script>
// import google from '@google'

// function initMap () {
//   var map = new google.maps.Map(document.getElementById('map'), {
//     zoom: 4,
//     center: {lat: -24.345, lng: 134.46}  // Australia.
//   })

//   var directionsService = new google.maps.DirectionsService
//   var directionsDisplay = new google.maps.DirectionsRenderer({
//     draggable: true,
//     map: map,
//     panel: document.getElementById('right-panel')
//   })

//   directionsDisplay.addListener('directions_changed', function () {
//     computeTotalDistance(directionsDisplay.getDirections())
//   })

//   displayRoute('Perth, WA', 'Sydney, NSW', directionsService,
//       directionsDisplay)
// }

// function displayRoute (origin, destination, service, display) {
//   service.route({
//     origin: origin,
//     destination: destination,
//     waypoints: [{location: 'Adelaide, SA'}, {location: 'Broken Hill, NSW'}],
//     travelMode: 'DRIVING',
//     avoidTolls: true
//   }, function (response, status) {
//     if (status === 'OK') {
//       display.setDirections(response)
//     } else {
//       // alert('Could not display directions due to: ' + status);
//     }
//   })
// }

// function computeTotalDistance (result) {
//   var total = 0
//   var myroute = result.routes[0]
//   for (var i = 0; i < myroute.legs.length; i++) {
//     total += myroute.legs[i].distance.value
//   }
//   total = total / 1000
//   document.getElementById('total').innerHTML = total + ' km'
// }
// var googleMapsClient = require('@google/maps').createClient({
//   key: 'AIzaSyBMSi1KFmkp-dto-D_21QPPkDvfaeE7l0w'
// });

export default {
  props: {
    data1: String,
    data2: String
  }
  // data () {
  // },
}
</script>

<!-- Add 'scoped' attribute to limit CSS to this component only -->
<style scoped>
/*h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}*/
#right-panel {
  font-family: 'Roboto','sans-serif';
  line-height: 30px;
  padding-left: 10px;
}

#right-panel select, #right-panel input {
  font-size: 15px;
}

#right-panel select {
  width: 100%;
}

#right-panel i {
  font-size: 12px;
}
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}
#map {
  height: 100%;
  float: left;
  width: 63%;
  height: 100%;
}
#right-panel {
  float: right;
  width: 34%;
  height: 100%;
}
.panel {
  height: 100%;
  overflow: auto;
}
</style>
