<template>
  <div class="state2">
    <maps></maps>
  </div>
</template>

<script>
import maps from './map'
import { Button, Select, Input } from 'element-ui'

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
  methods: {
    setSrc: function (ITEM) {
      this.$store.commit('SET_SRC', ITEM)
    }
  }
}
</script>

<style scoped>

</style>
