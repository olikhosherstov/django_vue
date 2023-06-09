<template>
  <RedComponent
    :data="gridData"
    :days="dateArray"
    :columns="gridColumns"
    :filter-key="searchQuery"
  >
  </RedComponent>
</template>

<script>
import RedComponent from "@/components/RedComponent.vue";
import axios from "axios";

export default {
  components: {
    RedComponent,
  },
  data: () => ({
    searchQuery: "",
    gridColumns: ["period", "1", "2", "3", "4", "5", "6", "7"],
    gridData: [],
  }),
  async beforeMount() {
    let url = "https://tennisvyshneve.pythonanywhere.com/api/kortred/";
    const config = {
      headers: {
        Authorization: "JWT " + this.$store.state.access,
      },
    };
    let response = await axios.get(url, config);
    this.gridData = response.data;
  },
  computed: {
    dateArray: function () {
      var date = new Date();

      var timeArray = ["Час"];

      for (let index = 0; index < 7; index++) {
        if (index > 0) {
          date.setDate(date.getDate() + 1);
        }
        timeArray.push(
          date.toLocaleString("uk", {
            weekday: "long",
            month: "long",
            day: "numeric",
          })
        );
      }
      return timeArray;
    },
  },
};
</script>
