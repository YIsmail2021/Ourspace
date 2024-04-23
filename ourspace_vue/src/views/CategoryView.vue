<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to Ourspace
        </p>
        <p class="subtitle">
          A rambling site
        </p>
      </div>
    </section>
    
    <!-- Displayed in a grid using bulma css-->
    <div class="columns is-multiline">
      <div class="column is-one-quarter" v-for="category in listCategories" v-bind:key="category.id">
        <div class="box">
          <h3 class="is-size-5 has-text-centered">{{ category.name }}</h3>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'categoryView',
  data() {
    return {
      listCategories: {},
    }
  },
  components: {
  },
  mounted() {
    this.getListCategories()
  },
  // Get category info, will return a list of categories.
  methods: {
  getListCategories() {
    // Get params
    const url = `/api/v1/category/`;
    axios
      .get(url)
      .then(response => {
        this.listCategories = response.data;
      })
      .catch(error => {
        console.log(error);
      });
  },
  }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: 1.25rem;
    margin-right: -1.25rem;
  }
</style>
