<template>
<v-container fluid>
  <v-breadcrumbs :items="$store.state.breadcrumbs" large></v-breadcrumbs>
  <v-row dense>
    <v-col
      v-for="article in articles"
      :key="article.title"
      cols="3">
      <v-card>
        <v-img src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
          class="white--text align-end"
          gradient="to bottom, rgba(0, 0, 0, .1), rgba(0, 0, 0, .5)"
          height="200">
          <v-card-title  v-text="article.title"></v-card-title>
        </v-img>
        <v-card-subtitle class="pb-0" v-text="article.sec_title"></v-card-subtitle>
        <v-card-text class="text-primary" v-text="article.content"></v-card-text>
        <!-- <v-card-actions>
          <v-btn color="deep-purple" text>share</v-btn>
          <v-btn color="deep-purple" text>more</v-btn>
        </v-card-actions> -->
      </v-card>
    </v-col>
  </v-row>
  <v-row>
    <v-col cols="12">
      <v-pagination
        :length="pagination.total/20"
        total-visible="6"
        v-model="pagination.page"
        @input="changeList"
      >
      </v-pagination>
    </v-col>
  </v-row>
</v-container>
</template>

<script>
import server from '../plugins/http-service'
export default {
  name: 'List',
  data () {
    return {
      pagination: {
        page: 1,
        total: 0,
        perPage: 0,
        visible: 10
      },
      articles: []
    }
  },
  mounted () {
    server.get('articles/').then(data => {
      this.articles = data.articles
      this.pagination = {
        page: 1,
        total: data.count,
        perPage: 20,
        visible: 10
      }
    })
  },
  methods: {
    changeList: function (page) {
      server.get('articles/', {page: page}).then(data => {
        this.articles = data.articles
        this.pagination = {
          page: page,
          total: data.count,
          perPage: 20,
          visible: 10
        }
      })
    }
  }
}
</script>

<style>

</style>
