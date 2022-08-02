export default {

    SET_USER(context, payload){
        console.log("vuex:" + payload);
        context.commit("USER", payload);
    },

    SET_MACHINE(context, payload){
        console.log("IP_Adress_MACHINE:" + payload);
        context.commit("MACHINE", payload);
    },
    
}