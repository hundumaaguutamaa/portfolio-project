import axios from 'axios'
// http://127.0.0.1:8000/

const getAPI = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    timeout: 1000,

})

export { getAPI}