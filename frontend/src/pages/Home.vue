<template>
    <q-page padding>
      <div class="row">
        <q-card class="my-card col">
          <q-card-section class="bg-cyan-8 text-white">
            <div class="text-h6">Crud de Produtos</div>
            <div class="text-subtitle2">by samueloliveiraf</div>
          </q-card-section>

          <q-card-actions vertical align="center">
            <q-btn push class="bg-cyan-8" icon="dns" color="white" dense size="md" :to="{ name: 'produtos' }">
            </q-btn>
          </q-card-actions>
        </q-card>
        <q-card class="my-card col">
          <q-card-section class="bg-cyan-8 text-white">
            <div class="text-h6">Crud de Funcionarios</div>
            <div class="text-subtitle2">by samueloliveiraf</div>
          </q-card-section>

        <q-card-actions vertical align="center">
          <q-btn push class="bg-cyan-8" icon="group" color="white" dense size="md" :to="{ name: 'funcionarios' }">
          </q-btn>
        </q-card-actions>
      </q-card>
    </div>
    </q-page>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'HomePage'
})
</script>
