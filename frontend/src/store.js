// Pinia store
import { createStore } from 'vuex';

const store = createStore({
  state: {
    isAuthenticated: !!localStorage.getItem('access_token'),
  },
  mutations: {
    setAuthenticated(state, status) {
      state.isAuthenticated = status;
    }
  },
  actions: {
    login({ commit }) {
      commit('setAuthenticated', true);
    },
    logout({ commit }) {
      commit('setAuthenticated', false);
    }
  }
});

export default store;
