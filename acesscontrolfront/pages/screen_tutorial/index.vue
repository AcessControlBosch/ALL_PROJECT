<template>

    <div class="container">
    
        <Header />

        <div class="content">

          <div class="row-superior">

              <TitlePage />

          </div>

          <div class="row-inferior">

              <p class="subtitle">Veja como é o funcionamento desta platafoma neste video:</p>

              <div class="video">

              </div>

              <div class="align-items-center">

                  <button class="btn" v-on:click="$router.push('/screen_home')">Finalizar</button>

              </div>


          </div>

        </div>

    
    </div>


</template>  

<script>

export default {
  name: 'screen_tutorial'
}

</script>

<style lang="scss" scoped>

   @import "@/layouts/_normal_pages/Screen_Tutorial.scss";
   @import "@/layouts/_responsividade/responsividade_grid.scss";

</style>