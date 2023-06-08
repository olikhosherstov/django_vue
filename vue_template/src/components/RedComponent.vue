<template>
  <table v-if="data.length">
    <thead>
      <tr>
        <th v-for="(item, index) in days" :key="index">
          {{ capitalize(item) }}
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(entry, indexY) in data" :key="indexY">
        <td v-for="(item, indexX) in columns" :key="indexX">
          <EventItemRed :indexX="indexX" :indexY="indexY" :data="entry[item]">
          </EventItemRed>
          <!-- {{ entry[item] }} -->
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import EventItemRed from "./EventItemRed.vue";
export default {
  components: {
    EventItemRed,
  },
  props: {
    data: Array,
    days: Array,
    columns: Array,
    filterKey: String,
  },
  data() {
    return {
      sortKey: "",
    };
  },
  computed: {},
  methods: {
    capitalize(str) {
      return str.charAt(0).toUpperCase() + str.slice(1);
    },
  },
};
</script>

<style scoped>
table {
  border: 2px solid #ff3333;
  border-radius: 3px;
  background-color: #fff;
  margin-left: auto;
  margin-right: auto;
}

th {
  background-color: #ff3333;
  color: rgba(255, 255, 255, 0.66);
  cursor: pointer;
  user-select: none;
}

td {
  background-color: #f9f9f9;
}

th,
td {
  min-width: 120px;
  padding: 10px 20px;
}

th.active {
  color: #fff;
}

th.active .arrow {
  opacity: 1;
}

.arrow {
  display: inline-block;
  vertical-align: middle;
  width: 0;
  height: 0;
  margin-left: 5px;
  opacity: 0.66;
}

.arrow.asc {
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-bottom: 4px solid #fff;
}

.arrow.dsc {
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-top: 4px solid #fff;
}
</style>
