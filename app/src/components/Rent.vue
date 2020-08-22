<template>
  <v-container>
    <div class="blue lighten-4">
      <p>恩师之谊</p>
      <p></p>
      <p>沈腾</p>
    </div>
    <v-bottom-navigation :value="activeBtn" color="primary" horizontal>
      <v-btn>
        <span>Rencents</span>
        <v-icon>mdi-history</v-icon>
      </v-btn>
      <v-btn>
        <span>Favorites</span>
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <v-btn>
        <span>Nearby</span>
        <v-icon>mdi-map-marker</v-icon>
      </v-btn>
    </v-bottom-navigation>
  </v-container>
</template>

<script>
export default {
  name: 'Rent',

  data: () => ({
    // information
    text: 'Hello from vuetify',
    activeBtn: '1'
  })
}
</script>
