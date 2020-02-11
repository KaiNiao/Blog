<template>
  <span>{{ msg }}</span>
</template>

<script>
export default {
  name: 'POST',
  data () {
    return {
      msg: 'POST'
    }
  },
  created () {
    var data = {name: 'Honor'}
    var that = this
    const path = 'http://127.0.0.1:8023/welcome/'
    that.$axios
      .post(path,
        that.$qs.stringify(data)
      )
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
