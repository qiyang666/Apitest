import Vue from 'vue'
import Vuex from 'vuex'

import crawler from './modules/crawler'

Vue.use(Vuex)

export function createStore () {
  return new Vuex.Store({
    modules: {
      crawler: {
        state: {
          list: '',
          project: {},
          keywords: '',
          pageIndex: 1
        },
        ...crawler
      }

    }
  })
}
