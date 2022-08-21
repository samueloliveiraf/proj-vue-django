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
                v-model="form.cargo"
                label="Cargo *"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Campo obrigatorio']"
              />
              <q-input
                filled
                type="number"
                v-model="form.idade"
                label="Idade *"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Campo obrigatorio']"
              />
            </div>
            <div class="col-12 q-gutter-sm">
              <q-btn push class="bg-cyan-8 float-right" dense size="md" text-color="white" icon="cancel" :to="{ name: 'funcionarios' }" />
              <q-btn push class="bg-cyan-8 float-right" dense size="md" icon="save" text-color="white" type="submit" />
            </div>
            </q-form>
        </q-card-section>
      </q-card>
    </q-page>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import useApiFuncionario from 'src/composables/UserApiFuncionarios'
import { useQuasar } from 'quasar'
import { useRouter, useRoute } from 'vue-router'

export default defineComponent({
  name: 'FormFuncionario',
  setup () {
    const $q = useQuasar()
    const { post, getById, put } = useApiFuncionario()
    const router = useRouter()
    const route = useRoute()
    const form = ref({
      nome: '',
      cargo: '',
      idade: 0
    })

    onMounted(async () => {
      if (route.params.id) {
        getFuncionario(route.params.id)
      }
    })

    const getFuncionario = async (id) => {
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
        router.push({ name: 'funcionarios' })
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
