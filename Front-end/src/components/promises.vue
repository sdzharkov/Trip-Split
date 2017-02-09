        // var promise = new Promise(function (resolve, reject) {
        //   var route = directionsService.route({
        //     origin: origin1,
        //     destination: destination1,
        //     waypoints: waypts,
        //     optimizeWaypoints: true,
        //     travelMode: 'DRIVING'
        //   }, function (response, status) {
        //     if (status === 'OK') {
        //       directionsDisplay.setDirections(response)
        //       var route = response.routes[0]
        //       var summaryPanel = document.getElementById('directions-panel')
        //       summaryPanel.innerHTML = ''
        //       // For each route, display summary information.
        //       for (var i = 0; i < route.legs.length; i++) {
        //         var routeSegment = i + 1
        //         summaryPanel.innerHTML += '<b>Route Segment: ' + routeSegment + '</b><br>'
        //         summaryPanel.innerHTML += route.legs[i].start_address + ' to '
        //         summaryPanel.innerHTML += route.legs[i].end_address + '<br>'
        //         summaryPanel.innerHTML += route.legs[i].distance.text + '<br><br>'
        //       }
        //       return route
        //     } else {
        //       window.alert('Directions request failed due to ' + status)
        //       return -1
        //     }
        //   })
        //   if (route !== -1) {
        //     resolve(route)
        //   } else {
        //     reject(Error('fuck'))
        //   }
        // })

        // promise.then(function (result) {
        //   console.log('result')
        //   console.log(result)
        // }, function (err) {
        //   console.log(err)
        // })

        // var route = directionsService.route({
        //   origin: this.data1,
        //   destination: this.data2,
        //   waypoints: waypts,
        //   optimizeWaypoints: true,
        //   travelMode: 'DRIVING'
        // }, function (response, status) {
        //   if (status === 'OK') {
        //     directionsDisplay.setDirections(response)
        //     var route = response.routes[0]
        //     var summaryPanel = document.getElementById('directions-panel')
        //     summaryPanel.innerHTML = ''
        //     // For each route, display summary information.
        //     for (var i = 0; i < route.legs.length; i++) {
        //       var routeSegment = i + 1
        //       summaryPanel.innerHTML += '<b>Route Segment: ' + routeSegment + '</b><br>'
        //       summaryPanel.innerHTML += route.legs[i].start_address + ' to '
        //       summaryPanel.innerHTML += route.legs[i].end_address + '<br>'
        //       summaryPanel.innerHTML += route.legs[i].distance.text + '<br><br>'
        //     }
        //     return route
        //   } else {
        //     window.alert('Directions request failed due to ' + status)
        //     return -1
        //   }
        // })

        // getRoute()

        // function getIt (route) {
        //   this.setRoute(route)
        // }

        // async function getRoute () {

                try {
          directionsService.route(input, function (response, status) {
            if (status === 'OK') {
              directionsDisplay.setDirections(response)
              var route = response.routes[0]
              var summaryPanel = document.getElementById('directions-panel')
              summaryPanel.innerHTML = ''
              // For each route, display summary information.
              for (var i = 0; i < route.legs.length; i++) {
                var routeSegment = i + 1
                summaryPanel.innerHTML += '<b>Route Segment: ' + routeSegment + '</b><br>'
                summaryPanel.innerHTML += route.legs[i].start_address + ' to '
                summaryPanel.innerHTML += route.legs[i].end_address + '<br>'
                summaryPanel.innerHTML += route.legs[i].distance.text + '<br><br>'
              }
              // getIt(response)
              return route
            } else {
              window.alert('Directions request failed due to ' + status)
              return -1
            }
          }).then(function (response) {
            console.log(response)
          })
          // console.log(await route)
        } catch (err) {
          console.log(err)
        }