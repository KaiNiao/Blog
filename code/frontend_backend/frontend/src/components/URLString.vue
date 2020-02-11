<template>
<!--  <input v-model="getName">-->
  <span>{{ msg }}</span>
</template>

<script>
export default {
  name: 'GETURL',
  data () {
    return {
      msg: 'respp'
      // getName: '姓名'
    }
  },
  // created VS mounted
  created () {
    var that = this
    // var getName = that.getName
    const path = 'http://127.0.0.1:8023/login/'
    // 发起查询字符串GET请求
    that.$axios
      // .get(path + getName, {   // 默认 / 分隔，不建议使用
      .get(path, {
        params: {
          // name: getName
          name: 'King'
        }
      })
      .then(function (response) {
        const msg = response.data.msg
        console.log(response.data)
        that.msg = msg
      })
  }
}
</script>

<style>
</style>
