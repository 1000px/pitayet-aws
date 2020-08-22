<template>
  <v-app>
    <v-header />
    <v-nav />
    <v-main>
      <v-container fluid>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Header from './components/Header'
import Nav from './components/Nav'
export default {
  name: 'App',
  components: {
    'VHeader': Header,
    'VNav': Nav
  },
  data () {
    //
    return {
      isShown: true
    }
  }
}
</script>
