import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    navShown: false,
    breadcrumbs: [
      {
        text: '首页',
        disabled: false,
        href: '#/'
      },
      {
        text: '当前',
        disabled: false,
        href: ''
      }
    ]
  },
  mutations: {
    toggleNav (state) {
      state.navShown = !state.navShown
    },
    updateBreadcrumbs (state, breadcrumbs) {
      state.breadcrumbs = breadcrumbs
    }
  },
  actions: {
    toggleNavFun (context) {
      context.commit('toggleNav')
    },
    updateBreadcrumbsFun (context, breadcrumbs) {
      context.commit('updateBreadcrumbs', breadcrumbs)
    }
  }
})

export default store
