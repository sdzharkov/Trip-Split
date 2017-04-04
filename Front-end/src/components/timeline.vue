<template>
<div class="hi">
	<ul class="timeline" id="timeline">
    <li class = "li" v-for="(entry,index) in values" v-bind:class="{ complete: bool[index] }">
      <div class="timestamp">
        <span class="author">{{ entry }}</span>
      </div>
       <div class="status" v-on:click="changeCurView(index)">      
        <h4 v-if="index === 0"> {{ returnVehicle }} </h4>
        <h4 v-else-if="index === 1"> {{ returnTrip }} </h4>
        <h4 v-else-if="index === 2"> {{ returnGas }} </h4>
        <h4 v-else> {{ last[index] }} </h4>
      </div>
    </li>
	</ul>     
 </div> 
</template>

<script>
export default {
  data () {
    return {
      values: ['Car', 'Location', 'Gas', 'Trip'],
      last: ['1', 'Destination', '3', 'Split'],
      bool: [false, false, false, false],
      curCar: 'Your Car',
      curDest: 'Destination'
    }
  },
  methods: {
    // changeCurView: function (index) {
    //   this.$parent.changeView(index)
    // },
    checkList: function (i, j) {
      this.$set(this.bool, parseInt(i), j)
    }
  },
  computed: {
    returnVehicle () {
      var x = this.$store.getters.getCar
      if (x != null){
        this.checkList(0, true)
        return x
      }
      return 'Your Car'
    },
    returnTrip () {
      var x = this.$store.getters.getEndDest
      if (x != null){
        this.checkList(1, true)
        return x.split(",")[0]
      }
      return 'Destination'
    },
    returnGas () {
      var x = this.$store.getters.getGasPrice
      if (x != null){
        this.checkList(2, true)
        return "$" + x
      }
      else{
        return "$"
      }
    }
  }
}
</script>

<style lang='sass'>
.timeline
  list-style-type: none
  display: flex
  align-items: center
  justify-content: center
  padding-left: 0px;
.li
  transition: all 200ms ease-in
  width: 18%

.timestamp
  margin-bottom: 20px
  padding: 0px 40px
  display: flex
  flex-direction: column
  align-items: center
  font-weight: 100
.status
  display: flex
  justify-content: center
  border-top: 2px solid #D6DCE0
  position: relative
  transition: all 200ms ease-in  
  h4
    font-weight: 600
  &:before
    content: ''
    width: 25px
    height: 25px
    background-color: white
    border-radius: 25px
    border: 1px solid #ddd
    position: absolute
    top: -15px
    left: 42%
    transition: all 200ms ease-in 
.li.complete
  .status
    border-top: 2px solid #66DC71
    &:before
      background-color: #66DC71
      border: none
      transition: all 200ms ease-in 
    h4
      color: #66DC71


@media (min-device-width: 320px) and (max-device-width: 700px)
  .timeline
    list-style-type: none
    display: block
  .li
    transition: all 200ms ease-in
    display: flex
    width: inherit
  .timestamp
    width: 100px
  .status
    &:before
      left: -8%
      top: 30%
      transition: all 200ms ease-in 
</style>