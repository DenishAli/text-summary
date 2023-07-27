<template>
    <div class="container">
    <div class="row" style="margin-bottom: 15px;">
        <div class="col-md-3"> </div>
        <div class="col-md-6 mt-5 m-container"> 
            <div class="image">
                <img alt="summarizer logo"  src="../assets/logo.svg">
            </div>
            <div class="text">
                <h1> Summary <br> Generator</h1>
            </div>
        </div>
        <div class="col-md-3"> </div>
    </div>
    <div class="row">
        <childView />
    </div>
        
        
    </div>
</template>
<script>
import childView from '../components/summaryInOut.vue'
export default {
    components: {childView}
}
</script>
<style scoped>
    .m-container {
        display: grid;
        align-items: center; 
        grid-template-columns: 1fr 1fr;        
    }
    .image {
        text-align: right !important
    }
    .text {
        margin-left: 20px;
    }
</style>