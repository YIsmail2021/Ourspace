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
        <div class="column is-12 mb-5">
          <h2 class="is-size-2 has-text-centered">Create a category</h2>
        </div>
        <!-- Text box where a user should input in a name for the category.-->
        <!-- Cant seem to centre the div properly with bulma css. Next best thing.-->
        <div style="display: flex; justify-content: center;">
            <div class="box">
                <input type="text" v-model="textBody" class="input" placeholder="Enter your category name here">
                <button @click="submitCategory" class="button is-primary">Submit</button>
            </div>
        </div>
      </div>
  
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import router from '@/router/index'
  
  export default {
    name: 'createCategoryView',
    components: {
    },
    mounted() {
      this.submitCategory()
    },
    // Create a category is needed here.
    // Will return a 201 status code if successful and should
    // redirect to the view category page.
    methods: {
    submitCategory() {
      const postData = {
        name: this.textBody,
  
      };
      axios
        .post('/api/v1/category/', postData)
        .then(response => {
          console.log('Category submitted successfully:', response.data);
          this.textBody = '';
          router.push({ name: 'category' })
        })
        .catch(error => {
          console.error('Error submitting category:', error);
        });
    }
    }
  }
  // add the submitted comment to the listComments array directly after a successful submission.
  </script>
  
  <style scoped>
    .image {
      margin-top: -1.25rem;
      margin-left: 1.25rem;
      margin-right: -1.25rem;
    }
  </style>
  