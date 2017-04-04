<template>
  <div class="state3">
    <UIRow :span ="24" id="myRow">
        <UIColumn :span="10" :offset="1" class="input3" id="enterGas">
          <div>How much did you pay for a gallon of gas?</div>
          <UIInput type='text' placeholder="$3.00" v-model='gasPrice'></UIInput>
        </UIColumn>
        <UIColumn :span ="10" :offset="1" class="input3" id="enterPassenger">
          <div>How many passengers?</div>
          <UIInput type='text' placeholder='0 passengers' v-model='passengers'></UIInput>
        </UIColumn>
    </UIRow> 
  </div>
</template>

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
  data () {
    return {
      gasPrice: null,
      passengers: null
    }
  },
  watch: {
    gasPrice: function () {
      this.$store.commit('SET_GAS_PRICE', this.gasPrice)
      this.$store.dispatch('FETCH_FINAL_DATA')
    },
    passengers: function () {
      this.$store.commit('SET_PASSENGERS', this.passengers)
    }
  }
}
</script>

<style scoped>
  .state3{
    width: 100%;
    height: 100%;
  }
  #myRow{
    width: 100%;
    display: block;
  }

</style>
