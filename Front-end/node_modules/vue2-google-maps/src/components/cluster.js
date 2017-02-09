/* vim: set softtabstop=2 shiftwidth=2 expandtab : */

/**
  * @class Cluster
  * @prop $clusterObject -- Exposes the marker clusterer to
        descendent Marker classes. Override this if you area
        extending the class
**/

import _ from 'lodash';
import propsBinder from '../utils/propsBinder.js'
import MapElementMixin from './mapElementMixin';
import getPropsValuesMixin from '../utils/getPropsValuesMixin.js'
import MarkerClusterer from 'marker-clusterer-plus'

const props = {
  maxZoom: {
    type: Number,
    twoWay: false
  },
  calculator: {
    type: Function,
    twoWay: false
  },
  gridSize: {
    type: Number,
    twoWay: false
  },
  styles: {
    type: Array,
    twoWay: false
  }
};

export default {
  mixins: [MapElementMixin, getPropsValuesMixin],
  props: props,

  render(h) {
    // <div><slot></slot></div>
    return h(
      'div',
      this.$slots.default
    )
  },

  deferredReady () {
    const options = _.clone(this.getPropsValues());

    if (typeof MarkerClusterer === 'undefined') {
      console.error("MarkerClusterer is not installed! require() it or include it from https://cdnjs.cloudflare.com/ajax/libs/js-marker-clusterer/1.0.0/markerclusterer.js")
      throw new Error("MarkerClusterer is not installed! require() it or include it from https://cdnjs.cloudflare.com/ajax/libs/js-marker-clusterer/1.0.0/markerclusterer.js")
    }

    this.$clusterObject = new MarkerClusterer(this.$map, [], options);

    propsBinder(this, this.$clusterObject, props, {
      afterModelChanged: (a, v) => {
        const oldMarkers = this.$clusterObject.getMarkers();
        this.$clusterObject.clearMarkers();
        this.$clusterObject.addMarkers(oldMarkers);
      }
    });
  },

  detached() {
    this.$clusterObject.clearMarkers();
  },
}
