<template>
  <div class="state3">
    <UIRow :span ="20" id="myRow">
        <UIColumn :span="10" :offset="1" class="gasEnter">
          <div>Enter how much you paid for gas</div>
          <UIInput type='text' placeholder='amount paid for a tank of gas:' v-model='gasPrice'></UIInput>
        </UIColumn>
        <UIColumn :span ="10" :offset="1" class="insert">
          <div>Number of Passengers</div>
          <UIInput type='text' placeholder='Number of passengers:' v-model='passengers'></UIInput>
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
      gasPrice: '',
      passengers: null
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
