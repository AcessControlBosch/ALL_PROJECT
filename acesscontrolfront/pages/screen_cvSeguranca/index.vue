<template>

    <div class="container">
    
        <Header />

        <div class="content">

            <div class="row-superior">

                <TitlePage />

            </div> 

            <div class="row-inferior">

                <div class="card-info">
                
                    <p class="card-title">Segurança</p>
                    <p class="card-subject">Requisitos de Segurança de acordo com o equipamento:​</p>


                </div> 

                <div class="formulario">
                    
                    <div class="line-question">

                        <input type="checkbox" class="checkbox" id="um"/>
                        <label class="p-question" for="um">1 - Proteções</label>
                        

                    </div>

                    <!--
                    
                    <div class="line-question" v-for:"question in allQuestions">

                        <input type="checkbox" class="checkbox" id="um" v-model:"responseQuestions[question.id-1]"/>
                        <label class="p-question" for="um">{{question.id}} - {{question.name}}</label>
                        
                    </div>

                    -->

                </div>

                <div class="align-items-center">
            
                    <button class="btn btn-sucess" v-on:click="">Continuar</button>
                    <button class="btn btn-alert" v-on:click="$router.push('/screen_home')">Cancelar</button>
            
                </div>
            
            </div>

        </div>
    
    </div>

</template>

<script>

export default {

    name: 'screen_cvSeguranca',

    data(){

        return{

            allQuestions: [],
            responseQuestions: [],

        }

    },

    created(){
        console.log('this.$store.state.machine', this.$store.state.machine)
        // this.$axios.get(this.$store.state.BASE_URL + '/greenbook?=' + this.$store.state.machine).then((response) => {
        //     console.log('oi created')
        //     this.allQuestions = response.data;

        //     let i = 0;

        //     for(i; i < this.allQuestions.length; i++){

        //         this.responseQuestions[i] = false

        //     }

        // }).catch((error) => {

        //     console.log(error)

        // })

    },


    methods: {

        verifyQuestions: function(){

            


        }


    },

}

</script>

<style lang="scss" scoped>

    @import "@/layouts/_normal_pages/Screen_CvSeguranca.scss";
    @import "@/layouts/_responsividade/responsividade_grid.scss";

</style>