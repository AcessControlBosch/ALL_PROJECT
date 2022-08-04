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
                    
                    <!-- <div class="line-question">

                        <input type="checkbox" class="checkbox" id="um"/>
                        <label class="p-question" for="um">1 - Proteções</label>
                        

                    </div> -->

                    
                    
                    <div class="line-question" v-for="(question, id) in allQuestions" :key="id">

                        <input type="checkbox" class="checkbox" v-bind:value="idQuestion[id]" v-model="valueCheckBox"/>
                        <label class="p-question" for="um">{{idQuestion[id]}} - {{question.question}}</label>
                        
                    </div>
                </div>
                <div>
                    <ul>
                        <li v-for="(category,id) in valueCheckBox" :key="id">{{category}}</li>
                    </ul>
                </div>
                <div class="align-items-center">
            
                    <button class="btn btn-sucess" v-on:click="$router.push('/screen_cvMeioAmbiente')">Continuar</button>
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
            valueCheckBox: [],
            idQuestion:[]    
        }

    },
    methods:{
        checkBoxclick(){

        }
    },
    created(){
        console.log('this.$store.state.machine', this.$store.state.machine)
        this.$axios.get(this.$store.state.BASE_URL + '/greenbooks/1/2').then((response) => {
            console.log('oi created')


            this.allQuestions = response.data;

            console.log(this.allQuestions)

            let i = 0;

            for(i; i < this.allQuestions.length; i++){

                this.responseQuestions.push(this.allQuestions[i].question);
                this.idQuestion.push(i+1);

            }
            console.log('this.idQuestion',this.idQuestion)

        }).catch((error) => {

            console.log(error)

        })

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