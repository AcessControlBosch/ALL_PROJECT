<template>

  <div class="container">

    <Header />

    <div class="content">

        <div class="formulario">

          <TitlePage />

          <label for="edv" class="label-form">EDV:</label>
          <input type="text" placeholder="Digite o EDV..." id="edv" class="input-form" v-model="user.username"/>

          <label for="senha" class="label-form">Senha:</label>
          <input type="password" placeholder="Digite a senha..." id="senha" class="input-form" v-model="user.password"/>


          <div class="align-items-center">

            <button class="btn-logar" v-on:click="makeLogin()">Logar</button>

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
  
  name: 'IndexPage',

  data(){

    return{

      user:{
        username: '',
        password: '',
      }

    }

  },

  methods: {

    //função para fazer login
    makeLogin: async function(){

      if(this.user.username && this.user.password){

        this.$auth.loginWith("local", {data: this.user}).then(() => {

        }).catch((error) =>{

          console.log(error)

        })

      } else {
        alert("Preencha todos os campos")
      }
    }
  },


}

</script>

<style lang="scss" scoped>

   @import "@/layouts/_normal_pages/Index.scss";
   @import "@/layouts/_responsividade/responsividade_formularios.scss";

</style>
