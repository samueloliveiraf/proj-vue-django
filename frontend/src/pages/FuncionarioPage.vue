<template>
    <q-page padding>
        <q-table
            title="Funcionarios"
            :rows="funcionarios"
            :columns="columns"
            row-key="name"
        >
        <template v-slot:top>
            <span class="text-h5">Funcionarios</span>
            <q-space></q-space>
            <q-btn push class="bg-cyan-8" color="white" size="md" dense icon="add_box" :to="{ name: 'formFuncionario' }" />
        </template>
        <template v-slot:body-cell-actions="props">
            <q-td :props="props" class="q-gutter-sm">
            <q-btn push class="bg-cyan-8" color="white" icon="edit" dense size="md" @click="editFuncionario(props.row.id)"></q-btn>
            <q-btn push class="bg-cyan-8" color="white" icon="delete" dense size="md" @click="deleteFuncionario(props.row.id)"></q-btn>
            </q-td>
        </template>
        </q-table>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import useApiFuncionario from 'src/composables/UserApiFuncionarios'
import { useQuasar } from 'quasar'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'IndexPage',
  setup () {
    const funcionarios = ref([])
    const { list, remove } = useApiFuncionario()
    const $q = useQuasar()
    const router = useRouter()

    const columns = [
      { name: 'id', field: 'id', label: 'ID', sortable: true, align: 'left' },
      { name: 'nome', field: 'nome', label: 'Nome', sortable: true, align: 'left' },
      { name: 'cargo', field: 'cargo', label: 'Cargo', sortable: true, align: 'left' },
      { name: 'idade', field: 'idade', label: 'Idade', sortable: true, align: 'left' },
      { name: 'data', field: 'data', label: 'Data', sortable: true, align: 'left' },
      { name: 'actions', field: 'actions', label: 'Ações', align: 'right' }
    ]

    onMounted(() => {
      getFuncionarios()
    })

    const getFuncionarios = async () => {
      try {
        const data = await list()
        funcionarios.value = data
      } catch (error) {
        console.error(error)
      }
    }

    const deleteFuncionario = async (id) => {
      try {
        $q.dialog({
          title: 'Remover',
          message: 'Tem certeza que deseja remover?',
          cancel: true,
          persistent: true
        }).onOk(async () => {
          await remove(id)
          $q.notify({ message: 'Deletado com sucesso', icon: 'check', color: 'positive' })
          await getFuncionarios()
        })
      } catch (error) {
        $q.notify({ message: 'Error ao deletar', icon: 'cancel', color: 'negative' })
      }
    }

    const editFuncionario = (id) => {
      router.push({ name: 'formFuncionario', params: { id } })
    }

    return {
      funcionarios,
      columns,
      deleteFuncionario,
      editFuncionario
    }
  }
})
</script>
