<template>
  <div class="state4">
    <h1> Your trip has been Split!</h1>
    <h2 v-if="passengerGetter == 1"> ${{ stateGetter }} for 1 passenger</h2>
    <h2 v-else> ${{ stateGetter }} for {{ passengerGetter }} passengers</h2>
  </div>
</template>
<!-- Add 'scoped' attribute to limit CSS to this component only -->

<script>
import { Row, Col, Input, Button } from 'element-ui'
var UIRow = Row
var UIColumn = Col
var UIInput = Input
var UIButton = Button
export default{
  components: {
    UIRow,
    UIColumn,
    UIInput,
    UIButton
  },
  computed: {
    stateGetter () {
      var x = this.$store.getters.getFinalValue
      if (x !== null) {
        return this.$store.getters.getFinalValue.toFixed(2)
      }
      return null
    },
    passengerGetter () {
      return this.$store.getters.getPassengers
    }
  },
  mounted () {
    this.$store.dispatch('FETCH_FINAL_DATA')
  }
}
</script>

<style scoped>

</style>
