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
      
      <div class="columns-is-multine">
        <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest posts</h2>
        </div>
  
        <div
          class="column is-3"
          v-for="post in listPosts"
          v-bind:key="post.id">
          <div class="box">
            <figure class="image mb-4">
              <img v-bind:src="product.get_thumbnail">
            </figure>
            <h3 class="is-size-4">{{ post.name }}</h3>
            <p class="is-size-6 has-text-grey">S{{ post.price }}</p>
            View details
          </div>
        </div>
  
      </div>
  
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'HomeView',
    data() {
      return {
        listPosts: []
      }
    },
    components: {
    },
    mounted() {
      this.getListPosts()
    },
    methods: {
      getListPosts(){
        axios
        .get('/api/v1/posts/')
        .then(response => {
          this.listPosts = response.data
        })
        .catch(error => {
          console.log(error)
        })
      }
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
  