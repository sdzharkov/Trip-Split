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
// import { stateGetters } from 'vuex'
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
  // data () {
  //   return {
  //     final: this.getFinalValue
  //   }
  // },
  computed: {
    stateGetter () {
      return this.$store.getters.getFinalValue.toFixed(2)
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
