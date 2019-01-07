<template>
  <div>
    <div class="fas fa-plus fa-2x" style="margin: 30px; color: white;" id="zoomIn" @click="onZoomInClick" />
    <div class="fas fa-minus fa-2x" style="maring: 30px; color: white;" id="zoomOut" @click="onZoomOutClick" />
  </div>
</template>


<script>

export default {
  name: "ZoomPannel",
  props: {
    zoomIn: {
      type: Object,
      required: true
    }
  },
  methods: {
      onZoomInClick(){
          this.$parent.paper.view.zoom += 0.01
      },
      onZoomOutClick(){
          this.$parent.paper.view.zoom -= 0.01
      }
  }
};

</script>
