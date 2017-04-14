<template>
  <div id="map_section">
    <UIRow :gutter="20">
      <UIColumn :span="10">
        <div class= "ui_inputs">
          <UIInput placeholder="Please input" class='form-control' v-model='data1'></UIInput>
          <UIInput placeholder="Enter destinations in between:" v-model='mid' @keyup.enter.native='submit_mid'>
                <UIButton slot="append" icon="search" v-on:click='submit_mid'></UIButton>
          </UIInput>
          </div>
          <UIColumn>
            <div id="mid-list" v-for="(city,index) in locations">
              <div class="legCity">{{ city }}</div>
              <i class="fa fa-minus-square" aria-hidden="true" @click="remove_mid(index)"></i>
            </div>      
          </UIColumn>   
          <UIInput placeholder='End Destination:' class='form-control' v-model='data2'>
            <UIButton slot="append" icon="search" v-on:click='loadDirections'></UIButton>
          </UIInput>
          <input type="submit" v-on:click='loadDirections' id="submit">
          <div id="directions-panel"></div>
      </UIColumn>
      <UIColumn :span="10">
        <div id="map"></div>
      </UIColumn>
    </UIRow>
  </div>
</template>

<script>
  import loadGoogleMapsAPI from 'load-google-maps-api'
  import { Row, Col, Input, Button } from 'element-ui'

  var UIRow = Row
  var UIColumn = Col
  var UIInput = Input
  var UIButton = Button
  export default {
    components: {
      UIRow,
      UIColumn,
      UIInput,
      UIButton
    },
    data () {
      return {
        data1: '',
        data2: '',
        mid: null,
        locations: [],
        route: null,
        directionsS: null,
        directionsD: null
      }
    },
    mounted: function () {
      loadGoogleMapsAPI({key: 'AIzaSyDWqkSWcyfLuSqhWaVGVexdWmIQvDCQQAs'}).then((googleMaps) => {
        var directionsService = new googleMaps.DirectionsService()
        var directionsDisplay = new googleMaps.DirectionsRenderer()
        this.$set(this, 'directionsS', directionsService)
        this.$set(this, 'directionsD', directionsDisplay)
        // this.$store.dispatch('FETCH_GAS_DATA')

        var map = new googleMaps.Map(document.getElementById('map'), {
          zoom: 6,
          center: {lat: 37.7749, lng: -122.4194}
        })
        this.directionsD.setMap(map)
      }).catch((err) => {
        console.error(err)
      })
    },
    methods: {
      submit_mid: function () {
        this.locations.push(this.mid)
        this.mid = ''
      },
      remove_mid: function (index) {
        this.locations.splice(index, 1)
      },
      loadDirections: function () {
        var storageThis = this
        this.calculateAndDisplayRoute(this.directionsS, this.directionsD, function (result) {
          storageThis.$store.commit('SET_ROUTE', result)
        })
      },
      calculateAndDisplayRoute: async function (directionsService, directionsDisplay, callback) {
        var waypts = []
        for (var i = 0; i < this.locations.length; i++) {
          waypts.push({
            location: this.locations[i],
            stopover: true
          })
        }
        var origin1 = this.data1
        var destination1 = this.data2

        var input = {
          origin: origin1,
          destination: destination1,
          waypoints: waypts,
          optimizeWaypoints: true,
          travelMode: 'DRIVING'
        }

        directionsService.route(input, function (response, status) {
          if (status === 'OK') {
            directionsDisplay.setDirections(response)
            var route = response.routes[0]
            callback(route)
            var summaryPanel = document.getElementById('directions-panel')
            summaryPanel.innerHTML = ''
            for (var i = 0; i < route.legs.length; i++) {
              var routeSegment = i + 1
              summaryPanel.innerHTML += '<b>Route Segment: ' + routeSegment + '</b><br>'
              summaryPanel.innerHTML += route.legs[i].start_address + ' to '
              summaryPanel.innerHTML += route.legs[i].end_address + '<br>'
              summaryPanel.innerHTML += route.legs[i].distance.text + '<br><br>'
            }
            // return route
          } else {
            window.alert('Directions request failed due to ' + status)
            return -1
          }
        })
      }
    }
  }
</script>

<style lang="scss">
  #mid-list {
    display: flex;
    padding: 5px;
    .fa {
      padding-left: 10px;
    }
  }

  .leg-city {
    width: 80%;
    display: block;
    padding-right: 15px;
  }

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
    height: 400px;
    float: left;
    width: 400px;
  }
  #right-panel {
    margin: 20px;
    border-width: 2px;
    width: 25%;
    height: 400px;
    float: left;
    text-align: left;
    padding-top: 0;
  }
  #directions-panel {
    margin-top: 10px;
    padding: 10px;
  }
  #map_section {
    display: inline-block;
    width: 80%;
  }
</style>

