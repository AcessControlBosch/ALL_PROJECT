<template>

  <div class="container">

    <Header />

    <div class="content">

        <div class="formulario">

          <TitlePage />

          <label for="edv" class="label-form">EDV:</label>
          <input type="text" placeholder="Digite o EDV..." id="edv" class="input-form"/>

          <label for="senha" class="label-form">Senha:</label>
          <input type="password" placeholder="Digite a senha..." id="senha" class="input-form"/>


          <div class="align-items-center">

            <button class="btn-logar" v-on:click="$router.push('/screen_utilizacao')">Logar</button>

          </div>

          <div class="align-items-center">

            <button class="btn-redirect" v-on:click="$router.push('/screen_criarConta')">Não possue conta? Clique aqui</button>

          </div>
        
        </div>
    
    </div>

  </div>

</template>

<script>

export default {
  name: 'IndexPage'
}

</script>

<style lang="scss" scoped>

   @import "@/layouts/_normal_pages/Index.scss";
   @import "@/layouts/_responsividade/responsividade_formularios.scss";

</style>
