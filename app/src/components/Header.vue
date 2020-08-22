<template>
  <v-app-bar
    app
    dark
    color="deep-purple accent-4">
      <v-app-bar-nav-icon @click="toggleNav"></v-app-bar-nav-icon>
      <v-toolbar-title>Pitayet Blog</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
  </v-app-bar>
</template>
<script>
export default {
  name: 'Header',
  data () {
    return {
    }
  },
  methods: {
    toggleNav () {
      this.$store.dispatch('toggleNavFun')
    }
  }
}
</script>

<style>

</style>
