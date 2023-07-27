<template lang="">
    <div class="container">
        <div class= "row">
            <div class="card w-50">
                <div class="card-body">
                    <form>
                        <div class="form-group">
                            <textarea 
                                id="text"
                                placeholder="Enter Your text"
                                name="text"
                                class="form-control"
                                rows="13"
                                v-model="form.text"
                                :class="{
                                    'is-invalid' : form.errors.has('text'),
                                }"
                            >
                            </textarea>
                        </div>
                        <div class="row mt-2">
                            <div class="col-md-8">
                                <button 
                                    type="submit"
                                    class="btn btn-outline-success"
                                    @click.prevent="generateSummary()"
                                >
                                    Geneare Summary
                                </button>
                                &nbsp;&nbsp;&nbsp;&nbsp;
                                <button 
                                    type="submit"
                                    class="btn btn-outline-info"
                                    v-show="this.form.text"
                                    @click.prevent="clear()"
                                >
                                    Clear
                                </button>
                                &nbsp;&nbsp;&nbsp;&nbsp;
                            </div>
                            <!-- <div class="col-md-4">
                                <button 
                                    type="submit"
                                    class="btn btn-secondary"
                                    @click.prevent="upload()"
                                >
                                    Upload Doc
                                </button>
                            </div> -->
                        </div>
                    </form>
                </div>   
            </div>

            <div class="card w-50">
                <div class="card-body">
                    <p> {{generatedSummary}} </p>
                </div>
                <div class="card-footer">
                    <button 
                        type="submit"
                        class="btn btn-success"
                        v-show="this.generatedSummary"
                        @click.prevent="copyToClipboard()"
                    >
                        Copy
                    </button>
                    <pre v-if="result">{{result}}</pre>
                </div>
            </div>
        </div>

        <!-- Model 
        <div class="modal fade" id="documentModel" tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Upload Document</h5>
                    </div>
                    <div class="modal-body">
                        <div class="input-group mb-3">
                            <input
                                type="file"
                                name="file" 
                                class="form-control" 
                                id="inputfileupload" 
                                v-on:change="onFileChange"
                            />
                            <label class="form-control" for="inputfileupload"> Upload Document </label>
                        </div>
                    </div>
                    <div class="modal-footer">
                        
                    </div>
                </div>
            </div>
        </div> -->
    </div>
</template>
<script>
import Form from 'vform'
import axios from 'axios';

const dict = {
    custom: {
        text: {
            required: () => "This field is required",
        }        
    }
};

export default {
    data() {
        return {
            generatedSummary: null,
            result: null,
            file: null,
            form: new Form({
                text: null,
            })
        }
    },
    methods: {
        generateSummary(){
            this.generatedSummary = null;
            axios
                .post("/genereate_summary", { text: this.form.text })
                .then((response) => {
                    this.generatedSummary = response.data.processed_text;
                })
                .catch((error) => {
                    console.error("Error processing text:", error);
                });
        },
        clear(){
            this.form.text = null;
        },
        upload(){
            $('#documentModel').model('show');
        },
        onFileChange(e){
            this.file = "";
            var file = e.target.files[0];
            if(file["type"] === "appliation/pdf"){
                this.file = file;
            }else{
                alert("the file accept only pdf");
            }
        },
        copyToClipboard(){
            navigator.clipboard.writeText(this.generatedSummary).then(
              () => {
                this.result = "Text copied";
                setTimeout(() => {
                  this.result = ""; // Clear the result message after 1 seconds
                }, 1000); // 1000 milliseconds = 1 seconds
              },
              (err) => {
                console.error("Could not copy text: ", err);
              }
            );
        }
    },
}
</script>
<style lang="">
    
</style>