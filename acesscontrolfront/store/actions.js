export default {

    SET_USER(context, payload){
        console.log("vuex:" + payload);
        context.commit("USER", payload);
    },

    SET_AREAS(context, payload){
        console.log("vuex:" + payload);
        context.commit("AREAS", payload);
    }
    
}