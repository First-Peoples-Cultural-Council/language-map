import { getCookie } from '@/plugins/utils.js'

export const state = () => ({
  user: null,
  isLoggedIn: false
})

export const mutations = {
  setUser(state, user) {
    state.user = user
  },

  setLoggedIn(state, loggedIn) {
    state.isLoggedIn = loggedIn
  }
}

export const actions = {
  async saveLocation({ commit }, data) {
    const headers = {
      headers: {
        'X-CSRFToken': getCookie('csrftoken')
      }
    }

    try {
      const result = await this.$axios.post(`/api/favourite/`, data, headers)
      return result
    } catch (e) {
      return { error: e, status: 'failed' }
    }
  }
}
