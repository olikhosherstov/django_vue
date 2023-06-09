<template>
  <div v-if="newsItems != []">
    <h1>Новини</h1>
    <div v-for="newsItem in newsItems" :key="newsItem.id">
      <NewsItem :news="newsItem" />
    </div>
  </div>
  <div v-else>
    <h1>Новини</h1>
    <br />
    <h3>Новин немає.</h3>
  </div>
</template>

<script>
import NewsItem from "@/components/NewsItem.vue";
import axios from "axios";

export default {
  name: "HomeView",
  components: {
    NewsItem,
  },
  data() {
    return {
      newsItems: [],
    };
  },
  async beforeMount() {
    let response = await axios.get(
      "http://tennisvyshneve.pythonanywhere.com/api/news/"
    );
    this.newsItems = response.data;
  },
};
</script>
