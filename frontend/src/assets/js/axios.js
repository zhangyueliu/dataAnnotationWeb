import axios from 'axios'
import getUrl from './getPath'

export default {
  Get: (config) => {
    return axios({
      method: 'get',
      url: getUrl(config.url),
      params: config.params
    }).then((res) => {
      stateDetection(res)
      return config.callback && config.callback(res)
    })
  },
  Post: (config) => {
    return axios({
      method: 'post',
      url: getUrl(config.url),
      data: config.params.data,
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      }
    }).then((res) => {
      stateDetection(res)
      return config.callback && config.callback(res)
    })
  }
}

// 状态检测
let stateDetection = (data, callback) => {
    let status = data.status_code
    switch (status) {
        case 102:
            break
        case 103:
            alert(data.content)
            break
        case 404:
            window.location.href = data.url
            break
    }
}

function getCookie (name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
