<script>
import paper from "paper";
import tool from "@/mixins/toolBar/tool";

export default {
  name: "MergerTool",
  mixins: [tool],
  props: {
    scale: {
      type: Number,
      default: 1
    }
  },
  data() {
    return {
      icon: "fa-compress-arrows-alt",
      name: "Merger",
      cursor: "pointer",
      firstAnnotationId: null,
      secondAnnotationId: null,
      selectedChildren: [],
    };
  },
  methods: {
    onMouseDown(event) {

      this.$parent.paper.project.activeLayer.selected = false;
      if (
        event.item &&
        event.item.visible &&
        event.item.data.hasOwnProperty("categoryId") &&
        event.item.hasChildren()
      ) {
        let item = event.item;

        for (let i = 0; i < item.children.length; i++) {
          let child = item.children[i];

          if (
            child.visible &&
            child.contains(event.point) &&
            child.data.hasOwnProperty("annotationId")
          ) {

            if (this.firstAnnotationId == null){
              this.firstAnnotationId = child.data.annotationId;
            }else if(child.data.annotationId != this.firstAnnotationId){
              this.secondAnnotationId = child.data.annotationId;
              
              // merge first and second annotation
              let category = this.$parent.current.category;
              
              let firstCompound = this.$parent.getCategory(category).getAnnotation(this.firstAnnotationId).getCompoundPath();
              let secondCompound = this.$parent.getCategory(category).getAnnotation(this.secondAnnotationId).getCompoundPath();
              
              // merge paths
              this.$parent.uniteCurrentAnnotation(secondCompound);
              // if (secondCompound.hasChildren()){
              //   for(let i = 0; i < secondCompound.children.length; i++){
              //     this.$parent.uniteCurrentAnnotation(secondCompound.children[i]);
              //   }
              // }

              // delete second annotation
              this.$parent.getCategory(category).getAnnotation(this.secondAnnotationId).deleteAnnotation();
              this.selectedChildren.splice(1, 1);
            
              this.gracefullExit();
              this.$parent.paper.project.activeLayer.selected = false;
              break;
            }else{
              this.gracefullExit()
              break;
            }

            //try something
            let category = this.$parent.current.category;
            let indices = {
            annotation: child.data.annotationId,
            category: category
            };
            this.$emit("click", indices);
            
            //
            this.$parent.current.annotation = child.data.annotationId;
            child.selected = true;
            break;
          }
        }
      }
    },
    gracefullExit() {
        this.firstAnnotationId = null;
        this.secondAnnotationId = null;
        for (let i = 0; i < this.selectedChildren.length; i++){
            this.selectedChildren[i].selected = false;
        }
        this.selectedChildren = [];
    }
  },
};
</script>
