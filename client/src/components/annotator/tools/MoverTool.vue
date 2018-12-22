<script>
import paper from "paper";
import tool from "@/mixins/toolBar/tool";

export default {
  name: "MoverTool",
  mixins: [tool],
  props: {
    scale: {
      type: Number,
      default: 1
    }
  },
  data() {
    return {
      icon: "fa-hand-paper",
      name: "Mover",
      cursor: "move",
      lastPosition: null,
    };
  },
  methods: {
      onMouseDrag: function (event) {
          if (this.lastPosition == null){
              this.lastPosition = event.point;
          }else{
              let delta = event.point.subtract(this.lastPosition);
              this.$parent.paper.view.center = this.$parent.paper.view.center.subtract(delta);
          }
      },
      onMouseUp: function(event){
          this.lastPosition = null;
      }
  },
};
</script>
