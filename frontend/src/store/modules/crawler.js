export default {
  namespaced: true,
  mutations: {

    SET_LIST (state, payload) {
      state.list = 'hello'
      // console.log("hello mutations.")
      // console.log(state)
      console.log(payload)
    }

  },
  actions: {

    FETCH ({ commit, state }) {
      commit('SET_LIST', 'hello actions')
      console.log(state.list)
    },

    REMOVE ({ dispatch }, projectId) {
      dispatch('FETCH')
    }

  }
}
