<template>
  <div class="state2">
    <maps></maps>
  </div>
</template>

<script>
import maps from './map'
import { Button, Select, Input } from 'element-ui'

// import axios from 'axios'
// import lodash from 'lodash'
var UIButton = Button
var UISelect = Select
var UIInput = Input

export default {
  components: {
    maps,
    UIButton,
    UISelect,
    UIInput
  },
  data () {
    return {
      src: 'SF',
      dest: 'Davis'
    }
  },
  watch: {
    dest: function () {
      if (this.src.length > 0 && this.dest.length > 0) {
        console.log('working')
        // this.findDist()
      }
    }
  },
  methods: {
    setSrc: function (ITEM) {
      this.$store.commit('SET_SRC', ITEM)
    }
  }
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
</style>
