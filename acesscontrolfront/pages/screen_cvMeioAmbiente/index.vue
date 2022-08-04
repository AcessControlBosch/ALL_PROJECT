<template>

    <div class="container">
    
        <Header />

        <div class="content">

            <div class="row-superior">

                <TitlePage />

            </div>

            <div class="row-inferior">

                <div class="card-info">
                    <div>
                        <p class="card-title">Meio Ambiente</p>
                    </div>
                    <div>
                        <p class="card-subject">Requisitos de Meio Ambiente de acordo com o equipamento:​​</p>
                    </div>
                </div>

                <div class="formulario">
                    
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
            
                    <button class="btn btn-sucess" v-on:click="showModal()">Finalizar</button>
                    <button class="btn btn-alert" v-on:click="$router.push('/screen_home')">Cancelar</button>
            
                </div>
                <div v-if="show">
                    <div>
                    <ModalLock/>
                </div>
                <div>
                    <ModalReleased/>
                </div>
            
                </div>
                
            </div>

        </div>
    
    </div>

</template>

<script>
export default {
    name: 'screen_cvMeioAmbiente',
    data() {
        return {
            showDialogV: false,
            intTest: 0,
            allQuestions: [],
            responseQuestions: [],
            valueCheckBox: [],
            idQuestion:[],
            show: false
        }
    },
    created(){
        console.log('this.$store.state.machine', this.$store.state.machine)
        this.$axios.get(this.$store.state.BASE_URL + '/greenbooks/1/1').then((response) => {
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
    methods:{
        showModal(intTest){
            this.showDialogV = true;
        }
    }
}
</script>

<style lang="scss" scoped>
    @import "@/layouts/_normal_pages/Screen_CvMeioAmbiente.scss";
    @import "@/layouts/_responsividade/responsividade_grid.scss";
</style>