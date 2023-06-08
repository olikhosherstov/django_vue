<template>
  <GreenComponent
    :data="gridData"
    :days="dateArray"
    :columns="gridColumns"
    :filter-key="searchQuery"
  >
  </GreenComponent>
</template>

<script>
import GreenComponent from "@/components/GreenComponent.vue";

export default {
  components: {
    GreenComponent,
  },
  data: () => ({
    searchQuery: "",
    gridColumns: ["period", "1", "2", "3", "4", "5", "6", "7"],
    gridData: [
      {
        period: "6:00 - 7:00",
        1: "Chuck Norris",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
      },
      {
        period: "7:00 - 8:00",
        1: "Chuck Norris",
        2: "",
        3: "Bruce Lee",
        4: "",
        5: "",
        6: "",
        7: "",
      },
      {
        period: "8:00 - 9:00",
        1: "Jackie Chan",
        2: "Jackie Chan",
        3: "Jackie Chan",
        4: "Jackie Chan",
        5: "Jackie Chan",
        6: "Jackie Chan",
        7: "Jackie Chan",
      },
      {
        period: "9:00 - 10:00",
        1: "Jet Li",
        2: "",
        3: "Bruce Lee",
        4: "",
        5: "",
        6: "",
        7: "",
      },
      {
        period: "10:00 - 11:00",
        1: "Chuck Norris",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
      },
      {
        period: "11:00 - 12:00",
        1: "Chuck Norris",
        2: "",
        3: "Bruce Lee",
        4: "",
        5: "",
        6: "",
        7: "",
      },
      {
        period: "12:00 - 13:00",
        1: "Jackie Chan",
        2: "Jackie Chan",
        3: "Jackie Chan",
        4: "Jackie Chan",
        5: "Jackie Chan",
        6: "Jackie Chan",
        7: "Jackie Chan",
      },
      {
        period: "13:00 - 14:00",
        1: "Chuck Norris",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
      },
      {
        period: "14:00 - 15:00",
        1: "Chuck Norris",
        2: "",
        3: "Bruce Lee",
        4: "",
        5: "",
        6: "",
        7: "",
      },
      {
        period: "15:00 - 16:00",
        1: "Jackie Chan",
        2: "Jackie Chan",
        3: "Jackie Chan",
        4: "Jackie Chan",
        5: "Jackie Chan",
        6: "Jackie Chan",
        7: "Jackie Chan",
      },
      {
        period: "16:00 - 17:00",
        1: "Jet Li",
        2: "",
        3: "Bruce Lee",
        4: "",
        5: "",
        6: "",
        7: "",
      },
      {
        period: "17:00 - 18:00",
        1: "Chuck Norris",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
      },
      {
        period: "18:00 - 19:00",
        1: "Chuck Norris",
        2: "",
        3: "Bruce Lee",
        4: "",
        5: "",
        6: "",
        7: "",
      },
      {
        period: "19:00 - 20:00",
        1: "Jackie Chan",
        2: "Jackie Chan",
        3: "Jackie Chan",
        4: "Jackie Chan",
        5: "Jackie Chan",
        6: "Jackie Chan",
        7: "Jackie Chan",
      },
      {
        period: "20:00 - 21:00",
        1: "Jet Li",
        2: "",
        3: "Bruce Lee",
        4: "",
        5: "",
        6: "",
        7: "",
      },
      {
        period: "21:00 - 22:00",
        1: "Chuck Norris",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
      },
    ],
  }),
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
