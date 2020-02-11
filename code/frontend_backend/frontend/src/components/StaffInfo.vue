<template>
  <div>
    <ul>
<!--      <li v-for="m in msg">-->
<!--        {{ m }}-->
<!--      </li>-->
    </ul>
  </div>
</template>

<script>
export default {
  name: 'StaffInfo',
  data () {
    return {
      msg: []
    }
  },
  mounted () {
    var that = this
    const path = 'http://127.0.0.1:5000/getStaffInfomation/'
    that.$axios
      .get(path, {
        params: {
          name: '王荣祥'
        }
      })
      .then(function (response) {
        // 接口返回列表
        const info = response.data.back_msg
        console.log(response.data)
        console.log(response.data)
        that.msg = info
      })
  }
}
</script>

<style>

</style>
