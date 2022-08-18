import { api } from 'boot/axios'

export default function useApi () {
  const tokenKEY = 'YWRtaW46MDEwMjAzc2E='
  const urlBase = '/produtos/api/'

  const list = async () => {
    try {
      const { data } = await api.get(
        urlBase,
        { headers: { Authorization: `Basic ${tokenKEY}` } }
      )
      return data
    } catch (error) {
      throw new Error(error)
    }
  }

  const getById = async (id) => {
    try {
      const { data } = await api.get(
        urlBase + `${id}`,
        { headers: { Authorization: `Basic ${tokenKEY}` } }
      )
      return data
    } catch (error) {
      throw new Error(error)
    }
  }

  const post = async (form) => {
    try {
      const { data } = await api.post(
        urlBase,
        form,
        { headers: { Authorization: `Basic ${tokenKEY}` } }
      )
      return data
    } catch (error) {
      throw new Error(error)
    }
  }

  const put = async (form) => {
    try {
      const { data } = await api.put(
        urlBase + `${form.id}/`,
        form,
        { headers: { Authorization: `Basic ${tokenKEY}` } }
      )
      return data
    } catch (error) {
      throw new Error(error)
    }
  }

  const remove = async (id) => {
    try {
      const { data } = await api.delete(
        urlBase + `${id}`,
        { headers: { Authorization: `Basic ${tokenKEY}` } }
      )
      return data
    } catch (error) {
      throw new Error(error)
    }
  }

  return {
    list,
    post,
    put,
    remove,
    getById
  }
}
