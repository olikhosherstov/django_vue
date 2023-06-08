<template>
  <div class="news-item">
    <h2 class="news-title">{{ news.title }}</h2>
    <img :src="news.img_field" alt="News Image" class="news-image" />
    <p class="news-content">{{ news.content }}</p>
    <p class="news-date">Опубліковано: {{ news.time_create }}</p>
  </div>
</template>

<script>
export default {
  props: {
    news: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.news-item {
  background-color: #f2f2f2;
  padding: 10px;
  margin-bottom: 20px;
  border-radius: 5px;
  margin-left: auto;
  margin-right: auto;
  width: 450px;
  text-align: justify;
}

.news-title {
  font-size: 18px;
  margin-bottom: 5px;
  color: #333;
}

.news-image {
  max-width: 100%;
  margin-bottom: 10px;
  width: 450px;
}

.news-content {
  font-size: 14px;
  margin-bottom: 5px;
  color: #666;
}

.news-date {
  font-size: 12px;
  color: #999;
}
</style>
