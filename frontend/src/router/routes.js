
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'home', component: () => import('src/pages/Home.vue') },
      { path: 'produtos/', name: 'produtos', component: () => import('src/pages/ProductPage.vue') },
      { path: 'funcionarios/', name: 'funcionarios', component: () => import('src/pages/FuncionarioPage.vue') },
      { path: 'form-product/:id?', name: 'formProduto', component: () => import('src/pages/FormProduct.vue') },
      { path: 'form-funcionario/:id?', name: 'formFuncionario', component: () => import('src/pages/FormFuncionario.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
