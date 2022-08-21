<template>
    <q-page padding>
      <q-card class="my-card">
        <q-card-section>
            <q-form
            @submit="onSubmit"
            class="row"
            >
            <div class="col-12 q-gutter-sm">
              <q-input
                filled
                v-model="form.nome"
                label="Nome *"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Campo obrigatorio']"
              />
              <q-input
                filled
                type="number"
                v-model="form.quantidade"
                label="Quantidade *"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Campo obrigatorio']"
              />
              <q-input
                filled
                type="number"
                v-model="form.preco"
                label="Preço *"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Campo obrigatorio']"
              />
            </div>
            <div class="col-12 q-gutter-sm">
              <q-btn push class="bg-cyan-8 float-right" dense size="md" text-color="white" icon="cancel" :to="{ name: 'produtos' }" />
              <q-btn push class="bg-cyan-8 float-right" dense size="md" icon="save" text-color="white" type="submit" />
            </div>
            </q-form>
        </q-card-section>
      </q-card>
    </q-page>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import useApi from 'src/composables/UseApiProdutos'
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
      nome: '',
      quantidade: '',
      preco: ''
    })

    onMounted(async () => {
      if (route.params.id) {
        getProduct(route.params.id)
      }
    })

    const getProduct = async (id) => {
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
        router.push({ name: 'produtos' })
      } catch (error) {
        $q.notify({ message: 'Error ao Salvar', icon: 'cancel', color: 'negative' })
      }
    }

    return {
      form,
      onSubmit
    }
  }
})
</script>
