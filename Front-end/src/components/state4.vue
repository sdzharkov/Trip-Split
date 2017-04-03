<template>
  <div class="state4">
    <h1> Your trip has been Split!</h1>
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
      final: ''
    }
  }
}
</script>

<style scoped>

</style>
