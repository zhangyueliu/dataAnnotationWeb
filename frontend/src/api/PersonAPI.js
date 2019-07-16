import axios from '../assets/js/axios'

var staticMethods = {
  getAllData ({ commit, state }, id) { // 得到指定文章详情
    return axios.Get({
      url: 'get_data',
      params: {
        id: id
      },
      callback: (res) => {
        return res
      }
    })
  }
}

function PersonAPI () {
  return Object.freeze(Object.assign(
    {},
    staticMethods
  ))
}

Object.assign(PersonAPI, staticMethods)
export default PersonAPI
