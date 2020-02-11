import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/HelloWorld'
import FrontEnd from '@/components/FrontEnd'
import GETURL from '@/components/URLString'
import POST from '@/components/POST'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/msg/',
      name: 'FrontEnd',
      component: FrontEnd
    },
    {
      path: '/login/',
      name: 'GETURL',
      component: GETURL
    },
    {
      path: '/welcome/',
      name: 'POST',
      component: POST
    }
  ]
})
