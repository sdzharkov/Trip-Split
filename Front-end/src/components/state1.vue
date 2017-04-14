<template>
  <div class='state1'>
    <div class="inputs">
      <UIInput type='text' class='form-control' placeholder='Enter Year:' v-model='car_year'></UIInput>
      <UIInput type='text' class='form-control' placeholder='Enter Make:' v-model='car_make'></UIInput>
      <UIInput type='text' class='form-control' placeholder='Enter Model:' v-model='car_model'></UIInput>
    </div>
    <demo-grid
      :data="cars"
      :columns="gridColumns">
    </demo-grid>
  </div>
</template>

<script>
import axios from 'axios'
import lodash from 'lodash'
import demoGrid from './demo-grid'
var _ = lodash
import { Input } from 'element-ui'

var UIInput = Input

export default {
  name: 'state1',
  components: {
    demoGrid,
    UIInput
  },
  data () {
    return {
      car_year: '',
      car_make: '',
      car_model: '',
      cars: [],
      gridColumns: ['car_model', 'car_cylinder', 'car_drive', 'fuel']
    }
  },
  watch: {
    car_model: function () {
      if (this.car_year.length > 3 && this.car_make.length && this.car_model.length === 0) {
        this.lookupnewCar()
      }
      if (this.car_make.length || this.car_model.length) {
        this.lookupnewCar()
      } else {
        this.clearCar()
      }
    }
  },
  methods: {
    lookupnewCar: _.debounce(function () {
      var inst = this
      axios.get('http://127.0.0.1:8000/carAPI/cars/?car_make=' + this.car_make + '&car_year=' + this.car_year + '&car_model=' + this.car_model)
        .then(function (response) {
          inst.$set(inst, 'cars', response.data)
        })
        .catch(function (error) {
          if (error) {
            console.log(error)
          }
        })
    }, 500),
    clearCar: function () {
      this.$set(this, 'cars', [])
    }
  }
}
</script>

<style scoped>
.el-input {
  width: 25%;
}

.inputs{
  padding-bottom: 15px;
}

/*h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}*/
</style>
