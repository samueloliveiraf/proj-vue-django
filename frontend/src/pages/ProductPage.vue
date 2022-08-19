<template>
  <q-page padding>
    <q-table
        title="Produtos"
        :rows="produtos"
        :columns="columns"
        row-key="name"
      >
      <template v-slot:top>
        <span class="text-h5">Produtos</span>
        <q-space></q-space>
        <q-btn push class="bg-cyan-8" color="white" size="md" dense icon="add_box" :to="{ name: 'formProduto' }" />
      </template>
      <template v-slot:body-cell-actions="props">
        <q-td :props="props" class="q-gutter-sm">
          <q-btn push class="bg-cyan-8" color="white" icon="edit" dense size="md" @click="editProduto(props.row.id)"></q-btn>
          <q-btn push class="bg-cyan-8" color="white" icon="delete" dense size="md" @click="deleteProduto(props.row.id)"></q-btn>
        </q-td>
      </template>
    </q-table>
  </q-page>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import useApiProduto from 'src/composables/UseApiProdutos'
import { useQuasar } from 'quasar'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'IndexPage',
  setup () {
    const produtos = ref([])
    const { list, remove } = useApiProduto()
    const $q = useQuasar()
    const router = useRouter()

    const columns = [
      { name: 'id', field: 'id', label: 'ID', sortable: true, align: 'left' },
      { name: 'nome', field: 'nome', label: 'Nome', sortable: true, align: 'left' },
      { name: 'quantidade', field: 'quantidade', label: 'Quantidade', sortable: true, align: 'left' },
      { name: 'preco', field: 'preco', label: 'Preço', sortable: true, align: 'left' },
      { name: 'data', field: 'data', label: 'Data', sortable: true, align: 'left' },
      { name: 'actions', field: 'actions', label: 'Ações', align: 'right' }
    ]

    onMounted(() => {
      getProdutos()
    })

    const getProdutos = async () => {
      try {
        const data = await list()
        produtos.value = data
      } catch (error) {
        console.error(error)
      }
    }

    const deleteProduto = async (id) => {
      try {
        $q.dialog({
          title: 'Remover',
          message: 'Tem certeza que deseja remover?',
          cancel: true,
          persistent: true
        }).onOk(async () => {
          await remove(id)
          $q.notify({ message: 'Deletado com sucesso', icon: 'check', color: 'positive' })
          await getProdutos()
        })
      } catch (error) {
        $q.notify({ message: 'Error ao deletar', icon: 'cancel', color: 'negative' })
      }
    }

    const editProduto = (id) => {
      router.push({ name: 'formProduto', params: { id } })
    }

    return {
      produtos,
      columns,
      deleteProduto,
      editProduto
    }
  }
})
</script>
