<template>

    <div>

        <div class="supergrafico"></div>

        <div class="row">

            <img src="../static/logo.svg" />

            <button v-on:click="$auth.logout()"><i class="pi pi-home"></i></button>

        </div>

    </div>

</template>

<script>
export default {
  name: 'HeaderWithLogout'
}
</script>

<style lang="scss" scoped>

    @import "@/layouts/_scss_components/HeaderWithHome.scss";

</style>