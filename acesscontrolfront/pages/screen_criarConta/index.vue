<template>

  <div class="container">

    <HeaderWithHome />

    <div class="content">

        <div class="formulario">

          <TitlePage />

          <label for="nome" class="label-form">Nome:</label>
          <input type="text" placeholder="Digite o seu nome..." id="nome" class="input-form"/>

          <label for="edv" class="label-form">EDV:</label>
          <input type="number" placeholder="Digite o seu EDV..." id="edv" class="input-form"/>

          <label for="edv" class="label-form">Área:</label>
          <Dropdown v-model="selectedArea" :options="this.dataArea" optionLabel="name" placeholder="Selecione a área..." />

          <div class="align-items-center">

            <button class="btn-send-approved">Enviar</button>

          </div>
        
        </div>
    
    </div>

  </div>

</template>

<script>

export default {

  name: 'screen_criarConta',

  data() {

	return {

    selectedArea: null,
    dataArea: [],

  }

},

  created(){

    this.$axios.get(this.$store.state.BASE_URL + "/areas").then((response) =>{

      this.dataArea = response.data;
    
    }).catch((error) => {

        console.log("Vish, deu ruim!");
        console.log(error);

    });

  }

}

</script>

<style lang="scss" scoped>
 
   @import "@/layouts/_normal_pages/Screen_CriarConta.scss";
   @import "@/layouts/_responsividade/responsividade_formularios.scss";

</style>
