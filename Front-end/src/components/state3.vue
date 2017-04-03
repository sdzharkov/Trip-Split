<template>
  <div class="state3">
    <UIRow :span ="20" id="myRow">
        <UIColumn :span="10" :offset="1" class="gasEnter">
          <div>How much did you pay for a gallon of gas?</div>
          <UIInput type='text' v-model='gasPrice'></UIInput>
        </UIColumn>
        <UIColumn :span ="10" :offset="1" class="insert">
          <div>How many passengers?</div>
          <UIInput type='text' placeholder='0 passengers' v-model='passengers'></UIInput>
        </UIColumn>
    </UIRow> 
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
  data () {
    return {
      gasPrice: 2.75,
      passengers: null
    }
  },
  watch: {
    gasPrice: function () {
      this.commit('SET_GAS', this.gasPrice)
    },
    passengers: function () {
      this.commit('SET_PASSENGERS', this.passengers)
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
    display: inline-flex;
  }

</style>
