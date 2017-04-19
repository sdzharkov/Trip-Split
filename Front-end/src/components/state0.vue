<template>
  <div class="state0">
    <h1>Need your trip split?</h1> 
    <h3>Click the arrow on the right to begin</h3>
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
  }
}
</script>

<style lang="scss" scoped>
@font-face {
  font-family: Bernier;
  src: url(../assets/fonts/BERNIERRegular-Regular.otf);
}

.state0{
  font-family: Bernier;
  h1 {
    font-size: 60px;
  }
  h3 {
    font-size: 30px;
  }
}

</style>
