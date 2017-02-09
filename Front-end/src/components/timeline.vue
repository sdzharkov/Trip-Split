<template>
<div class="hi">
	<ul class="timeline" id="timeline">
    <li class = "li" v-for="(entry,index) in values" v-bind:class="{ complete: bool[index] }">
      <div class="timestamp">
        <span class="author">{{ entry }}</span>
        <span class="date"> {{ date[index] }}<span>
      </div>
       <div class="status" v-on:click="changeCurView(index)">      
          <h4 v-if="index === 0"> {{ returnVehicle }} </h4>
          <h4 v-else-if="index === 1"> {{ returnTrip }} </h4>
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
      values: ['Select Car', 'Location', 'Gas', 'Split Trip'],
      date: ['TBD', 'tbd', 'TBF', 'DFD'],
      last: ['1', 'Destination', '3', '4'],
      bool: [false, false, false, false],
      curCar: 'Your Car',
      curDest: 'Destination'
    }
  },
  watch: {
    curCar: function () {
      if (this.curCar != 'Your Car'){
        this.checkList(0)
      }
    },
    curDest: function () {
      if (this.curDest != 'Destination'){
        this.checkList(1)
      }
    }
  },
  methods: {
    changeCurView: function (index) {
      this.$parent.changeView(index)
    },
    checkList: function (i) {
      if (this.bool[i] === true) {
        this.$set(this.bool, parseInt(i), false)
      } else {
        this.$set(this.bool, parseInt(i), true)
      }
    }
  },
  computed: {
    returnVehicle () {
      this.$set(this,'curCar',this.$store.getters.getCar)
      return this.$store.getters.getCar
    },
    returnTrip () {
      this.$set(this, 'curDest', this.$store.getters.getStartDest)
      return this.$store.getters.getStartDest
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
.li
  transition: all 200ms ease-in

.timestamp
  margin-bottom: 20px
  padding: 0px 40px
  display: flex
  flex-direction: column
  align-items: center
  font-weight: 100
.status
  padding: 0px 40px
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