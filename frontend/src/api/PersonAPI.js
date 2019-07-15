import axios from "../assets/js/axios"

var staticMethods = {
  getArticlesSpecific({ commit, state }, id) { //得到指定文章详情
    axios.Get({
      url: 'get_article_specific',
      params: {
        id: id
      },
      callback: (res) => {
        return res.data;
      }
    })
  }
}

function PersonAPI(){
  return Object.freeze(Object.assign(
    {},
    staticMethods
  ))
}

Object.assign(PersonAPI, staticMethods);
export default PersonAPI

