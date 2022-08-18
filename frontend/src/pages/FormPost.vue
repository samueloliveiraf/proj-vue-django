<template>
    <q-page padding>
      <q-card class="my-card">
        <q-card-section>
            <q-form
            @submit="onSubmit"
            class="row"
            >
            <q-input
                filled
                v-model="form.nome"
                label="Nome *"
                class="col-lg-6 col-xs-12"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Campo obrigatorio']"
            />
            <div class="col-12 q-gutter-sm">
                <q-btn class="float-right" text-color="primary" label="Cancelar" :to="{ name: 'home' }" />
                <q-btn class="float-right" label="Salvar" color="primary" type="submit" />
            </div>
            </q-form>
        </q-card-section>
      </q-card>
    </q-page>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import useApi from 'src/composables/UseApi'
import { useQuasar } from 'quasar'
import { useRouter, useRoute } from 'vue-router'

export default defineComponent({
  name: 'FormPost',
  setup () {
    const $q = useQuasar()
    const { post, getById, put } = useApi()
    const router = useRouter()
    const route = useRoute()
    const form = ref({
      nome: ''
    })

    onMounted(async () => {
      if (route.params.id) {
        getPost(route.params.id)
      }
    })

    const getPost = async (id) => {
      try {
        const response = await getById(route.params.id)
        form.value = response
      } catch (error) {
        console.error(error)
      }
    }

    const onSubmit = async () => {
      try {
        if (form.value.id) {
          await put(form.value)
        } else {
          await post(form.value)
        }
        $q.notify({ message: 'Salvo com sucesso!', icon: 'check', color: 'positive' })
        router.push({ name: 'home' })
      } catch (error) {
        alert(error)
      }
    }

    return {
      form,
      onSubmit
    }
  }
})
</script>
